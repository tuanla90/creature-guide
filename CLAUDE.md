@AGENTS.md

# Riêng cho Claude Code

Luật chung, bản đồ đọc, bố cục và gotcha đều ở `AGENTS.md` (nhúng ở trên). Ở đây chỉ có phần dùng công
cụ riêng của Claude Code.

## Skill và lệnh (`.claude/`)

- Viết lời → skill `creature-field-guide-scriptwriter`. Dựng hình → `creature-field-guide-production`.
  Cho ảnh thở → `creature-motion`.
- Lên lịch, xem tập nào tới đâu → `episode-plan`. Soát kịch bản trước khi sinh ảnh → `episode-review`
  (gọi `stop-slop`). Soạn gói đăng → `episode-publish`.
- Mở tập mới → `/tap-moi <loài>`. Soát trước khi thu giọng / render → `/soat-tap <slug>`.
- Chỉ nghĩ và chấm ý tưởng, chưa mở tập → `/nghi-y-tuong <loài>`. Chỉ review nội dung một bản nháp hoặc
  trang duyệt, không xét UI / code → `/review-noi-dung <file hoặc slug>`.
- Người dùng nói **"xong"** (xong ý tưởng · kịch bản · refs · ảnh · clip · earth · giọng…) → `/xong`. Bảng
  từ khoá ở [docs/HANDOFF.md](docs/HANDOFF.md).
- Nạp âm thanh vừa tải → `/nap-am`.

## Trang duyệt (Artifact)

`PYTHONUTF8=1 python tools/review-page.py <slug> --img-root <thư mục ảnh thật> --out <file>`, rồi đăng
Artifact có capability `db` + `assets`. Người duyệt bấm Duyệt / Cần sửa trên trang; đọc lại ở
collection `review` (và `edits`, `picks`). Đăng lại **cùng link** (tập 001:
`https://claude.ai/artifact/MTsxXxEN591WeSxaGsRzW7`). Bản nằm trong dự án: thêm `--local --out
videos/<slug>/drafts/5-review.html --md videos/<slug>/drafts/5-review.md`.

## Công cụ cục bộ khác

- Xem bản dựng và ghi chú tại chỗ → `PYTHONUTF8=1 python tools/review.py <slug>`.
- Khoanh vùng ảnh thở bằng chuột → `PYTHONUTF8=1 python tools/motion-studio.py <ảnh>`.
- Sao lưu → `PYTHONUTF8=1 python tools/backup-all.py [--zip]` ([docs/BACKUP.md](docs/BACKUP.md)).
