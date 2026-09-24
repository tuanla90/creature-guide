# Bộ câu lệnh nhạc · Gemini → Tạo nhạc (Lyria 3.5)

Hai mươi đoạn, xếp theo mười chặng của [EPISODE-FRAME.md](EPISODE-FRAME.md) — đủ để dựng một tập
mà không phải đi mượn nhạc ở đâu. Luật nhạc của kênh ở [SOUND.md](SOUND.md); file này là chỗ để bấm.

## Trước khi bấm

1. Gemini → nút **+** → **Tạo nhạc** (Create music).
2. Chip **Thời lượng**: **Tiêu chuẩn** (Standard, ~3 phút) cho mọi đoạn nền; **Ngắn** cho ba đoạn
   có ghi ⏱ *Ngắn* ở dưới (A4, C3, C4).
3. Chip **Có giọng hát: Không lời** (Instrumental). Quên bước này là ra bản có người hát.
4. Câu lệnh viết **tiếng Anh**.
5. Tải về: nút tải → **Chỉ riêng âm thanh · Bản nhạc MP3**.

## Cất file ở đâu

Hai nơi, đừng lẫn:

```
assets/music-src/<tên>.mp3           ← file GỐC tải về. Để nguyên, không sửa, không ghi đè.
public/audio/music/<tên>.wav         ← bản đã cắt để dùng. import-music.py tự ghi ra đây.
public/audio/music/<loài>/<tên>.wav  ← bộ tiếng của một loài khác, nằm riêng
```

Bạn chỉ phải làm bước đầu: bỏ mp3 vào `assets/music-src/` rồi chạy lệnh import. Chỗ thứ hai tool
tự lo.

```bash
# đoạn nền, chạy suốt một chương -> cắt thành vòng lặp liền mạch
PYTHONUTF8=1 python tools/import-music.py assets/music-src/<file>.mp3 --name field-bed-<tên>-lyria
# đoạn chơi một lần (A1 mở tập, A4 kết tập, C3 cú ra đòn, C4 nhịp nạp) -> giữ nguyên mở và kết
PYTHONUTF8=1 python tools/import-music.py assets/music-src/<file>.mp3 --name music-<tên>-lyria --once
# đo tông cả bộ: bè trầm phải ra La (55 Hz) hoặc Mi (82 Hz)
PYTHONUTF8=1 python tools/build-music.py --check
```

**Đặt tên theo cột cuối của mỗi mục, cộng hậu tố `-lyria`.** Ví dụ C1 thì đặt
`field-bed-stalk-lyria`. Như vậy bản Lyria nằm ngay cạnh bản dựng bằng máy
(`field-bed-stalk.wav`), nghe so được, và chọn bản nào thì chỉ việc đổi tên trong
`video.config.json` hoặc trong `scenes.json`.

Cả `assets/` lẫn `public/audio/` đều nằm **ngoài git** — nặng, và mỗi file một giấy phép riêng.
Nguồn của từng file ghi ở bảng cuối [SOUND.md](SOUND.md); nhạc là thứ dễ dính Content ID nhất
trong cả tập nên chỗ ấy phải luôn trả lời được "file này ở đâu ra".

## Ba luật xuyên suốt

**Tông.** Mọi đoạn là **La thứ**, và điều kiện thật sự là **cả bộ nốt nằm trong bảy nốt La–Si–Do–Re–
Mi–Fa–Sol**; bè trầm đứng ở bậc nào cũng được, vì Do trưởng và La thứ dùng chung đúng bảy nốt ấy.
Đây là chỗ cho phép hai đoạn chồng lên nhau ở chỗ chuyển chương mà không chỏi.

**Đã đo, và Lyria không giữ tông giúp bạn.** Hai mươi bản sinh bằng bộ câu lệnh cũ (cụm nhẹ
*"in A minor, with a sustained low A drone"*): **1/20 đúng tông ngay**; kéo về bằng
`--shift auto` thì được **8/20**. Số còn lại không cứu được bằng cách kéo, vì kéo thì cả bản dịch
theo — cái sai nằm ở **thể**, không ở cao độ: Lyria viết nhạc có nốt thăng và có chuyển hợp âm,
đúng thứ câu lệnh đã dặn là đừng.

