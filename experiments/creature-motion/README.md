# Ảnh tĩnh thở được

Thử nghiệm: biến ảnh Flow thành một vòng lặp động nhẹ, để cảnh đứng không còn là một bức ảnh chết.
Không gọi model nào, chỉ làm biến dạng cục bộ bằng OpenCV — chạy offline, không tốn credit.

Skill: `.claude/skills/creature-motion/`. Chạy:

```bash
PYTHONUTF8=1 python .claude/skills/creature-motion/scripts/render.py \
  --input public/img/kanto-001/s02-bulbasaur-plate.jpg \
  --spec  .claude/skills/creature-motion/assets/bulbasaur-plate.spec.json \
  --output out/s02.gif --contact-sheet experiments/creature-motion/s02-plate-contact.jpg
```

rồi đổi sang mp4 (dùng ffmpeg đi kèm Remotion, máy không cần cài riêng):

```bash
npx remotion ffmpeg -y -i out/s02.gif -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" \
  -c:v libx264 -crf 19 -pix_fmt yuv420p -movflags faststart public/video/kanto-001/s02-plate-breath.mp4
```

## Đã dựng

| Clip | Từ ảnh | Cái gì động |
|---|---|---|
| `s02-plate-breath.mp4` | `s02-bulbasaur-plate` | ngực phập phồng, mắt khép nhẹ, củ hơi lay — đầu và bốn chân đứng yên |
| `n03-nest-breath.mp4` | `n03-nest-guarded` | con mẹ thở, lá quanh tổ lay; trứng **không** được động |
| `n12-ivysaur-breath.mp4` | `n12-ivysaur-plate` | thở, lá trái/phải và hoa lệch pha nhau |

Ảnh `*-contact.jpg` ở đây là bản soát bốn khung — xem ở cỡ thật để bắt lỗi mép đôi và thân tách mảng.

## Ba luật rút ra

1. **Mỏ neo trước, chuyển động sau.** Xác định sọ, chỗ chân chạm đất, gốc của từng bộ phận rồi mới
   cho cái gì lay. Cho cả thân phồng lên là thành đồ chơi bơm hơi.
2. **`composite_mode: warp_only` cho cảnh có nền phức tạp** (tổ, lá, trứng chồng nhau). Chế độ
   `cutout` cắt nền bằng GrabCut, chỉ hợp khi con vật nằm trên nền trơn — không thì lộ viền.
3. **Đừng cho mọi thứ động chỉ vì nó động được.** Cảnh đọc tự nhiên thì dừng.

## Giới hạn đã biết

- Ảnh nguồn của tập 1 chỉ 1376×768 nên clip cũng vậy. Trên timeline 1920×1080 là phóng 1,4×; **đừng
  lia/phóng thêm** trên mấy clip này. Ảnh từ 2400 px trở lên thì thoải mái hơn.
- `s02-plate-breath` dựng từ ảnh mẫu **củ mọc thẳng**. Sinh lại ảnh mẫu có củ nghẹo (Búp Lệch) thì
  phải render lại clip này, không thì hai cảnh không khớp nhau.
- Đây là biến dạng 2D. Đổi góc máy hay pose thật thì cần dựng 3D — xem `img2threejs` bên
  `re-engineering/` (repo ngoài, không thuộc dự án này).

## Lớp tách nền

`public/img/kanto-001/layers/` là Ivysaur đã tách thành thân, lá trái, lá phải, hoa và một tấm nền
sạch. Dùng cho element `world` để có parallax thật (mỗi lớp một `depth` và một `sway`), thay vì
Ken Burns trên một ảnh phẳng. Mấy file này cắt bằng tay, không sinh lại tự động được — đừng xoá.
