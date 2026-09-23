# TẬP 001 V2 · "SAUR — KẺ MANG MẦM SỐNG" (MASTER PRODUCTION SCRIPT)

> **Dự án:** Creature Field Guide  
> **Tập:** Kanto #001 · Bulbasaur  
> **Cá thể trung tâm:** `K-01 "Saur"`  
> **Địa danh Canon:** `Viridian Forest` (Rừng Viridian, Kanto)  
> **Triết lý sản xuất:** 100% Animation (Full-Motion) · Không ảnh tĩnh · Không hứa hẹn tập sau · Chuẩn format 9:16 an toàn.

---

## I. BẢNG PHÂN BỔ 3 TẦNG CHUYỂN ĐỘNG (ANIMATION ENGINE ALLOCATION)

| Tầng công nghệ | Tên công cụ | Chi phí | Tần suất trong V2 | Loại cảnh đảm nhận |
|---|---|---|---|---|
| **Tầng 1 (Free / Offline)** | **OpenCV `creature-motion`** | **0 Credit (Offline)** | 40% thời lượng | Các cảnh con vật đứng yên thở, nằm sưởi nắng, chớp mắt, nụ lay nhẹ, mẹ canh tổ trứng. |
| **Tầng 2 (Standard Motion)** | **Google Flow / Veo** | Trong gói token | 40% thời lượng | Sinh hoạt dã sinh tốc độ vừa: lội bùn, vươn dây leo chạm nhau, bầy di chuyển, sương sớm. |
| **Tầng 3 (Dynamic Action)** | **Seedance / Topview / MiniMax** | Dè xẻn (High-impact) | 20% thời lượng | Hành động cực nhanh: Fearow bổ nhào, nổ sương bào tử, sới đấu quất dây leo, SolarBeam nổ chói lòa. |

---

## II. KHO SHOTLIST MỚI CẦN GEN ẢNH CHO BẢN V2 (PROMPT SPECIFICATION)

Để kịch bản V2 phát huy 100% sức mạnh điện ảnh, đây là danh mục 10 khung hình mới cần sinh ảnh (sau đó đưa vào 3 tầng animation):

1. **`v2-s01-macro-breath` (Cận cảnh cực hạn nhịp thở):**
   * *Prompt:* `Extreme macro cinematic close-up of a living green plant bulb attached to the leathery reptilian skin of a Bulbasaur, visible breathing movement, translucent sap beads on leaf veins, dappled forest sunlight, photorealistic documentary style, BBC Planet Earth style --ar 16:9 --style raw`
   * *Engine:* `creature-motion` (vòng lặp thở co bóp).

2. **`v2-s02-saur-crooked` (Saur với củ nghiêng 23 độ):**
   * *Prompt:* `A young Bulbasaur lying in a bright shaft of sunlight on the forest floor of Viridian Forest, viewed from behind and slightly above, the green bulb on its back visibly tilted to the right side toward the sun while its body lies straight, shallow depth of field, naturalistic lighting --ar 16:9`
   * *Engine:* `creature-motion` (thở nhẹ + mắt khép).

3. **`v2-s03-anatomy-conduit` (Giải phẫu X-quang sinh học):**
   * *Prompt:* `Biological medical X-ray style visualization of a Bulbasaur on a dark teal background, semi-transparent body revealing internal skeletal structure and luminous green bio-vascular conduits connecting the back bulb directly to the creature's heart and digestive system, no blood, clean scientific diagram --ar 16:9`
   * *Engine:* Dựng bằng `specimen` quét callout.

4. **`v2-s04-mud-absorption` (Thẩm thấu nước qua da chân):**
   * *Prompt:* `Low ground-level macro shot of sturdy blue-green reptilian legs of Bulbasaur sunken into rich wet black marsh mud beside a forest stream, moisture and tiny droplets beading along the porous skin texture, gentle ripples in shallow water --ar 16:9`
   * *Engine:* Google Flow (nước gợn sóng nhẹ).

5. **`v2-s05-vine-embrace` (Hai dây leo chạm nhau):**
   * *Prompt:* `Two slender flexible green vine tendrils extending from two Bulbasaur meeting in mid-air at dusk, gently curling together like elephant trunks, warm golden backlight shining through the translucent green plant tissue, floating pollen --ar 16:9`
   * *Engine:* Google Flow (dây leo uốn lượn mềm mại).

