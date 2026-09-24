# TẬP 001 V3 · "CROOKEDBUD — AI ĐANG NUÔI AI?" · bản phân cảnh

> ⚠ **Bản này viết TRƯỚC các luật chốt ngày 2026-09-24** và sẽ được làm lại theo chúng: không đặt tên
> riêng (cá thể trung tâm là `Shiny Bulbasaur · K-01`, không còn Crookedbud / Búp Lệch / Vai Rách /
> Mắt Tro / Lưng Rêu) · đặc điểm nhận dạng là màu Shiny, không còn củ nghẹo · góc máy `size`/`angle` ·
> ảnh `motion` riêng cho creature-motion · địa điểm là tài sản · ảnh tham chiếu. **Đừng lấy bản này
> làm mẫu cho tập sau** — mẫu là `docs/CAST.md`, `docs/SCENE-TYPES.md`, `docs/NARRATOR.md`.

> **Tập:** Kanto #001 · dòng Bulbasaur · Khung A (một cá thể)
> **Cá thể trung tâm:** `K-01` · màn hình **Crookedbud** · giọng VI đọc **Búp Lệch**
> **Người dẫn:** Dr. Holth — bìa sổ `DR. HOLTH · FIELD NOTES`, không bao giờ đọc tên (docs/NARRATOR.md)
> **Địa danh:** Viridian Forest 📖 *Let's Go Pikachu/Eevee* · lòng chảo tụ họp: The Mysterious Garden 🎬 *anime tập 51*
> **Dài:** ~11,3 phút · 16 beat + `short-outro`

**V3 khác V2 ở bảy chỗ**, mỗi chỗ đều là một luật kênh bị V2 vi phạm — xem mục V ở cuối.

---

## I · Ba trục phải giữ cùng lúc

**1 · Xương sống.** Một câu hỏi duy nhất, hỏi ở beat 00, hỏi lại ở beat 05, **không trả lời** ở beat 15:

> *Con thú đang nuôi cái hạt, hay cái hạt đang nuôi con thú?*

**2 · Cái tên là câu chuyện.** `Crookedbud` được đặt ở beat 02 vì cái củ mọc nghẹo — khán giả tưởng là tật bẩm sinh. Beat 12 lật lại: đó là **vết của động tác vặn mình đón nắng lặp lại mỗi ngày**. Cú lật ấy chỉ dựng được khi cái tên mang thông tin, nên tên **không** được là mẩu cắt của tên loài.

**3 · Mỗi khả năng nêu cái giá.** Bào tử (beat 09) và tia nắng (beat 11) đều trả giá bằng đúng cái kho đã phơi nắng cả tháng để tích.

## II · Phân bổ hình — năm động từ, không một động từ

| `el` | Số cảnh | Tỉ lệ | Vì sao |
|---|---|---|---|
| `world` | 20 | 38% | Ảnh tĩnh 2000px + camera lia chậm. **Miễn phí, và trông giống phim tài liệu hơn clip AI 5 giây** — con vật đứng yên đúng hình, không trôi, không biến dạng |
| `clip` | 17 | 32% | Trong đó **10 cảnh dùng `creature-motion` (miễn phí, offline)**, 6 Veo, **1 Seedance** |
| `specimen` | 8 | 15% | Soi từng điểm — chỗ lời dẫn đang chỉ ra chi tiết. Hai trong số đó soi trên ảnh `kind:"anatomy"` |
| `notepage` | 8 | 15% | Người kể đang phân vân hoặc đang liệt kê |

*(`anatomy` là một **`kind` ảnh**, không phải một `el` — nó được dựng bằng `specimen`. Đừng lẫn hai trục.)*

**Ngân sách clip trả phí: 7/tập** (V2 là 18). Ở nhịp 2 tập/tuần là ~61 clip/tháng thay vì ~157. Chưa ai đo một clip Veo tốn bao nhiêu trong hạn mức 25k token — đo một lần rồi chốt lại con số này.

> `check-episode.py` báo khi một `el` chiếm quá 75%, hoặc bốn beat liền cùng công thức hình. Bảng trên nằm dưới ngưỡng.

---

## III · Bảng phân cảnh

Cột **Hình** ghi `el` · nguồn ảnh · tầng chuyển động. Cột **Chữ** là chữ trên màn hình — **dùng chung cho cả hai track giọng**, nên ghi tên EN.

### HỒI 1 · NGHỊCH LÝ (beat 00–02 · 78s)

```
[TIẾNG] 2 giây im tuyệt đối. Rồi gió qua trảng cỏ; một nhịp trầm rất khẽ, không rõ là tim hay là mô thực vật giãn.
[NHẠC] open-question.wav — một nốt treo, không giải quyết.
```

