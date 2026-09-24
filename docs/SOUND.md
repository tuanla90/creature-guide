# Tiếng của sinh vật · Sound bible

Cùng vai trò với `bible/creatures/*.json` nhưng cho tai: **một loài phải nghe giống nhau ở mọi tập**.
Nên thứ được lưu lại là **công thức**, không phải file wav. File có thể làm lại; công thức thì không
nhớ nổi sau sáu tháng.

## Luật

1. **Không dùng tiếng kêu trong game và tiếng lồng trong anime.** Vừa là audio có bản quyền, vừa phá
   khung "đây là con vật thật" — một tiếng 8-bit là hỏng cả tập.
2. **Mọi tiếng kêu là 🔬 giả thuyết.** Danh lục gần như không mô tả âm thanh của dòng Bulbasaur.
   Nên mỗi cue phải neo vào **một loài có thật**, ghi rõ trong bảng, đúng luật của [CREATURE-LENS.md](CREATURE-LENS.md).
3. **Giải phẫu quyết định âm sắc.** Con vật lưỡng cư bốn chân, cổ ngắn, có túi khí → tiếng trầm, ngắn,
   có cộng hưởng; không rít, không gầm kiểu thú ăn thịt có răng nanh. Cái củ là **mô thực vật**, nên
   tiếng của nó là tiếng gỗ ẩm vặn và lá cọ, không phải tiếng thịt.
