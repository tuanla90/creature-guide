# Dựng kênh · làm một lần

Checklist cho cụm 0 của [BUSINESS-FLOW.md](BUSINESS-FLOW.md). Kênh lập mới từ đầu.

**Thứ tự ở đây có ràng buộc thật**, không phải xếp cho gọn: multi-audio cần Advanced features, mà
Advanced features cần xác minh danh tính. Làm sai thứ tự thì phát hiện lúc sắp đăng tập đầu, và lúc
đó phải chờ.

---

## 1 · Lập kênh

- [ ] Tạo kênh mới (đừng dùng kênh cá nhân đã có — kênh riêng thì lịch sử xem của bạn không làm
      nhiễu tín hiệu khán giả mà YouTube học).
- [ ] **Tên kênh** và **handle** `@…`. Đặt tên đi được với cả Pokémon lẫn thần thoại: Kanto chỉ là
      mùa đầu, 8–9 tháng nữa kênh sẽ nói về rồng và kỳ lân. Tên có chữ "Pokémon" là tự khoá mình.
- [ ] Avatar, banner.
- [ ] **Mô tả kênh**, hai ngôn ngữ. Phải nói rõ: phim tài liệu **giả tưởng** về sinh vật hư cấu,
      góc nhìn sinh học, không liên kết với chủ sở hữu nguồn.
- [ ] **Ngôn ngữ kênh** — đặt theo quyết định ở mục 3 dưới.

## 2 · Mở khoá multi-audio

- [ ] Xác minh danh tính / số điện thoại trong YouTube Studio.
- [ ] Bật **Advanced features**.
- [ ] Kiểm: trong trình đơn phụ đề của một video nháp đã thấy mục nạp **audio track** chưa.

> **Cổng:** chưa thấy mục nạp audio track thì toàn bộ kế hoạch "một kênh hai thứ tiếng" chưa đứng
> được. Phát hiện bây giờ thì chỉ là chờ; phát hiện lúc tập đầu render xong thì là hỏng kế hoạch.

Nhắc lại giới hạn đã biết: thumbnail theo ngôn ngữ **chỉ có ở video dài**, Shorts không có.

## 3 · Chốt track gốc: VI hay EN

Vẫn treo. Hai hướng, hai hệ quả:

| Chọn | Được | Mất |
|---|---|---|
| **Gốc EN** | khớp với việc kịch bản viết EN trước; YouTube coi kênh là kênh tiếng Anh, tệp rộng hơn | tệp Pokémon Việt là nhóm kéo sub giai đoạn đầu, lại thành track phụ |
| **Gốc VI** | đúng tệp khán giả của 8–9 tháng đầu | lệch với ngôn ngữ bản gốc của kịch bản |

Đây là thứ **khó đổi sau**, nên quyết trước tập đầu. Không có phương án nào sai rõ ràng; chọn theo
việc sáu tháng đầu bạn muốn ai xem.

## 4 · Kiếm tiền — chưa phải bây giờ

Kênh mới thì chưa vào được YouTube Partner Program. Nhưng ghi ra đây vì **nó đổi mức rủi ro**: khi
kênh bắt đầu có tiền, câu "file này ở đâu ra, ai cho phép dùng" thành câu bắt buộc trả lời được cho
**từng** file.

- [ ] Từ tập đầu tiên đã ghi sổ tài sản, đừng đợi tới lúc đủ điều kiện mới ghi ngược.
- [ ] Kiểm điều khoản của Lyria/Gemini cho video có kiếm tiền, ghi ngày kiểm (xem
      [SOUND.md](SOUND.md)).

## 5 · Việc trong repo

- [x] Khung tập thứ hai — [EPISODE-FRAME.md](EPISODE-FRAME.md) khung B.
- [x] `CREATURE-LENS.md` trung lập với Pokémon.
- [x] Skill `episode-plan`, `episode-review`, `episode-publish`, `stop-slop`.
- [x] `tools/review.py` — xem bản dựng, ghi chú, lấy toạ độ callout.
- [x] `tools/backup-episode.py` — sao lưu một chiều.
- [ ] Thư viện nhạc: bảy bản trong [SOUND.md](SOUND.md) — chưa sinh.
- [ ] Chọn thư mục Drive và đặt `CFG_BACKUP_DIR`, chạy thử một lần với tập 001.

## 6 · Mỗi tập đăng xong

Không thuộc cụm 0 nhưng hay quên, nên để ở đây:

- [ ] Bật khai báo **nội dung tổng hợp bằng AI**.
- [ ] Nạp track giọng thứ hai + tiêu đề/mô tả/thumbnail bản địa hoá.
- [ ] `python tools/backup-episode.py <slug> --to "<Drive>"`.

---

## Theo dõi để biết lúc nào rẽ nhánh

Điều kiện rẽ khỏi Pokémon sang nhóm phạm vi công cộng là **sự kiện, không phải ngày**. Có nghĩa là
phải có người nhìn. Rà cùng lúc với lịch (skill `episode-plan`):

- [ ] Có claim bản quyền, strike, hay video bị gỡ nào không?
- [ ] Số sub — đã tới ngưỡng tự đặt chưa?
- [ ] Số giờ xem — có đủ để một kênh chủ đề khác đứng được chưa?

Ghi ngày rà và kết quả vào [SLATE.md](SLATE.md). Không ghi thì sáu tháng sau không ai nhớ đã rà chưa.
