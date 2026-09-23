---
description: Mở một tập mới — từ ý tưởng tới bộ prompt ảnh, theo đúng dây chuyền của kênh
argument-hint: <loài hoặc số dex, vd "0004 Charmander">
---

Mở tập mới cho **$ARGUMENTS**.

Đọc trước, theo thứ tự: `docs/PIPELINE.md` (chặng 1–4), `docs/CREATURE-LENS.md`, `docs/IDEA-BANK.md`,
`docs/CAST.md`. Dùng skill `creature-field-guide-scriptwriter` để viết, `creature-field-guide-production`
để soạn shot.

Làm đúng bốn chặng đầu, dừng lại ở cổng của chặng 4 rồi báo cáo — **đừng sinh ảnh**, đó là việc tốn
tiền và cần người duyệt.

1. **Ý tưởng.** Chọn từ IDEA-BANK nếu đã có mục cho loài này, không thì soi qua 16 trục của
   CREATURE-LENS và đề xuất 3 hướng, kèm câu hỏi mở màn của từng hướng. **Hỏi tôi chọn hướng nào
   trước khi viết.**
2. **Canon.** Tra Bulbapedia từng mục danh lục. Mọi câu lấy từ đó phải vào `NGUON` kèm nguồn; mọi
   suy đoán phải kèm một loài có thật ở Trái Đất. Cập nhật `bible/creatures/<loài>.json`
   (anchor, appearance, sexDifferences, forbidden) và khai `individuals` cho cá thể trung tâm nếu nó
   có dấu riêng.
3. **Kịch bản.** `videos/<slug>/content.py`: `ORDER`, `BEATS` (nhớ `short-outro`), `PRON`, `NGUON`.
   Tên nhân vật đặt theo vết tích hoặc hành vi, là danh từ, và **chỉ xuất hiện sau khi khán giả đã
   thấy cái dấu ấy**. Ghi vào `docs/CAST.md` cả cột VI và EN. Người dẫn xưng "tôi", không nói tên.
4. **Shot.** `bible/shots/<ep>.json` rồi `node tools/build-prompts.mjs <ep>`. Mỗi beat ít nhất một
   shot; mỗi dấu tích dùng để đặt tên phải có một shot cận cảnh riêng.

Rồi chạy `PYTHONUTF8=1 python tools/check-episode.py <slug>` và báo cáo: hướng đã chọn, cấu trúc tập,
những chỗ canon mỏng phải dùng giả thuyết, số shot, và những gì còn thiếu trước khi sinh ảnh.