Nên cụm giữ tông giờ nói thẳng bằng lời cấm, và **đừng bỏ nó đi**:

> *Strictly in A natural minor: use ONLY the notes A B C D E F G — no sharps, no flats, no
> accidentals, no key change, no modulation, one single harmony for the whole piece.*

Tải về xong vẫn phải đo: `build-music.py --check`. Hai ngưỡng, tuỳ cách dùng: **≥95%** nếu đoạn ấy
sẽ chồng lên một đoạn khác, **≥80%** nếu nó chạy một mình trong một chương. Dưới 80% thì bỏ —
bản ấy có chuyển hợp âm thật bên trong, xoay kiểu nào cũng còn nốt lạc. Chi tiết ở
[SOUND.md](SOUND.md).

**Nhịp.** Không bộ gõ. Cột tempo dưới đây không phải nhịp trống mà là **bản nhạc thở mấy giây một
lần** — trong câu lệnh nó nằm ở chữ *swell every N seconds*.

**Nhạc trận đấu không được nghe ra nhạc game.** Đây là luật số 1 của [SOUND.md](SOUND.md) áp cho
nhạc: một tiếng kêu 8-bit làm hỏng cả tập, thì một đoạn nhạc kiểu trailer phim hành động hay nhạc
nền trận đấu trong game cũng hỏng y như vậy — nó nói thẳng với khán giả rằng đây không phải phim
tài liệu. Năm câu lệnh có hành động ở nhóm C (C1–C5) vì thế đều mang câu chặn *no video-game battle music,
no cinematic trailer hits, no heroic brass fanfare*; riêng C6 là đoạn kiệt sức nên không cần. Phim tài liệu tự nhiên chấm điểm cảnh săn mồi bằng **dây kéo
căng và nhịp trầm**, không bằng kèn đồng hùng tráng.

## Bộ tiếng đổi theo loài — đọc trước khi bấm cho tập mới

Hai mươi câu lệnh dưới đây viết cho **dòng Bulbasaur**: một con vật ăn nắng, nằm im, tích trữ.
Đo lại thì thấy rõ cái thiên lệch ấy — 17/20 bối cảnh dưới 70 BPM, trung vị 58, và họ dây được
nhắc 29 lần. Đúng với Búp Lệch, **sai với một con vật chạy bằng lửa hay một con côn trùng**.

Nên với loài mới, giữ nguyên toàn bộ câu lệnh, chỉ thay **hai chỗ**: cụm nhạc cụ, và con số BPM.
Cụm giữ tông *in A minor, with a sustained low A drone in the bass* thì không bao giờ đụng tới —
nhờ nó mà nhạc của hai loài vẫn ghép được với nhau.

| Vật liệu cơ thể | Thay cụm nhạc cụ bằng | BPM |
|---|---|---|
| thực vật, gỗ ẩm, ăn nắng | *warm analog pad and bowed double bass* | giữ nguyên |
| lửa, khí nóng | *low brass, breathy metallic tones and dry crackling air* | ×1.35 |
| nước, vỏ | *resonant tube tones, round sub-bass and soft glass* | ×1.1 |
| côn trùng, cánh mỏng | *thin high shimmer and fast bowed tremolo, no low strings* | ×1.7 |
| điện | *struck metal and short-decay bells, clipped resonance* | ×1.5 |
| đá, đất, dưới hang | *muffled low brass and felt-covered tones, no high frequencies* | ×0.8 |

Ví dụ, B1 cho Charmander: giữ nguyên câu lệnh, đổi *"Warm analog pad and bowed double bass, very
slow swells roughly every 8 seconds, around 56 BPM"* thành *"Low brass, breathy metallic tones and
dry crackling air, swells roughly every 6 seconds, around 76 BPM"*.

