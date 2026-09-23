# Creature Field Guide — brief cho Claude

Kênh phim tài liệu tự nhiên về sinh vật hư cấu (dòng Pokédex), dựng bằng Remotion, làm **hai bản
Việt và Anh**. Đọc [README.md](README.md) để biết cửa vào, [docs/PIPELINE.md](docs/PIPELINE.md) để
biết mười một chặng làm một tập, [docs/BUSINESS-FLOW.md](docs/BUSINESS-FLOW.md) để biết toàn cảnh 52 bước
nghiệp vụ và chỗ nào còn làm tay.

## Trước khi làm gì

- Viết lời → skill `creature-field-guide-scriptwriter`. Dựng hình → `creature-field-guide-production`.
  Cho ảnh thở → `creature-motion`.
- Lên lịch, xem tập nào tới đâu → `episode-plan`. Soát kịch bản trước khi sinh ảnh → `episode-review`
  (gọi `stop-slop`). Soạn gói đăng → `episode-publish`. Tất cả nằm trong `.claude/skills/`.
- Mở tập mới → `/tap-moi <loài>`. Soát trước khi thu giọng/render → `/soat-tap <slug>`.
- Xem bản dựng và ghi chú tại chỗ → `PYTHONUTF8=1 python tools/review.py <slug>`.
- Đăng xong thì sao lưu → `PYTHONUTF8=1 python tools/backup-episode.py <slug> --to "<Drive>"`.
- **Luôn** chạy `PYTHONUTF8=1 python tools/check-episode.py <slug>` trước khi thu giọng hoặc render.

## Luật của kênh, không thương lượng

- Lời dẫn là **nhà sinh vật học thực địa của thế giới chúng ta**, xưng "tôi", **không bao giờ nói tên
  mình**. Tên thật "Tuấn La" chỉ hiện dưới dạng chữ trên màn hình và ở credit.
- Không nhắc game, không nhắc AI, không nhắc đoàn làm phim. Pokédex gọi là "cuốn danh lục".
- Ba nhãn không được trộn: 📖 danh lục (phải có nguồn trong `NGUON`) · 👁 quan sát · 🔬 giả thuyết
  (phải kèm một loài có thật ở Trái Đất).
- **Cảnh tiến hoá không có lột da.** Chỉ sưng nở, sức nặng, ánh sáng, bóng dáng, dấu vết.
- Mọi khả năng phải nêu **cái giá** của nó.
- **Tên và địa danh lấy tiếng Anh làm gốc**, là **danh từ chỉ một dấu tích nhìn thấy được**
  (Crookedbud, Scar-Shoulder, Ash-Eye, Moss-Back), và **chỉ được gọi sau khi** khán giả đã thấy cái
  dấu ấy. Mọi tên gọi và địa danh phải có **dẫn chứng canon**: game + phiên bản · anime + số tập ·
  manga + chương. **Không bịa địa danh** khi canon đã có (Kanto → Viridian Forest). Mã thực địa
  (K-01) là neo giữa hai bản: **màn hình ghi tên EN, giọng VI đọc tên VI**.
- **Giải phẫu**: được bàn và được vẽ, nhưng theo lối nghiên cứu — dạng X-quang mô phỏng, nền xanh,
  xương, mạch năng lượng chạy trong thân; vết thương nhỏ trên da thì được. Không máu me, không nội
  tạng, không mổ xẻ. Cảnh ghép đôi dừng ở phô diễn, làm tổ, chăm con.

## Bố cục

```
videos/<slug>/     content.py (lời) · scenes.json (hình) · thumb.json · timings.json
bible/             style.json · creatures/<loài>.json · shots/<ep>.json
prompts/           sinh ra từ bible, đừng sửa tay
public/            img/<ep>/ · video/<ep>/ · audio/sfx/<ep>/   (ảnh và clip KHÔNG nằm trong git)
docs/              PIPELINE · BUSINESS-FLOW · CHANNEL-SETUP · SLATE · CREATURE-LENS
                   IDEA-BANK · CAST · SOUND · EPISODE-FRAME · SCENE-TYPES
tools/             build-prompts.mjs · import-flow.py · unwatermark.py · export-subs.py
                   check-episode.py · review.py · backup-episode.py
experiments/       ghi chép những thứ đã thử và giới hạn của chúng
```

Engine dựng video là **blog2video**, nối bằng `file:` trong `package.json` trỏ sang
`D:\Users\tuanla2\blog2video`. Tính năng dùng chung cho mọi kênh thì sửa bên engine; nội dung của
kênh thì nằm ở đây. Engine là repo công khai — **đừng đưa nội dung Pokémon sang đó**.

## Gotcha hay cắn

- Console Windows là cp1252 → mọi lệnh Python phải có `PYTHONUTF8=1`.
- Render chết ở `SELF_SIGNED_CERT_IN_CHAIN` là do **mạng công ty chặn TLS**, không phải lỗi Remotion:
  nó đang tải Chrome Headless Shell. Dùng Chrome cài sẵn là hết, `remotion.config.ts` đã có sẵn móc:
  `setx CHROME "C:\Program Files\Google\Chrome\Application\chrome.exe"` (mở lại terminal sau khi
  chạy). `npm run studio` **không** dính lỗi này vì nó chạy trong trình duyệt của bạn.
- Sửa `content.py` thì phải `npm run scaffold -- <slug>` rồi `python tools/export-subs.py <slug>`,
  không thì timing và phụ đề vẫn là của bản cũ.
- `_note` trong `scenes.json` **không được chứa dấu ngoặc kép** — hỏng JSON.
- Toạ độ callout đo **trên ảnh thật**, sau khi ảnh đã chốt. Sinh lại ảnh là phải đo lại.
- Google Flow: pane trình duyệt bị ẩn thì tab treo I/O và mọi ảnh báo "Failed to load image" —
  không phải lỗi phía Google.
