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
| ~~`real`~~ | **ngừng dùng** — loài Trái Đất không sinh bằng AI nữa, xem mục B2 | — |
| `anatomy` | X-quang mô phỏng: nền teal, thân trong mờ, xương và mạch năng lượng phát sáng | **không** |
| `fieldnote` | một trang sổ: giấy + hình vẽ, **chừa khoảng trống theo họ bố cục** (`layout`, xem *Ngữ pháp trang sổ*) | **không** |

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

### Convention mở đầu tập — 4 shot bắt buộc

Không có trung gian ở shot đầu: hoặc **cực rộng** (vùng đất là nhân vật) hoặc **cực gần** (một chi tiết gây tò mò trước khi thấy toàn cảnh). Chưa bao giờ mở bằng medium shot.

| Thứ tự | Shot | Nội dung | Khai `size` / `angle` |
|---|---|---|---|
| **1 · Establish** | `extreme-wide` hoặc `macro` | Địa điểm hoặc chi tiết — **chưa thấy sinh vật** | `low` cho rừng; `macro` cho dấu vết / bào tử |
| **2 · Reveal** | `wide` hoặc `medium` | Sinh vật xuất hiện lần đầu — **không phán xét, chỉ quan sát** | `low` để thấy nó to |
| **3 · Detail/Hook** | `close` hoặc `macro` | Đặc điểm nhận dạng hoặc hành vi lạ → câu hỏi treo | `eye` hoặc `rear` |
| **4 · Title card** | — | Tên loài + mã cá thể. Dứt điểm trước khi narrator bắt đầu nói | — |

**Narrator bắt đầu VÀO hoặc SAU shot 3**, không trước. Shot 1 và 2 là tiếng thiên nhiên thuần — không lời.

---

## B · Vai sinh thái của Pokemon khách

Mỗi tập phải có **2–4 Pokemon khách** với vai rõ ràng. Vai quyết định cách chúng xuất hiện, tần suất, và mức độ tương tác với cá thể trung tâm.

| Vai | Chức năng trong tập | Xuất hiện | Lấy mã? |
|---|---|---|---|
| **Predator** | Tạo nguy hiểm, test phản ứng sinh vật trung tâm | 1–2 lần, dramatic | Không (ẩn danh = đáng sợ hơn) |
| **Prey** | Đặt sinh vật trung tâm trong food chain; cho thấy nó ăn gì | 1 lần, không kịch tính | Không |
| **Competitor** | Cùng niche, tranh tài nguyên — tạo tension không phải chiến đấu | 1–2 lần | Không |
| **Mutualist** | Tương hỗ; cho thấy sinh vật trung tâm có vai trò trong ecosystem | Xuất hiện đều, không dramatic | Nếu quay lại > 2 lần thì cho mã |

**Không đặt tên riêng** cho bất kỳ Pokemon khách nào — đây là luật chung của kênh. Nếu một con khách xuất hiện đủ nhiều để cần nhận dạng, cho mã thực địa (K-04) và gọi bằng đặc điểm.

**Vai Mutualist** là cách xây dựng ecosystem mà không cần tập riêng: Butterfree thụ phấn cho củ của Bulbasaur, Caterpie làm sạch lá mục → khán giả thấy Viridian Forest như một hệ thống sống, không phải sân khấu.

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

### Ngữ pháp trang sổ · bố cục tách khỏi style

Trang sổ không có một bố cục cố định. Sức hút của cuốn sổ nằm ở chỗ **mỗi trang chọn một khối dẫn mắt
khác nhau** (bài học từ Journal 3: tác giả làm "hàng chục bố cục mới"). Mục này chỉ chốt **bố cục**: loại
bố cục, thứ bậc thông tin, quan hệ chữ – hình – sơ đồ, vùng để engine chèn chữ, nhịp đọc, một trang hay
trang đôi, và phần nào nằm trong ảnh, phần nào engine vẽ. **Không** chốt giấy, mực, nét, độ cũ, font:
đó là *style*, nằm ở `bible/style.json` → `fieldNoteStyle` (hướng đang thử: `experiments/notebook-style/`).