Bản dựng bằng máy cũng có đúng trục ấy:

```bash
PYTHONUTF8=1 python tools/build-music.py --list                  # xem cả bảng bộ tiếng
PYTHONUTF8=1 python tools/build-music.py --creature charmander   # -> public/audio/music/charmander/
```

## Khi kịch bản cần một loại nhạc chưa có

Hai mươi đoạn là **điểm xuất phát, không phải cái trần**. Một tập có chặng mà không đoạn nào thuộc
về thì **đừng ép đoạn gần giống vào** — đó là kiểu sai khán giả không gọi được tên nhưng nghe ra
ngay. Thêm một đoạn mới, theo đúng vòng này:

1. Đặt tên bối cảnh theo **chặng trong khung tập**, không theo cảm xúc chung chung
   ("di cư qua đèo" chứ không phải "hùng tráng").
2. Chọn **tempo** theo nhịp sống của con vật lúc ấy, và **nhạc cụ** theo vật liệu cơ thể nó.
3. Viết câu lệnh theo khuôn dưới đây.
4. Thêm một mục vào `PIECES` trong `tools/build-music.py` để có bản máy dự phòng.
5. Sinh xong **đo tông**: `build-music.py --check`, bè trầm phải ra La (55 Hz) hoặc Mi (82 Hz).
6. Ghi vào bảng tra ở cuối file này.

### Khuôn câu lệnh

```
<một câu nói đây là nhạc nền cho cảnh gì, trong phim tài liệu tự nhiên, có lời dẫn ở trên>.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass<, + nốt thêm nếu cần: an open fifth on E /
a soft minor third / a faint minor sixth>.
<bộ nhạc cụ theo vật liệu cơ thể>, swelling every <N> seconds, around <BPM> BPM.
No percussion, no beat, no melody line, no chord changes<, + câu chặn riêng nếu là cảnh hành động:
no video-game battle music, no cinematic trailer hits, no heroic brass fanfare>.
<một câu nói rõ tâm trạng, và nói rõ cái KHÔNG được có>. Steady enough to loop.
```

Câu cuối là câu quan trọng nhất và hay bị viết hời hợt. Lyria nghe lời **cấm** tốt hơn lời tả: so
*"mysterious"* với *"unresolved and foggy, like something not yet explained"* — vế sau ra bản dùng
được, vế trước ra nhạc phim kinh dị.

---

# A · Khung tập (4 đoạn)

## A1 · `open` — mở tập

**Bối cảnh:** chặng 0, câu hỏi mở màn (beat 00–01) · **Tempo:** 66 BPM, xây 20 giây rồi mở ra
**Style:** một nốt trầm dày dần thành quãng năm · ⏱ Tiêu chuẩn · chơi một lần

```
Opening underscore for a natural-history documentary, 20 seconds of build then settling.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass. Start with one low sustained note alone,
let strings and a warm pad thicken around it, then open into a bare fifth and hold there.
Around 66 BPM. No percussion, no drums, no melody line, no cinematic impact or riser cliche.
Patient and serious, the feeling of a long project beginning.
```
→ `--name music-open --once`

## A2 · `bridge` — chuyển chặng, ghi sổ thực địa

**Bối cảnh:** chỗ nối giữa hai chặng, lúc người kể lật sổ · **Tempo:** 60 BPM, phồng 6 giây
**Style:** mỏng, chỉ một bè dây và không khí — nhạt hơn mọi đoạn khác · ⏱ Tiêu chuẩn

```
Very thin connective underscore for a nature documentary, meant to sit between two chapters.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass. Almost nothing: one quiet sustained
viola note and room tone, swelling every 6 seconds, around 60 BPM. No percussion, no melody,
no development at all. It should feel like a page turning, not like a new section starting.
```
→ `--name field-bed-bridge`

## A3 · `reveal` — lúc trả bài, câu hỏi được đóng