| Beat | Lời dẫn (VI) | Hình | Chữ trên màn hình | Ghi chú |
|---|---|---|---|---|
| **00** *(13,4s)* | "Ngày đầu tiên tôi gặp nó, nó đang nằm giữa lối mòn, bất động dưới nắng trưa. <br><br> Tôi tưởng nó đã chết. <br><br> Rồi cái hạt trên lưng nó khẽ co lại. <br><br> Nó đang thở. Và không phải chỉ bằng phổi." | **m1** `w:1.6` · `clip` · `creature-motion` từ `s04-bulbasaur-sunbath` — cả con nằm im, sườn phập phồng rất khẽ<br>**m2** `w:2.2` · `clip` · `creature-motion` macro bẹ củ co nhịp<br>`sfx` `breath-low.wav` v0.35 neo "thở" | `text` "VIRIDIAN FOREST" (3.8)<br>`caption` "Cá thể K-01 · ngày 1" (2.5) | Nhịp thở của **củ** phải lệch pha với nhịp thở của **thân** — đó là cả cái hook |
| **01** *(20,2s)* | "Tôi mang theo một câu hỏi từ rất lâu: có những sinh vật mà sự sống và năng lượng không tách rời nhau. <br><br> Tôi tới Viridian để làm một việc mà ở quê tôi người ta làm với sói và với voi: chọn một con, đi theo nó đủ lâu, rồi xem cái gì thay đổi. <br><br> Trong sổ của người bản xứ, con vật này được ghi là Bulbasaur. Trong sổ của tôi, nó là cá thể K-01. <br><br> Suốt mấy tuần đầu, nó chỉ có chừng ấy: một chữ và một con số." | **m1** `w:2.0` · `world` · `n01-forest-edge-dawn` — sương sớm, camera lia chậm, `fx:"dust"`<br>**m2** `w:2.0` · `notepage` · `v3-x01-day-one` — 3 dòng chữ tay hiện dần | `text` "SỔ THỰC ĐỊA" (4.0)<br>`caption` "Bulbasaur · K-01" (2.5)<br>`chip` "👁 QUAN SÁT" | `notepage` mở sớm để khán giả quen với quy ước "chữ tay = người kể đang viết". **Câu đầu là mục đích nghiên cứu của Dr. Holth** — nói một lần ở tập đầu, các tập sau tự chứng minh (docs/NARRATOR.md). Beat dài thêm ~4s |
| **02** *(44,6s)* | "Viridian là chỗ rừng già chạm vào đồng cỏ. Giữa hai thứ đó có một lối mòn nhỏ, cỏ bị đè rạp, và lối mòn ấy do chúng đi. <br><br> Ở trảng này tôi đếm được bảy cá thể. K-01 là con nhỏ nhất, và lúc nào cũng đi sau. Nếu chỉ nhìn qua, nó là con yếu nhất trong bảy con. <br><br> Nhưng suốt một tuần đầu tiên, tôi ghi lại chỗ nằm của từng con vào mỗi buổi trưa. Và K-01 luôn nằm đúng vệt nắng sáng nhất trong trảng. Không phải một hôm. Là cả bảy hôm. <br><br> Ở đây người ta không gọi con vật bằng số. Họ gọi theo dấu nó mang trên người. Con này có sẵn một dấu: cái củ trên lưng nó không mọc thẳng như sáu con kia, mà nghẹo hẳn về một bên. <br><br> Từ hôm ấy, trong sổ tôi, K-01 thành Búp Lệch." | **m1** `w:1.4` · `world` · `n02-population-scatter` — lối mòn cỏ rạp<br>**m2** `w:1.6` · `clip` · Veo — bảy con rải rác trên trảng<br>**m3** `w:1.8` · `notepage` · `v3-x02-sun-map` — sơ đồ bảy chỗ nằm, 7 chấm hiện dần theo "cả bảy hôm"<br>**m4** `w:2.0` · `specimen` · `v3-m06-crooked-bulb` — 1 callout "the crooked bud", `atWord:"nghẹo"` | `caption` "K-01 · Crookedbud" (2.5)<br>`chip` "👁 DẤU HÌNH THÁI" | **Tên đến SAU cái dấu.** Callout phải mở trước khi lời đọc tới chữ "Búp Lệch" |

### HỒI 2 · CÁI DẠ DÀY THỨ HAI (beat 03–05 · 116s)

