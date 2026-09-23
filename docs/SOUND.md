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
4. **Nguồn chỉ lấy hai nơi**: Pixabay (Content License — thương mại tự do, không cần ghi nguồn) và
   Freesound **lọc CC0**. Không đụng BBC Sound Effects (cấm thương mại), xeno-canto (đa số NC),
   Macaulay (phải mua license).
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

Mỗi cue: loài thật làm gốc · từ khoá đi tìm · xử lý. `k7` là cá thể Búp Lệch.

| id | beat | Cue | Thân | Giọng | Chi tiết | Xử lý |
|---|---|---|---|---|---|---|
| `amb-edge-day` | nền | rừng chạm đồng cỏ, trưa | — | ve sầu xa | gió qua cỏ khô | loop, cắt bớt 4–8 kHz cho lùi ra sau |
| `amb-edge-dawn` | 01,12 | bìa rừng lúc rạng | — | chim thưa | sương rơi trên lá | như trên, tối hơn |
| `call-k7-soft` | 00,03 | tiếng thở của K7 lúc nằm | bò rống −70% | ếch ương một tiếng | hơi thở qua lỗ mũi ướt | `asetrate*0.55`, `tremolo=f=17`, lowpass 2.2 kHz |
| `call-contact` | 06 | tiếng gọi giữ khoảng cách | lợn grunt | cóc trầm | — | như trên, ngắn 0.4 s, lặp 2 tiếng cách 1.2 s |
| `call-alarm` | 08 | lúc Mắt Tro bổ nhào | — | vạc kêu, hạ 4 bán cung | cỏ bật | attack gắt, cắt đuôi vang |
| `bulb-creak` | 12 | củ vặn theo mặt trời | — | — | bẻ cần tây + vặn vải ướt | `asetrate*0.7`, bandpass 1.6 kHz, `aecho` nhẹ |
| `bulb-open` | 08 | củ hé ra ở đỉnh | — | — | tách vỏ măng, lá tươi xé chậm | kéo dài 1.5 s bằng paulstretch |
| `powder-burst` | 08 | màn bào tử bung | — | — | nhiễu trắng + thổi miệng đã lọc hơi người | bandpass 4 kHz, fade 15 ms vào / 300 ms ra |
| `vine-touch` | 07 | hai dây leo cuộn nhau | — | — | vải ướt trượt, dây thừng mềm | rất khẽ, gần mic, không vang |
| `vine-whip` | 09,10 | dây leo quật | gỗ gãy trầm | — | roi vút (hạ tông) | cắt ngay đuôi vút — đây là mô thực vật, không phải roi da |
| `mud-suck` | 04 | rút chân khỏi bùn | — | — | bùn/đất nhão | giữ nguyên, chỉ hạ 2 bán cung |
| `step-soft` | nhiều | bước chân K7 | sine 45 Hz | — | lá khô vò | 3 lớp, tổng dưới 0.25 s |
| `step-heavy` | 15 | bước chân Venusaur | sine 38 Hz | — | lá + cành nhỏ gãy | như trên, thêm rung đất 0.6 s sau |
| `raptor-dive` | 08 | Mắt Tro lao xuống | — | quạ hạ 5 bán cung | gió qua lông cánh | **tránh** tiếng chim ưng đuôi đỏ kinh điển |
| `rain-leaves` | 15 | mưa trên tán lá | — | — | mưa rơi trên lá rộng | loop |
| `arena-crowd` | 10,11 | trận đấu của trainer | — | đám đông xa | — | lowpass 1 kHz, mono, đẩy xuống −24 dB |
| `swell-change` | 13,14 | đêm cả đàn tụ về | gió hút trầm | — | mô gỗ căng, đất lún | **không có tiếng biến hình** — chỉ căng và nín |

## Quy trình

1. Tìm theo từ khoá ở cột trên, tải về `assets/sfx-src/<id>/<loài>.wav` (giữ file gốc, đừng ghi đè).
2. Ghép theo công thức, xuất `public/audio/sfx/kanto-001/<id>.wav` 48 kHz.
3. Ghi lại **đúng công thức đã dùng** vào `videos/<slug>/sfx.json` — lần sau làm Ivysaur ở tập khác
   phải ra cùng một con vật.
4. Trộn: tiếng nền −28 dB, cue −12 tới −18 dB, lời dẫn luôn là thứ to nhất. Cue nào đè lên một câu
   quan trọng thì bỏ cue, đừng hạ lời.

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

- `sfx.json` (bảng công thức máy đọc được) — dựng sau khi chốt bảng cue này.
- Thư viện nhạc: bảy bản ở trên **chưa sinh**. Đây là việc một lần, làm trước tập thứ hai.
