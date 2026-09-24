---
description: Người dùng vừa làm xong một việc tay — tìm xem cái gì vừa tới, nạp vào đúng chỗ, làm bước kế tiếp
argument-hint: (để trống) · ý tưởng · kịch bản · refs · ảnh mẫu · ảnh · clip · earth · giọng · duyệt · đăng
---

Người dùng báo xong: **$ARGUMENTS**

Bảng từ khoá và luật đặt tên: [docs/HANDOFF.md](../../docs/HANDOFF.md). Tập đang chạy: xem
`docs/SLATE.md` (WIP = 1, nên thường chỉ có một).

1. Xem trước, chưa đụng file nào:

   ```bash
   PYTHONUTF8=1 python tools/handoff.py <slug>
   PYTHONUTF8=1 python tools/handoff.py <slug> --take --dry-run
   ```

2. Có file khớp thì nạp thật (`--take`). Có file **không rõ** thì hỏi người dùng nó là gì, đừng đoán
   một id rồi đặt vào.
3. Làm bước kế tiếp đúng cột "Claude làm tiếp" trong HANDOFF.md:
   - `ý tưởng` → chấm sáu ý, chọn một kèm lý do và dự phòng, tra canon, viết `2-skeleton.md`, rồi
     `--brief script`. Chi tiết: lệnh `/tap-moi` bước 2.
   - `kịch bản` / `gemini` → `--draft`, đọc hết theo skill `episode-review`, chuẩn hoá vào `content.py`,
     ghi `4-review.md`. Không sửa nguyên văn của Gemini trong `3-script-gemini*.md`.
   - `ảnh` / `ảnh mẫu` → `tools/unwatermark.py <ep>`, rồi **cho người dùng xem ảnh** trước khi đo toạ
     độ hay chạy loạt tiếp. Ảnh mẫu hỏng thì mọi cảnh ăn theo đều hỏng.
   - `âm` → không phải việc của tool này, chạy `/nap-am`.
4. Báo lại ngắn gọn: đã nạp gì, còn thiếu gì, bước tiếp là của ai.

Không tự sinh ảnh, không tự render, không tự đăng. Mỗi loạt tốn credit Flow/Veo/Seedance phải hỏi trước.