| Beat | Lời dẫn (VI) | Hình | Chữ trên màn hình | Ghi chú |
|---|---|---|---|---|
| **03** *(36,4s)* | "Mỗi buổi trưa, Búp Lệch bỏ ăn. <br><br> Nó nằm yên tới mức có hôm tôi tưởng mình đã mất dấu, và bò vòng qua bụi dương xỉ để tìm. <br><br> Nhưng sau vài giờ, cái hạt trên lưng nó căng lên, còn cái bụng thì vẫn phẳng. <br><br> Nó không nhịn đói. Nó đang ăn một thứ khác. <br><br> Cuốn danh lục ghi hai dòng rời nhau, và tôi mất gần một tháng mới ghép được chúng lại: cái hạt lớn lên nhờ hút ánh mặt trời, và con vật này nhịn ăn được nhiều ngày liền nhờ phần dự trữ nằm trong củ. <br><br> Nói cách khác, thứ trên lưng nó không phải đồ trang trí, mà là một cái dạ dày thứ hai." | **m1** `w:1.8` · `clip` · `creature-motion` — ngủ trưa, bụi nắng, lá lay<br>**m2** `w:1.4` · `world` · `s04-bulbasaur-sunbath` — bụng phẳng, camera đẩy rất chậm<br>**m3** `w:2.4` · `specimen` trên ảnh `anatomy` `v3-a01-conduit` — 2 callout: "mạch dẫn từ củ vào thân", "khoang dự trữ" | `text` "DẠ DÀY THỨ HAI" (4.0)<br>`caption` "Quang năng nuôi thẳng mô động vật" (2.5)<br>`chip` "📖 DANH LỤC" | Hai dòng danh lục là **📖 có nguồn**; chữ "dạ dày thứ hai" là **🔬 cách nói của người kể** — tách rõ trong lời |
| **04** *(41,0s)* | "Nhưng ăn nắng thôi thì chưa đủ. Một cái cây còn cần nước và khoáng. <br><br> Tôi mất thêm ba tuần mới thấy Búp Lệch lấy hai thứ đó ở đâu. <br><br> Cuối buổi chiều, nó ra mép ao, đứng lún hai chân trước trong lớp bùn nhão, rất lâu, và không uống ngụm nào. <br><br> Ở quê tôi, ếch nhái gần như không uống bằng miệng. Chúng hút nước qua một vùng da mỏng ở bụng. <br><br> Còn phần khoáng, tôi ngờ nó không đến từ bên ngoài chút nào. Dưới rạn san hô, tảo sống trong mô con vật chủ dùng lại chính chất thải của nó để lớn. <br><br> Nếu cái củ này cũng vậy, thì nó đang được bón bằng thứ mà cơ thể Búp Lệch thải ra. Một vòng khép kín. Không rơi mất giọt nào." | **m1** `w:1.6` · `clip` · Veo — chân lún bùn, nước gợn<br>**m2** `w:1.2` · `world` · `v3-r01-coral-zoox` (ảnh `real`) — rạn san hô<br>**m3** `w:2.0` · `notepage` · `v3-x03-loop` — vòng khép kín vẽ dần: thải → rễ củ → đường → thân | `caption` "Thấm qua da · vòng khép kín" (2.4)<br>`chip` "🔬 ĐỐI CHIẾU TRÁI ĐẤT" | **Đối chứng là tảo cộng sinh trong mô san hô**, không phải sên lục Elysia — Elysia nổi tiếng vì *cướp lục lạp*, đó là đối chứng cho việc ăn nắng, không phải cho vòng tái dùng chất thải |
| **05** *(38,8s)* | "Tới đây thì câu hỏi trong sổ tôi đổi hẳn. <br><br> Ban đầu tôi viết: cái hạt này là vật ký sinh. Nó bám trên lưng, nó hút, nó lớn lên bằng thứ con vật kiếm được. <br><br> Nhưng ký sinh thì không làm cho vật chủ no. Còn Búp Lệch thì những ngày nắng gắt lại là những ngày nó khoẻ nhất. <br><br> Vậy Búp Lệch đang nuôi cái hạt, hay cái hạt đang nuôi Búp Lệch? <br><br> Ở quê tôi, hai kiểu sống chung này chỉ cách nhau một sợi tóc. Địa y là nấm và tảo dính vào nhau tới mức người ta từng tưởng là một loài. Còn cây tầm gửi thì cắm vòi vào thân cây chủ, rồi rút dần cho tới khi cây chủ chết đứng." | **m1** `w:1.6` · `notepage` · `v3-x04-crossed-out` — dòng "vật ký sinh" bị gạch, dòng mới viết đè lên<br>**m2** `w:1.3` · `world` · `v3-r02-lichen` (`real`) — địa y trên đá<br>**m3** `w:1.3` · `world` · `v3-r03-mistletoe` (`real`) — tầm gửi trên thân cây chết | `text` "AI ĐANG NUÔI AI?" (4.0)<br>`caption` "Cộng sinh và ký sinh cách nhau một sợi tóc" (2.6)<br>`chip` "🔬 GIẢ THUYẾT" | **Beat V2 đã xoá. Đây là chỗ đặt câu hỏi của cả tập** — bỏ nó đi thì mười phút giữa không còn xương sống. Câu gạch xoá trong sổ là hình ảnh mạnh nhất của beat |

### HỒI 3 · CHẠM (beat 06–07 · 82s)