**Bối cảnh:** chặng 9, chỗ câu hỏi mở màn được trả lời · **Tempo:** 58 BPM, phồng 10 giây
**Style:** sáng dần, mở ra — nhưng **không thắng lợi**, đây là hiểu ra chứ không phải chiến thắng

```
Underscore for the moment a long-running question is finally answered in a nature documentary.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass. Strings and warm pad slowly opening
upward into a bare fifth, gaining light over 10-second swells, around 58 BPM. No percussion,
no melody line. Quietly moving but NOT triumphant and NOT sentimental - the feeling of
understanding something, not of winning. Steady enough to loop.
```
→ `--name field-bed-reveal`

## A4 · `close` — kết tập, chỗ đặt logo

**Bối cảnh:** `short-outro` và đuôi bản Long · **Tempo:** 56 BPM, tan dần · ⏱ **Ngắn**

```
Closing underscore for a natural-history documentary, thinning out toward silence.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass and an open fifth on E.
Warm pad and distant strings gradually dropping away layer by layer until only one sustained
low note and air remain. Around 56 BPM. No percussion, no melody, no final chord that resolves -
it should end open, as if the recording simply stops. Calm, unsentimental.
```
→ `--name music-close --once`

---

# B · Vùng đất và đời thường (6 đoạn)

## B1 · `calm` — nền chung của kênh

**Bối cảnh:** mặc định, mọi chặng kể chuyện và quan sát · **Tempo:** 56 BPM, phồng 8 giây
**Style:** warm analog pad + contrabass kéo vĩ, không nhạc cụ nào nổi lên trước

```
Ambient underscore for a natural-history documentary, with a narrator speaking over it.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass and an open fifth on E above it.
Warm analog pad and bowed double bass, very slow swells roughly every 8 seconds, around 56 BPM.
No percussion, no beat, no melody line, no chord changes. Neutral in mood - not sad, not
triumphant. Same texture from start to finish, steady enough to loop.
```
→ `--name field-bed-calm`

## B2 · `vista` — vùng đất, cảnh rộng

**Bối cảnh:** chặng 1, khí hậu và địa hình, cảnh mở toàn vùng · **Tempo:** 52 BPM, phồng 14 giây
**Style:** rộng và cao, dây trải nhiều quãng tám, có gió trong tiếng

```
Wide, open ambient underscore for an aerial landscape shot in a nature documentary.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass and the same note spread across several
octaves above. Sustained strings stacked wide, airy and spacious, swelling every 14 seconds,
around 52 BPM. No percussion, no melody line, no rising build. Vast and impersonal - the land
was here before the animal. Steady enough to loop.
```
→ `--name field-bed-vista`

## B3 · `warm` — ban ngày, phơi nắng

**Bối cảnh:** chặng 3, ăn gì sống bằng gì; đàn nằm trong vệt nắng · **Tempo:** 63 BPM, phồng 6 giây
**Style:** dàn dây giữ nốt + celesta rung nhẹ, có nốt ba thứ nên ấm hơn nền chung

```
Gentle, relaxed ambient underscore for a nature documentary, with a narrator speaking over it.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass, plus a soft minor third and fifth above.
Warm string ensemble holding long notes with a faint celesta shimmer, swelling every 6 seconds,
around 63 BPM. No percussion, no beat, no melody line. Comforting but not sentimental,
like slow afternoon sunlight. Same texture throughout, steady enough to loop.
```
→ `--name field-bed-warm`

## B4 · `still` — tĩnh lặng, chỗ cần nghe thấy tiếng thở

**Bối cảnh:** cận cảnh, lúc chờ, con vật nằm im · **Tempo:** 40 BPM, phồng 16 giây
**Style:** sub bass + một bè cello rất xa, gần như chỉ còn không khí

```
Extremely still and quiet ambient drone for a nature documentary, with a narrator speaking over it.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass, almost nothing else.
A single deep sub-bass tone and one distant bowed cello note, barely moving, swelling once every
16 seconds, around 40 BPM. No percussion, no melody, no chord changes, no build-up.
Dark, distant, patient - the sound of waiting. Steady enough to loop.
```
→ `--name field-bed-still`