6. **`v2-s06-fearow-dive` (Cú bổ nhào của Ash-Eye):**
   * *Prompt:* `Dynamic high-speed action shot of a large fierce Fearow raptor bird with one milky-gray blind eye diving violently from an overcast sky with talons extended, wings blurred from speed, targeting a small camouflaged creature below --ar 16:9`
   * *Engine:* Seedance (chuyển động bổ nhào tốc độ cao).

7. **`v2-s07-powder-burst` (Nổ sương bào tử tự vệ):**
   * *Prompt:* `Slow motion explosion of dense glowing golden-yellow sleep spores erupting from the top aperture of a Bulbasaur's back bulb, sparkling dust cloud swirling through sunbeams, stunning visual impact --ar 16:9`
   * *Engine:* Seedance (khói bào tử bùng nổ phân tán).

8. **`v2-s08-solarbeam-charge` (Sới đấu đất nện SolarBeam):**
   * *Prompt:* `Cinematic shot inside a packed dirt arena at dusk, an Ivysaur bracing its thick legs into the ground, its pink bud glowing intensely with concentrated solar radiation, golden energy threads warping the air, dramatic rim light --ar 16:9`
   * *Engine:* Seedance (hạt năng lượng hội tụ chói lòa).

9. **`v2-s09-metamorphosis-gathering` (Đêm biến thái trăng rằm):**
   * *Prompt:* `Mystical night gathering inside a hidden rocky hollow in Viridian Forest, a dozen Bulbasaur standing in a silent circle under moonlight, soft bioluminescent emerald light rising from all their bulbs into mist --ar 16:9`
   * *Engine:* Google Flow (sương đêm bồng bềnh + ánh lân tinh nhấp nháy).

10. **`v2-s10-mossback-portrait` (Chân dung cổ thụ Moss-Back):**
    * *Prompt:* `Profile portrait of a massive ancient female Venusaur resting near mossy rocks after rain, thick woody textured hide covered in living ferns and moss, enormous faded pink flower with a prominent central pistil seed, gentle breathing, raindrops --ar 16:9`
    * *Engine:* `creature-motion` (cơ thể đồ sộ thở chậm rãi).

---

## III. KỊCH BẢN PHÂN CẢNH V2 CHI TIẾT (DIRECTOR'S PRODUCTION SCRIPT)

### HOOK: NGHỊCH LÝ CỦA SỰ SỐNG (00:00 - 00:14)

```
[AUDIO CUE]
SFX: Im lặng tuyệt đối ở 2 giây đầu. Sau đó tiếng gió rít qua trảng cỏ cao; tiếng tim đập trầm [Thump... Thump...]; tiếng rít nhẹ của mô thực vật giãn nở.
BGM: Nốt cello trầm đơn độc, bí ẩn, phong cách BBC Dynasties.
```

| Beat | Thoại lồng tiếng (Voice-over) | Kỹ thuật Visual & Animation | Chữ trên màn hình (An toàn 9:16) | Ghi chú đạo diễn |
|---|---|---|---|---|
| **00** <br> *(13.4s)* | "Ở rìa Rừng Viridian, ranh giới giữa động vật và thực vật... không tồn tại. <br><br> Thoạt nhìn, con vật này như một tảng đá phủ rêu bất động dưới nắng trưa. <br><br> Nhưng cái bọc trên lưng nó... đang thở. <br><br> Nó là con thú mang trên lưng một cái cây, hay một cái cây đang mượn đôi chân của con thú?" | **Moment 1 (w: 1.8 - ~5.8s)**<br>`el: clip` (Tầng 1: `creature-motion` từ `v2-s02`)<br>• Dán chặt bụng xuống đất, thở phập phồng rất khẽ.<br><br>**Moment 2 (w: 2.4 - ~7.6s)**<br>`el: clip` (Tầng 1: `creature-motion` từ `v2-s01`)<br>• Cận cảnh bẹ củ co thắt nhịp nhàng theo nhịp thở.<br>• `sfx: creature-breath.wav` (vol 0.4, lead 0.1s neo tại "thở"). | **Lower-third:**<br>`text`: "BÍ ẨN VIRIDIAN #001" (size 3.8)<br>`caption`: "Rừng Viridian · Cá thể K-01 [Saur]" (size 2.5)<br><br>`chip`: "👁 THỰC ĐỊA KANTO" | **Visual Paradox:** Đập ngay chuyển động thở độc lập của củ vào mắt người xem. |