| Beat | Lời dẫn (VI) | Hình | Chữ trên màn hình | Ghi chú |
|---|---|---|---|---|
| **06** *(44,5s)* | "Bảy con trong trảng không bao giờ nằm sát nhau. Mỗi con giữ một khoảng trống đủ rộng để nắng chạm được xuống lưng mình. <br><br> Chiều xuống, khi bóng rừng bò ra, những vệt nắng còn lại co rất nhanh, và lúc đó thì có chen lấn. Không con nào cắn con nào. Chúng ép vai, đẩy nhau, rồi con thua bỏ đi tìm vệt khác. <br><br> Búp Lệch thường ngủ cách một con lớn hơn chừng hai thân người. Đêm nào cũng vậy, cùng một khoảng cách. Hai con ấy chưa bao giờ chạm vào nhau. <br><br> Hôm con lớn kia bị rách một mảng da bên sườn, tôi mới đặt được tên cho nó: Vai Rách. Ở đây người ta đặt tên như thế. Cái tên đến sau vết thương. <br><br> Và cả trảng đổi chỗ nằm. Tới tối, bốn con đã nằm quanh Vai Rách." | **m1** `w:1.5` · `world` · `n04-sun-patch-dispute` — vệt nắng co lại, `camera` đẩy chậm<br>**m2** `w:1.6` · `clip` · Veo — hai con ép vai giành vệt nắng<br>**m3** `w:1.6` · `specimen` · `v3-s07-torn-flank` — 1 callout "torn flank", `atWord:"rách"`<br>**m4** `w:1.3` · `world` · `v3-s08-night-ring` — bốn con quanh Vai Rách, ánh trăng | `caption` "K-04 · Scar-Shoulder" (2.5)<br>`chip` "👁 TẬP TÍNH BẦY" | Lại đúng luật: callout mở **trước** khi lời đọc tới tên |
| **07** *(37,8s)* | "Chúng cũng chạm vào nhau, chỉ là không nằm cạnh nhau. <br><br> Hai sợi dây leo thò ra từ dưới củ, gặp nhau giữa không trung, cuộn lấy nhau vài giây, rồi thả. <br><br> Tôi đứng nhìn cảnh đó hai mươi phút và không ghi nổi chữ nào. <br><br> Vì thứ tôi vừa thấy không phải một cái roi. Nó gần với cái vòi con voi hơn. Để cầm, để chạm, để chào. <br><br> Và để gãi. Lưng là điểm mù: một con vật bốn chân, cổ ngắn, không thể tự quay lại chỗ cái củ. <br><br> Chiều hôm đó tôi thấy Búp Lệch vẩy một sợi dây leo qua lưng, gạt phắt một con sâu đang bò lên mép lá, đúng động tác cái đuôi ngựa xua ruồi trâu." | **m1** `w:2.2` · `clip` · Veo — hai dây leo cuộn nhau trong ráng chiều<br>**m2** `w:1.4` · `world` · `m02-vine-groom` — nhìn từ trên xuống, cho thấy lưng là điểm mù<br>**m3** `w:1.6` · `clip` · `creature-motion` — dây leo vẩy qua lưng gạt sâu | `text` "XÚC GIÁC, KHÔNG PHẢI VŨ KHÍ" (3.8)<br>`caption` "Dây leo: cầm · chạm · vệ sinh điểm mù" (2.6)<br>`chip` "👁 QUAN SÁT" | **Không gọi tên đòn đánh.** Tả cơ quan và việc nó làm |

### HỒI 4 · CÁI GIÁ (beat 08–09 · 79s)

```
[TIẾNG] Tiếng cánh lớn rẽ gió. Rồi im. Rồi một tiếng bung rất khẽ, gần như tiếng thở dài.
[NHẠC] tension.wav — trầm, dồn, KHÔNG cao trào kiểu phim hành động.
```

| Beat | Lời dẫn (VI) | Hình | Chữ trên màn hình | Ghi chú |
|---|---|---|---|---|
| **08** *(52,4s)* | "Con chim xuất hiện vào ngày thứ hai mươi hai. <br><br> Một con chim lớn, mỏ dài, bay vòng rất cao. Nó không săn cả trảng. Nó chỉ theo Búp Lệch. <br><br> Một bên mắt nó phủ một lớp màng đục màu tro, dấu của một vết thương cũ. Người bản xứ gọi nó theo đúng cái mắt ấy: Mắt Tro. <br><br> Lần bổ nhào đầu tiên, Búp Lệch không chạy. Nó ép sát người xuống nền đất ẩm dưới một tán dương xỉ, và đứng im. <br><br> Đây là lúc tôi hiểu ra bộ da của nó. Màu xanh lam với những đốm sẫm không đều, nhìn gần thì kỳ quặc, nhưng nằm dưới tán lá thì những đốm ấy trùng khít với các mảng nắng lọt qua kẽ lá rọi xuống đất. <br><br> Mắt Tro sượt qua cách chừng một sải tay, rồi bay vòng lại. <br><br> Lần thứ hai, cái củ trên lưng Búp Lệch hé ra ở đỉnh, và một màn bào tử mịn bung lên. Con chim đảo cánh, mất hướng, rồi bỏ đi." | **m1** `w:1.2` · `specimen` · `v3-s10-ashen-eye` — 1 callout "the ashen eye", `atWord:"tro"`<br>**m2** `w:1.6` · `specimen` · `v3-s11-camouflage` — 2 callout: đốm da / mảng nắng, cho thấy chúng trùng nhau<br>**m3** `w:1.6` · `clip` · **Seedance** — cú bổ nhào *(cảnh Seedance duy nhất của tập)*<br>**m4** `w:1.4` · `clip` · `creature-motion` — đỉnh củ hé, bào tử toả chậm<br>`sfx` `powder-burst.wav` v0.4 lead 0.2 neo "bung" | `caption` "Mắt Tro · một mắt mù" (2.5)<br>`chip` "📖 DANH LỤC · bột ngủ" | Nguỵ trang là **quan sát**, không phải canon → `specimen` để khán giả **tự thấy** hai mảng trùng nhau. Không viết tên đòn đánh bằng tiếng Anh |
| **09** *(26,6s)* | "Nhưng cái tôi ghi đậm nhất hôm đó không phải màn bào tử. <br><br> Sau khi Mắt Tro bỏ đi, Búp Lệch nằm im gần hết buổi chiều. Không ăn, không đổi chỗ, không phản ứng khi tôi lại gần. <br><br> Và cái củ trên lưng nó nhỏ lại thấy rõ. <br><br> Thứ vừa cứu mạng nó được lấy ra từ đúng cái kho mà nó phơi nắng cả tháng để tích. <br><br> Từ hôm đó tôi thôi ghi những thứ này vào mục khả năng. Tôi chuyển hết sang mục thu và chi." | **m1** `w:1.8` · `clip` · `creature-motion` — nằm im, thở nông<br>**m2** `w:2.0` · `notepage` · `v3-x05-ledger` — trang sổ: tiêu đề "KHẢ NĂNG" bị gạch, viết đè "THU & CHI", hai cột hiện dần | `text` "THU VÀ CHI" (4.0)<br>`caption` "Cái kho một tháng · tiêu trong một hơi" (2.6)<br>`chip` "👁 QUAN SÁT" | **Không có con số.** "Nhỏ lại thấy rõ" là quan sát; "50%" là bịa. Cái sổ kế toán làm hình ảnh thay cho con số |

