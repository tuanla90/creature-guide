---
description: Review nội dung kịch bản Creature Field Guide như chuyên gia tài liệu sinh vật fantasy, không review UI hay code
argument-hint: <file HTML/Markdown/Python hoặc slug tập>
---

Review **nội dung** của **$ARGUMENTS** trong vai biên tập viên phim tài liệu tự nhiên và chuyên gia
worldbuilding sinh vật fantasy.

Đây là review biên tập **chỉ đọc**. Không đánh giá giao diện trang review, CSS, HTML, JavaScript hay
chất lượng code. Không tự sửa file và không chạy pipeline sản xuất trừ khi người dùng yêu cầu rõ.

## Lấy nội dung cần review

- Nếu đối số là file HTML trang duyệt, trích dữ liệu kịch bản trong `const DATA`: tiêu đề, beat, lời EN,
  lời VI, caption và mô tả cảnh. Bỏ toàn bộ UI/code.
- Nếu là slug, ưu tiên bản mới nhất theo thứ tự: `drafts/*review*.md` hoặc `drafts/*review*.html`, rồi
  `content.py`, `drafts/*script*.md`, `drafts/*skeleton*.md`.
- Nếu có cả EN và VI, review tính nhất quán của hai bản nhưng coi EN là bản gốc theo quy ước dự án.
- Đọc thêm `bible/creatures/<loài>.json`, `NGUON` trong `content.py`, và các file nguồn liên quan nếu có.

Đọc quy chuẩn tại:

- `CLAUDE.md`
- `docs/CREATURE-LENS.md`
- `docs/EPISODE-FRAME.md`
- `docs/NARRATOR.md`
- `.claude/skills/creature-field-guide-scriptwriter/references/episode-checklist.md`

## Cách review

Đánh giá theo thứ tự ưu tiên sau:

### 1. Canon và tính trung thực

- Tách từng khẳng định thành: canon/danh lục, quan sát hư cấu, giả thuyết, hoặc trận đấu.
- Kiểm tra các dữ kiện quan trọng bằng nguồn có thể truy xuất; ưu tiên nguồn chính thức của IP và nguồn
  khoa học sơ cấp/uy tín cho loài Trái Đất.
- Chỉ ra xung đột giữa lời kể và canon/cơ chế, bao gồm khác biệt giữa các phiên bản.
- Không phản đối sáng tạo chỉ vì nó không có trong canon. Chỉ yêu cầu hạ giọng thành giả thuyết khi
  bằng chứng chưa đủ.

### 2. Speculative biology

- Khả năng dùng cơ quan nào, lấy vật chất/năng lượng từ đâu, được kích hoạt thế nào, sản phẩm thừa
  thoát đi đâu, cái giá là gì và hỏng ra sao.
- Đối chiếu Trái Đất có thực sự giải thích cơ chế hay chỉ trang trí.
- Thuật ngữ giải phẫu, sinh thái, thực vật học và hành vi có chính xác không.
- Phân biệt quan sát trực tiếp với suy luận. Đặc biệt bắt các câu mở bằng quan sát nhưng kết thúc như
  một kết luận đã được chứng minh.

### 3. Câu chuyện và retention

- Hook có phải một dấu hiệu nhìn thấy được và tạo câu hỏi chưa thể trả lời ngay không.
- Có một câu hỏi xương sống hay nhiều câu hỏi tranh nhau.
- Cá thể trung tâm muốn/cần gì; áp lực nào cản nó; tình thế có tăng dần không.
- Kiến thức có xuất hiện vì cá thể vừa làm gì đó hay bị đọc như danh sách dữ kiện.
- Chỉ ra beat lặp chức năng, đoạn trũng, lời hứa bị trả quá muộn và nơi nên cài báo trước.
- Kiểm tra lời hứa của tiêu đề/thumbnail có được tập trả hay không.

### 4. Tuyến cá thể và cảm xúc

- Mỗi cá thể có mã phải quay lại và có chức năng kể chuyện.
- Chi tiết hành vi đã gieo phải có payoff nếu nó được nhấn mạnh nhiều lần.
- Cảm xúc phải đến từ hành vi quan sát được, khoảng cách, dấu vết và thay đổi, không từ việc người kể
  gán tâm lý người cho con vật.
- Dr. Holth tò mò, có thể sai và sửa sai, nhưng không can thiệp hay phán xét sinh tồn.

### 5. Lời dẫn và bản dịch

- Câu đọc thành tiếng có tự nhiên, quá dài, trùng ý hoặc quá văn viết không.
- EN và VI có cùng nghĩa, cùng mức độ chắc chắn và đủ gần thời lượng từng beat không.
- Thuật ngữ nhất quán qua các giai đoạn sống; tên riêng, mã cá thể và địa danh đúng quy ước.
- Phát hiện câu khẩu hiệu, tương phản công thức, câu hỏi tu từ dư thừa và các đoạn giải thích lại điều
  hình ảnh đã nói rõ.

### 6. Khả năng dựng nội dung

- Mỗi kết luận quan trọng có bằng chứng hình ảnh dự kiến hay không.
- Cảnh X-quang, trang sổ, freeze và loài Trái Đất có phục vụ lập luận.
- Không chấm mỹ thuật, bố cục trang web hay chất lượng prompt; chỉ báo cảnh nào không thể chứng minh
  lời dẫn hoặc dễ khiến khán giả hiểu sai.

## Đầu ra

Mở đầu bằng một kết luận biên tập ngắn: **điểm mạnh cốt lõi**, **vấn đề lớn nhất**, và bản có nên đi
tiếp sang sản xuất hay chưa.

Sau đó trình bày:

1. **Điểm đang làm tốt** — nêu chi tiết cụ thể, không khen chung chung.
2. **Phải sửa trước khi sản xuất** — findings theo mức `Nghiêm trọng / Cao / Vừa`, ghi beat hoặc trích
   câu ngắn, giải thích vì sao và đưa hướng sửa cụ thể.
3. **Nên cải thiện** — nhịp, payoff, giọng kể, thuật ngữ và các cơ hội tăng retention.
4. **Canon / giả thuyết** — bảng các claim đáng chú ý, trạng thái và cách đóng khung phù hợp.
5. **Bốn thay đổi có tác động lớn nhất** — ưu tiên theo hiệu quả, không theo thứ tự xuất hiện.
6. **Chấm điểm 10**: ý tưởng/bản sắc, worldbuilding sinh học, canon, cấu trúc, retention, cảm xúc,
   giọng tài liệu và khả năng dựng.

Khi đề xuất sửa câu, chỉ viết lại đoạn ngắn cần thiết; không tự viết lại toàn bộ tập. Dẫn link nguồn
gần claim được kiểm tra. Nếu thiếu nguồn hoặc không đọc được một phần dữ liệu, nói rõ giới hạn thay vì đoán.