## B5 · `alive` — đàn đông, nhiều cá thể

**Bối cảnh:** chặng 4, sống trong đàn; tranh chỗ nằm, chen lấn · **Tempo:** 90 BPM, phồng 1.5 giây
**Style:** nhiều bè dây chồng + rung kiểu mallet, chuyển động liên tục nhưng **không trống**

```
Busy, alive ambient underscore for a nature documentary, with a narrator speaking over it.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass and a minor seventh chord above it.
Many layered sustained strings and bright mallet-like resonance moving constantly, a restless
shimmering texture at around 90 BPM, pulsing every 1.5 seconds. Absolutely no drums, no
percussion, no beat you can tap to - the movement comes from the layers, not from rhythm.
A sense of crowd and activity. Steady enough to loop.
```
→ `--name field-bed-alive`

## B6 · `mystic` — đêm, sương, chỗ chưa giải thích được

**Bối cảnh:** chặng 6 láng giềng về đêm; mọi chỗ còn là 🔬 giả thuyết · **Tempo:** 50 BPM, phồng 12 giây
**Style:** glass harmonica, vibraphone kéo vĩ, sáo hơi — bè cao trôi, không neo

```
Mysterious, otherworldly ambient drone for a nature documentary, with a narrator speaking over it.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass and a faint minor sixth rubbing quietly
against the fifth. Glass harmonica, bowed vibraphone and breathy flute drifting in the high
register, swelling every 12 seconds, around 50 BPM. No percussion, no melody, no resolution -
it should feel unresolved and foggy, like something not yet explained. Steady enough to loop.
```
→ `--name field-bed-mystic`

---

# C · Kẻ địch và trận đấu (6 đoạn)

Sáu đoạn này chia làm hai nhánh **không được nghe giống nhau**: C1–C3 là **săn mồi ngoài hoang dã**
(chặng 5) — không ai chọn đánh nhau, một bên đang kiếm ăn, một bên đang giữ mạng. C4–C5 là
**trận đấu của người bản xứ** (chặng 5b) — có khán giả, có luật, có người ra lệnh, nên trong tiếng
phải có con người. C6 là chỗ trả bài cho cả hai.

> **Luật của kênh:** *mọi khả năng phải nêu cái giá*. Dùng `strike` hay `charge` mà không có
> `aftermath` đằng sau là nhạc đang kể một câu chuyện khác với lời dẫn.

## C1 · `stalk` — kẻ săn đang theo, chưa ra tay

**Bối cảnh:** chặng 5, Mắt Tro bay vòng rất cao · **Tempo:** 46 BPM, phồng 12 giây
**Style:** contrabass + cello lệch tông nhẹ + kèn đồng trầm, **cắt hết dải cao**

```
Heavy, pressing underscore for a predator circling its prey in a nature documentary, with a
narrator speaking over it. Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass and a semitone
tension between E and F in the low register. Low brass, contrabass and slightly detuned cellos,
dense and dark, with a very slow crescendo every 12 seconds, around 46 BPM. No percussion, no
melody, no high frequencies at all. No video-game battle music, no cinematic trailer hits, no
heroic brass fanfare. Foreboding but restrained - nothing has happened yet. Steady enough to loop.
```
→ `--name field-bed-stalk`

## C2 · `chase` — rượt và bỏ chạy

**Bối cảnh:** chặng 5, lúc con mồi vỡ chạy · **Tempo:** 112 BPM, dây rung liên tục
**Style:** tremolo dây chạy không nghỉ, contrabass nhấn từng nhịp dài — gấp mà vẫn không có trống

```
Urgent underscore for a chase in a nature documentary, predator and prey running.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone under everything. Fast tremolo strings running
continuously in the middle register, with long bowed contrabass accents pushing underneath,
around 112 BPM. No drum kit, no percussion, no taiko, no cinematic hits - the urgency must come
from the bowing speed, not from a beat. No video-game battle music, no heroic brass fanfare.
Breathless and unglamorous. Steady enough to loop.
```
→ `--name field-bed-chase`