---

### HỒI 1: SAUR — KẺ YẾU THẾ ĐÓN NẮNG (00:14 - 01:19)

| Beat | Thoại lồng tiếng | Kỹ thuật Visual & Animation | Chữ trên màn hình | Ghi chú đạo diễn |
|---|---|---|---|---|
| **01** <br> *(20.2s)* | "Cuốn danh lục của người bản xứ gọi loài này là Bulbasaur. Trong sổ thực địa của tôi, nó mang mã K-01. <br><br> Tôi đến Viridian làm một việc mà ở quê nhà người ta làm với bầy sói: chọn một cá thể, bám dấu đủ lâu, và đợi tự nhiên lên tiếng. <br><br> Suốt một tháng đầu, nó chỉ có bấy nhiêu: một mã số và một vệt nắng." | **Moment 1 (w: 2.0 - ~10.1s)**<br>`el: clip` (Tầng 2: Flow từ cảnh sương rừng Viridian)<br>• Sương sớm bảng lảng trôi qua gốc đại thụ.<br><br>**Moment 2 (w: 2.0 - ~10.1s)**<br>`el: notepage` (Diễn hoạt lật trang sổ thực địa)<br>• Chữ viết tay và hình vẽ phác thảo Saur hiện dần. | **Text:**<br>`text`: "SỔ TAY THỰC ĐỊA" (size 4.0)<br>`caption`: "Loài: Bulbasaur · Định danh: Saur (K-01)" (size 2.5)<br><br>`chip`: "📖 DANH LỤC BẢN XỨ" | Khẳng định thế giới quan: Nhà khoa học thực địa đối mặt với tự nhiên. |
| **02** <br> *(44.6s)* | "Trảng cỏ Viridian này có bảy cá thể. K-01 nhỏ bé nhất, luôn đi sau cùng. <br><br> Nhưng bảy ngày liền, nó luôn giành được vệt nắng chói nhất trảng. <br><br> Khác với đồng loại có củ mọc thẳng đứng, cái củ trên lưng nó vặn nghiêng hẳn sang một bên—hậu quả của những ngày dài vặn mình đón nắng. <br><br> Từ hôm ấy, trong sổ tôi, K-01 có một cái tên: Saur." | **Moment 1 (w: 1.5 - ~12.0s)**<br>`el: clip` (Tầng 2: Flow bầy 7 con rải rác)<br>• Bầy Bulbasaur chậm rãi bước trên cỏ ẩm.<br><br>**Moment 2 (w: 2.0 - ~16.0s)**<br>`el: clip` (Tầng 1: `creature-motion` từ `v2-s02`)<br>• Saur nằm thở, thớ cơ bắp căng nhẹ.<br><br>**Moment 3 (w: 2.1 - ~16.6s)**<br>`el: specimen` (Soi trên clip động)<br>• Callout 1 (zoom 2.0): "Góc nghiêng 23°" · sub: "Vết tích vặn mình đón nắng". | **Caption:**<br>`caption`: "Saur · Lệch trục củ do hướng dương" (size 2.5)<br><br>`chip`: "👁 DẤU HÌNH THÁI" | Tên gọi xuất hiện sau quan sát hình thái học. |

---

### HỒI 2: CHIẾC DẠ DÀY THỨ HAI (01:19 - 02:37)