Không mặc định "trang trái là con vật, trang phải là phân tích". Không bắt mọi trang sổ phải là trang đôi.

**Ba tầng, khai trong shot và trong cảnh:**

```json
{ "kind": "fieldnote", "canvas": "spread", "layout": "correction", "readingOrder": "top-to-bottom" }
```

1. **`canvas`:** `page` (một trang) hoặc `spread` (trang đôi). Đây là cỡ sân khấu, không quyết định nội
   dung. Khung 16:9 hợp nhất với `spread`; `page` thì phải đặt lên nền (mặt bàn, lề tối).
2. **`layout`:** một trong 12 họ dưới đây. Mỗi họ chỉ quy định quan hệ và ưu tiên không gian. Câu tả
   bố cục cho prompt nằm ở `bible/layouts.json`, `build-prompts.mjs` tự ghép theo `layout`.
3. **Khối (`blocks`)** do engine vẽ lên ảnh, đặt vào **vùng có tên** (`region`). Toạ độ của vùng **đo
   trên ảnh thật** sau khi ảnh đã chốt, như toạ độ callout: Flow không giữ đúng một vùng trống theo prompt.

**12 họ bố cục**

| `layout` | Khối dẫn mắt | Dùng khi lời dẫn đang… |
|---|---|---|
| `hero` | một hình lớn (½–⅔ trang), ghi chú và chi tiết bám quanh | giới thiệu loài, một cơ quan quan trọng |
| `text-led` | khối ghi chép là chính, hình nhỏ chen ở đầu, chân, lề | kể nhật ký theo ngày, lập luận |
| `diagram-led` | một sơ đồ lớn ở giữa, chữ thành chú thích quanh nó | giải thích một cơ chế (vòng khép kín, tụ năng lượng) |
| `full-spread` | một hình vượt qua gáy, phủ cả hai trang | giải phẫu toàn thân, mạng năng lượng, chu trình lớn |
| `atlas` | nhiều hình nhỏ ngang hàng, xếp hàng, cụm hoặc ô | dấu chân, bộ phận, tư thế, so nhiều cá thể |
| `comparison` | hai đối tượng đối diện, giữa là vùng mũi tên và điểm chung / khác | so hai cơ chế, hai trạng thái, hai cột |
| `map` | bản đồ hoặc mặt bằng, dấu vết và mốc thời gian nằm ngay trên đó | chỗ nằm, đường đi, vùng sống |
| `sequence` | 3–6 trạng thái theo đường ngang, dọc hoặc vòng cung | một quá trình: đổi hình, tích – xả, một hành vi |
| `correction` | ghi chép cũ làm nền, rồi gạch, sửa, khoanh, thêm giả thuyết mới | **người kể đổi nhận định** |
| `evidence-board` | các mảnh bằng chứng rời quanh một câu hỏi ở giữa | beat chưa có kết luận |
| `sparse` | một hình hoặc một câu giữa nhiều khoảng trống | chuyển hồi, phát hiện lớn, câu kết |
| `marginalia` | trang cố ý dày; nội dung chính rõ, lề đầy ghi chú phụ, phép tính | đang đào sâu một vấn đề (dùng hiếm) |

**Khối cơ bản và ai vẽ**

| Khối | Nằm trong ảnh (Flow sinh) | Engine vẽ |
|---|---|---|
| `figure` · `detail` | ✓ hình chính, chi tiết bóc riêng | — |
| `map` · `timeline` · khung của `comparison` | ✓ nét bản đồ, trục, hai khung | — |
| `body` (đoạn ghi chép) | — | ✓ chữ viết tay hiện dần (`notes` hiện có) |
| `label` + `connector` | — | ✓ nhãn IN HOA + đường chỉ tới đích |
| `measurement` | — | ✓ số ước lượng có `~` (DNA D15) |
| `crossref` | — | ✓ `→ xem trang…` · `📖 danh lục` |
| `correction` | — | ✓ gạch bỏ rồi viết đè: kể được lúc người kể đổi ý |