## C3 · `strike` — cú ra đòn

**Bối cảnh:** cú bổ nhào, cú quật dây leo · **Tempo:** một cú, 15–20 giây · ⏱ **Ngắn**
**Style:** nén rồi bung rồi tắt hẳn — không có đuôi vang dài

```
A single short musical gesture for the instant a predator strikes, in a nature documentary.
About 15 seconds total. Strictly in A natural minor - only the notes A B C D E F G, no sharps or flats, no key
change - over a low A drone. Strings compress and tighten, one sharp
collective bow attack, then everything cuts away to almost nothing. No drums, no percussion,
no orchestral hit, no trailer boom, no video-game battle sting. It should land and immediately
leave silence behind it, not ring out heroically.
```
→ `--name music-strike --once`

## C4 · `charge` — nhịp nạp trước khi phóng

**Bối cảnh:** chặng 5b, "đứng yên một nhịp, cái củ sáng lên, rồi mới phóng" · **Tempo:** 60 BPM, nén 12 giây rồi cắt
**Style:** một nốt dâng và đặc dần, dừng đột ngột · ⏱ **Ngắn**

```
A slow 12-second build for the moment an animal gathers stored energy before releasing it,
in a nature documentary. Strictly in A natural minor - only the notes A B C D E F G, no sharps or flats, no key
change - over a low A drone. One sustained note growing denser and
brighter as strings and a warm pad pile onto it, tightening, then stopping abruptly - no
release, no payoff chord. Around 60 BPM. No drums, no percussion, no riser sweep, no trailer
boom, no video-game charge-up sound effect. Tension held, then cut.
```
→ `--name music-charge --once`

## C5 · `arena` — trận đấu của người bản xứ

**Bối cảnh:** chặng 5b, sân đất trong thị trấn, có khán giả · **Tempo:** 84 BPM, phồng 2 giây
**Style:** dây dày + một bè kèn gỗ trầm; **có hơi người trong tiếng**, nhưng vẫn là phim tài liệu

```
Underscore for a staged animal contest watched by a village crowd, filmed as documentary.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass. Dense sustained strings with a low
woodwind line moving underneath, restless, around 84 BPM, pulsing every 2 seconds. No drum kit,
no percussion, no video-game battle music, no heroic fanfare, no sports-broadcast energy.
The tone is observational and slightly uneasy - the camera is outside the ring, not cheering.
Steady enough to loop.
```
→ `--name field-bed-arena`

## C6 · `aftermath` — sau trận, cái giá phải trả

**Bối cảnh:** chặng 8, cơ thể kiệt, cái kho bị rút cạn · **Tempo:** 44 BPM, phồng 18 giây
**Style:** thưa và trống — những bè vừa dày đặc giờ chỉ còn một hai nốt

```
Underscore for the exhausted aftermath of a fight in a nature documentary, counting the cost.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass. Very sparse: one cello and a thin pad,
long gaps of near-silence between 18-second swells, around 44 BPM. No percussion, no melody,
no resolution, nothing uplifting. Emptied out and tired, but not tragic or sentimental.
Steady enough to loop.
```
→ `--name field-bed-aftermath`

---

# D · Vòng đời (4 đoạn)

## D1 · `birth` — tổ và lúc chào đời

**Bối cảnh:** chặng 2, trứng, ổ, con non · **Tempo:** 60 BPM, phồng 8 giây
**Style:** nhỏ và sáng — celesta, harp gảy thưa, dây cao rất khẽ; mong manh chứ không dễ thương

```
Delicate underscore for eggs and newborn animals in a nature documentary.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone far underneath. Small and bright on top: celesta,
sparse plucked harp and very quiet high strings, swelling every 8 seconds, around 60 BPM.
No percussion, no melody line, nothing childlike or cute - fragile and uncertain, most of
them will not survive. Steady enough to loop.
```
→ `--name field-bed-birth`