### HỒI 5 · CÙNG MỘT CƠ QUAN (beat 10–11 · 101s)

| Beat | Lời dẫn (VI) | Hình | Chữ trên màn hình | Ghi chú |
|---|---|---|---|---|
| **10** *(49,5s)* | "Ở vùng đất này có một thứ mà quê tôi không có. Người ta đấu với nhau bằng chính những con vật này. <br><br> Tối hôm ấy tôi xuống thị trấn, đứng ở vòng ngoài một sân đất, và xem một trận. <br><br> Trong sân, hai sợi dây leo không còn để chào nhau nữa. Chúng quật. <br><br> Cùng một cơ quan: ngoài rừng để hái quả và gạt sâu, trong sân để đánh. <br><br> Tôi không thấy điều đó đáng lên án. Cái vòi voi ở quê tôi cũng vừa vuốt ve con non, vừa quật gãy được xương người. <br><br> Nhưng có một cú làm tôi ngồi viết tới gần sáng. Con vật trong sân không bắn ngay. Nó đứng yên một nhịp, cái củ trên lưng sáng lên, rồi mới phóng ra một luồng sáng. <br><br> Khán giả quanh tôi coi nhịp chờ ấy là điểm yếu. Tôi thì nhận ra mình vừa nhìn thấy cái kho ban trưa, bị rút cạn trong một hơi thở. <br><br> Về tới rừng thì trời đã sáng. Búp Lệch đã nằm sẵn trong vệt nắng đầu tiên." | **m1** `w:1.5` · `world` · `b01-arena-dusk` — sân đất, bóng người mờ ở vòng ngoài (`allow:["humans"]`)<br>**m2** `w:1.6` · `clip` · Veo — dây leo quật xuống nền đất<br>**m3** `w:1.4` · `world` · `b03-solarbeam-charge` — củ sáng lên, khoảnh khắc đứng yên trước khi phóng<br>**m4** `w:1.5` · `world` · `s04-bulbasaur-sunbath` — **về lại Búp Lệch trong vệt nắng** | `caption` "Cùng một cơ quan · hai cách dùng" (2.6)<br>`chip` "⚔ TRẬN ĐẤU" | V1 và V2 đều **bỏ rơi cá thể trung tâm cả beat này**. Câu cuối và `m4` kéo về — vắng chủ thể một beat là chỗ mạch đứt |
| **11** *(51,9s)* | "Những người nuôi lâu năm ở đây nói mỗi loài có một nết riêng. Với loài này thì có hai. <br><br> Nết thứ nhất tôi tự đo được trước khi nghe ai nói. Giữa trưa nắng gắt, Búp Lệch đi nhanh hơn hẳn chính nó lúc trời râm. Tôi bấm giờ trên cùng một quãng đường, và con số gần như gấp đôi. <br><br> Ở quê tôi, thằn lằn và rắn phải phơi nắng cho ấm người đã, rồi mới chạy nhanh được. Một cỗ máy chạy bằng nắng thì nắng càng gắt, máy càng khoẻ. <br><br> Nết thứ hai tôi chỉ thấy trong sân đấu, và nó làm tôi khó chịu hơn là thán phục. Khi con vật đã bị thương nặng, gần như không đứng nổi, những cú đánh của nó đột nhiên mạnh hẳn lên. <br><br> Tôi không nghĩ nó khoẻ hơn. Tôi nghĩ nó đang dốc nốt chỗ dự trữ. Một lần. Và hết. <br><br> Ở quê tôi, cây thùa sống mấy chục năm chỉ để dồn tất cả vào một lần trổ hoa, rồi chết." | **m1** `w:1.8` · `notepage` · `v3-x06-stopwatch` — hai cột số bấm giờ, nắng / râm<br>**m2** `w:1.3` · `world` · `v3-r04-lizard-basking` (`real`) — thằn lằn phơi nắng<br>**m3** `w:1.6` · `specimen` trên `anatomy` `v3-a02-reserve` — 1 callout: khoang dự trữ cạn dần<br>**m4** `w:1.3` · `world` · `v3-r05-agave` (`real`) — cây thùa trổ hoa rồi chết | `caption` "Nắng gắt thì nhanh gấp đôi" (2.5)<br>`chip` "📖 DANH LỤC · hai nết" | Con số bấm giờ là **quan sát của người kể**, hợp lệ — khác hẳn "23°" bịa ra |

### HỒI 6 · ĐỔI HÌNH (beat 12–14 · 138s)