**Luật không đổi:** ảnh không có chữ, không số, không mũi tên. Mọi thứ đọc được đều do engine vẽ, nên
sửa lời không phải sinh lại ảnh và hai bản VI / EN dùng chung một tấm giấy.

**Engine** (`el: "notepage"`, nhánh `feat/specimen-freeze-media`, 2026-09-25) vẽ được: `notes` (thân), `labels`
(nhãn IN HOA, có `anchor` thì có đường chỉ), `diagrams` (7 kiểu ở mục *Diagram khoa học*), `corrections`
(`strike` + chữ viết đè), `crossrefs`, `mark` vẽ tay trên note / nhãn / diagram, `short.page` cho khung dọc,
và `debug: true` (lưới 10% + khung `keepout`, để đo toạ độ trên ảnh thật). Mực lấy từ `video.config.json` →
`notebook.{ink, accent}`; chữ `{vi, en}` chọn theo `text.lang`.

**Một video, một lớp chữ.** YouTube multi-audio chỉ đổi track giọng, không đổi chữ trên hình. Nên mỗi lần
render chỉ mang **một** ngôn ngữ chữ (`text.lang`). Chữ còn lại đi bằng phụ đề của track ấy. Chọn ngôn ngữ
chữ gắn với quyết định *track gốc VI hay EN* (CHANNEL-SETUP mục 3), vẫn đang treo.

**Cảnh sổ trong Short phải render thử.** Ở 9:16 chữ tự to lên cỡ tối thiểu, note dài xuống thêm dòng và có
thể đè khối bên dưới (đã thấy khi thử). Khai toạ độ riêng cho Short nếu cần.

### Style bắt buộc của trang sổ

**Mọi ảnh `kind: "fieldnote"` và mọi cảnh `el: "notepage"` bắt buộc theo [JOURNAL-STYLE.md](JOURNAL-STYLE.md)**:
giấy, mực, màu nhấn, độ cũ, ba lớp chữ (tiêu đề · thân · nhãn IN HOA), cách vẽ mũi tên. Tài liệu này không
chép lại style. Chỉ một điều ghi cứng ở đây, vì nó đúng với mọi style: tinh thần là **khoa học năng lượng
sinh học thực địa, không phải bí ẩn**. Không bí mật, không kịch tính; một người quan sát bình thản đang
đo, ghi, và sửa nhận định của chính mình. (Style đang thử ba hướng: `experiments/notebook-style/`.)

### Diagram khoa học · `diagram`

Trang sổ phân tích năm loại việc (JOURNAL-STYLE mục F). Mỗi loại cần một kiểu diagram. **Nguyên tắc: nét
nào mang dữ liệu thì engine vẽ** (chiều mũi tên, độ dài thanh, vạch mốc, đường năng lượng, dấu trên bản
đồ): như thế số đúng, hai bản ngôn ngữ dùng chung, và sửa không phải sinh lại ảnh. Ảnh Flow chỉ mang
**hình vẽ con vật, chi tiết, nền bản đồ, và khoảng trống**. Engine vẽ diagram theo lối tay (nét hơi run,
mực và màu nhấn lấy từ JOURNAL-STYLE).

| Việc phân tích | `diagram.type` | Ảnh mang | Engine vẽ |
|---|---|---|---|
| Vật lý khả năng | `force` · `energy-bar` | hình con vật, khoảng trống | mũi tên lực (gốc, hướng, độ lớn `~`), thanh năng lượng so sánh |
| Anatomy (nhẹ) | `energy-flow` | hình con vật | đường năng lượng chạy trên thân (màu nhấn), nhãn cơ quan |
| Tương tác hệ | `phase` | khoảng trống | sơ đồ ion / tinh thể / trạng thái pha: ô, mũi tên chuyển trạng thái |
| Hành vi | `field-map` · `day-timeline` | nền bản đồ (`layout: map`) | dấu vết, chỗ nằm, giờ; trục giờ trong ngày và sự kiện |
| Vòng đời, tích luỹ | `life-timeline` | khoảng trống | trục tuyến tính, các giai đoạn, **ngưỡng** tích luỹ |

