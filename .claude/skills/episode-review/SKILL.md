---
name: episode-review
description: Soát kịch bản một tập trước khi sinh ảnh — ba lớp: máy soát logic và nguồn, soát văn bằng stop-slop, rồi trình người duyệt. Ra bảng PASS/FAIL. Dùng sau khi viết xong bản EN, trước khi dịch VI và trước khi tiêu credit ảnh.
---

# Episode Review — soát kịch bản trước khi tiêu tiền

Chạy trên **một tập**. Xuất bảng **PASS/FAIL** + danh sách cần sửa. **Không tự sửa** trừ khi user bảo.

Vị trí trong dây chuyền: [PIPELINE.md](../../../docs/PIPELINE.md) chặng 4. Soát **trước khi sinh ảnh**,
vì script quyết định ảnh — sửa script sau khi đã có ảnh là hỏng cả loạt ảnh đã trả credit.

Phân công đã chốt: **máy lo logic và kiểm chứng · Gemini lo giọng văn và khả năng kể chuyện · người
quyết đi tiếp**.

---

## Lớp 1 · Máy soát logic

```bash
PYTHONUTF8=1 python tools/check-episode.py <slug>
```

Rồi đọc tay những thứ linter chưa bắt được:

### 1.1 Khung tập
- [ ] Khung đã chọn rõ (A một cá thể / B so sánh) và bố cục theo đúng khung đó.
- [ ] **Khung A:** câu hỏi mở màn viết được trong một câu; trả lời được "cá thể này muốn gì, cái gì cản nó".
- [ ] **Khung B:** trục so sánh nói được trong một câu; **mỗi chủ thể thắng ở ít nhất một điểm**.
- [ ] Mỗi chặng đóng đúng **một** câu hỏi. Câu hỏi lớn để mở tới chặng cuối.

### 1.2 Nhãn bằng chứng và nguồn
- [ ] Mọi câu chỉ ra được là 📖 danh lục · 👁 quan sát · 🔬 giả thuyết · ⚔ trận đấu (chỉ Pokémon).
- [ ] Mỗi 📖 có một dòng trong `NGUON` kèm tên bản game/nguồn lore.
- [ ] Mỗi 🔬 kèm **một loài có thật ở Trái Đất**, và loài thật đó **cũng tra được nguồn** — không nói vo.
- [ ] Nguồn đúng tầng: IP còn sống thì bám canon chặt; phạm vi công cộng thì ghi rõ **chọn dị bản nào**.
- [ ] Không có giả thuyết nào bị kể như sự thật.

### 1.3 Luật kênh
- [ ] Không nhắc game, không nhắc AI, không nhắc đoàn làm phim. Pokédex → "cuốn danh lục".
- [ ] Người dẫn xưng "tôi", **không bao giờ nói tên mình**.
- [ ] Cảnh tiến hoá **không có lột da** — chỉ sưng nở, sức nặng, ánh sáng, bóng dáng, dấu vết.
- [ ] Mọi khả năng đều nêu **cái giá** của nó.
- [ ] Giải phẫu đúng ranh giới: X-quang mô phỏng, xương, mạch năng lượng, vết thương nhỏ — không máu
      me, không nội tạng, không mổ xẻ.
- [ ] Ghép đôi dừng ở phô diễn, làm tổ, chăm con.

### 1.4 Tên cá thể
- [ ] Tên canon (Smaug, Buckbeak) thì giữ nguyên.
- [ ] Tên tự đặt là **danh từ chỉ một dấu tích nhìn thấy được**, và chỉ được gọi **sau khi** khán giả
      đã thấy dấu ấy — tức là dấu ấy phải có **một shot cận cảnh riêng**.
- [ ] Khớp `docs/CAST.md`, cả VI lẫn EN, và mã thực địa neo được hai bản.

### 1.5 Cấu trúc kỹ thuật
- [ ] Có `ORDER`, `BEATS`, beat `"short-outro"` (thiếu là không có bản Short).
- [ ] `PRON` có mọi tên loài và tên riêng khó đọc (chỉ cần cho bản VI).

## Lớp 2 · Soát văn

Chạy skill **`stop-slop`** trên bản EN. Lưu ý **ba luật đã bị cắt** cho kênh này — xem phần
CHANNEL OVERRIDES trong `.claude/skills/stop-slop/SKILL.md`. Đừng khôi phục chúng:

- con vật được làm chủ ngữ, không bắt buộc phải là người;
- người dẫn xưng "tôi", **không gọi "bạn"**;
- giữ **một** câu kết đắt cho mỗi tập.

Ngoài `stop-slop`, soát thêm phần chỉ kênh này mới có:
- [ ] Sức ép kể chuyện: có cái gì đang đe doạ cá thể này không, hay chỉ là một chuỗi sự thật?
- [ ] Nhãn 👁 mở đầu mỗi chặng: chặng bắt đầu bằng **quan sát tận mắt**, rồi mới 📖, rồi 🔬.
- [ ] Giọng nhà sinh vật học: được phép sai, được phép chờ, được phép không biết.

Đây cũng là lớp giao cho **Gemini** review song song nếu muốn ý kiến thứ hai về giọng văn.

## Lớp 3 · Trình người duyệt

Dùng [episode-checklist.md](../creature-field-guide-scriptwriter/references/episode-checklist.md).

Xuất bảng cuối:

```
LỚP 1 · logic      ✅ / ❌ (n mục)
LỚP 2 · văn        ✅ / ❌ (n mục)
---
VERDICT: ĐI TIẾP ĐƯỢC  /  CẦN SỬA (n mục)
```

Kèm danh sách sửa gọn, mỗi dòng: *chỗ nào · sai gì · sửa thế nào*.

> **Cổng chặng 4:** hết cả ba lớp mới được sang chặng 5 (dịch VI) và chặng 6–7 (sinh ảnh).