```
[TIẾNG] Tiếng mô căng, rất chậm. Gió trong lòng chảo. KHÔNG có tiếng xương gãy, KHÔNG có tiếng rách.
[NHẠC] threshold.wav — căng và nín, không giải quyết.
```

| Beat | Lời dẫn (VI) | Hình | Chữ trên màn hình | Ghi chú |
|---|---|---|---|---|
| **12** *(54,2s)* | "Tháng thứ tư, Búp Lệch đổi nếp. <br><br> Nó nằm ngoài nắng lâu hơn hẳn, bỏ cả nhịp trú trưa trong bóng râm, và ăn nhiều hơn trước. Nó cũng đi chậm lại. Hai sợi dây leo dày lên, cử động nặng nề, có lần vươn ra rồi rơi xuống như chính nó cũng không điều khiển nổi. <br><br> Có một buổi sáng tôi ngồi đúng ba tiếng chỉ để ghi một chi tiết. <br><br> Đầu Búp Lệch quay về hướng nam, nằm im. Nhưng cái củ trên lưng thì vặn chậm về phía đông, theo mặt trời. Hai thứ trên cùng một cơ thể, quay về hai hướng khác nhau, trong cùng một buổi sáng. <br><br> Và cái củ mọc lệch mà tôi lấy làm tên cho nó, hoá ra không phải một tật bẩm sinh. <br><br> Đó là vết của một động tác lặp lại mỗi ngày, từ ngày nó còn nằm trong vệt nắng ấy. <br><br> Ở quê tôi, hoa hướng dương non cũng quay theo mặt trời suốt ngày. Tới khi nở hẳn thì đứng yên, và đứng mãi về một hướng." | **m1** `w:1.5` · `clip` · `creature-motion` — dây leo vươn rồi rơi<br>**m2** `w:2.2` · `clip` · `creature-motion` **time-lapse**: đầu đứng yên, củ vặn theo nắng<br>**m3** `w:1.8` · `specimen` · `v3-m06-crooked-bulb` — **quay lại đúng ảnh của beat 02**, lần này callout đọc là "the trace, not the defect"<br>**m4** `w:1.2` · `world` · `v3-r06-sunflower` (`real`) | `text` "KHÔNG PHẢI TẬT" (4.0)<br>`caption` "Crookedbud · vết của một động tác lặp lại" (2.6)<br>`chip` "👁 QUAN SÁT" | **Đỉnh của tập.** Dùng lại **đúng tấm ảnh** của beat 02 là cả sức mạnh của cú lật — khán giả nhận ra ngay |
| **13** *(32,0s)* | "Cuối tháng ấy, Búp Lệch rời đàn. <br><br> Nó bỏ trảng nắng, đi sâu vào phía rừng già, và tôi mất dấu nó bốn ngày. <br><br> Vai Rách vẫn ở lại trảng. Sáng nào nó cũng nằm đúng chỗ cũ, cách một khoảng đúng bằng hai thân người — chỗ trống ấy không ai vào nằm. <br><br> Đêm thứ năm tôi tìm thấy Búp Lệch trong một hõm đất khuất sau vành cây, cùng hơn mười con khác, đứng thành vòng. Không con nào chạm vào con nào. Không con nào phát ra tiếng. <br><br> Người bản xứ kể rằng mỗi năm chúng tụ về đây một lần. Họ gọi chỗ này là Khu Vườn Kỳ Bí. <br><br> Lúc đó tôi nghĩ nó sắp chết. Tôi đã viết nguyên một trang về chuyện ấy." | **m1** `w:1.3` · `world` · `v3-s08-night-ring` — **chỗ trống bên cạnh Vai Rách**<br>**m2** `w:1.6` · `clip` · Veo — vòng tròn trong lòng chảo, sương đêm<br>**m3** `w:1.5` · `notepage` · `v3-x07-wrong-page` — trang "tôi nghĩ nó sắp chết", chữ viết vội | `caption` "The Mysterious Garden" (2.5)<br>`chip` "🎬 NGƯỜI BẢN XỨ KỂ" | **Vai Rách quay lại** — V1 và V2 đều bỏ dở tuyến này. Nghi lễ tụ họp chỉ có trong anime → nhãn **🎬**, kể như lời người bản xứ, **không** gắn 📖. Không có "chu kỳ trăng" |
| **14** *(51,6s)* | "Tôi không nhìn thấy khoảnh khắc ấy. Tôi ngủ quên sau hai đêm thức trắng, và khi tỉnh dậy thì trời đã sáng. <br><br> Cái hõm đất trống không. <br><br> Nhưng nó để lại đủ thứ cho một người có nghề đọc. <br><br> Đất bị cày lên thành những rãnh ngắn, chỗ bốn cái chân đã bấu xuống để chống đỡ một sức nặng mới. Cỏ quanh đó bẹp thành một vòng tròn. Quanh cổ củ, những bẹ lá già bong ra, khô, cuộn lại như vỏ hành. <br><br> Và cả hõm đất sực mùi hoa, thứ mùi mà trước đó tôi chưa từng ngửi thấy ở loài này. <br><br> Phía bên kia bãi cỏ, trong sương, có một cái bóng lớn hơn cái bóng tôi đã theo suốt một năm. Nó bước ra khỏi vùng sáng, và để lại những dấu chân sâu hơn hẳn, có một vệt kéo lê phía sau. <br><br> Thứ đứng đó không còn là con vật tôi từng ghi chép. <br><br> Nhưng khi tôi mở sổ, nó vẫn nghiêng đầu về phía tiếng bút." | **m1** `w:1.6` · `specimen` · `m04-hollow-empty` — 3 callout: rãnh cày · cỏ bẹp · bẹ lá khô<br>**m2** `w:1.4` · `world` · `m05-silhouette-mist` — bóng lớn trong sương<br>**m3** `w:1.5` · `clip` · `creature-motion` — Ivysaur thở, nụ phập phồng<br>**m4** `w:1.2` · `world` · `n11-tracks-mud` — dấu chân sâu, vệt kéo lê | `text` "ĐỌC HIỆN TRƯỜNG" (3.8)<br>`caption` "Chân hoá cột · một sức nặng mới" (2.6)<br>`chip` "👁 DẤU VẾT" | **Không lột da, không cảnh biến hình.** Cả beat kể bằng dấu vết — đúng luật kênh, và cũng là cách rẻ nhất |