| Beat | Thoại lồng tiếng | Kỹ thuật Visual & Animation | Chữ trên màn hình | Ghi chú đạo diễn |
|---|---|---|---|---|
| **03** <br> *(36.4s)* | "Mỗi buổi trưa, Saur bỏ ăn hoàn toàn. Nó phơi mình hàng giờ liền dưới nắng gắt, mắt khép hờ, lá củ khẽ động. <br><br> Khi đứng dậy, khoang bụng nó vẫn phẳng lì, nhưng cái củ trên lưng đã căng mọng dịch lỏng. <br><br> Nó không nhịn đói. Nó đang ăn nắng. <br><br> Thứ trên lưng Saur không phải vật ký sinh, mà là một chiếc dạ dày thứ hai, chuyển hóa trực tiếp quang năng thành sinh khối." | **Moment 1 (w: 1.8 - ~14.5s)**<br>`el: clip` (Tầng 1: `creature-motion` phơi nắng)<br>• Saur ngủ trưa, bụi nắng lơ lửng, lá lay nhẹ.<br><br>**Moment 2 (w: 2.7 - ~21.9s)**<br>`el: specimen` (Soi trên ảnh `anatomy` X-quang `v2-s03`)<br>• Nền teal: Mạch năng lượng phát sáng dẫn từ rễ củ vào tủy sống.<br>• Callout 1: "Ống dẫn quang năng" · sub: "Nuôi trực tiếp hệ tuần hoàn". | **Text:**<br>`text`: "CHIẾC DẠ DÀY THỨ HAI" (size 4.0)<br>`caption`: "Quang hợp trực tiếp nuôi mô động vật" (size 2.5)<br><br>`chip`: "🔬 GIẢ THUYẾT SINH HỌC" | Dùng `specimen` trên ảnh `anatomy` để giải thích triệt để cơ chế sinh học. |
| **04** <br> *(41.0s)* | "Nhưng quang hợp cần nước và muối khoáng. <br><br> Cuối chiều, Saur lội xuống đầm lầy, cắm sâu bốn chân vào bùn nhão nửa giờ liền mà không uống một ngụm nào. <br><br> Da chân của nó hoạt động như loài lưỡng cư: hút ẩm và khoáng chất trực tiếp từ bùn. <br><br> Còn chất đạm để nuôi củ, nó lấy từ chính chất thải bài tiết của con vật. <br><br> Tương tự như loài sên lục Elysia ở biển: một vòng tuần hoàn khép kín tuyệt đối, không lọt mất một giọt năng lượng." | **Moment 1 (w: 1.8 - ~15.0s)**<br>`el: clip` (Tầng 2: Flow từ `v2-s04`)<br>• Bùn đen nhão bao quanh móng chân, nước gợn sóng nhẹ.<br><br>**Moment 2 (w: 1.5 - ~12.5s)**<br>`el: clip` (Tầng 2: Flow ảnh `real` sên lục Elysia)<br>• Sên lục Elysia chlorotica bơi lượn trong nước.<br><br>**Moment 3 (w: 1.6 - ~13.5s)**<br>`el: notepage` (Diễn hoạt nét vẽ sổ tay)<br>• Sơ đồ mũi tên: Đạm bài tiết $\to$ Rễ củ $\to$ Dưỡng chất quang năng. | **Caption:**<br>`caption`: "Thẩm thấu qua biểu mô chân · Vòng khép kín" (size 2.4)<br><br>`chip`: "🔬 ĐỐI CHIẾU TRÁI ĐẤT" | Đối chiếu sinh vật Trái Đất chuẩn cam kết của kênh. |

---

### HỒI 3: DÂY LEO VÀ MÀN BÀO TỬ TỰ VỆ (02:37 - 04:31)