Toạ độ `[x, y]` là tỉ lệ trên ảnh (0–1), **đo trên ảnh thật** như toạ độ callout. Ví dụ đủ bảy kiểu:

```json
{ "el": "notepage", "src": "img/kanto-001/x09-capacitor.jpg", "layout": "diagram-led", "page": 14,
  "keepout": [[0.08, 0.20, 0.46, 0.78]],
  "diagrams": [
    {"type": "force", "from": [0.40, 0.52], "angle": -25, "length": 0.12,
     "value": "~7 N", "label": "VINE STRIKE", "mark": "hypothesis", "atWord": "quất"},
    {"type": "energy-bar", "region": [0.56, 0.20, 0.92, 0.36], "unit": "kJ",
     "bars": [{"label": "ONE MORNING OF SUN", "value": 17}, {"label": "ONE BEAM", "value": 17}],
     "mark": "hypothesis"},
    {"type": "energy-flow", "path": [[0.30, 0.30], [0.33, 0.45], [0.38, 0.60]], "label": "SOLAR SKIN → BULB"},
    {"type": "field-map", "marks": [{"at": [0.62, 0.40], "kind": "rest", "t": "D14 · 09:23"},
                                    {"at": [0.70, 0.55], "kind": "track"}]},
    {"type": "day-timeline", "region": [0.55, 0.70, 0.95, 0.80], "from": "06:00", "to": "18:00",
     "events": [{"t": "09:23", "label": "FACES THE SUN"}, {"t": "12:00", "label": "SUNBATH"}]},
    {"type": "life-timeline", "region": [0.55, 0.82, 0.95, 0.92],
     "stages": ["BULB", "BUD", "FLOWER"], "threshold": {"at": 0.62, "label": "CHANGE"}},
    {"type": "phase", "region": [0.56, 0.40, 0.92, 0.66], "states": ["STORED", "FOCUSED", "RELEASED"],
     "arrows": [[0, 1], [1, 2]]}
  ],
  "labels": [{"text": "SOLAR SKIN", "anchor": [0.34, 0.33], "at": [0.52, 0.16], "atWord": "da"}] }
```

- **Nhãn gắn với một điểm trên hình:** `anchor` là điểm trên con vật, `at` là chỗ đặt chữ; engine vẽ
  đường chỉ tay từ chữ tới điểm. Nhãn không có `anchor` thì là chữ tự do.
- `keepout`: các khung của hình chính và chi tiết, đo trên ảnh thật. Chữ và diagram **không được đè**
  lên đó.
- Số trong diagram theo DNA D15: ước lượng, có `~`, cách tính nằm trên chính trang ấy.

### Bằng chứng và tham chiếu trên trang sổ

- **`chip` chỉ dùng ngoài sổ.** Viên bo tròn phát sáng là ngôn ngữ của lớp chữ trên phim. Trên trang sổ,
  bằng chứng là **`mark`** gắn vào note, nhãn hoặc diagram: `catalogue` · `observation` · `hypothesis`.
  Engine vẽ nó thành **ký hiệu vẽ tay** (cuốn sách · con mắt · bình thí nghiệm) bằng mực của JOURNAL-STYLE,
  không bao giờ là emoji.
- **Giả thuyết luôn lộ ra là giả thuyết:** `mark: "hypothesis"` thì engine thêm `(?)` sau con số hoặc câu,
  hoặc dòng "chưa xác nhận" / "unconfirmed" dưới diagram.
- **Tham chiếu chéo** có cú pháp riêng và không lộ nguồn thật:

  ```json
  {"type": "crossref", "to": "page:14"}      // → xem tr. 14   /  → see p. 14
  {"type": "crossref", "to": "species:venusaur"}   // → Venusaur
  {"type": "crossref", "to": "catalogue"}    // [ký hiệu sách] danh lục  /  catalogue
  ```

  `page:<n>` phải trỏ tới một `notepage` có `"page": n` trong cùng tập. Tên Bulbapedia, bản game, số tập
  anime **chỉ** nằm trong `NGUON` của `content.py` (DNA D16).

