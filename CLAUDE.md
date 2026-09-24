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
- Khoanh vùng ảnh thở bằng chuột → `PYTHONUTF8=1 python tools/motion-studio.py <ảnh>`.
- Người dùng nói **"xong"** (xong ý tưởng · kịch bản · refs · ảnh · clip · earth · giọng…) → `/xong`,
  bảng từ khoá và luật đặt tên ở [docs/HANDOFF.md](docs/HANDOFF.md).
- Luồng kịch bản năm bước (Gemini ý → Claude khung → Gemini lời → Claude chuẩn hoá → người duyệt):
  bản dán cho Gemini ghép bằng `tools/handoff.py <slug> --brief ideas|script`, không viết tay.
- Duyệt kịch bản + cảnh dự kiến → `PYTHONUTF8=1 python tools/review-page.py <slug>`, đăng Artifact có
  capability `db`, đọc lại Duyệt / Cần sửa ở collection `review`.
- Đăng xong thì sao lưu → `PYTHONUTF8=1 python tools/backup-episode.py <slug> --to "<Drive>"`.
- **Luôn** chạy `PYTHONUTF8=1 python tools/check-episode.py <slug>` trước khi thu giọng hoặc render.
- Bài học từ các vòng duyệt nằm ở [docs/DNA.md](docs/DNA.md) — đọc trước khi viết hoặc duyệt; góp ý
  mới lộ ra lỗi mới thì đóng gói vào đó (lỗi → luật → chỗ ép: brief · máy · checklist).

## Luật của kênh, không thương lượng

- Người dẫn là **Dr. Holth**, nhà sinh vật học thực địa của thế giới chúng ta — xem
  [docs/NARRATOR.md](docs/NARRATOR.md). Xưng "tôi", **không bao giờ nói tên mình**; tên chỉ hiện bằng
  chữ trên bìa sổ và chữ ký. ⛔ **Không bao giờ hiện "Gilbert"** — "Gilbert D. Holth" là đảo chữ của
  "Blight Lord", cú lật của game Blightfall. "Tuấn La" **không xuất hiện trong video**, chỉ ở mô tả
  YouTube.
- Không nhắc game, không nhắc AI, không nhắc đoàn làm phim. Pokédex gọi là "cuốn danh lục".
- Ba nhãn không được trộn: 📖 danh lục (phải có nguồn trong `NGUON`) · 👁 quan sát · 🔬 giả thuyết
  (phải kèm một loài có thật ở Trái Đất).
- **Cảnh tiến hoá không có lột da.** Chỉ sưng nở, sức nặng, ánh sáng, bóng dáng, dấu vết.
- Mọi khả năng phải nêu **cái giá** của nó.
- **Không đặt tên riêng cho con vật.** Cá thể trung tâm = **đặc điểm canon + mã thực địa**
  (`Shiny Bulbasaur · K-01`) — ưu tiên Shiny. Con khác gọi bằng tên loài; con phụ quay lại nhiều lần
  thì cho mã (`K-04`), vẫn không đặt tên. Đặc điểm **chỉ được gọi sau khi** khán giả đã thấy nó.
  "Shiny" là từ của người bản xứ, nói một lần rồi dùng mã. Xem [docs/CAST.md](docs/CAST.md).
- Địa danh phải có **dẫn chứng canon** (game + phiên bản · anime + số tập · manga + chương). **Không
  bịa địa danh** khi canon đã có (Kanto → Viridian Forest).
- **Giải phẫu**: được bàn và được vẽ, nhưng theo lối nghiên cứu — dạng X-quang mô phỏng, nền xanh,
  xương, mạch năng lượng chạy trong thân; vết thương nhỏ trên da thì được. Không máu me, không nội
  tạng, không mổ xẻ. Cảnh ghép đôi dừng ở phô diễn, làm tổ, chăm con.

## Bố cục

```
videos/<slug>/     content.py (lời) · scenes.json (hình) · thumb.json · timings.json
bible/             style.json · creatures/<loài>.json · shots/<ep>.json
                   locations/<nơi>.json · refs/<loài>/refs.json   (ảnh tham chiếu KHÔNG nằm trong git)
prompts/           sinh ra từ bible, đừng sửa tay
public/            img/<ep>/ · video/<ep>/ · audio/sfx/<ep>/   (ảnh và clip KHÔNG nằm trong git)
docs/              PIPELINE · BUSINESS-FLOW · HANDOFF · DNA · VOICE · briefs/ · CHANNEL-SETUP · SLATE · CREATURE-LENS
                   IDEA-BANK · CAST · SOUND · EPISODE-FRAME · SCENE-TYPES
tools/             build-prompts.mjs · import-flow.py · unwatermark.py · export-subs.py
                   check-episode.py · review.py · backup-episode.py · motion-studio.py · handoff.py
                   review-page.py (trang duyệt) · templates/
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
- Engine đang nối vào worktree `blog2video/.claude/worktrees/specimen-media` (nhánh
  `feat/specimen-freeze-media`: notepage + dừng hình + ảnh quê nhà), **chưa gộp vào `main` của
  engine**. Sửa engine xong phải `node scripts/build-lib.mjs` bên đó.
- Claude làm trong worktree rồi fast-forward `master`. Thư mục chính có sửa dở thì cất vào một nhánh
  `wip/…` trước khi gộp — đừng stash, đừng ghi đè.
- Không tin mục SELF-CHECK của Gemini: soát lại bằng `handoff.py --draft` và đọc bằng mắt.