| Beat | Thoại lồng tiếng | Kỹ thuật Visual & Animation | Chữ trên màn hình | Ghi chú đạo diễn |
|---|---|---|---|---|
| **06 & 07** <br> *(82.3s)* | "Chiều tà, khi vệt nắng co lại, những con Bulbasaur dùng vai huých đẩy nhau để giành ánh sáng. Nhưng tuyệt nhiên không cắn xé. <br><br> Saur thường nằm cách con đực lớn nhất hai thân người. Con lớn ấy mang một vết sẹo dài bên sườn sau một trận kịch chiến cũ. Tôi gọi nó là Scar-Shoulder. <br><br> Hai sợi dây leo thò ra từ nách củ của Saur và Scar-Shoulder, vươn cao, xoắn lấy nhau giữa không trung vài giây rồi buông lơi. <br><br> Đó không phải vũ khí để quất. Đó là xúc tu cảm giác. Chúng chạm để nhận diện đồng loại, và để vệ sinh vùng lưng—điểm mù giải phẫu của loài." | **Moment 1 (w: 2.0 - ~25.0s)**<br>`el: clip` (Tầng 2: Flow tranh chấp vệt nắng chiều)<br>• Hai con huých vai tranh vệt nắng vàng.<br><br>**Moment 2 (w: 2.3 - ~28.0s)**<br>`el: clip` (Tầng 2: Flow từ `v2-s05`)<br>• Hai dây leo mềm mại xoắn lấy nhau trong ráng chiều.<br><br>**Moment 3 (w: 2.4 - ~29.3s)**<br>`el: clip` (Tầng 2: Flow gạt sâu bọ sau gáy)<br>• Dây leo vung nhẹ gạt con sâu bọ rơi khỏi phiến lá. | **Text:**<br>`text`: "GIAO TIẾP XÚC GIÁC" (size 4.0)<br>`caption`: "Dây leo cảm giác và vệ sinh điểm mù" (size 2.5)<br><br>`chip`: "👁 TẬP TÍNH BẦY ĐÀN" | Tái định nghĩa đòn đánh game thành tập tính dã sinh. |
| **08 & 09** <br> *(79.0s)* | "Ngày thứ hai mươi hai, một bóng đen xé toạc bầu trời Viridian. Đó là Ash-Eye—con Fearow già với một bên mắt mờ đục màu tro, chuyên săn lùng con non. <br><br> Khi bóng chim bổ nhào, Saur không chạy trốn. Nó ép sát bụng xuống rêu ẩm. Bộ da hoa văn xanh lốm đốm tan biến hoàn toàn vào những mảng nắng tán xạ qua kẽ lá. <br><br> Cú sà xuống lần hai, đỉnh củ của Saur nứt mở. Một làn sương bào tử vàng mịn bung ra mù mịt. Con chim hoảng loạn, mất hướng rồi vội vã tháo lui. <br><br> Nhưng cái giá của sự sống sót hiện rõ ngay buổi chiều: cái củ của Saur teo tóp lại thấy rõ. Nó vừa đốt sạch lượng dinh dưỡng tích lũy cả tháng trời." | **Moment 1 (w: 2.0 - ~24.0s)**<br>`el: clip` (Tầng 3: Seedance từ `v2-s06`)<br>• Chim Fearow lao vút xuống như tên bắn, móng vuốt giương sắc nhọn.<br><br>**Moment 2 (w: 2.3 - ~27.0s)**<br>`el: clip` (Tầng 3: Seedance từ `v2-s07`)<br>• Bào tử nổ bùng như pháo hoa vàng rực.<br>• `sfx: powder-explosion.wav` (vol 0.5, lead 0.2s tại "bung").<br><br>**Moment 3 (w: 2.4 - ~28.0s)**<br>`el: clip` (Tầng 1: `creature-motion` Saur kiệt sức)<br>• Củ teo tóp, Saur nằm thở dốc mệt mỏi. | **Text:**<br>`text`: "BÀO TỬ PHÒNG THỦ" (size 4.0)<br>`caption`: "Sleep Powder · Cái giá: Tiêu hao 50% sinh khối" (size 2.4)<br><br>`chip`: "📖 DANH LỤC · BỘT NGỦ" | Nhấn mạnh luật: Mọi năng lực đều có cái giá sinh học. |

---

### HỒI 4: VŨ KHÍ TRONG SỚI ĐẤU (04:31 - 06:12)

| Beat | Thoại lồng tiếng | Kỹ thuật Visual & Animation | Chữ trên màn hình | Ghi chú đạo diễn |
|---|---|---|---|---|
| **10 & 11** <br> *(101.3s)* | "Ở các thị trấn quanh Viridian, con người dùng chính những con vật này trong các sới đấu đất nện. Dây leo ở đây không còn để chải chuốt—chúng quất mạnh như roi thép xé toạc mặt đất. <br><br> Nhưng đáng sợ nhất là cú phóng quang SolarBeam: con vật đứng khựng lại, củ trên lưng hút cạn quang năng xung quanh rồi phóng ra một luồng nhiệt chói lòa. <br><br> Khán giả reo hò trước uy lực. Còn tôi thấy một kho dự trữ bị vắt kiệt tới tế bào cuối cùng. <br><br> Giống như loài thùa sa mạc: gom góp cả đời chỉ để bung nở một lần duy nhất trước khi tàn lụi." | **Moment 1 (w: 2.2 - ~30.0s)**<br>`el: clip` (Tầng 3: Seedance sới đấu quất dây)<br>• Dây leo quất thẳng xuống nền đất tung bụi đất mù mịt.<br><br>**Moment 2 (w: 2.5 - ~35.0s)**<br>`el: clip` (Tầng 3: Seedance từ `v2-s08`)<br>• Nụ hoa sáng lóa, phóng luồng nhiệt SolarBeam nổ chấn động.<br>• `sfx: beam-blast.wav` (vol 0.45).<br><br>**Moment 3 (w: 2.6 - ~36.3s)**<br>`el: clip` (Tầng 2: Flow ảnh cây thùa Trái Đất)<br>• Cây thùa sa mạc bung ngọn hoa khổng lồ rồi chết khô rũ. | **Text:**<br>`text`: "BỨC XẠ QUANG NĂNG" (size 4.0)<br>`caption`: "Tia Nắng (SolarBeam) · Xả kiệt toàn bộ dự trữ" (size 2.4)<br><br>`chip`: "⚔ TRẬN ĐẤU THỰC NGHIỆM" | Đối chiếu sự tàn nhẫn của đấu trường với giới hạn chuyển hóa. |