### Giới hạn chữ trên trang sổ · hai ngôn ngữ trên một tấm giấy

Mỗi chữ trên trang sổ khai **cả hai bản**: `"text": {"vi": "…", "en": "…"}`. Nhãn kỹ thuật IN HOA thì
giữ tiếng Anh ở cả hai bản, nên chỉ cần một chuỗi. **Mọi giới hạn tính theo bản dài hơn**; bản VI thường
dài hơn EN chừng 20–30% số ký tự, nên vùng chữ phải đo theo bản VI.

| Khối | Giới hạn |
|---|---|
| `body` (một note) | ≤ **80 ký tự**, tối đa 2 dòng trong vùng của nó |
| số note mỗi trang | ≤ **5** (trang đôi ≤ **8**) · đoạn thân dài ≤ **3** mỗi trang |
| `label` | ≤ **22 ký tự**, IN HOA · ≤ **6** nhãn mỗi trang |
| `measurement` / `value` | ≤ **16 ký tự**, có `~` |
| bề rộng vùng chữ | ≥ **18%** bề rộng khung |
| cỡ chữ tối thiểu, 16:9 1080p | thân ≥ **34 px** · nhãn ≥ **26 px** |
| cỡ chữ tối thiểu, 9:16 | thân ≥ **44 px** sau khi cắt khung |

- **Bản dọc 9:16 không nhét cả trang đôi.** Cảnh sổ trong Short khai `"short": {"page": "left" | "right"}`
  hoặc một vùng `[x0, y0, x1, y1]` để cắt đúng một trang. Chữ phải đọc được ở cỡ tối thiểu sau khi cắt.
- **Tràn chữ:** engine thu cỡ chữ tới mức tối thiểu rồi xuống dòng. Vẫn tràn thì `check-episode.py` báo
  **trước khi render**. Không để engine tự cắt chữ.
- Chữ không bao giờ đè lên `keepout`.

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

### Dừng hình để phân tích — `specimen` trên video

Con vật đang làm một việc, lời dẫn tới đúng chữ quan trọng thì **hình đứng lại**, nền tối đi, rồi
camera soi vào bộ phận đang làm việc ấy. Đây là lúc người kể dừng lại để nghĩ.

```json
{ "el": "specimen", "aspect": 1.7917,
  "video": {"src": "video/kanto-001/b02-vine-lash.mp4", "from": 0.5, "to": 4},
  "introW": 1.2,
  "callouts": [
    {"x": 0.52, "y": 0.3, "zoom": 2.0, "label": "Vine · one organ", "sub": "grasp · greet · strike",
     "atWord": "quật", "media": {"src": "video/kanto-001/earth-elephant-trunk.mp4",
     "from": 2, "to": 6, "caption": "Elephas maximus · trunk"}}
  ] }
```

- Video chạy trong đoạn tổng thể đầu, **đứng hình đúng lúc callout đầu tiên mở** — neo nó bằng
  `atWord` vào chữ đang nói. Khung đứng lấy từ chính video nên không có vết nối.
- `to` chặn trên: đoạn tổng thể dài hơn nguồn thì đứng ở `to`. `dim` độ tối thêm (mặc định 0.35).
- Lời dẫn phải **chừa chỗ** cho cú dừng: quyết từ kịch bản, không chèn sau khi đã thu giọng.

### Ảnh quê nhà — `callout.media`

Trong thẻ callout, một tấm ảnh in dán vào như ảnh ông mang theo từ quê nhà: viền giấy, băng
dính, màu ngả, hạt phim, tên Latin viết tay trên mép (`caption`). Ảnh hoặc video lặp đều được.

Trình bày kiểu này vì ba lẽ: khán giả đọc ra ngay đó là **ký ức "ở quê tôi"**, không phải cảnh ở
Viridian; phim thật đặt cạnh ảnh AI không bị lệch chất liệu, vì chúng rõ ràng thuộc hai thế giới; và
nó là ảnh ông mang theo chứ không phải máy quay, nên không phạm luật "không có đoàn làm phim".

