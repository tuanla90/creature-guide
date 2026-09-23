---
name: creature-motion
description: Turn a single creature still into a short, seamless ambient motion loop with anchored anatomy, localized breathing, facial micro-motion, and independently swaying organic parts. Use for subtle documentary shots, not articulated walking or combat.
---

# Creature motion from one image

Create a visibly living creature while preserving its identity and weight. Start from the supplied image; the reusable renderer is `scripts/render.py`. It uses OpenCV and Pillow locally and does not call a model provider. This is 2D image warping; use a 3D reconstruction workflow such as `img2threejs` when the shot needs a new camera angle or actual rigged geometry.

## Decide whether this method fits

Use this for a mostly stationary subject: breathing, an eyelid or jaw twitch, leaves, fur, antennae, tail, petals, and a little ambient movement. A single view cannot reveal hidden anatomy. If the shot requires walking, turning, a major pose change, or transformation, make separate keyframes or use a rig/video model.

## Build the motion spec

Inspect the image and record normalized coordinates (0–1). Mark rigid anchors first: skull, spine/shoulder junction, feet/ground contact, and roots of appendages. Place the breath region on the lower chest or abdomen; fade it toward the skull and planted feet. Give organic parts different pivots, axes, phases, and modest amplitudes. A blink or jaw movement stays local to the face.

Use `assets/ivysaur.spec.json` as the field example. Its numbers are **not** universal defaults. Match region centers and radii to the new image. Keep the first frame near the reference pose; movement should be noticeable within about two seconds without requiring a two-second cycle.

For a simple background, let GrabCut infer the whole creature silhouette. When it cuts off feet/fur or includes background, supply a corrected alpha mask with `--mask`. A matching clean background plate can be supplied with `--background`; otherwise the renderer inpaints the subject area.

## Render and review

Run:

```text
python scripts/render.py --input <image> --spec <spec.json> --output <loop.gif> --contact-sheet <review.jpg>
```

Dependencies: Python, `opencv-python`, `numpy`, `Pillow`.

Inspect the animation itself and the contact sheet at normal viewing size. Check that the skull and feet stay stable, chest movement reads as breathing rather than whole-body inflation, plant/soft parts move around their roots, and no doubled edges or detached body patches appear. Use `loop_mode: cyclic` for a closed forward path: the exact first/last pose matches while offset sway axes continue through the seam. Use `boomerang` only if the user wants a deliberate return along the same path. If these checks fail, adjust the spec or mask and render again. Stop when the shot reads naturally; don't make every part move just because it is available.

Deliver the loop plus its source spec. Mention any remaining visual limitations honestly. `scripts/render.py` is the portable motion engine; the Ivysaur spec is only one preset.