### HỒI 7 · KHÔNG CÓ CÂU TRẢ LỜI (beat 15 · 86s)

```
[TIẾNG] Mưa trên tán lá. Một nhịp thở rất lớn, rất chậm. Côn trùng.
[NHẠC] close-circle.wav — ấm, ngắn. Tắt hẳn ở câu cuối cùng: KHÔNG có nhạc dưới câu hỏi kết.
```

| Beat | Lời dẫn (VI) | Hình | Chữ trên màn hình | Ghi chú |
|---|---|---|---|---|
| **15** *(86,2s)* | "Cái nụ trên lưng nó bây giờ nặng tới mức nó không đứng bằng hai chân sau được nữa. Chân và thân đã dày lên để đỡ. Ở quê tôi, voi và rùa khổng lồ trả đúng cái giá ấy: mang nặng thì chân phải thành cột. <br><br> Mùa mưa cuối cùng trong cuốn sổ này, tôi gặp một con trưởng thành già sống ở bìa rừng. Thân nó đã hoá gỗ, dương xỉ nhỏ và rêu mọc luôn trên lưng, bông hoa to và hơi bạc màu. <br><br> Người bản xứ gọi con này là Lưng Rêu, và họ bảo nó ở bìa rừng ấy từ trước khi họ sinh ra. <br><br> Chính giữa bông hoa của Lưng Rêu có một cái nhụy. Ở những con khác tôi từng gặp thì không có. Lưng Rêu là con cái. Và đó là lần đầu tiên tôi phân biệt được giới tính của loài này bằng mắt thường. <br><br> Còn Búp Lệch thì chưa. Cái nụ của nó chưa nở, nên tôi vẫn chưa biết mình đã theo một con đực hay con cái. <br><br> Sau mỗi trận mưa, hương hoa của Lưng Rêu đậm hẳn lên, và tôi đã ngồi nhìn hai con vật đang gầm gừ nhau cùng ngồi xuống, cách nhau vài bước, trong làn hương ấy. <br><br> Tôi vẫn không biết cái hạt trên lưng Búp Lệch là một phần của nó, hay một sinh vật khác sống nhờ nó. <br><br> Có lẽ câu trả lời không nằm ở chỗ ta gọi nó là gì. Có lẽ một cơ thể có thể bắt đầu từ hai sự sống, và vẫn thành một cá thể duy nhất. <br><br> Ở trang sau của cuốn danh lục có một loài mang lửa ở chóp đuôi. Nếu ngọn lửa ấy tắt khi trời mưa, nó sống sót bằng cách nào?" | **m1** `w:1.4` · `world` · `n13-ivysaur-strain` — chân dày, camera đẩy từ bàn chân lên<br>**m2** `w:1.6` · `clip` · `creature-motion` — Lưng Rêu thở chậm trong mưa<br>**m3** `w:1.5` · `specimen` · `n19-old-venusaur` — 1 callout "the pistil", `atWord:"nhụy"`<br>**m4** `w:1.3` · `world` · `n18-scent-truce` — hai con ngồi xuống cách nhau vài bước<br>**m5** `w:1.8` · `notepage` · `v3-x08-last-page` — trang cuối, câu hỏi viết ra rồi **để trống bên dưới** | `caption` "Moss-Back · con cái, bìa rừng già" (2.6)<br>`text` "HAI SỰ SỐNG, MỘT CÁ THỂ" (3.8)<br>`chip` "🔬 KHÔNG KẾT LUẬN" | Trang sổ cuối để trống là hình ảnh của việc **không trả lời**. Câu hỏi treo sang tập sau được giữ — kênh mới cần lý do để người ta bấm tập tiếp |

### `short-outro` *(bắt buộc — thiếu là không có bản Short)*

| Lời | Hình | Chữ |
|---|---|---|
| "Cái hạt ấy là một phần của nó, hay một sinh vật khác đang sống nhờ nó? <br><br> Sau mười bốn tháng ngoài đồng, tôi vẫn chưa trả lời được." | `notepage` · `v3-x08-last-page` — chữ hiện rồi dừng ở khoảng trống | `caption` "K-01 · Crookedbud" (2.5) — **không chữ tràn**, Short không có thumbnail theo ngôn ngữ |