## D2 · `threshold` — ngưỡng tiến hoá, đàn tụ về

**Bối cảnh:** chặng 7, đêm cả đàn đứng thành vòng · **Tempo:** 48 BPM, phồng 20 giây
**Style:** căng và nín, không có gì "biến hình" — luật kênh: cảnh tiến hoá chỉ có sức nặng và dấu vết

```
Underscore for a gathering of animals at night, something about to change but not yet changing.
Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass. Everything held and tightening: low
strings pressing quietly, one high harmonic hanging above, swells stretched to 20 seconds,
around 48 BPM. No percussion, no melody, no transformation sound effects, no shimmer or magic
sparkle, no crescendo that pays off. Held breath, weight, waiting. Steady enough to loop.
```
→ `--name field-bed-threshold`

## D3 · `courtship` — mùa sinh sản, phô diễn

**Bối cảnh:** chặng 9, mùa mưa, hương đậm, phô diễn và làm tổ · **Tempo:** 68 BPM, phồng 7 giây
**Style:** ấm và có màu hơn mọi đoạn khác, nhưng kiềm chế — không lãng mạn hoá

```
Warm, slightly colourful underscore for a breeding season in a nature documentary - display,
scent, nest-building after rain. Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass and a
soft minor third above. Warm strings and a gentle woodwind, swelling every 7 seconds, around
68 BPM. No percussion, no melody line, nothing romantic or sweeping - this is biology, observed
plainly. Steady enough to loop.
```
→ `--name field-bed-courtship`

## D4 · `elegy` — cái chết và thứ để lại

**Bối cảnh:** trục 16, xác một cá thể trả khoáng lại cho đất · **Tempo:** 50 BPM, phồng 14 giây
**Style:** trang nghiêm, dây trầm giữ nốt dài — **không bi luỵ**, không nốt nào rơi xuống kiểu đưa tang

```
Underscore for the death of a single animal in a nature documentary, and what its body returns
to the soil. Strictly in A natural minor: use ONLY the notes A B C D E F G - no sharps, no flats,
no accidentals, no key change, no modulation, one single harmony for the whole piece.
With a sustained low A drone in the bass. Low sustained strings held
for a long time, one distant high note above, swelling every 14 seconds, around 50 BPM.
No percussion, no melody, no descending funeral figure, no choir, nothing mournful or
manipulative. Grave and matter-of-fact - the forest carries on. Steady enough to loop.
```
→ `--name field-bed-elegy`

---

## Bảng tra nhanh

| | Đoạn | Chặng | Tempo | Chip | Tên file |
|---|---|---|---|---|---|
| A1 | mở tập | 0 | 66, xây 20 s | Tiêu chuẩn | `music-open --once` |
| A2 | chuyển chặng | mọi chỗ nối | 60 / 6 s | Tiêu chuẩn | `field-bed-bridge` |
| A3 | trả bài | 9 | 58 / 10 s | Tiêu chuẩn | `field-bed-reveal` |
| A4 | kết tập | outro | 56, tan dần | **Ngắn** | `music-close --once` |
| B1 | nền chung | mặc định | 56 / 8 s | Tiêu chuẩn | `field-bed-calm` |
| B2 | cảnh rộng | 1 | 52 / 14 s | Tiêu chuẩn | `field-bed-vista` |
| B3 | phơi nắng | 3 | 63 / 6 s | Tiêu chuẩn | `field-bed-warm` |
| B4 | tĩnh lặng | 3 | 40 / 16 s | Tiêu chuẩn | `field-bed-still` |
| B5 | đàn đông | 4 | 90 / 1.5 s | Tiêu chuẩn | `field-bed-alive` |
| B6 | đêm, thần bí | 6 | 50 / 12 s | Tiêu chuẩn | `field-bed-mystic` |
| C1 | kẻ săn rình | 5 | 46 / 12 s | Tiêu chuẩn | `field-bed-stalk` |
| C2 | rượt đuổi | 5 | 112, dây rung | Tiêu chuẩn | `field-bed-chase` |
| C3 | cú ra đòn | 5 | một cú 15 s | **Ngắn** | `music-strike --once` |
| C4 | nhịp nạp | 5b | 60, nén 12 s | **Ngắn** | `music-charge --once` |
| C5 | sân đấu | 5b | 84 / 2 s | Tiêu chuẩn | `field-bed-arena` |
| C6 | sau trận | 8 | 44 / 18 s | Tiêu chuẩn | `field-bed-aftermath` |
| D1 | tổ, con non | 2 | 60 / 8 s | Tiêu chuẩn | `field-bed-birth` |
| D2 | ngưỡng đổi hình | 7 | 48 / 20 s | Tiêu chuẩn | `field-bed-threshold` |
| D3 | mùa sinh sản | 9 | 68 / 7 s | Tiêu chuẩn | `field-bed-courtship` |
| D4 | cái chết | trục 16 | 50 / 14 s | Tiêu chuẩn | `field-bed-elegy` |

