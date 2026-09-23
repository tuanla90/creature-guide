---
name: episode-plan
description: Lên và cập nhật lịch sản xuất của kênh — tập nào đang ở chặng nào, tập nào làm tiếp, tập nào tới ngày đăng. Dùng khi hỏi "làm tập nào tiếp", "tập X tới đâu rồi", hoặc rà tiến độ cả kênh.
---

# Episode Planner

Vai: người lên lịch và điều phối. Mục tiêu: **2 tập/tuần, cuốn chiếu, WIP = 1** — ưng tập này mới
mở tập sau.

Nguyên tắc gốc bê từ `semantix-docs/content-plan`: **không giữ một cái lịch riêng để phải đồng bộ tay.**
Quét trạng thái thật từ file, rồi đối chiếu với hàng đợi. File nói gì thì đó là sự thật.

## Đọc trước

- `docs/IDEA-BANK.md` — hàng đợi ý tưởng, trạng thái ✅ đã dùng · ⏸ hoãn · ⬜ chưa dùng.
- `docs/SLATE.md` — lịch phát hành và tập đang chạy. Chưa có thì tạo theo mẫu dưới.
- `docs/BUSINESS-FLOW.md` — những gì đã chốt, và ba thứ còn treo.

## Quy trình

### 1. Quét trạng thái thật

Với mỗi thư mục trong `videos/`, suy ra chặng đang đứng (theo [PIPELINE.md](../../../docs/PIPELINE.md)):

| Có file gì | Đang ở chặng |
|---|---|
| chỉ có bản EN, chưa có `content.py` | 3–4 · viết và duyệt script |
| có `content.py`, chưa có `bible/shots/<ep>.json` | 5 · đã dịch VI |
| có shots, `public/img/<ep>/` rỗng | 6–7 · chờ sinh ảnh |
| có ảnh, chưa có `scenes.json` | 8 · chờ dựng hình |
| có `scenes.json`, `timings.json` còn là scaffold | 8–9 · chờ giọng |
| có giọng, `timings.json` đã align | 10 · chờ soát |
| có `out/<slug>/` | 11 · chờ render / đăng |

Chạy `PYTHONUTF8=1 python tools/check-episode.py <slug>` cho tập đang chạy để biết còn ✗ nào.

### 2. Đối chiếu với hàng đợi

Tập nào xong, tập nào đang dở, tập nào trong IDEA-BANK còn ⬜ mà đủ tư liệu để mở.

### 3. Đề xuất việc tiếp theo

- **WIP = 1.** Tập đang dở chưa qua cổng chặng 10 thì **đừng đề xuất mở tập mới** — nói thẳng là
  đang bị chặn ở đâu.
- Chọn tập tiếp theo: hook mạnh · đủ canon để không phải bịa · có ít nhất một dấu tích nhìn thấy
  được để đặt tên cá thể.
- Xen **Khung B (so sánh)** khi hai loài trong hàng đợi giải cùng một bài toán sinh tồn — xem
  [EPISODE-FRAME.md](../../../docs/EPISODE-FRAME.md).

### 4. Cập nhật `docs/SLATE.md`

## Nguyên tắc

- **KHÔNG tự đánh dấu một tập là xong.** Trạng thái suy ra từ file; cột "đã đăng" chỉ người điền.
- **KHÔNG tự render, tự sinh ảnh, tự đăng.** Skill này lên kế hoạch, không bấm nút.
- Nhắc **A5** khi rà định kỳ: đã kiểm tín hiệu IP (claim, strike, video bị gỡ) và con số sub chưa?
  Điều kiện rẽ nhánh của kênh là sự kiện, không phải ngày.

## Mẫu `docs/SLATE.md`

```markdown
# Lịch sản xuất

Nhịp mục tiêu: 2 tập/tuần · cuốn chiếu, WIP = 1

## Đang chạy

| Slug | Khung | Chặng | Chặn ở đâu | Dự kiến đăng |
|---|---|---|---|---|
| kanto-001-bulbasaur | A | 8 | chờ giọng EN (chưa chốt nhà cung cấp) | — |

## Hàng đợi

| # | Loài / trục | Khung | Vì sao chọn |
|---|---|---|---|

## Đã đăng

| Ngày | Slug | Link | CTR | Giữ chân 30s |
|---|---|---|---|---|
```