---

### HỒI 5: BIẾN THÁI DƯỚI ÁNH TRĂNG (06:12 - 08:30)

```
[AUDIO CUE]
SFX: Tiếng rắc rắc sâu của cấu trúc xương giãn nở; tiếng gió thổi thung lũng đá; tiếng thở dốc rung chuyển.
BGM: Dàn hợp xướng trầm hùng, huyền bí.
```

| Beat | Thoại lồng tiếng | Kỹ thuật Visual & Animation | Chữ trên màn hình | Ghi chú đạo diễn |
|---|---|---|---|---|
| **12 & 13** <br> *(86.2s)* | "Tháng thứ tư, Saur thay đổi nếp sống. Nó nằm lì ngoài nắng, ăn mùn đất không ngừng nghỉ. Bước đi của nó bắt đầu nặng nề. Đầu Saur hướng về phía nam, nhưng cái củ lại vặn gắt về phía đông đón nắng. <br><br> Rồi một đêm trăng khuyết, Saur rời bỏ trảng cỏ, đi sâu vào rừng thẳm. <br><br> Dấu vết dẫn tôi đến một hõm đất bí mật khuất sau vành đá cổ thụ. Hơn mười cá thể Bulbasaur đang đứng ken đặc thành một vòng tròn im lìm. <br><br> Ánh lân tinh xanh biếc bốc lên từ những đỉnh củ, hòa vào màn sương đêm. Đó là nghi lễ biến thái thiêng liêng của cả giống loài." | **Moment 1 (w: 2.2 - ~28.0s)**<br>`el: clip` (Tầng 1: `creature-motion` củ vặn hướng nắng)<br>• Củ nghiêng gắt gao theo góc chiếu mặt trời.<br><br>**Moment 2 (w: 2.2 - ~28.0s)**<br>`el: clip` (Tầng 2: Flow từ `v2-s09`)<br>• Bầy Bulbasaur tụ họp dưới ánh trăng, ánh lân tinh xanh dịu bốc lên bồng bềnh.<br><br>**Moment 3 (w: 2.3 - ~30.2s)**<br>`el: notepage` (Diễn hoạt lật sổ)<br>• Bản vẽ chu kỳ tích lũy sinh khối trước khi đổi dạng. | **Text:**<br>`text`: "NGHI LỄ THAY DẠNG" (size 4.0)<br>`caption`: "Đồng pha sinh học dưới chu kỳ trăng" (size 2.5)<br><br>`chip`: "📖 DANH LỤC BẢN XỨ" | Tái hiện trọn vẹn tập Anime kinh điển 51 (*Mysterious Garden*). |
| **14** <br> *(51.6s)* | "Sáng hôm sau, thung lũng chỉ còn lại hiện trường: đất bị cày nát thành những rãnh sâu bởi bốn cái chân vừa phải chống đỡ một sức nặng tăng vọt. Những bẹ lá khô bong tróc nằm cuộn tròn như vỏ hành già. Và không khí sực nức mùi hương hoa lạ. <br><br> Từ trong sương mù, một bóng hình sừng sững bước ra. Bốn chân nó to dày như những cây cột đá để nâng đỡ cái nụ hoa hồng rực nặng trĩu trên lưng. <br><br> Nó đã trở thành Ivysaur. <br><br> Nhưng khi tôi mở sổ tay, con thú to lớn ấy vẫn khẽ nghiêng đầu về phía tiếng ngòi bút của tôi." | **Moment 1 (w: 2.0 - ~17.0s)**<br>`el: clip` (Tầng 2: Flow hiện trường thung lũng)<br>• Rãnh cày sâu, bẹ lá khô rụng trên cỏ.<br><br>**Moment 2 (w: 2.0 - ~17.0s)**<br>`el: clip` (Tầng 2: Flow bóng Ivysaur trong sương)<br>• Dáng hình đồ sộ bước chậm qua màn sương sớm.<br><br>**Moment 3 (w: 2.2 - ~17.6s)**<br>`el: clip` (Tầng 1: `creature-motion` Ivysaur thở)<br>• Ivysaur thở sâu, nụ hoa phập phồng, mắt chớp nhẹ. | **Text:**<br>`text`: "BƯỚC CHUYỂN: IVYSAUR" (size 3.8)<br>`caption`: "Tái cấu trúc khung xương chịu lực · Chân hoá trụ" (size 2.4)<br><br>`chip`: "👁 BIẾN THÁI HOÀN TẤT" | Mô tả tiến hóa thuần chất sinh học cơ học. |

