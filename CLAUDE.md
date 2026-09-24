# Creature Field Guide — brief cho Claude

Kênh phim tài liệu tự nhiên về sinh vật hư cấu (dòng Pokédex), dựng bằng Remotion, làm **hai bản
Việt và Anh**. Đọc [README.md](README.md) để biết cửa vào, [docs/PIPELINE.md](docs/PIPELINE.md) để
biết mười chặng làm một tập, [docs/BUSINESS-FLOW.md](docs/BUSINESS-FLOW.md) để biết toàn cảnh 33 bước
nghiệp vụ và chỗ nào còn làm tay.

## Trước khi làm gì

- Viết lời → skill `creature-field-guide-scriptwriter`. Dựng hình → `creature-field-guide-production`.
  Cho ảnh thở → `creature-motion`. Cả ba nằm trong `.claude/skills/`.
- Mở tập mới → `/tap-moi <loài>`. Soát trước khi thu giọng/render → `/soat-tap <slug>`.
- **Luôn** chạy `PYTHONUTF8=1 python tools/check-episode.py <slug>` trước khi thu giọng hoặc render.

## Luật của kênh, không thương lượng

- Lời dẫn là **nhà sinh vật học thực địa của thế giới chúng ta**, xưng "tôi", **không bao giờ nói tên
  mình**. Tên thật "Tuấn La" chỉ hiện dưới dạng chữ trên màn hình và ở credit.
- Không nhắc game, không nhắc AI, không nhắc đoàn làm phim. Pokédex gọi là "cuốn danh lục".
- Ba nhãn không được trộn: 📖 danh lục (phải có nguồn trong `NGUON`) · 👁 quan sát · 🔬 giả thuyết
  (phải kèm một loài có thật ở Trái Đất).
- **Cảnh tiến hoá không có lột da.** Chỉ sưng nở, sức nặng, ánh sáng, bóng dáng, dấu vết.
- Mọi khả năng phải nêu **cái giá** của nó.
- Tên nhân vật, địa danh base tiếng Anh làm gốc (Saur, Scar-Shoulder, Ash-Eye, Moss-Back; Viridian Forest),
  chỉ danh từ chỉ một dấu tích nhìn thấy được hoặc phong cách Trainer canon. Mọi tên gọi và địa danh
  phải có lý do sinh học và DẪN CHỨNG CANON (Game, Anime, Manga). Mã thực địa (K-01) là neo giữa bản VI và EN.
- Không làm giải phẫu, mổ xẻ. Cảnh ghép đôi dừng ở phô diễn, làm tổ, chăm con.

## Bố cục

```
videos/<slug>/     content.py (lời) · scenes.json (hình) · thumb.json · timings.json
bible/             style.json · creatures/<loài>.json · shots/<ep>.json
prompts/           sinh ra từ bible, đừng sửa tay
public/            img/<ep>/ · video/<ep>/ · audio/sfx/<ep>/   (ảnh và clip KHÔNG nằm trong git)
docs/              PIPELINE · BUSINESS-FLOW · CREATURE-LENS · IDEA-BANK · CAST · SOUND · EPISODE-FRAME
tools/             build-prompts.mjs · import-flow.py · unwatermark.py · export-subs.py · check-episode.py
experiments/       ghi chép những thứ đã thử và giới hạn của chúng
```

Engine dựng video là **blog2video**, nối bằng `file:` trong `package.json` trỏ sang
`D:\Users\tuanla2\blog2video`. Tính năng dùng chung cho mọi kênh thì sửa bên engine; nội dung của
kênh thì nằm ở đây. Engine là repo công khai — **đừng đưa nội dung Pokémon sang đó**.

## Gotcha hay cắn

- Console Windows là cp1252 → mọi lệnh Python phải có `PYTHONUTF8=1`.
- Sửa `content.py` thì phải `npm run scaffold -- <slug>` rồi `python tools/export-subs.py <slug>`,
  không thì timing và phụ đề vẫn là của bản cũ.
- `_note` trong `scenes.json` **không được chứa dấu ngoặc kép** — hỏng JSON.
- Toạ độ callout đo **trên ảnh thật**, sau khi ảnh đã chốt. Sinh lại ảnh là phải đo lại.
- Google Flow: pane trình duyệt bị ẩn thì tab treo I/O và mọi ảnh báo "Failed to load image" —
  không phải lỗi phía Google.
