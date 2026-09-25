# Thử style trang sổ của Dr. Holth (2026-09-25)

Bố cục trang sổ đã được tách khỏi style ([docs/SCENE-TYPES.md](../../docs/SCENE-TYPES.md) mục *Ngữ pháp trang
sổ*). File này chỉ thử **style**: giấy, nét, màu, độ cũ. Dán `prompts.flow.txt` vào Batch Image Studio
Pro. `style-a-sequence` lấy `style-a-hero` làm ref, nên để hai khối này trong cùng một lượt chạy.

Ba khối `*-hero` vẽ **cùng một nội dung, cùng một bố cục**, chỉ khác style, để so cho công bằng.

| id | Hướng | Hợp canon ở đâu | Rủi ro |
|---|---|---|---|
| `style-a-hero` | **A · Sổ thực địa hôm nay** — giấy chống nước kẻ lưới, chì + mực đen, **một màu nhấn xanh cyan chỉ dành cho đường năng lượng** | Dr. Holth là nhà sinh vật học *của thế giới chúng ta, bây giờ*, đi thực địa thật (sổ dính bùn, lá ép). Màu nhấn duy nhất vẽ đúng câu hỏi của ông: năng lượng chạy ở đâu trong sự sống. Màu nhấn này trùng tông với cảnh X-quang (nền xanh, mạch năng lượng), nên sổ và X-quang thành một hệ nhận diện | Ít "cổ kính" hơn, phải nhờ màu nhấn và lối vẽ để có cá tính |
| `style-b-hero` | **B · Darwin / da Vinci** — giấy ngà cũ, mực nâu, chì | NARRATOR.md đã viết "kiểu Darwin, da Vinci" cho *lối vẽ*: một hình chính và nhiều chi tiết bóc riêng | Trông như đồ cổ thế kỷ 19, lệch với một người thực địa đương đại; toàn nâu thì không có chỗ cho "năng lượng" |
| `style-c-hero` | **C · Nhật ký thám hiểm bí ẩn** — giấy da ố, sepia đậm, không khí bí mật | Hợp khẩu vị fan, gần Journal 3 | Kéo kênh về giọng "bí ẩn / cryptid", ngược với tính khí quan sát bình thản và "không phán xét" của ông; dễ bị coi là bắt chước một IP khác |
| `style-a-sequence` | A, thử một bố cục khác (sequence: củ xoay theo nắng) | kiểm tra style A có giữ được qua nhiều họ bố cục không | — |
| `style-a-cover` | A, bìa sổ: nhãn trắng để engine viết `Dr. Holth` | bìa sổ là chỗ **duy nhất** tên ông được hiện | — |

**Đề xuất: A.** Lấy **lối vẽ** của B (một hình chính, chi tiết bóc riêng, nét dựng hình) và **bố cục
biến đổi** của Journal 3; bỏ cái vỏ bí ẩn của C. Nếu chốt A thì cập nhật `fieldNoteStyle` trong
`bible/style.json` và viết lại `docs/JOURNAL-STYLE.md` theo A.

Soát khi xem ảnh: có chữ hay mũi tên nào lọt vào không (phải không có) · khoảng trống đủ rộng để viết
không · màu nhấn có đúng chỉ nằm trên đường năng lượng không · con vật có đọc ra là Bulbasaur không.