**Cả hai mươi đoạn đều đã có bản dựng bằng máy** trong `public/audio/music/` — đúng tông, đúng độ
lớn, dùng ngay được:

```bash
PYTHONUTF8=1 python tools/build-music.py --list      # xem cả bộ
PYTHONUTF8=1 python tools/build-music.py --group C   # dựng lại riêng nhóm chiến đấu
```

Bản máy và bản Lyria cùng tên gọi, chỉ khác đuôi: bản Lyria tải về thì đặt tên có hậu tố `-lyria`
(ví dụ `field-bed-stalk-lyria`) để hai bản nằm cạnh nhau mà nghe so, rồi chọn.

## Sau khi có đủ

```bash
PYTHONUTF8=1 python tools/build-music.py --check
```

Bè trầm phải ra **La (55 Hz)** hoặc **Mi (82 Hz)**. Lệch thì kéo về:

```bash
PYTHONUTF8=1 python tools/import-music.py assets/music-src/<file>.mp3 --name <tên> --shift 2
```

Dùng trong tập: một bản làm `audio.bed` cho cả tập, các bản khác chèn theo chương như một cue tiếng —
cách làm ở [SOUND.md](SOUND.md), mục *Dùng nhiều bản trong một tập*. Chúng chồng lên nhau chứ không
thay nhau, và vì cùng La thứ nên chồng vào là dày lên, không chỏi.

## Chỗ hay hỏng

- **Lyria báo lỗi liên tục** ("Sorry, something went wrong" / "I'm having a hard time fulfilling
  your request"): đã gặp ba lần liên tiếp ngay sau một lần thành công, cùng tài khoản. Nhiều khả
  năng là hạn mức trong ngày. Nghỉ rồi bấm lại, đừng sửa câu lệnh — sửa lung tung là mất luôn bản
  đã đúng ý.
- **Dùng lại nguyên bộ câu lệnh cho loài mới** → hai mươi đoạn đều hay mà cả tập vẫn sai con vật.
  Chọn bộ nhạc cụ và hệ số BPM theo vật liệu cơ thể **trước khi bấm cái đầu tiên**, bảng ở trên.
- **Quên chip "Không lời"** → ra bản có người hát, mất một lượt sinh.
- **Quên `--once` với A1, A4, C3, C4** → tool cắt mất phần mở và phần kết, mà ba đoạn ấy sống bằng đúng
  cái mở và cái kết ấy.
- **Đoạn nhóm C nghe ra nhạc game** → sinh lại, đừng cố cứu bằng cách hạ âm lượng. Khán giả nhận ra
  ngay, và nó phá đúng cái khung mà cả kênh dựng lên.
- **Nghe thấy chỗ nối khi lặp** → `--cross` lớn hơn, ví dụ `--cross 10`.
- **Nhạc lấn lời dẫn** → hạ `bedVolume` (0.12–0.15), đừng hạ giọng.
