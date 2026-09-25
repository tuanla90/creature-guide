# Sổ thực địa Dr. Holth — Visual spec (một hướng style, CHƯA CHỐT)

> 2026-09-25: đây là hướng **C** trong `experiments/notebook-style/`. Style của kênh chốt sau khi thử ba
> hướng; phần giọng văn (D), chú thích (E), nội dung trang phải (F) và điều cấm (G) dùng được cho mọi style.

Tài liệu này mô tả phong cách hình ảnh của sổ tay Dr. Holth khi xuất hiện trong video
(kind `fieldnote` trong `bible/shots/`) và trong thumbnail, intro card, v.v.

**Tham chiếu gốc:** Gravity Falls Journal 3 (Ford Pines) — xem ảnh lưu ở `bible/refs/journal/`.  
**Tinh thần:** nhà nghiên cứu năng lượng sinh học thực địa, không phải thám tử bí ẩn.  
Cùng aesthetic, khác nội dung — thay mystery bằng science.

---

## A. Vật liệu và màu sắc

| Yếu tố | Spec |
|---|---|
| Giấy | Parchment ố vàng nâu — tone `#C8A96E` đến `#8B6914`; cạnh tối hơn trung tâm |
| Mực | Monochrome nâu sepia — `#3D1F00` đến `#7A4A1E`; **không màu khác** |
| Vết ố | Coffee stain, vết ngón tay, vết ẩm ở góc — thêm vào hình sau khi vẽ |
| Độ cũ | Cũ nhưng chưa mục — tờ giấy này được dùng thường xuyên, không phải bỏ xó |

---

## B. Ba lớp chữ

| Lớp | Font / style | Dùng cho |
|---|---|---|
| **Title** | Cursive lớn, in đậm, có swash — kiểu chữ tay trang trọng | Tên loài ở trang trái |
| **Body** | Handwritten italic nhỏ hơn, hơi nghiêng, đều đặn | Field notes ngôi thứ nhất |
| **Label** | ALL CAPS, chắc tay, thẳng — gắn với mũi tên | Chú thích bộ phận, con số đo đạc |

**Label example:** `SOLAR ABSORPTION ZONE` · `VINE LAUNCH POINT` · `EST. OUTPUT: ~7N` · `COST: ~8 MIN PHOTOSYNTHESIS`

Chú thích số không bao giờ viết chắc chắn hơn dữ liệu — nếu là ước lượng thì ghi `~`, nếu là giả thuyết thì ghi `(?)`.

---

## C. Bố cục: chuyển sang SCENE-TYPES

Bố cục trang sổ **không** thuộc style. Xem [SCENE-TYPES.md](SCENE-TYPES.md) mục *Ngữ pháp trang sổ*: 12
họ bố cục, khối cơ bản, `canvas` một trang hay trang đôi. Không mặc định trang trái là con vật, trang
phải là phân tích.

---

## D. Giọng văn trong field notes

**Ngôi thứ nhất, quan sát kỹ, đôi khi có nhận xét cá nhân — nhưng không bao giờ cảm xúc quá.** Dr. Holth là nhà khoa học, không phải fan.

| Đúng | Sai |
|---|---|
| "Cá thể K-01 không rời bóng tán cây trong hai giờ đầu buổi sáng." | "Thật tuyệt vời khi được nhìn thấy nó!" |
| "Tôi ước lượng lực vine whip ở khoảng 7N — xem trang 14." | "Đòn đánh của nó cực kỳ mạnh mẽ!" |
| "Điều kỳ lạ: cá thể này không phản ứng với Fearow gần đó. Chưa rõ lý do." | "Có vẻ nó rất dũng cảm." |
| "Xem thêm: Venusaur · trang 31. 📖 danh lục." | "Bulbapedia · Gen I · Red" (tên nguồn chỉ nằm trong `NGUON`) |

**Dry humor được phép, một lần mỗi trang:** *"Con vật khó quan sát hơn tôi nghĩ — nhất là khi nó nhìn thẳng vào ống kính."*

---

## E. Annotation và cross-reference

**Mũi tên:** vẽ tay, hơi cong, đầu mũi tên đơn giản. Không thẳng tắp như diagram công nghệ.

**Cross-reference format:**
- Canon: `→ 📖 danh lục` (nguồn thật — Bulbapedia, bản game — chỉ ghi trong `NGUON` của `content.py`, không lên trang)
- Nội bộ: `→ Xem trang [N]` hoặc `→ Xem [loài khác]`
- Giả thuyết: `🔬 Chưa xác nhận — cần quan sát thêm`

**Ký hiệu trang:**
- `📖` — thông tin từ danh lục (canon)
- `👁` — quan sát trực tiếp của Dr. Holth
- `🔬` — giả thuyết chưa được xác nhận

---

## F. Loại phân tích → diagram

Cách khai và ai vẽ gì: [SCENE-TYPES.md](SCENE-TYPES.md) mục *Diagram khoa học* (`force` · `energy-bar` · `energy-flow` · `phase` · `field-map` · `day-timeline` · `life-timeline`). Bảng dưới chỉ giữ phần hình dung.

### Hình dung theo loại phân tích

| Loại phân tích | Detail sketch trang phải |
|---|---|
| Vật lý khả năng | Diagram lực: vector mũi tên, con số `~7N`, bar năng lượng so sánh |
| Anatomy | X-quang đơn giản: outline thân, điểm sáng cơ quan, không có máu/nội tạng |
| Tương tác hệ | Sơ đồ tinh thể / ion / trạng thái pha — abstract, scientific illustration |
| Hành vi | Bản đồ nhỏ vùng thực địa, ký hiệu track, timeline ngày |
| Sinh sản / vòng đời | Timeline tuyến tính với ngưỡng tích luỹ |

---

## G. Những thứ không được xuất hiện trong sổ tay

- Màu sắc ngoài sepia/nâu
- Font in máy hoàn toàn đều đặn (phá cảm giác handmade)
- Emoji hoặc icon hiện đại — ba dấu 📖 👁 🔬 **vẽ tay** thành cuốn sách / con mắt / bình thí nghiệm bằng mực sepia
- Tên đòn, tên hệ, tên nguồn game trên nhãn (`VINE WHIP`, `SOLAR BEAM`, `Gen I`): nhãn tả việc cơ quan làm (`VINE STRIKE`, `BEAM`)
- Screenshot, ảnh chụp thật
- Tên game, tên anime, từ ngữ của fandom

Sổ tay là tài liệu của một nhà khoa học sống trong thế giới đó — ông ta không biết Pokemon là game.
