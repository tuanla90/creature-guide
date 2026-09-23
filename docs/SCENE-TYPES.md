# Danh mục khung cảnh · bảng tra khi viết kịch bản hình

Tài liệu này để **đưa cho người viết kịch bản** (người hoặc máy) biết kênh có sẵn những loại cảnh
nào, mỗi loại làm được gì, và tốn gì. Viết lời mà không biết bảng này thì lời hay tới đâu cũng ra
một tập chỉ có một loại hình.

**Hai trục đừng lẫn:**

| | Khai ở đâu | Trả lời câu gì |
|---|---|---|
| **`kind`** | `bible/shots/<ep>.json` | *Sinh ra tấm ảnh kiểu gì?* |
| **`el`** | `videos/<slug>/scenes.json` | *Dựng tấm ảnh đó lên màn hình kiểu gì?* |

Một tấm ảnh `kind: "fieldnote"` được dựng bằng `el: "notepage"`. Một tấm `kind: "anatomy"` thường
dựng bằng `el: "specimen"` để soi từng điểm. Chọn `kind` là việc của khâu sinh ảnh; chọn `el` là việc
của khâu dựng hình.

---

## A · Năm loại ảnh (`kind`)

| `kind` | Sinh ra cái gì | Lấy `[ref]` ảnh mẫu? |
|---|---|---|
| `plate` | ảnh mẫu: cả thân, nền trơn, ánh sáng đều | không — **nó chính là ref** |
| `scene` | cảnh thật ngoài thực địa | có |
| `real` | động vật có thật ở Trái Đất, để đối chiếu 🔬 | không |
| `anatomy` | X-quang mô phỏng: nền teal, thân trong mờ, xương và mạch năng lượng phát sáng | **không** |
| `fieldnote` | một trang sổ: giấy + hình vẽ chì mực, **chừa trống một phần ba bên phải** | **không** |

`anatomy` và `fieldnote` không lấy `[ref]` vì ref là một ảnh *chụp* — nó kéo bản x-quang và bản vẽ
tay ngược về thành ảnh chụp. Cái giá: hai loại này dễ lệch hình hơn, nên phải tả `scene` kỹ hơn.

**Ranh giới của `anatomy`:** xương, mạch năng lượng, vết thương nhỏ ngoài da thì được. Máu me, nội
tạng, mổ xẻ thì **không**. Thân luôn nguyên vẹn và khép kín.

**Luật của `fieldnote`:** ảnh **không có một chữ nào, không một mũi tên nào**. Chữ và mũi tên do
engine vẽ lên sau. Vì thế sửa lời không phải sinh lại ảnh, và bản EN dùng chung y hệt tấm giấy.

---

## B · Năm loại cảnh tràn khung (`el`) — đây là "động từ" của hình

Mỗi loại là một động tác khác nhau của máy quay. Một tập dùng mãi một loại thì beat nào cũng giống
beat nào — `check-episode.py` sẽ báo khi một loại chiếm quá 75%, hoặc khi bốn beat liền cùng công thức.

### `world` — mở ra
Ảnh tĩnh, camera lia và phóng chậm (Ken Burns). Cảnh nền, cảnh rộng, cảnh khí quyển.

```json
{ "el": "world", "src": "img/kanto-001/s04-sunbath.jpg",
  "camera": { "from": {"x": 0.45, "zoom": 1.02}, "to": {"x": 0.62, "zoom": 1.22}, "ease": "inOut" },
  "fx": "dust", "vignette": true }
```
- `camera.from/to`: `{x, y, zoom}` — toạ độ **trên ảnh**, 0..1, gốc trên-trái.
- `ease`: `linear` · `in` · `out` · `inOut` (mặc định).
- `fx`: `dust` · `snow` · `embers`. Hạt bay trong không khí, có chiều sâu.
- `layers`: `[{src, depth, sway, keep}]` — parallax nhiều lớp thật. **Đắt**: phải cắt nền bằng tay
  và Flow không sinh lại được, nên chỉ dùng cho một hai cảnh chủ chốt của cả kênh.
- `portrait: {camera}`: khung dọc canh lại riêng.

### `specimen` — soi vào
Một ảnh, camera **lần lượt đẩy vào từng điểm**, mỗi điểm hiện một thẻ nhãn có đường chỉ. Dùng khi
lời dẫn đang chỉ ra từng chi tiết trên cơ thể.

```json
{ "el": "specimen", "src": "img/kanto-001/s02-plate.jpg",
  "overview": {"x": 0.5, "y": 0.5, "zoom": 1}, "introW": 0.8, "outroW": 0.8,
  "callouts": [
    {"x": 0.41, "y": 0.28, "zoom": 2.2, "label": "củ mọc nghẹo", "sub": "vết của bảy hôm nằm vặn",
     "atWord": "nghẹo", "w": 1, "side": "right"}
  ] }
```
- Toạ độ callout **đo trên ảnh thật** bằng `python tools/review.py <slug>`, sau khi ảnh đã chốt.
- `atWord`: neo vào một từ trong giọng đọc — **đừng neo vào từ cuối câu**, cảnh sẽ chỉ hiện một giây.
- `w`: trọng số thời lượng của từng callout. Dưới ~1,2 giây thì thẻ chưa kịp hiện.
- `outro`: `"overview"` (lùi ra, mặc định) hoặc `"hold"` (giữ nguyên ở callout cuối).

### `clip` — chuyển động thật
Một đoạn video. Vẫn lia và phóng được như `world`.

