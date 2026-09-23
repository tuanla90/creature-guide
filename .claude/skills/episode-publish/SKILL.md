---
name: episode-publish
description: Soạn gói đăng một tập — 3 phương án tiêu đề, mô tả SEO, chapters, comment ghim, hashtag, cho cả hai ngôn ngữ; kèm checklist nạp multi-audio và sao lưu. Dùng khi tập đã render xong và chuẩn bị đăng.
---

# Episode Publish — soạn gói đăng

⚠️ **KHÔNG tự đăng, không tự render, không tự upload.** Vai này *chuẩn bị đầy đủ* rồi trình user bấm
nút cuối. Đăng là việc ra ngoài, không quay lại được.

Ra một file: `videos/<slug>/PUBLISH.md`.

---

## Bối cảnh đã chốt

- **Một kênh, YouTube multi-audio.** Một video mang hai track giọng; YouTube tự chọn theo ngôn ngữ
  người xem. Tiêu đề, mô tả và thumbnail đều bản địa hoá được.
- **Thumbnail theo ngôn ngữ chỉ có ở video dài.** Shorts không có → ảnh bìa Short phải không chữ,
  hoặc chọn một thứ tiếng.
- **Đăng tay.** Tự động hoá vướng xác minh app với Google, không vướng code (xem `docs/BUSINESS-FLOW.md`
  phần phụ lục). Chưa làm.

## Soạn gói đăng

### 1. Tiêu đề — 3 phương án, mỗi ngôn ngữ

Kênh là phim tài liệu sinh học giả định. Tiêu đề phải hứa **một câu hỏi sinh học**, không hứa một
danh sách sự thật.

- Một phương án đặt thẳng câu hỏi sinh tồn của tập.
- Một phương án nêu **cái giá** mà loài phải trả.
- Một phương án nêu nghịch lý quan sát được.

❌ Tránh: tên chiêu thức, cấp độ, hệ khắc hệ, "top 10", "sự thật bạn chưa biết".

### 2. Mô tả SEO — mỗi ngôn ngữ

- Hai câu đầu là phần hiện trước khi bấm "xem thêm" — đặt câu hỏi của tập ở đó.
- Giữa: tóm tắt 3–4 câu, có từ khoá tên loài ở cả hai cách viết.
- Cuối, **bắt buộc**: ghi rõ đây là phim tài liệu giả tưởng về sinh vật hư cấu · credit **Tuấn La** ·
  nguồn canon đã dùng · nguồn nhạc và tiếng CC0.

### 3. Chapters

Lấy từ `ORDER` và `timings.json` (timing **thật**, sau align — không phải scaffold).

### 4. Comment ghim

Một câu hỏi mở gửi khán giả, nối vào câu hỏi treo cuối tập. Đây cũng là chỗ để **đính chính** về sau
nếu phát hiện lỗi sau khi đăng — chính sách của kênh là ghim đính chính, không gỡ video.

### 5. Hashtag

3–5 cái, đúng tệp: speculative biology, phim tài liệu, tên loài.

---

## Checklist trình user

**Trước khi đăng**
- [ ] Skill `episode-review` PASS ở chặng 4, và `check-episode.py` sạch ở chặng 10.
- [ ] Đã xem bản render cuối **có tiếng, từ đầu tới cuối, không tua**.
- [ ] Long + Short đã render. Short có hook riêng và tiêu đề riêng.
- [ ] Thumbnail: vài phương án, cả hai ngôn ngữ (video dài); Short dùng bản không chữ.
- [ ] Phụ đề `out/<slug>/*.srt` cả hai thứ tiếng.
- [ ] Hai track giọng đã khít cùng một dòng thời gian.

**Lúc đăng (người làm tay)**
- [ ] Bật khai báo **nội dung tổng hợp bằng AI**.
- [ ] Nạp track giọng thứ hai (cần Advanced features đã bật).
- [ ] Nạp tiêu đề + mô tả bản địa hoá, thumbnail bản địa hoá.
- [ ] Gắn phụ đề hai thứ tiếng.
- [ ] Ghim comment.

**Sau khi đăng**
- [ ] **Sao lưu một chiều lên Drive** những thứ không tái tạo được: ảnh đã đo toạ độ callout, giọng
      đã duyệt, nhạc đã chọn. Đừng dùng đồng bộ hai chiều — xoá nhầm dưới máy là Drive xoá theo.
- [ ] Ghi sổ tài sản của tập (từng file: prompt nào, model nào, giấy phép gì).
- [ ] Ghi vào `docs/SLATE.md`: ngày đăng, link.

## Mẫu `videos/<slug>/PUBLISH.md`

```markdown
# Gói đăng · <slug>

## EN
### Tiêu đề (chọn 1)
1.
2.
3.
### Mô tả
### Thumbnail: phương án A / B / C

## VI
### Tiêu đề (chọn 1)
1.
2.
3.
### Mô tả
### Thumbnail: phương án A / B / C

## Chapters
00:00

## Comment ghim
## Hashtag
## Short — tiêu đề riêng, hook riêng
```
