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

## A2 · Ngữ pháp góc máy — `size` · `angle` · `motion`

Ba trường của shot, **quyết từ lúc viết prompt**, không phải lúc dựng. Góc máy là thứ không sửa được
sau khi ảnh đã sinh — muốn cảnh từ trên xuống thì phải sinh ra cảnh từ trên xuống.

**`size` — cỡ cảnh, con vật chiếm bao nhiêu khung**

| `size` | Khi nào dùng |
|---|---|
| `extreme-wide` | mở một hồi, đổi địa điểm. Vùng đất là nhân vật |
| `wide` | cảnh định vị: con vật ở đâu, bầy đứng thế nào |
| `medium` | hành vi — cả con vật cùng việc nó đang làm |
| `close` | cảm xúc, giác quan, đặc điểm nhận dạng của cá thể trung tâm |
| `macro` | một chi tiết giải phẫu: vảy, bẹ củ, móng |

**`angle` — máy đặt ở đâu**

| `angle` | Cho người xem cảm giác gì |
|---|---|
| `eye` | ngang hàng với con vật — mặc định, đừng lạm dụng |
| `low` | con vật to lớn, đáng gờm |
| `high` | con vật nhỏ bé, dễ tổn thương |
| `overhead` | bản đồ: khoảng cách giữa các cá thể, hình dạng trảng — **thứ không thấy được từ mặt đất** |
| `rear` | nhìn cùng hướng con vật, **thấy thứ nó thấy** — mạnh nhất cho cảnh chờ, cảnh đối mặt |
| `profile` | dáng hình, so sánh tỉ lệ |
| `pov` | mắt con vật — dùng rất ít |

**Luật soát** (`check-episode.py`): một tập phải có **ít nhất 3 cỡ cảnh và 3 góc máy**, không giá
trị nào chiếm quá 60%, và **phải có ít nhất một cảnh toàn**. Shot chưa khai hai trường này thì bị báo.

**Dựng một hồi:** mở bằng `extreme-wide` hoặc `wide` · vào hành vi bằng `medium` · chốt bằng `close`
hoặc `macro`. Khán giả luôn biết mình đang ở đâu trước khi được đưa lại gần.

### `motion: true` — ảnh sinh ra để chạy `creature-motion`

`creature-motion` **chỉ làm động được con vật**. Nó không biết làm gió, tia nắng, nước chảy. Mọi thứ
trong cảnh vốn phải động mà đứng im sẽ trông như **ảnh hỏng** — tia nắng xuyên rừng đứng sững trong
khi con vật thở là lộ ngay.

Đã dính thật ở `s04-bulbasaur-sunbath`: góc tương đối xa, có tia nắng, có cỏ, có cây. Chỉnh cả buổi
vẫn trông lỗi, vì **bản thân tấm ảnh không hợp** với loại chuyển động này.

Nên ảnh nào định chạy `creature-motion` thì khai `motion: true` **từ lúc sinh**. Prompt được thêm:

> *the creature fills most of the frame and is the only subject, completely still air, no wind,
> soft even overcast light, background calm and softly out of focus*

và cấm thêm: tia nắng, gió thổi lá, cỏ lay, nước chảy, lá rơi, bụi bay, sương trôi, nắng loang lổ.

**Chọn công nghệ theo tấm ảnh:**

| Tấm ảnh có… | Dùng |
|---|---|
| con vật chiếm khung, môi trường đứng yên (`motion: true`) | `creature-motion` — miễn phí, không méo hình |
| con vật **và** môi trường cùng có thứ phải động | Veo |
| hành động nhanh: săn, đấu, bổ nhào | Seedance |
| sự đứng yên **chính là** nội dung (hõm đất trống, dấu vết) | `world` — ảnh tĩnh, máy lia chậm |

### Chi phí đã đo

**Veo trong Flow: 15 token/clip.** Hạn mức 25.000/tháng → ~1.666 clip/tháng, ~190 clip mỗi tập ở nhịp
2 tập/tuần. Ở quy mô này Veo gần như không tốn; giới hạn thật là **thời gian bấm tay** vì Flow chưa tự
động hoá được (Chrome chặn CDP trên profile đang đăng nhập).

### Đánh giá Flow một lần trước khi dựa vào nó

Sinh **một** clip cho mỗi loại rủi ro, từ ảnh đã có, rồi chấm:

| Ảnh thử | Rủi ro cần xem |
|---|---|
| cận cảnh con vật đứng yên | có tự thêm chuyển động thừa không |
| cảnh toàn có gió, nắng, cỏ | môi trường có động tự nhiên không |
| con vật đang làm một việc | tay chân có biến dạng không |
| tấm có đặc điểm nhận dạng (màu Shiny) | **đặc điểm có giữ nguyên không** — cái này quyết định |

Năm tiêu chí, đạt / không đạt:

1. **Đúng hình** — đúng dáng, đúng hoa văn, đúng tỉ lệ từ đầu tới cuối
2. **Không méo** — không mọc thêm chi, không chảy nhão, không đổi cấu trúc
3. **Giữ đặc điểm** — đặc điểm nhận dạng của cá thể trung tâm còn nhìn ra được
4. **Chuyển động hợp lý** — đọc ra là hành vi của một con vật, không phải hiệu ứng
5. **Dùng được bao nhiêu giây** — thường chỉ 2–3 giây đầu sạch; đó mới là độ dài thật

Trượt tiêu chí 3 thì **không dùng Veo cho mọi cảnh có dấu tích**, dù các tiêu chí khác đạt.
Ghi kết quả vào `experiments/flow-veo/`.

---