```json
{ "el": "clip", "src": "video/kanto-001/c02-growth.mp4",
  "from": 1.5, "to": 5.0, "speed": 0.75, "loop": true,
  "camera": {"from": {"zoom": 1.0}, "to": {"zoom": 1.12}} }
```
- `from`/`to` tính bằng **giây** trong file gốc; `speed` chỉnh tốc độ; đoạn ngắn hơn cảnh thì tự lặp.
- Ba nguồn clip, chọn **tầng rẻ nhất còn dùng được**:

  | Loại cảnh | Công nghệ | Chi phí |
  |---|---|---|
  | cảnh đứng, thở, lá lay, mắt khép | skill `creature-motion` (OpenCV) | **miễn phí, offline** |
  | sinh hoạt thường | Veo / Nano Banana | trong 25k token/tháng |
  | hành động | Topview (Seedance, MiniMax) | token riêng, dè xẻn |

  Tầng đầu gần như chưa được dùng, mà nó không tốn gì. Ảnh nào đứng yên lâu quá đều là ứng viên.

### `notepage` — dừng lại ghi chép
Một trang giấy đứng gần như yên, chữ viết tay hiện dần vào chỗ trống, **tích lại** tới hết cảnh.

```json
{ "el": "notepage", "src": "img/kanto-001/x02-fieldnote.jpg",
  "notes": [
    {"x": 0.72, "y": 0.22, "text": "củ nghiêng hẳn sang trái", "atWord": "nghiêng"},
    {"x": 0.72, "y": 0.41, "text": "ba lớp bẹ, lớp ngoài đã khô", "atWord": "bẹ"}
  ] }
```
- Hợp nhất với đoạn lời **liệt kê quan sát**, hoặc đoạn người kể đang phân vân — chữ hiện ra đúng lúc
  anh ta viết nó.
- Không thẻ, không đường chỉ, không phóng vào từng điểm. Khác `specimen` ở đúng ba chỗ đó.

### `anatomy` — nhìn xuyên qua
Không phải một `el` riêng: dùng ảnh `kind: "anatomy"` rồi dựng bằng `world` (nhìn toàn thân) hoặc
`specimen` (soi từng cơ quan). Hợp với đoạn lời giải thích **cơ chế bên trong**: năng lượng đi đâu,
cái gì nối với cái gì.

---

## C · Chữ trên màn hình

Chữ **không** chọn vị trí tự do được (trừ `notepage`). Nó nằm trong cột chữ của cảnh, đặt bằng
`place` của moment: `top` · `center` · `bottom`.

| `el` | Là gì | Giới hạn |
|---|---|---|
| `text` | tiêu đề lớn | `size` ≤ **4.2** ·  ≤ 52 ký tự |
| `caption` | lower-third, dòng chú thích dưới | `size` ≤ **2.7** · ≤ 68 ký tự |
| `label` | dòng chữ nhỏ chữ mono, giãn cách rộng — nhãn mục, ngày tháng | ≤ 46 ký tự |
| `chip` | viên bo tròn có viền phát sáng — nhãn bằng chứng 📖 👁 🔬 | ngắn |

Neo bằng `atWord` (một từ trong giọng đọc) hoặc `at` (số khung trong cảnh).
**Giới hạn ký tự là cho khung dọc 9:16** — vừa khít ở 16:9 mà tràn ở 9:16 là lỗi đã xảy ra nhiều lần.

## D · Tiếng

```json
{ "el": "sfx", "name": "kanto-001/powder-burst.wav", "atWord": "bào", "volume": 0.35, "lead": 0.2 }
```
`volume` mặc định 0.1 — quá nhỏ cho tiếng sinh vật; cue thật nên 0.3–0.5, tiếng nền 0.06–0.1.
`lead` đẩy cue bắt đầu sớm hơn từ được neo, cho tiếng có đà.

---

## E · Cách chia thời lượng — vì sao cảnh hay bị ngắt sớm

Một beat dài bằng đúng đoạn giọng đọc của nó. Các moment trong beat chia nhau khoảng đó:

- Moment có `atWord` hoặc `atSec` thì **neo cứng** vào đúng chỗ ấy.
- Moment không neo thì chia phần còn lại **theo trọng số `w`**.

Nên thêm một moment vào beat là **lấy bớt thời gian của các moment khác**, không phải kéo dài beat.
Ngưỡng `check-episode.py` đang soát:

| | Ngưỡng |
|---|---|
| moment | dưới **1,2s** ✗ · dưới **2,5s** ⚠ · dưới **25% trung vị của chính tập đó** ⚠ |
| callout của `specimen` | dưới **1,2s** ✗ · dưới **2,0s** ⚠ |

Sửa bằng cách tăng `w` hoặc **bỏ bớt một moment** — đừng kéo dài lời dẫn cho vừa hình.

---

## F · Bảng chọn nhanh

| Lời dẫn đang làm gì | Dùng |
|---|---|
| mở ra một nơi chốn, một không khí | `world` + `fx` |
| chỉ ra từng chi tiết trên cơ thể | `specimen` |
| kể một hành vi đang diễn ra | `clip` |
| con vật đứng yên, thở, chờ | `clip` từ `creature-motion` (miễn phí) |
| liệt kê quan sát, người kể đang phân vân | `notepage` |
| giải thích cơ chế bên trong | ảnh `anatomy` dựng bằng `specimen` |
| đối chiếu một loài có thật ở Trái Đất 🔬 | ảnh `real` dựng bằng `world` |
| nêu cái giá của một khả năng | `specimen` soi đúng chỗ bị hao |
