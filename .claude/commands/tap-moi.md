---
description: Mở một tập mới — luồng kịch bản năm bước (Gemini ý tưởng → Claude khung → Gemini lời → Claude chuẩn hoá → người duyệt)
argument-hint: <loài hoặc số dex, vd "#0004 Charmander">
---

Mở tập mới cho **$ARGUMENTS**.

Trước tiên: **WIP = 1.** Chạy skill `episode-plan` — tập đang chạy chưa qua cổng chặng 10 thì dừng
lại và nói rõ nó đang kẹt ở đâu, đừng mở tập mới.

Đọc: `docs/PIPELINE.md` (chặng 1–4), `docs/HANDOFF.md` (luồng năm bước và tên file),
`docs/CREATURE-LENS.md`, `docs/EPISODE-FRAME.md`, `docs/CAST.md`.

Slug theo mẫu `<vùng>-<số>-<loài>` (vd `kanto-004-charmander`).

1. **Bước 1 · ý tưởng.** `PYTHONUTF8=1 python tools/handoff.py <slug> --brief ideas "$ARGUMENTS"`.
   Đọc lại `drafts/1-ideas-brief.md` một lượt (phần "What the channel already knows" lấy tự động từ
   IDEA-BANK và SLATE — sửa nếu lệch), rồi **dừng**: đưa người dùng bản dán, chờ “xong ý tưởng”.
2. **Bước 2 · khung** (sau “xong ý tưởng”). Chấm sáu ý theo năm tiêu chí (PIPELINE chặng 1), chọn
   một, nêu lý do, giữ một ý dự phòng. Tra canon trên Bulbapedia cho **từng** câu định đưa vào bảng
   nguồn — Gemini hay bịa canon, đừng chép nguồn nó ghi. Cập nhật `bible/creatures/<loài>.json`
   (anchor, appearance, sexDifferences, forbidden, `individuals.K-01` với `trait`), `bible/refs/`,
   `bible/locations/`. Viết `drafts/2-skeleton.md` theo mẫu của tập 001 (dòng `<!-- handoff: … -->`,
   bảng nguồn, so sánh lõi/tuỳ chọn, chỗ dừng hình, beat gợi ý, `who`/`loc`). Rồi
   `--brief script`, và **dừng**: chờ “xong kịch bản”.
3. **Bước 4 · chuẩn hoá** (sau “xong kịch bản”). `--draft`, rồi đọc hết theo skill `episode-review`.
   Ghi `content.py` (`BEATS` VI + `BEATS_EN`) và `drafts/4-review.md`. Chạy `check-episode.py`.
   Soạn `drafts/4-scene-plan.json` (cảnh dự kiến từng beat + ảnh mẫu, **kèm cờ DNA** `incident` ·
   `promise` · `sets`/`pays` · `change` — [docs/DNA.md](../../docs/DNA.md)). Khai `RESERVED` / `SPINE_KEY`
   trong `content.py`. `check-episode.py` phải sạch mọi dòng `DNA`, rồi chạy
   `tools/review-page.py <slug>`, đăng `out/<slug>/review.html` thành Artifact có `capabilities: {db: {}}`,
   đưa link. **Dừng** chờ người duyệt bấm Duyệt / Cần sửa trên trang.
4. **Sau “duyệt”** (đọc collection `review`; beat cần sửa thì sửa và đăng lại cùng link): ghi
   `Đã duyệt: <ngày>` vào `4-review.md`, soạn `bible/shots/<ep>.json` từ cảnh dự kiến, chạy
   `node tools/build-prompts.mjs <ep>`, báo số shot, số ảnh mẫu phải sinh trước và những gì còn thiếu.

**Không sinh ảnh, không render, không đăng.** Mỗi loạt tốn credit phải hỏi trước.