---

## IV · Ảnh — dùng lại gì, sinh thêm gì

**Dùng lại 15 ảnh đã có** trong `public/img/kanto-001/`, **đừng sinh lại** — sinh lại ra ảnh khác là
hỏng mọi toạ độ callout đã đo:

`n01-forest-edge-dawn` · `n02-population-scatter` · `s04-bulbasaur-sunbath` · `n04-sun-patch-dispute` ·
`n05-sunbathing-group` · `n06-vine-touch` · `m02-vine-groom` · `n08-raptor-strike` · `n09-sleep-powder` ·
`b01-arena-dusk` · `b02-vine-whip-battle` · `b03-solarbeam-charge` · `m01-mud-soak` · `m03-heliotropism` ·
`m04-hollow-empty` · `m05-silhouette-mist` · `n11-tracks-mud` · `n12-ivysaur-plate` ·
`n13-ivysaur-strain` · `n16-evolution-gathering` · `n18-scent-truce` · `n19-old-venusaur`

**Sinh thêm 21 ảnh** — `bible/shots/kanto-001-v3.json` → `prompts/kanto-001-v3.flow.txt`:

| Nhóm | `kind` | Số | Id |
|---|---|---|---|
| Giải phẫu | `anatomy` | 2 | `v3-a01-conduit` · `v3-a02-reserve` |
| Trang sổ | `fieldnote` | 8 | `v3-x01`…`v3-x08` |
| Loài Trái Đất | `real` | 6 | coral · lichen · mistletoe · lizard · agave · sunflower |
| Cảnh thiếu | `scene` | 5 | `v3-m06-crooked-bulb` · `v3-s07-torn-flank` · `v3-s10-ashen-eye` · `v3-s11-camouflage` · `v3-s08-night-ring` |

Ảnh `fieldnote` **chừa trống một phần ba bên phải, không một chữ, không một mũi tên** — chữ do
`el:"notepage"` vẽ lên. Nhờ vậy bản EN dùng chung y hệt tấm giấy, chỉ đổi lớp chữ.

`v3-m06-crooked-bulb` là ảnh quan trọng nhất trong đợt này: nó xuất hiện **hai lần** (beat 02 đặt tên,
beat 12 lật lại), và cú lật chỉ ăn khi khán giả nhận ra **đúng tấm ảnh cũ**.

---

## V · V3 sửa gì so với V2

| # | V2 | V3 |
|---|---|---|
| 1 | `Saur`, `Scar-Shoulder`, `Ash-Eye`, `Moss-Back` đọc trong lời VI | Màn hình ghi tên EN, giọng VI đọc **Búp Lệch · Vai Rách · Mắt Tro · Lưng Rêu**. `Crookedbud` thay `Saur` để beat 12 dựng được |
| 2 | `SolarBeam` ×5, `Sleep Powder` ×1, in lên màn hình | Gọi theo nghĩa sinh học. Không một tên đòn đánh nào |
| 3 | "Tiêu hao 50% sinh khối" dưới nhãn 📖; "góc nghiêng 23°" | Bỏ hết số bịa. Beat 09 dùng **trang sổ thu–chi** làm hình ảnh thay con số |
| 4 | Nghi lễ đổi hình gắn 📖 | Gắn **🎬**, kể như lời người bản xứ. Bỏ "chu kỳ trăng" |
| 5 | **Xoá beat 05** — câu hỏi trung tâm biến mất khỏi mười phút giữa | Dựng lại beat 05, kèm địa y / tầm gửi |
| 6 | Không có `short-outro` | Có |
| 7 | `clip` 81% · 18 clip trả phí | `world` 38% · `clip` 32% (chỉ **7** clip trả phí, 10 cảnh còn lại miễn phí) · `specimen` 15% · `notepage` 15% |

Kèm bốn sửa nhỏ: `specimen` không soi được trên clip (engine dùng `<Img>`, không nhận video) nên mọi `specimen` ở đây đều trên ảnh tĩnh · đối chứng vòng khép kín trả về **tảo cộng sinh trong san hô** thay vì sên lục Elysia · **Vai Rách quay lại** ở beat 13 · beat 10 kéo về cá thể trung tâm ở câu cuối.

---

## VI · Còn nợ

1. **Bản EN chưa có.** Kênh đã chốt EN là bản gốc, nhưng V1, V2 và V3 đều viết tiếng Việt trước. Đây là món nợ có ý thức: cần viết bản EN rồi đối chiếu ngược, hoặc chấp nhận tập 001 là ngoại lệ và áp luật EN-trước từ tập 002.
2. **`thumb.json` chưa sửa.** Vẫn hứa "Vì sao cứ 8 con Bulbasaur thì 7 con là đực?" — câu hỏi tập không trả lời. Đề nghị đổi sang chính câu hỏi của tập: *"Con thú nuôi cái hạt, hay cái hạt nuôi con thú?"*
3. **Chưa chuyển thành `content.py` + `scenes.json`.** Bản này là kịch bản để duyệt; máy chưa đọc được.
4. **Chưa đo một clip Veo tốn bao nhiêu** trong hạn mức 25k token/tháng. Con số "5 clip trả phí/tập" là mục tiêu, chưa phải ràng buộc đã kiểm.