4. **Nguồn chỉ lấy ba nơi** (đã đọc giấy phép tận nơi, không nghe đồn):

   | Nguồn | Giấy phép | Ghi nguồn | Hợp với |
   |---|---|---|---|
   | [Freesound](https://freesound.org) **lọc CC0** | CC0 — từ bỏ mọi quyền | không cần | tiếng loài cụ thể: ếch, cóc, vạc, quạ |
   | [Pixabay](https://pixabay.com/sound-effects/) | Pixabay Content License | không cần | tiếng thường gặp, lớp nền phổ thông |
   | [Sonniss GDC Bundle](https://gdc.sonniss.com/) | royalty-free, thương mại, có kiếm tiền | không cần | lớp nền và foley chất lượng cao, mỗi năm ~20 GB |

   Lọc CC0 trên Freesound: gõ từ khoá rồi bấm **Creative Commons 0** ở cột *licenses* bên phải.

   **Hai điều cấm của Sonniss, đọc kỹ vì nó dính tới cách kênh này làm việc:**
   - *Không phát tán lại chính file tiếng.* `assets/` nằm ngoài git là đúng — đẩy thư mục ấy lên
     một repo công khai là vi phạm.
   - *Không dùng để huấn luyện AI.* Đưa vào video thì được, đưa vào một mô hình audio thì không.

   Không đụng: BBC Sound Effects (cấm thương mại), Macaulay (phải mua license).

   **Không dùng CC-BY, và không dùng xeno-canto.** CC-BY cho phép thương mại, nhưng đổi lại mỗi
   tập phải nuôi một danh sách credit trong phần mô tả — việc tay, lặp mãi, và sai một dòng là vi
   phạm. Ba nguồn trên đều **không đòi ghi nguồn**; giữ đúng ba nguồn ấy.

   **Khi kho CC0 không có loài đúng** — hay gặp nhất với chim nước như vạc — thì **đổi loài, đừng
   đổi nguồn.** Luật 2 đòi mỗi lớp neo vào *một loài có thật*, chứ không đòi đúng loài đã ghi lúc
   soạn bảng. Cái tai cần là **hình dạng tiếng**: một tiếng quạc khàn, ngắn, gắt. Con ngỗng cho
   đúng thứ ấy và có đầy trong kho CC0. Đổi xong thì **sửa trường `species` trong `sfx.json` thành
   con vật thật sự đã dùng** — bảng đó là chỗ trả lời "tiếng này ở đâu ra", nó phải đúng.
5. **Tránh âm có chữ ký.** Tiếng hét chim ưng đuôi đỏ, tiếng voi rống, tiếng sư tử — tai người nhận
   ra ngay "à, con này". Nếu buộc phải dùng, chỉ lấy làm **lớp chìm** dưới 25% âm lượng.

## Cách ghép nhiều loài thành một con

Không phải chồng đống lên nhau — **chia theo vai, mỗi vai một dải tần**:

| Lớp | Dải | Nó nói lên điều gì | Lấy từ |
|---|---|---|---|
| **Thân** (body) | 40–150 Hz | con vật **to cỡ nào** | bò rống, lợn gầm gừ, sine 45 Hz bọc envelope |
| **Giọng** (voice) | 200–1200 Hz | nó là **loài gì**, cảm xúc gì | ếch, cóc, vạc, ngỗng — lớp mang bản sắc |
| **Chi tiết** (texture) | 2–8 kHz | nó **ướt hay khô**, gần hay xa | thở qua mũi, nước bọt, lá cọ, cỏ sột soạt |

Luật ghép: **mỗi lớp một loài, không hơn**. Ba loài là đủ để tai không nhận ra con nào; bốn năm loài
thì thành cháo, mất luôn cảm giác đây là một cơ thể. Và cả ba lớp phải **bắt đầu cùng một khoảnh khắc**
— lệch 40 ms là tai nghe ra hai con vật đứng cạnh nhau chứ không phải một con.

Hạ cao độ: dịch **cả formant** (`asetrate`, hoặc "Change Speed" trong Audacity) thì nghe như **con vật
to hơn**; giữ formant (`rubberband ... formant=preserved`, "Change Pitch") thì vẫn nghe là **đúng con
ấy đang hạ giọng**. Sinh vật hư cấu gần như luôn muốn vế đầu.

## Bảng cue — Kanto #001–003

Mỗi cue: loài thật làm gốc · từ khoá đi tìm · xử lý. `k7` là cá thể trung tâm K-01 (Shiny Bulbasaur).

| id | beat | Cue | Thân | Giọng | Chi tiết | Xử lý |
|---|---|---|---|---|---|---|
| `amb-edge-day` | nền | rừng chạm đồng cỏ, trưa | — | ve sầu xa | gió qua cỏ khô | loop, cắt bớt 4–8 kHz cho lùi ra sau |
| `amb-edge-dawn` | 01,12 | bìa rừng lúc rạng | — | chim thưa | sương rơi trên lá | như trên, tối hơn |
| `call-k7-soft` | 00,03 | tiếng thở của K7 lúc nằm | bò rống −70% | ếch ương một tiếng | hơi thở qua lỗ mũi ướt | `asetrate*0.55`, `tremolo=f=17`, lowpass 2.2 kHz |
| `call-contact` | 06 | tiếng gọi giữ khoảng cách | lợn grunt | cóc trầm | — | như trên, ngắn 0.4 s, lặp 2 tiếng cách 1.2 s |
| `call-alarm` | 08 | lúc con Fearow bổ nhào | — | vạc kêu, hạ 4 bán cung | cỏ bật | attack gắt, cắt đuôi vang |
| `bulb-creak` | 12 | củ vặn theo mặt trời | — | — | bẻ cần tây + vặn vải ướt | `asetrate*0.7`, bandpass 1.6 kHz, `aecho` nhẹ |
| `bulb-open` | 08 | củ hé ra ở đỉnh | — | — | tách vỏ măng, lá tươi xé chậm | kéo dài 1.5 s bằng paulstretch |
| `powder-burst` | 08 | màn bào tử bung | — | — | nhiễu trắng + thổi miệng đã lọc hơi người | bandpass 4 kHz, fade 15 ms vào / 300 ms ra |
| `vine-touch` | 07 | hai dây leo cuộn nhau | — | — | vải ướt trượt, dây thừng mềm | rất khẽ, gần mic, không vang |
| `vine-whip` | 09,10 | dây leo quật | gỗ gãy trầm | — | roi vút (hạ tông) | cắt ngay đuôi vút — đây là mô thực vật, không phải roi da |
| `mud-suck` | 04 | rút chân khỏi bùn | — | — | bùn/đất nhão | giữ nguyên, chỉ hạ 2 bán cung |
| `step-soft` | nhiều | bước chân K7 | sine 45 Hz | — | lá khô vò | 3 lớp, tổng dưới 0.25 s |
| `step-heavy` | 15 | bước chân Venusaur | sine 38 Hz | — | lá + cành nhỏ gãy | như trên, thêm rung đất 0.6 s sau |
| `raptor-dive` | 08 | con Fearow lao xuống | — | quạ hạ 5 bán cung | gió qua lông cánh | **tránh** tiếng chim ưng đuôi đỏ kinh điển |
| `rain-leaves` | 15 | mưa trên tán lá | — | — | mưa rơi trên lá rộng | loop |
| `arena-crowd` | 10,11 | trận đấu của trainer | — | đám đông xa | — | lowpass 1 kHz, mono, đẩy xuống −24 dB |
| `swell-change` | 13,14 | đêm cả đàn tụ về | gió hút trầm | — | mô gỗ căng, đất lún | **không có tiếng biến hình** — chỉ căng và nín |

## Máy dựng được cái gì, và không dựng được cái gì

Đã nghe hết 17 cue rồi mới viết mục này, nên nó là kết quả chứ không phải dự đoán. Ranh giới
nằm đúng ở chỗ **cái gì sinh ra âm thanh ấy**:

| | Máy dựng | Vì sao |
|---|---|---|
| **Chất liệu** — bẻ, xé, vò lá khô, trượt vải ướt, bùn, roi vút, bước chân | **được, dùng luôn** | tiếng của chúng *đúng là* nhiễu qua bộ lọc cộng hưởng rồi tắt dần. Viết bằng numpy không phải bắt chước, mà là làm đúng cái vật lý ấy |
| **Giọng** — ếch, cóc, vạc, quạ | **không** | tai người có phần chuyên trách cho tiếng sinh vật. Chuỗi xung + formant cố định thiếu đúng những thứ nó bắt: hơi rung thất thường, formant trôi trong một tiếng kêu, tạp âm của mô sống |
| **Không gian** — rừng trưa, rạng sáng, mưa, đám đông | **không** | nghe ra *nhiễu*, không ra *một chỗ*. Một khu rừng là hàng trăm sự kiện rời nhau ở những khoảng cách khác nhau, cộng tiếng vang và độ hút của không khí |

Suy ra thẳng từ dữ liệu, không phải đánh dấu tay: cue nào có lớp `role: "voice"` là có dây thanh,
cue nào `loop: true` là một không gian. `build-sfx.py` tự tách hai nhóm ấy ra, gắn nhãn
**PHẢI THAY**, và in sẵn từ khoá đi tìm cho từng lớp.

Với Kanto #001 thì danh sách phải đi tìm là **10 lớp trong 8 cue** — bốn tiếng con vật, bốn lớp
nền. Chín cue chất liệu còn lại dùng được ngay.

> **Cổng:** không cue nào còn nhãn PHẢI THAY khi lên YouTube. Tiếng tổng hợp để dựng và canh nhịp
> thì được; để đăng thì không.

## Quy trình

Công thức của tập nằm ở `videos/<slug>/sfx.json` — bảng cue ở trên, viết ra dạng máy đọc được.

```bash
PYTHONUTF8=1 python tools/build-sfx.py <slug>                  # cả tập
PYTHONUTF8=1 python tools/build-sfx.py <slug> --only powder-burst
PYTHONUTF8=1 python tools/build-sfx.py <slug> --list           # xem bảng cue
```

Với mỗi lớp, tool tìm file thật ở `assets/sfx-src/<cue>/<tên lớp>.wav` — `<tên lớp>` là trường
`synth` của lớp ấy (`frog_uong.wav`, `cow_bellow.wav`…), hoặc đặt thẳng trường `file` nếu muốn tên
khác. **Không có file thật thì tool tự dựng lấy một tiếng tổng hợp** đúng dải tần, đúng giải phẫu,
đúng độ dài — đủ để dựng hình, canh nhịp và soát, nhưng chưa phải con vật thật.

Tải về rồi thì **đừng chép tay** — `/nap-am <cue>/<lớp>` lấy file mới nhất trong Downloads, đổi
sang wav 48 kHz, đặt đúng chỗ và dựng lại cue ấy; bản gốc chỉ nằm ở một nơi duy nhất.

Nên thứ tự làm ngược lại so với trước: dựng trước, nghe, rồi mới đi tìm. Đi tìm theo cột "từ khoá"
trong bảng, tải về đúng chỗ trên (giữ nguyên file gốc, đừng ghi đè), chạy lại lệnh cũ — công thức
không đổi, chỉ nguyên liệu tốt lên.

**Lớp phải thay trước tiên là GIỌNG.** Thân và chi tiết tổng hợp thì tai bỏ qua được; còn ếch, cóc,
vạc, quạ là chỗ tai người bắt bài trong nửa giây.

Ra: `public/audio/sfx/<ep>/<cue>.wav`, 48 kHz, đỉnh −3 dBFS (tiếng nền chuẩn theo độ lớn nghe được
chứ không theo đỉnh — nếu không, một giọt sương to nhất sẽ dìm cả lớp nền xuống).

Trộn: tiếng nền −28 dB, cue −12 tới −18 dB, lời dẫn luôn là thứ to nhất. Độ lớn của từng cue để sẵn
ở trường `volume` trong `sfx.json`, chép thẳng sang `scenes.json`. Cue nào đè lên một câu quan trọng
thì bỏ cue, đừng hạ lời.

## Nhạc nền

```bash
PYTHONUTF8=1 python tools/build-music.py            # cả bộ -> public/audio/music/
PYTHONUTF8=1 python tools/build-music.py --only mystic
PYTHONUTF8=1 python tools/build-music.py --check    # đo tông của thứ đang có
```

### Tông của kênh: La thứ (A minor), trục La–Mi

Đây là luật quan trọng nhất của phần nhạc, và là lý do bộ nhạc được dựng chứ không đi nhặt mỗi
nơi một bản. **Mọi đoạn chỉ được dùng bảy nốt của La thứ** (La Si Do Re Mi Fa Sol).

Điều kiện là **bộ nốt**, không phải nốt trầm: Do trưởng và La thứ dùng chung đúng bảy nốt ấy. Một
bản viết ở La trưởng chỉ cần dịch xuống ba bán cung là thành Do trưởng, và lúc đó nó dùng đúng bộ
nốt của La thứ — `import-music.py --shift auto` thử cả mười hai vòng xoay nên nó tự tìm ra nước đi
ấy. **Bản nghiêng về Do trưởng không phải bản hỏng**: cùng bộ nốt, khác cảm giác, và một tập mười
hai phút toàn màu thứ thì mới là thứ đáng lo.

**Hai ngưỡng, vì hai kiểu dùng khác nhau** — đo bằng `build-music.py --check`:

| Cách dùng | Ngưỡng | Vì sao |
|---|---|---|
| **chồng lên nhau** — bed chạy dưới, cue chương chạy trên | **≥ 95%** | hai bộ nốt vang cùng lúc, lệch một nốt là nghe ra ngay |
| **nối tiếp** — đoạn này tắt rồi đoạn kia mới vào | **≥ 80%** | tai không có gì để đối chiếu, miễn đừng cắt thẳng: chừa 2–3 giây, hoặc cho tan hẳn rồi mới vào |

Dưới 80% thì bỏ, đừng tiếc — đó là bản có chuyển hợp âm thật bên trong, xoay kiểu nào cũng còn lạc.

Sàn của phép đo là ~2%: các bản dựng bằng máy, đúng tông 100% theo cấu tạo, đo ra 98–100%. Nên
con số đọc được là lệch thật, không phải nhiễu.

**Nhạc sinh bằng AI không tự giữ tông.** Đã đo 20 bản Lyria: 1/20 đúng ngay, kéo về bằng
`import-music.py --shift auto` thì được 8/20. Số còn lại không kéo được, vì kéo thì cả bản dịch
theo — cái sai nằm ở **thể**: có nốt thăng, có chuyển hợp âm. Chỉ có hai đường: siết câu lệnh bằng
lời cấm (đã làm, xem [MUSIC-PROMPTS.md](MUSIC-PROMPTS.md)) rồi sinh lại, hoặc dùng bản dựng bằng
máy — bản máy thì tông là thứ mình đặt, chắc chắn 100%.

Vì sao: một tập có nhiều loại khung cảnh, và chỗ chuyển chương là chỗ hai đoạn nhạc gặp nhau —
hoặc nối tiếp, hoặc chồng lên nhau vài giây. Cùng tông thì hai đoạn chồng nhau vẫn là một hoà âm.
Khác tông thì chỗ nối nghe như hai cái đài mở cùng lúc, và khán giả nhận ra ngay có gì đó sai
dù không gọi được tên nó.

Các đoạn khác nhau ở chỗ **chọn nốt nào trong tông**, **ở quãng nào**, **tiếng nhạc cụ gì**, và
**động tới đâu** — chứ không bao giờ ở chỗ đổi tông.

Hai mươi đoạn, xếp theo mười chặng của [EPISODE-FRAME.md](EPISODE-FRAME.md). Bảng đầy đủ kèm
tempo, bộ nhạc cụ và câu lệnh sinh bản có nhạc cụ thật: **[MUSIC-PROMPTS.md](MUSIC-PROMPTS.md)**.

```bash
PYTHONUTF8=1 python tools/build-music.py --list      # xem cả bộ
PYTHONUTF8=1 python tools/build-music.py --group C   # dựng lại riêng nhóm chiến đấu
PYTHONUTF8=1 python tools/build-music.py --check     # đo tông của thứ đang có
```

| Nhóm | Đoạn |
|---|---|
| **A · khung tập** | mở tập · chuyển chặng · trả bài · kết tập |
| **B · vùng đất, đời thường** | nền chung · cảnh rộng · phơi nắng · tĩnh lặng · đàn đông · đêm thần bí |
| **C · kẻ địch, trận đấu** | kẻ săn rình · rượt đuổi · cú ra đòn · nhịp nạp · sân đấu · sau trận |
| **D · vòng đời** | tổ và con non · ngưỡng đổi hình · mùa sinh sản · cái chết |

Mười sáu đoạn là vòng lặp; bốn đoạn (mở tập, kết tập, cú ra đòn, nhịp nạp) chơi một lần, vì chúng
sống bằng đúng cái mở và cái kết của mình.

**Một cái bẫy của tông thứ.** Hoạ âm tự nhiên bậc 5 và bậc 10 của nốt La là **Do#** — quãng ba
*trưởng*. Bè nào có tiếng nhạc cụ thật (kéo vĩ, kèn đồng) đều lén mang nó theo, và nó chỏi thẳng
với nốt Do của những đoạn dùng đủ bộ hợp âm thứ. Trong `build-music.py` hai bậc ấy bị ghìm xuống
(`HARMONIC_TRIM`). Bản tải về từ Lyria cũng phải nghe kỹ chỗ này: nhạc cụ thật thì không ghìm được.

### Tiếng theo loài — luật 3 áp cho nhạc

Luật 3 ở đầu file nói *giải phẫu quyết định âm sắc*, và nó đúng với nhạc y như với tiếng kêu:

> **Vật liệu cơ thể chọn bộ nhạc cụ. Nhịp sống chọn tempo.**

Hai mươi đoạn ở trên là **bối cảnh** — chúng đến từ mười chặng của khung tập nên tập nào cũng
cần. Nhưng bộ tiếng thì không được dùng lại: bộ mặc định là của dòng Bulbasaur, một con vật ăn
nắng, nằm im, tích trữ — nên nó chậm (17/20 đoạn dưới 70 BPM) và một nửa số đoạn là dây kéo vĩ.
Đem nguyên bộ ấy sang một con vật chạy bằng lửa thì từng đoạn vẫn hay mà cả tập vẫn sai.

| Vật liệu cơ thể | Bộ nhạc cụ | Tempo | `--creature` |
|---|---|---|---|
| thực vật, gỗ ẩm, ăn nắng | dây kéo vĩ, pad ấm | ×1.0 | `bulbasaur` |
| lửa, khí nóng | kèn đồng, hơi thổi, kim loại nóng | ×1.35 | `charmander` |
| nước, vỏ | ống cộng hưởng, trầm tròn, thuỷ tinh mềm | ×1.1 | `squirtle` |
| côn trùng, cánh mỏng | bè cao mỏng, rung nhanh, gần như không có trầm | ×1.7 | `caterpie` |
| điện | kim loại gõ, tắt nhanh, đứt đoạn | ×1.5 | `pikachu` |
| đá, đất, dưới hang | trầm bịt kín, cắt gần hết dải cao | ×0.8 | `diglett` |

```bash
PYTHONUTF8=1 python tools/build-music.py --creature charmander   # -> public/audio/music/charmander/
```

**Nốt không đổi.** Bộ tiếng chỉ thay nhạc cụ, tempo và độ sáng; bộ nốt vẫn nguyên La thứ. Nhờ vậy
nhạc của hai loài khác nhau vẫn ghép được với nhau — cần cho những tập có hai loài cùng xuất hiện,
và cho cả playlist của kênh. Đây là chỗ việc khoá tông trả bài lần thứ hai.

Loài mới mà không có dòng nào trong bảng hợp thì thêm một mục vào `CREATURES` — đừng dùng tạm bộ
gần giống. Cũng nhớ đổi cụm nhạc cụ trong câu lệnh Lyria: bảng cụm thay sẵn nằm ở
[MUSIC-PROMPTS.md](MUSIC-PROMPTS.md).

### Vòng lặp của bộ nhạc — làm ở mỗi tập

Bộ hai mươi đoạn là **điểm xuất phát, không phải cái trần**. Mỗi tập chạy lại vòng này:

1. **Có kịch bản rồi mới soi nhạc.** Đọc `ORDER` và `BEATS`, đối chiếu với hai mươi bối cảnh.
2. **Chặng nào không có đoạn hợp thì đừng ép.** Ép một đoạn sẵn vào chỗ nó không thuộc về là
   kiểu sai mà khán giả không gọi được tên nhưng nghe ra ngay — y như dùng tiếng kêu của loài khác.
   Viết thêm một câu lệnh vào [MUSIC-PROMPTS.md](MUSIC-PROMPTS.md) và thêm một mục vào `PIECES`.
3. **Loài mới thì chọn bộ tiếng trước khi sinh bất cứ đoạn nào**, theo bảng ở trên.
4. **Sinh xong đo tông** bằng `build-music.py --check`: bè trầm phải ra La hoặc Mi.
5. **Ghi lại** — đoạn mới vào bảng, bộ tiếng mới vào `CREATURES`. Tập sau đỡ được đúng phần ấy.

### Luật chung

- **Không giai điệu, không nhịp gõ, không nhạc cụ solo.** Bản nền chỉ có ba việc: giữ không gian
  khỏi chết, đỡ chỗ nối giữa hai chương, đặt tâm trạng.
- **Chừa dải 2–4 kHz cho giọng.** Cả bộ đã khoét sẵn chỗ ấy.
- **Vòng lặp phải liền mạch.** Mọi thành phần có chu kỳ chia hết độ dài vòng (72 giây), nên chỗ
  nối không có cú nhảy. Đo lại bằng `--check`.
- **Cả bộ cùng một độ lớn** (RMS −20 dBFS trước khi trải rộng), nên đổi bản giữa tập không nhảy
  âm lượng. Bản tải về cũng đi qua đúng bước cuối ấy.
- `bedVolume` 0.12–0.15. To hơn là bắt đầu tranh với lời dẫn.
- Cả bộ nặng ~110 MB, mà `public/` thì bị Remotion đóng gói mỗi lần render. Bản nào không dùng
  tới thì **xoá đi** — `--only <tên>` dựng lại ra đúng bản cũ, không mất gì.

### Dùng nhiều bản trong một tập

Engine chỉ có **một** `audio.bed` cho cả tập. Muốn đổi nhạc theo chương thì đặt bản ấy vào thư mục
tiếng và neo như một cue:

```bash
cp public/audio/music/field-bed-mystic.wav public/audio/sfx/kanto-001/music-mystic.wav
```

```json
{ "el": "sfx", "name": "kanto-001/music-mystic.wav", "atWord": "đêm", "volume": 0.09 }
```

Cue tiếng chạy từ chỗ được neo cho tới hết, không lặp — 72 giây đủ một chương. Nó **chồng lên**
bản nền chính chứ không thay thế, và đó chính là chỗ việc khoá tông trả bài: hai bản cùng La thứ
chồng nhau thì dày lên, không chỏi.

### Nhạc tải về

Muốn một bản có nhạc cụ thật thì sinh bằng **Gemini → Tạo nhạc (Lyria)**, hoặc lấy ở **YouTube
Audio Library** (xem kỹ mục nào cần ghi nguồn). Tải về `assets/music-src/` (để nguyên file gốc), rồi:

```bash
PYTHONUTF8=1 python tools/import-music.py assets/music-src/<file>.mp3 --name field-bed-lyria
```

Tool cắt đoạn mở dần và đoạn tắt dần rồi gấp đuôi chồng lên đầu — vì mọi bản nhạc đều có kết, còn
bản nền thì không được có kết: engine lặp nó suốt cả tập. Nó cũng **đo tông và báo lại**; lệch thì
`--shift <bán cung>` kéo về La, hoặc bỏ bản ấy đi.

Câu lệnh sẵn cho tám bối cảnh — mỗi bản một tempo, một bộ nhạc cụ, cùng một tông — nằm ở
**[MUSIC-PROMPTS.md](MUSIC-PROMPTS.md)**. Chép thẳng vào ô prompt của Gemini, đừng bỏ cụm
*in A minor, with a sustained low A drone in the bass*: đó là chỗ giữ tông. Lyria không hứa đúng
tông, nên tải về xong vẫn phải `--check`, không tin lời nó.

Nhạc là thứ dễ dính Content ID nhất trong cả tập, nên **nguồn của từng file phải ghi lại được**.
`assets/` nằm ngoài git (nặng, giấy phép riêng) — đang dùng:

| File | Ở đâu ra | Ghi chú |
|---|---|---|
| `field-bed*.wav` (6 bản) | `tools/build-music.py` dựng tại chỗ | kênh sở hữu hẳn; dựng lại ra đúng bản cũ |
| `field-bed-lyria.wav` | Gemini → Tạo nhạc (Lyria 3.5), tài khoản của kênh | gốc ở `assets/music-src/gemini-lyria-field-bed.mp3` · **đang là bản dùng** |

## Nối vào scenes.json

Engine đã dùng được ngay, không phải sửa gì: element `sfx` lấy file trong `public/<audio.sfxDir>`
(kênh này là `public/audio/sfx/`), và **tên có dấu chấm thì được dùng nguyên văn**, nên đặt theo tập
được. Neo bằng `atWord` giống caption, hoặc `at` tính theo frame trong moment.

```json
{ "el": "sfx", "name": "kanto-001/powder-burst.wav", "atWord": "bào", "volume": 0.35 }
```

`volume` mặc định 0.1 — hợp cho whoosh giao diện, quá nhỏ cho tiếng sinh vật; cue thật nên 0.3–0.5,
tiếng nền 0.06–0.1. `lead` đẩy cue bắt đầu sớm hơn từ được neo (cho tiếng có đà, vd bào tử bung).

## Nhạc nền — thư viện dựng một lần, không sinh mới mỗi tập

Nhạc **không** làm lại từ đầu mỗi tập. Dựng một thư viện nhỏ ở `public/audio/music/`, rồi mỗi tập chỉ
chọn và chuyển đoạn. Được hai thứ: bớt một thuế mỗi tập, và kênh có âm sắc nhận ra được sau vài tập.

### Luật

1. **Nhạc không được kể hộ.** Phim tài liệu thiên nhiên dùng nhạc để giữ nhịp, không để bảo khán giả
   nên thấy thế nào. Cảnh con vật sắp chết không cần nhạc buồn — cần im lặng.
2. **Không có giai điệu bám tai.** Bất cứ đoạn nào bạn hát theo được là đoạn đang tranh chỗ với lời dẫn.
3. **Mỗi bản phải loop được** và phải có bản *bed* (chỉ nền, không lớp trên) để chui xuống dưới lời dẫn.
4. **Im lặng là một track.** Chặng mạnh nhất của tập thường nên không có nhạc.

### Bảy bản cần có

| Tên file | Dùng ở chặng | Tính chất |
|---|---|---|
| `open-question.wav` | 0 · câu hỏi mở màn | thưa, một nốt treo không giải quyết |
| `land-wide.wav` | 1 · vùng đất | dàn trải, chậm, không nhịp rõ |
| `daily.wav` | 2–4 · ăn, đàn, thường nhật | nhịp nhẹ đều, gần như nền |
| `tension.wav` | 5 · kẻ địch | trầm, dồn, **không** cao trào kiểu phim hành động |
| `threshold.wav` | 7–8 · điều kiện đổi hình, trưởng thành | căng và nín, hợp với luật "không lột da" |
| `close-circle.wav` | 9 · khép vòng | giải quyết, ấm, ngắn |
| `sting-note.wav` | chấm câu | 2–4 giây, đánh dấu một phát hiện |

Mỗi bản xuất hai lớp: `<tên>.wav` (đầy đủ) và `<tên>-bed.wav` (chỉ nền, −6 dB, đã lọc bớt dải giọng
người 1–4 kHz để không tranh chỗ với lời dẫn).

### Sinh bằng Gemini (Lyria)

Khung prompt dùng chung — đổi phần in nghiêng:

> Instrumental score for a wildlife documentary. *(tính chất của bản)*. Sparse arrangement, no melody
> that draws attention, no drums, no vocals, no orchestral swell. Room for a narrator to speak over it.
> Seamless loop. *(khoảng 60–90 giây)*.

Sinh xong nghe thử **cùng lúc với một đoạn lời dẫn thật** trước khi giữ lại. Nghe một mình thì bản nào
cũng hay; đặt dưới giọng đọc mới biết bản nào tranh chỗ.

### Giấy phép — phải chốt trước khi đăng

Điều khoản của Lyria/Gemini cho **video có kiếm tiền** hay đổi. Kiểm một lần, ghi ngày kiểm và kết
luận vào sổ tài sản của tập. Không chắc thì lùi về YouTube Audio Library (rõ ràng, miễn phí, dùng
thương mại được) cho tới khi kiểm xong.

## Chưa làm

- Neo cue vào `scenes.json` (`atWord` / `at`) — mới có `powder-burst` làm mẫu ở bảng trên.
- Lớp giọng của cả 17 cue còn là tiếng tổng hợp, chưa có file thật nào trong `assets/sfx-src/`.