---

### HỒI 6: MOSS-BACK VÀ VÒNG KHÉP KÍN (08:30 - 10:15)
*(Kết thúc trọn vẹn, sâu lắng — Hoàn toàn làm chủ lịch phát hành)*

```
[AUDIO CUE]
SFX: Tiếng mưa rơi rào rạt trên tán lá cổ thụ; tiếng thở rền vang của Venusaur; tiếng côn trùng ngân nga.
BGM: Dàn dây du dương, lắng đọng, mở ra không gian triết lý sâu thẳm.
```

| Beat | Thoại lồng tiếng | Kỹ thuật Visual & Animation | Chữ trên màn hình | Ghi chú đạo diễn |
|---|---|---|---|---|
| **15** <br> *(86.2s)* | "Mang nụ hoa nặng nề khiến Ivysaur vĩnh viễn mất khả năng đứng bằng hai chân sau. Chân phải thành cột. <br><br> Mùa mưa cuối, tôi bắt gặp Moss-Back—cá thể Venusaur khổng lồ canh giữ lối vào rừng già Viridian. Lưng nó đã hóa gỗ nứt nẻ, rêu phong phủ đầy mai. Ở tâm hoa nhô lên một chiếc nhụy hạt: một con cái cổ thụ. <br><br> Hương hoa sau mưa của Moss-Back làm dịu đi cơn hung hăng của những con thú dữ tợn nhất. <br><br> Rời khỏi Viridian, tôi vẫn không có câu trả lời: hạt mầm là một phần cơ thể hay là một sinh vật sống cộng sinh? <br><br> Nhưng có lẽ thiên nhiên không cần một định nghĩa rạch ròi. Hai sự sống đã nương tựa vào nhau, để cùng tạo nên một thực thể hoàn mỹ." | **Moment 1 (w: 2.2 - ~22.0s)**<br>`el: specimen` (Soi trên clip `v2-s10`)<br>• Callout: "Nhụy hạt trung tâm" · sub: "Dị hình giới tính cá thể cái".<br><br>**Moment 2 (w: 2.5 - ~25.0s)**<br>`el: clip` (Tầng 1: `creature-motion` tổ trứng)<br>• Venusaur mẹ nằm thở chậm rãi bên ổ trứng dưới tán lá.<br><br>**Moment 3 (w: 2.4 - ~24.0s)**<br>`el: clip` (Tầng 1: `creature-motion` Moss-Back)<br>• Toàn thân Moss-Back phủ rêu thở trầm tĩnh trong mưa bay.<br><br>**Moment 4 (w: 1.5 - ~15.2s)**<br>`el: clip` (Tầng 2: Flow bầy Venusaur đi xa)<br>• Ba cá thể sải bước chậm rãi về phía chân trời vàng rực. | **Text:**<br>`text`: "MOSS-BACK: CỔ THỤ RỪNG GIÀ" (size 3.8)<br>`caption`: "Bảo chứng sinh thái của rừng nguyên sinh Viridian" (size 2.4)<br><br>**Thông điệp kết thúc:**<br>`caption`: "Hai sự sống · Một thực thể hoàn mỹ" (size 2.5)<br><br>`chip`: "📖 KHÉP LẠI SỔ THỰC ĐỊA" | Kết thúc triết lý, tạo ấn tượng sâu sắc, hoàn toàn không bị ràng buộc tập sau. |