## B1 · Chuyển cảnh — cắt thẳng trong hồi, thẻ chương giữa hồi

Phim tài liệu không dừng lại giữa mọi đoạn. `video.config.json` → `pacing.between: "cut"`: giữa hai
beat cùng một hồi là **cắt thẳng**, không nền, không tiếng vút. Beat **mở một hồi mới** khai
`"chapter": {"kicker": "V", "title": "One organ, two uses"}` trong `scenes.json`: trước beat ấy
engine chèn **thẻ chương** (`pacing.chapterGap`, mặc định 2,2 giây): hình beat trước tối dần, số hồi
và tên hồi hiện lên giữa nền tối, rồi beat sau cắt vào. Chữ EN — chữ trên hình dùng chung hai track.

Thẻ chương cho biết **đã sang phần khác**, không nói **vì sao**. Câu mở hồi vẫn phải có cầu nối
(docs/VOICE.md, luật 2) — `check-episode.py` soát chỗ này. Hồi lấy từ `drafts/4-scene-plan.json`,
trang duyệt vẽ thẻ chương ở đúng chỗ.

## B2 · Loài Trái Đất — luật cường độ

1. **Tối đa 3 cú dừng hình mỗi tập**, trong đó **tối đa 2 cú có ảnh quê nhà**. Khung chia đôi
   (đặt hai thứ cạnh nhau cả khung) chưa làm — để dành cho khi thật cần.
2. **Mọi so sánh khác chỉ nói, không lên hình.** Một so sánh chỉ được lên hình khi nó đẩy câu hỏi
   của tập đi tiếp.
3. **Loài Trái Đất không sinh bằng AI.** Ảnh AI "chụp thật" một loài thật sai là bị bắt ngay, và dễ
   bị tưởng là ảnh thật. Lấy từ nguồn **không đòi ghi tên tác giả** (cùng luật với âm thanh): Pexels,
   Pixabay (video) · ảnh và phim của cơ quan chính phủ Mỹ (NOAA, USFWS, NPS — thuộc phạm vi công
   cộng) · tranh cổ Biodiversity Heritage Library · Wikimedia Commons chỉ bản công cộng hoặc CC0.
   **Không** lấy thẳng từ kết quả Google.
4. **Mỗi file ghi vào `videos/<slug>/earth.json`**: loài, link gốc, giấy phép. Pexels/Pixabay đôi khi
   bị Content ID nhận vơ — link gốc là thứ để kháng nghị.

   ```json
   [{"file": "earth-elephant-trunk.mp4", "species": "Elephas maximus",
     "source": "<link trang gốc>", "license": "Pexels License"}]
   ```
5. Tên file `earth-<loài>-<bộ phận>.mp4|jpg`, thả vào `inbox/` như mọi file bàn giao (docs/HANDOFF.md).

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
| `chip` | viên bo tròn có viền phát sáng — nhãn bằng chứng 📖 👁 🔬. **Chỉ dùng ngoài sổ**: trên `notepage` dùng `mark` vẽ tay | ngắn |

Neo bằng `atWord` (một từ trong giọng đọc) hoặc `at` (số khung trong cảnh).
Giới hạn riêng cho chữ **trên trang sổ** (hai ngôn ngữ, note, nhãn, số) ở mục *Giới hạn chữ trên trang sổ*.
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
| liệt kê quan sát, người kể đang phân vân | `notepage` (chọn `layout` theo bảng *Ngữ pháp trang sổ*) |
| giải thích cơ chế bên trong | ảnh `anatomy` dựng bằng `specimen` |
| đối chiếu một loài có thật ở Trái Đất 🔬 | **nói**; nếu đẩy câu hỏi đi tiếp thì dừng hình + ảnh quê nhà (tối đa 2/tập) |
| con vật vừa làm một động tác đáng soi | dừng hình: `specimen` với `video` |
| nêu cái giá của một khả năng | `specimen` soi đúng chỗ bị hao |
