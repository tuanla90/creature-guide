#!/usr/bin/env python3
"""Render a reusable single-image creature motion spec to a seamless GIF."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import cv2
import numpy as np
from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Source creature image")
    parser.add_argument("--spec", type=Path, required=True, help="Motion spec JSON")
    parser.add_argument("--output", type=Path, required=True, help="Output .gif path")
    parser.add_argument("--contact-sheet", type=Path, help="Optional four-pose .jpg review sheet")
    parser.add_argument("--mask", type=Path, help="Optional corrected whole-creature alpha mask")
    parser.add_argument("--background", type=Path, help="Optional clean background plate")
    return parser.parse_args()


def image_or_fail(path: Path, flags: int = cv2.IMREAD_UNCHANGED) -> np.ndarray:
    image = cv2.imread(str(path), flags)
    if image is None:
        raise ValueError(f"Cannot read image: {path}")
    return image


def normalized_pair(value, label: str) -> tuple[float, float]:
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(f"{label} must be a two-number list")
    a, b = float(value[0]), float(value[1])
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError(f"{label} must contain finite numbers")
    return a, b


def load_alpha(mask_path: Path | None, source: np.ndarray, bgr: np.ndarray, rect_values) -> np.ndarray:
    height, width = bgr.shape[:2]
    if mask_path:
        mask = image_or_fail(mask_path)
        if mask.shape[:2] != (height, width):
            raise ValueError("Alpha mask must match source image size")
        alpha = mask[:, :, 3] if mask.ndim == 3 and mask.shape[2] == 4 else (
            cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) if mask.ndim == 3 else mask
        )
    elif source.ndim == 3 and source.shape[2] == 4:
        alpha = source[:, :, 3]
    else:
        rx, ry, rw, rh = [float(v) for v in rect_values]
        rect = (round(rx * width), round(ry * height), round(rw * width), round(rh * height))
        if rect[2] <= 0 or rect[3] <= 0 or rect[0] < 0 or rect[1] < 0 or rect[0] + rect[2] > width or rect[1] + rect[3] > height:
            raise ValueError("foreground_rect must fit within the image")
        segmentation = np.zeros((height, width), np.uint8)
        bgd = np.zeros((1, 65), np.float64)
        fgd = np.zeros((1, 65), np.float64)
        cv2.grabCut(bgr, segmentation, rect, bgd, fgd, 8, cv2.GC_INIT_WITH_RECT)
        alpha = np.where((segmentation == cv2.GC_FGD) | (segmentation == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
        alpha = cv2.morphologyEx(alpha, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    return cv2.GaussianBlur(alpha.astype(np.uint8), (0, 0), 1.0)


def color_gates(rgb: np.ndarray) -> dict[str, np.ndarray]:
    values = rgb.astype(np.float32)
    green = np.clip((values[:, :, 1] - values[:, :, 0] - 4) / 24, 0, 1)
    green *= np.clip((values[:, :, 1] - values[:, :, 2]) / 24, 0, 1)
    pink = np.clip((values[:, :, 0] - values[:, :, 1] - 10) / 32, 0, 1)
    pink *= np.clip((values[:, :, 0] - values[:, :, 2]) / 32, 0, 1)
    return {
        "green": cv2.GaussianBlur(green.astype(np.float32), (0, 0), 5),
        "pink": cv2.GaussianBlur(pink.astype(np.float32), (0, 0), 5),
    }


def build_region(motion: dict, xx: np.ndarray, yy: np.ndarray, gates: dict, spec_dir: Path) -> dict:
    height, width = xx.shape
    cx, cy = normalized_pair(motion["center"], f"{motion['name']}.center")
    sx, sy = normalized_pair(motion["sigma"], f"{motion['name']}.sigma")
    if sx <= 0 or sy <= 0:
        raise ValueError(f"{motion['name']}.sigma must be positive")
    cx, cy, sx, sy = cx * width, cy * height, sx * width, sy * height
    weight = np.exp(-.5 * (((xx - cx) / sx) ** 2 + ((yy - cy) / sy) ** 2)).astype(np.float32)

    gate = motion.get("color_gate")
    if isinstance(gate, str) and gate not in ("none", "green", "pink"):
        raise ValueError(f"Unknown color_gate: {gate}")
    if isinstance(gate, str) and gate in gates:
        weight *= gates[gate]
    elif isinstance(gate, dict):
        low, high = normalized_pair(gate["hue_degrees"], "hue_degrees")
        hsv = cv2.cvtColor((gates["rgb"]).astype(np.uint8), cv2.COLOR_RGB2HSV)
        hue = hsv[:, :, 0].astype(np.float32) * 2
        saturation = hsv[:, :, 1].astype(np.float32) / 255
        selected = ((hue >= low) & (hue <= high)) if low <= high else ((hue >= low) | (hue <= high))
        selected &= saturation >= float(gate.get("min_saturation", .12))
        weight *= cv2.GaussianBlur(selected.astype(np.float32), (0, 0), 5)

    if motion.get("region_mask"):
        region_path = spec_dir / motion["region_mask"]
        region_mask = image_or_fail(region_path, cv2.IMREAD_GRAYSCALE)
        if region_mask.shape != xx.shape:
            raise ValueError(f"{motion['name']}.region_mask size does not match image")
        weight *= region_mask.astype(np.float32) / 255

    return {"config": motion, "weight": weight, "center": (cx, cy)}


def add_motion(region: dict, progress: float, mode: str, breath_skew: float, xx: np.ndarray, yy: np.ndarray, dx: np.ndarray, dy: np.ndarray) -> None:
    motion = region["config"]
    weight = region["weight"]
    cx, cy = region["center"]
    kind = motion["kind"]
    height, width = xx.shape
    angle = 2 * math.pi * progress
    travel = .5 - .5 * math.cos(angle)
    breath = travel if mode == "boomerang" else .5 - .5 * math.cos(angle + breath_skew * (1 - math.cos(angle)))

    if kind == "breath":
        anchors = motion.get("anchors", {})
        top_a, top_b = normalized_pair(anchors.get("top_fade", [0, 1]), "top_fade")
        bottom_a, bottom_b = normalized_pair(anchors.get("bottom_fade", [0, 1]), "bottom_fade")
        face_a, face_b = normalized_pair(anchors.get("face_fade", [1, 2]), "face_fade")
        if top_a >= top_b or bottom_a >= bottom_b or face_a >= face_b:
            raise ValueError(f"Invalid anchor fade in {motion['name']}")
        weight = weight * np.clip((yy / height - top_a) / (top_b - top_a), 0, 1)
        weight *= np.clip((bottom_b - yy / height) / (bottom_b - bottom_a), 0, 1)
        face_min = float(anchors.get("face_min", 0))
        weight *= 1 - (1 - face_min) * np.clip((xx / width - face_a) / (face_b - face_a), 0, 1)
        dx += (xx - cx) * float(motion.get("width_scale", 0)) * breath * weight
        dy += (float(motion.get("drop_px", 0)) + (yy - cy) * float(motion.get("height_scale", 0))) * breath * weight
    elif kind == "blink":
        peak = float(motion.get("peak", .65))
        spread = float(motion.get("width", .08))
        if spread <= 0:
            raise ValueError(f"{motion['name']}.width must be positive")
        if mode == "boomerang":
            distance = travel - peak
        else:
            distance = math.atan2(math.sin(angle - 2 * math.pi * peak), math.cos(angle - 2 * math.pi * peak)) / (2 * math.pi)
        blink = math.exp(-.5 * (distance / spread) ** 2)
        dy -= (yy - cy) * float(motion.get("strength", .25)) * blink * weight
    elif kind == "jaw":
        jaw_open = math.sin(math.pi * travel) ** 2 if mode == "boomerang" else breath
        dy += float(motion.get("drop_px", 2)) * jaw_open * weight
    elif kind == "sway":
        px, py = normalized_pair(motion["pivot"], f"{motion['name']}.pivot")
        px *= width
        py *= height
        phase = (2 * math.pi * travel if mode == "boomerang" else angle) + float(motion.get("phase", 0))
        oscillation = math.sin(phase)
        theta = math.radians(float(motion.get("angle_degrees", 0))) * oscillation
        shift_x, shift_y = normalized_pair(motion.get("shift_px", [0, 0]), "shift_px")
        dx += (-theta * (yy - py) + shift_x * oscillation) * weight
        vertical_oscillation = oscillation if mode == "boomerang" else math.cos(phase)
        dy += (theta * (xx - px) + shift_y * vertical_oscillation) * weight
    else:
        raise ValueError(f"Unknown motion kind in {motion['name']}: {kind}")


def main() -> None:
    args = parse_args()
    if args.output.suffix.lower() != ".gif":
        raise ValueError("--output must end in .gif")
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    source = image_or_fail(args.input)
    if source.ndim != 3 or source.shape[2] not in (3, 4):
        raise ValueError("Source must be an RGB/RGBA image")
    bgr = source[:, :, :3]
    height, width = bgr.shape[:2]
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    alpha = load_alpha(args.mask, source, bgr, spec.get("foreground_rect", [0, 0, 1, 1]))

    if args.background:
        background = image_or_fail(args.background, cv2.IMREAD_COLOR)
        if background.shape[:2] != (height, width):
            raise ValueError("Background plate must match source image size")
    else:
        hole = cv2.dilate((alpha > 20).astype(np.uint8) * 255, np.ones((11, 11), np.uint8))
        background = cv2.inpaint(bgr, hole, 11, cv2.INPAINT_TELEA)
    plate = cv2.cvtColor(background, cv2.COLOR_BGR2RGB).astype(np.float32)

    yy, xx = np.mgrid[0:height, 0:width].astype(np.float32)
    gates = color_gates(rgb)
    gates["rgb"] = rgb
    regions = [build_region(m, xx, yy, gates, args.spec.parent) for m in spec["motions"]]
    duration = float(spec.get("duration_seconds", 4))
    fps = int(spec.get("fps", 12))
    count = round(duration * fps)
    if count < 8 or count > 300 or duration <= 0:
        raise ValueError("Expected 8–300 frames and a positive duration")
    output_width = int(spec.get("output_width", min(width, 1032)))
    output_height = round(output_width * height / width)
    if output_width < 160:
        raise ValueError("output_width is too small")
    mode = spec.get("loop_mode", "cyclic")
    if mode not in ("cyclic", "boomerang"):
        raise ValueError("loop_mode must be cyclic or boomerang")
    breath_skew = float(spec.get("breath_skew", .35))
    if abs(breath_skew) >= 1:
        raise ValueError("breath_skew must be between -1 and 1")

    frames = []
    for index in range(count):
        u = index / (count - 1)
        dx = np.zeros((height, width), np.float32)
        dy = np.zeros((height, width), np.float32)
        for region in regions:
            add_motion(region, u, mode, breath_skew, xx, yy, dx, dy)
        map_x = np.ascontiguousarray(xx - dx)
        map_y = np.ascontiguousarray(yy - dy)
        warped_rgb = cv2.remap(rgb, map_x, map_y, cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        warped_alpha = cv2.remap(alpha, map_x, map_y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
        opacity = warped_alpha.astype(np.float32)[:, :, None] / 255
        composite = np.clip(warped_rgb.astype(np.float32) * opacity + plate * (1 - opacity), 0, 255).astype(np.uint8)
        frames.append(Image.fromarray(composite).resize((output_width, output_height), Image.Resampling.LANCZOS))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    # The exact endpoint pose is held for only 10 ms; the next cycle starts with the same
    # pose and velocity, without a visible pause at the GIF boundary.
    delays = [round(duration * 1000 / (count - 1))] * (count - 1) + [10]
    frames[0].save(args.output, save_all=True, append_images=frames[1:], duration=delays, loop=0, optimize=True, disposal=2)
    if args.contact_sheet:
        sheet = Image.new("RGB", (output_width * 2, output_height * 2), "#18201d")
        for slot, index in enumerate([0, count // 4, count // 2, 3 * count // 4]):
            sheet.paste(frames[index], ((slot % 2) * output_width, (slot // 2) * output_height))
        args.contact_sheet.parent.mkdir(parents=True, exist_ok=True)
        sheet.save(args.contact_sheet, quality=90)
    difference = np.max(np.abs(np.asarray(frames[0], dtype=np.int16) - np.asarray(frames[-1], dtype=np.int16)))
    print(f"Rendered {count} frames ({mode}). First/last pose max pixel difference: {difference}.")


if __name__ == "__main__":
    main()
