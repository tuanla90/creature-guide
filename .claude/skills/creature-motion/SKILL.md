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

Use `assets/ivysaur.spec.json` as a field example, `assets/bulbasaur-plate.spec.json` for a standing creature with a fixed head/feet, and `assets/nest-guarded.spec.json` for a crouching subject among eggs and foliage. Their numbers are **not** universal defaults. Match region centers and radii to the new image. Keep the first frame near the reference pose; movement should be noticeable within about two seconds without requiring a two-second cycle.

Choose compositing before rendering. `composite_mode: warp_only` deforms only local image regions and leaves the rest of the original frame intact. Prefer it for foliage, nests, overlapping eggs, cropped anatomy, or subtle motion where a cutout boundary would show. Keep each motion region away from rigid contacts and unrelated objects. `composite_mode: cutout` lets GrabCut infer the creature silhouette for a clear subject on a simple background; supply a corrected alpha mask with `--mask` if its outline is wrong. A matching clean background plate can be supplied with `--background`; otherwise the renderer inpaints the subject area.

## Render and review

Run:

```text
python scripts/render.py --input <image> --spec <spec.json> --output <loop.gif> --contact-sheet <review.jpg>
```

Dependencies: Python, `opencv-python`, `numpy`, `Pillow`.

Inspect the animation itself and the contact sheet at normal viewing size. Check that the skull, planted feet, eggs and nest stay stable; chest movement reads as breathing rather than whole-body inflation; plant/soft parts move around their roots; and no doubled edges or detached body patches appear. Keep the head shape and crown stable. Use `loop_mode: cyclic` for a closed forward path: the exact first/last pose matches while offset sway axes continue through the seam. Use `boomerang` only if the user wants a deliberate return along the same path. If these checks fail, adjust the spec, compositing mode or mask and render again. Stop when the shot reads naturally; don't make every part move just because it is available.

Deliver the loop plus its source spec. Mention any remaining visual limitations honestly. `scripts/render.py` is the portable motion engine; the Ivysaur spec is only one preset.

## Hai thứ hay sai, và cách bắt bằng số

**1 · `face_side` — con vật quay đầu sang đâu.**
`anchors.face_fade` che một phía để hơi thở không lan lên đầu, nhưng nó **mặc định giả sử đầu ở bên
phải khung**. Ảnh nào con vật quay đầu sang trái thì phải khai `"face_side": "left"`, nếu không mặt
nạ sẽ che **đúng cái sườn cần thở** và để nguyên cái sọ.

Dấu hiệu: **sọ lệch ngang hoặc hơn sườn**. Đã dính thật ở `s04-bulbasaur-sunbath` — sọ 2,78 còn
sườn chỉ 1,01. Khai `face_side: "left"` là đảo lại ngay.

**2 · Đừng nghiệm thu bằng mắt trên contact sheet.** Chênh vài pixel thì mắt không thấy, nhưng chạy
ở tốc độ thật lại thành cả con vật phồng lên. Đo:

```bash
PYTHONUTF8=1 python .claude/skills/creature-motion/scripts/check-motion.py out/<shot>.gif   --still "SỌ=0.46,0.42,0.68,0.62" --still "CHÂN=0.44,0.80,0.90,0.88" --still "NỀN=0,0.88,1,1"   --move  "SƯỜN=0.72,0.60,0.88,0.85" --move "CỦ=0.57,0.16,0.87,0.50"
```

Dáng số ĐÚNG: vùng phải-động lệch **gấp vài lần** vùng phải-đứng-yên.

| | sọ | chân | nền | sườn | củ |
|---|---|---|---|---|---|
| sai (`face_side` thiếu) | 2,78 | 1,23 | 0,18 | 1,01 | 5,23 |
| đúng | **0,58** | **0,59** | **0,20** | **4,16** | **2,22** |

## Khoanh vùng bằng chuột thay vì đoán số

```bash
PYTHONUTF8=1 python tools/motion-studio.py public/img/<ep>/<shot>.jpg
```

Kéo chuột khoanh elip → tâm và sigma. Kéo từ tâm ra → hướng và biên độ. Chọn kiểu, kéo thanh cắt,
bấm **Render thử**, xem mp4 ngay trong trang. Ưng thì **Lưu spec**.

Đặt toạ độ bằng cách đoán số trong JSON rồi render lại để xem là vòng lặp rất chậm, và **người nhìn
ảnh thì biết ngay chỗ nào phải thở, chỗ nào phải đứng yên — máy thì không**. Spec lưu kèm khoá
`_studio` để mở lại còn sửa tiếp đúng những hình đã vẽ.

## Cổng màu là con dao hai lưỡi

`color_gate: "green"` tính theo `(G−R)` và `(G−B)`. Phần lá **đang cháy nắng** ngả vàng-trắng nên
`R ≈ G`, cổng trả về gần 0 và **loại mất đúng nửa đó** — kết quả là củ chỉ lắc nửa bên trong bóng
râm, nhìn rất sai. Đã dính thật ở `s04-bulbasaur-sunbath`: bỏ cổng màu thì nửa củ ăn nắng từ ~0
lên 21,0.

Tương tự, `"bright"` bắt **mọi** thứ sáng — kể cả cái mặt con vật đang được nắng chiếu. Dùng `fade`
khoanh biên thì chắc hơn cổng màu; cổng màu chỉ nên dùng khi màu thật sự tách bạch.