## A3 · Ba lớp tham chiếu — ảnh tham chiếu, ảnh mẫu, cảnh

Mọi thứ AI sinh ra được giữ đúng hình bằng **một chuỗi tham chiếu ba lớp**. Sai ở lớp dưới là sai
lan lên mọi lớp trên.

```
ảnh tham chiếu tải về      →   ảnh mẫu (plate)          →   mọi cảnh
bible/refs/<loài>/              kind: plate / location       [ref: <plate>]
kích thước · dấu chân · Shiny   con thường · con được chọn
                                · địa điểm trống
```

**Lớp 1 · Ảnh tham chiếu tải về** — `bible/refs/<loài>/refs.json`. AI biết dáng một Pokémon phổ biến,
nhưng **không biết chắc tiểu tiết**: kích thước so với người, hình dấu chân, màu Shiny. Tải những tấm
đó về, nạp lên Flow, và `build-prompts` tự gắn chúng vào đúng ảnh mẫu. Mỗi tấm ghi nguồn trong
`refs.json` — đó là một phần của sổ tài sản. Ảnh là của bên thứ ba: **chỉ để tham chiếu khi sinh, không
đăng, không đưa vào git**.

**Lớp 2 · Ảnh mẫu — ba loại, sinh TRƯỚC mọi cảnh:**

| Ảnh mẫu | Khai | Nuôi cảnh nào |
|---|---|---|
| **con thường** của loài | `kind: plate`, `creatures: ["bulbasaur"]` | mọi cảnh có đàn, có con không tên |
| **con được chọn** | `kind: plate`, `creatures: ["bulbasaur:K-01"]` | mọi cảnh có cá thể trung tâm |
| **địa điểm trống** | `kind: location`, `location: "viridian-forest"`, **không có sinh vật** | mọi cảnh có cùng `location` |

Ảnh mẫu khoá theo **cá thể trước, loài sau**. Trước đây chỉ khoá theo loài, nên 21 cảnh đàn thường của
tập 001 lấy **con được chọn** làm mẫu — dấu nhận dạng của nhân vật chính lan sang cả đàn. `male` /
`female` là biến thể của loài, không phải cá thể được chọn, nên vẫn làm được ảnh mẫu loài.

### Cá thể trung tâm — chốt đúng MỘT đặc điểm

Kịch bản chốt **một** đặc điểm nhìn thấy được của con được theo dõi, ghi vào
`bible/creatures/<loài>.json` → `individuals.<mã>.trait`. Từ đó ra hai mẫu: con thường và con được chọn.
**Không đặt tên riêng**: nó được gọi bằng đặc điểm ấy cộng mã thực địa — `Shiny Bulbasaur · K-01`.

**Ưu tiên Shiny khi loài có Shiny.** Ba lý do:

1. **Có sẵn trong canon** — không phải bịa, thoả luật dẫn chứng.
2. **AI giữ màu dễ hơn giữ hình.** Một cái củ nghiêng 20° rất dễ bị sinh lại thành thẳng; một thân
   màu xanh vàng thì khó lẫn. Đây là thứ quyết định khi chấm Veo — tiêu chí "giữ dấu tích".
3. **Có đối chứng thật trên Trái Đất** 🔬: biến thể sắc tố hiếm — xanthism ở ếch, rắn; leucism ở cá
   sấu, chim. Và nó có **cái giá** đúng luật kênh: con khác màu thì kém nguỵ trang.

Cá thể có thể **thay** một dòng mô tả của loài bằng `dropAppearance` — Shiny thay dòng màu da. Cộng
thêm thôi thì prompt tự mâu thuẫn. **Đừng nhắc tên màu sai trong `marks`** (kể cả *"instead of
blue-green"*): mô hình sinh ảnh hay bỏ qua phủ định. Màu sai đưa vào `forbidden` của cá thể.

### Địa điểm — tài sản dùng lại được

`bible/locations/<id>.json`: tên EN/VI, **dẫn chứng canon**, mô tả, và các khu (`areas`). Shot khai
`location: "viridian-forest:clearing"` thì prompt nhận mô tả địa điểm và `[ref]` tới ảnh mẫu địa điểm.

Ảnh mẫu địa điểm là **cảnh trống, không một sinh vật nào**. Nhờ vậy nó dùng lại được: làm cảnh toàn
mở hồi, làm nền cho trang sổ, làm nền để ghép sinh vật vào, và **dùng lại ở tập sau** nếu cùng vùng đất.

### Trang sổ nghiên cứu — kiểu Darwin, da Vinci

Nhà khoa học không chỉ vẽ cả thân: họ **bóc từng chi tiết ra vẽ riêng** trên cùng trang — một cái móng,
một con mắt, một bẹ lá, một mảng da. Khai trong shot:

```json
{ "kind": "fieldnote", "creatures": ["bulbasaur:K-01"],
  "studies": ["one claw seen from below", "the eye in profile", "a single leaf of the bulb", "footprint"] }
```

`"footprint"` lấy **dấu chân canon** của loài (`bible/creatures/<loài>.json` → `footprint`) và tự gắn ảnh
tham chiếu dấu chân. "Bóc tách" là tách **hình vẽ** ra khỏi thân — **không phải mổ xẻ**: chỉ bộ phận nhìn
thấy từ bên ngoài, không nội tạng.

**Mỗi tập bắt buộc có ít nhất một cảnh X-quang (`anatomy`) và một trang sổ (`fieldnote`).** Người dẫn
là người đi tìm sự sống × năng lượng; hai loại cảnh này là cách ông **nhìn xuyên qua** và **ghi lại**.
`check-episode.py` báo ✗ nếu thiếu.

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
