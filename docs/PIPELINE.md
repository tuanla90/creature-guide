# Dây chuyền một tập · từ ý tưởng tới bản upload

Mười một chặng. Mỗi chặng có **một cổng**: không qua cổng thì đừng đi tiếp, vì mọi lỗi lọt qua cổng
đều đắt gấp mười ở chặng sau — sửa một câu thoại tốn ba phút, sửa nó sau khi đã thu giọng và dựng
hình tốn ba tiếng.

Đây là bản **kỹ thuật**, chỉ nói việc làm một tập. Việc dựng kênh (làm một lần) và việc vận hành
(lịch, sao lưu, đọc số) nằm ở [BUSINESS-FLOW.md](BUSINESS-FLOW.md).

Ô 🤖 là chặng máy làm được gần hết, ✋ là chặng phải có người quyết.

| # | Chặng | | Ra cái gì |
|---|---|---|---|
| 1 | Chọn ý tưởng và khung tập | ✋ | một dòng trong `docs/IDEA-BANK.md` + khung đã chọn |
| 2 | Tra canon | 🤖 | bảng `NGUON` + `bible/creatures/<loài>.json` |
| 3 | Viết kịch bản **EN** | 🤖 | bản EN |
| 4 | Soát và duyệt kịch bản | ✋🤖 | bản EN chốt |
| 5 | Dịch VI, khít beat | 🤖 | `videos/<slug>/content.py` |
| 6 | Soạn shot | 🤖 | `bible/shots/<ep>.json` → `prompts/<ep>.flow.txt` |
| 7 | Sinh ảnh | ✋🤖 | `public/img/<ep>/*.jpg` |
| 8 | Dựng hình và chuyển động | 🤖 | `videos/<slug>/scenes.json` + `public/video/<ep>/*.mp4` |
| 9 | Tiếng và giọng | ✋🤖 | sfx, nhạc, hai track giọng |
| 10 | Soát | ✋🤖 | `check-episode.py` sạch + một lượt xem của người |
| 11 | Render, gói đăng, sao lưu | ✋🤖 | mp4 Long + Short, thumbnail, `<slug>.PUBLISH.md` |

---

## 1 · Chọn ý tưởng và khung tập ✋

Skill: **`episode-plan`** (xem tập nào đang ở chặng nào, tập nào nên mở tiếp).
Lấy từ [IDEA-BANK.md](IDEA-BANK.md), hoặc soi loài mới qua 16 trục của [CREATURE-LENS.md](CREATURE-LENS.md).

Rồi **chọn khung** trong [EPISODE-FRAME.md](EPISODE-FRAME.md):
- **Khung A · một cá thể** — mặc định. Một câu hỏi sinh tồn, một con vật cụ thể có mã thực địa.
- **Khung B · so sánh** — hai hoặc ba chủ thể trên một trục. Ba dạng Eevee của Kanto; rồng phương
  Đông và phương Tây; Hydra và Yamata no Orochi.

> **Cổng:** Khung A — viết được câu hỏi mở màn trong đúng một câu, và trả lời được "cá thể này muốn
> gì, cái gì cản nó". Khung B — nói được **trục so sánh** trong một câu, và mỗi chủ thể phải có ít
> nhất một điểm nó **thắng** các chủ thể kia. So sánh mà một bên thua toàn diện thì không phải so sánh.

## 2 · Tra canon 🤖

Mọi câu lấy từ danh lục phải vào `NGUON` kèm tên bản game/nguồn. Mọi suy đoán phải kèm **một loài có
thật ở Trái Đất** — và loài thật đó **cũng phải có nguồn tra được**, không được nói vo.

Nguồn có **hai tầng**:
- **IP còn sống** (Pokémon, Harry Potter, LOTR, Game of Thrones): bám canon chặt, ghi nguồn chính xác.
- **Phạm vi công cộng** (thần thoại, cổ tích, dân gian): lỏng hơn, nhưng nhiều dị bản nên **phải ghi
  rõ chọn bản nào và vì sao**.

> **Cổng:** không có câu nào trong tập mà bạn không chỉ được ra nó là 📖 danh lục, 👁 quan sát,
> hay 🔬 giả thuyết. Mỗi 📖 và mỗi 🔬 đều có một dòng nguồn.

## 3 · Viết kịch bản EN 🤖

**Bản gốc của kênh là tiếng Anh.** Máy viết tiếng Anh tự nhiên hơn viết tiếng Việt, và bản EN là thứ
quyết định bố cục, timing và ảnh.

Skill: **`creature-field-guide-scriptwriter`** (luật kể chuyện, giọng, nhãn bằng chứng, cách đặt tên).
Ghi tên nhân vật vào [CAST.md](CAST.md) — cả bản VI và EN.

Đặt tên cá thể có **hai luật**:
- Cá thể **có tên canon** (Smaug, Buckbeak) → tôn trọng tên gốc.
- Cá thể **vô danh** trong lore (như K7) → danh từ chỉ một dấu tích nhìn thấy được, và chỉ được gọi
  **sau khi** khán giả đã thấy dấu ấy.

> **Cổng:** mỗi beat có đúng một việc để kể, và bạn chỉ được ra nhãn bằng chứng của từng câu.

## 4 · Soát và duyệt kịch bản ✋🤖

Skill: **`episode-review`**. Ba lớp, đúng thứ tự, và **hết cả ba mới được đi tiếp**:

1. **Máy soát logic** — `check-episode.py` + Claude: khung tập, nhãn bằng chứng, nguồn, chữ làm lộ
   khung (game, AI, đoàn phim), tên nhân vật khớp CAST.md.
2. **Gemini soát văn** — giọng và sức ép kể chuyện, kèm `stop-slop` (đã cắt ba luật, xem
   [BUSINESS-FLOW.md](BUSINESS-FLOW.md) phần phụ lục).
3. **Người duyệt** — dùng
   [episode-checklist.md](../.claude/skills/creature-field-guide-scriptwriter/references/episode-checklist.md).

> **Cổng:** soát **trước khi sinh ảnh**. Script quyết định ảnh; sửa script sau khi đã có ảnh là hỏng
> cả loạt ảnh đã trả credit.

## 5 · Dịch VI, khít beat 🤖

Một video mang **hai track giọng** trên **một dòng thời gian** (YouTube multi-audio). Nên bản VI
không được dài ngắn tuỳ ý: mỗi beat có hạn mức thời lượng lấy từ bản EN.

Ra `videos/<slug>/content.py`. Nhớ: `ORDER`, `BEATS`, beat `"short-outro"` (thiếu là không có bản
Short), `PRON` cho VBee, `NGUON`.

Rồi bạn **tinh chỉnh tay** bản VI. Sau lúc đó **bản VI đóng băng**: sửa EN nữa thì phải sửa tay cả
hai bên, đừng dịch lại — dịch lại là xoá sạch phần đã chỉnh.

> **Cổng:** `python tools/check-episode.py <slug>` không còn ✗, và không beat nào lệch thời lượng
> quá ngưỡng so với bản EN.

## 6 · Soạn shot 🤖

Skill: **`creature-field-guide-production`** (phần "Soạn shot").

`bible/shots/<ep>.json` → `node tools/build-prompts.mjs <ep>` → bốn file trong `prompts/`.
Ảnh mẫu (`kind: "plate"`) sinh trước, mọi cảnh khác lấy nó làm `[ref]` để con vật không đổi hình.
Cá thể có dấu riêng thì khai ở `individuals` trong `bible/creatures/<loài>.json` và gọi bằng
`"creatures": ["bulbasaur:K7"]`.

Hồ sơ hình dáng có **hai đường ngược nhau**:
- *Hình cố định* (Pokémon): hình có sẵn → suy ra câu chuyện.
- *Hình không cố định* (rồng, kỳ lân): **câu chuyện trước** → suy ra hình tượng cá thể (một khiếm
  khuyết hay một nét nổi bật trên ngoại hình) → rồi mới sinh ảnh.

> **Cổng:** mỗi beat trong `ORDER` có ít nhất một shot; mỗi dấu tích dùng để đặt tên đều có **một
> shot cận cảnh riêng** — tên đặt theo thứ khán giả không nhìn thấy là tên chết.

## 7 · Sinh ảnh ✋🤖

Google Flow, project "Creature". Một hai ảnh lẻ thì gõ thẳng vào ô prompt của project; cả loạt thì
mở Tools → Batch Image Studio Pro, dán `prompts/<ep>.flow.txt`.

Tải ZIP về → `python tools/import-flow.py <ep>` → `python tools/unwatermark.py <ep>`.

**Hai loại cảnh có luật riêng:**

- **`kind: "anatomy"`** — X-quang mô phỏng phục vụ nghiên cứu: nền xanh, xương, mạch năng lượng chạy
  trong thân. Thân **nguyên vẹn, khép kín**. Không máu me, không nội tạng, không mổ xẻ.
- **`kind: "fieldnote"`** — trang sổ thực địa: Flow chỉ sinh **giấy và hình vẽ, chừa trống một phần
  ba bên phải**; chữ do element `notepage` của engine vẽ lên sau (xem skill production).

Cả hai **không lấy `[ref]`** từ ảnh mẫu — ref là ảnh chụp, nó kéo bản vẽ ngược về thành ảnh chụp.
Nên tả `scene` kỹ hơn bình thường để bù.

> **Cổng:** ảnh nào định zoom ≥ 2× phải từ 2000 px trở lên, và watermark đã sạch. Zoom vào ảnh vỡ
> thì cả cảnh hỏng, mà lúc đó bạn đã đo toạ độ callout xong rồi.

## 8 · Dựng hình và chuyển động 🤖

Skill: **`creature-field-guide-production`** (phần "Dựng cảnh").

`scenes.json`: `world` cho cảnh tràn khung, `specimen` cho cảnh soi từng điểm, `clip` cho video.
Chữ lower-third: `text` ≤ 4.2, `caption` ≤ 2.7.

**Chuyển động chia ba tầng — chọn tầng rẻ nhất còn dùng được:**

| Loại cảnh | Công nghệ | Chi phí |
|---|---|---|
| Cảnh đứng, tĩnh | skill `creature-motion` (OpenCV) | miễn phí, offline |
| Sinh hoạt thường | Veo / Nano Banana | trong 25k token/tháng |
| Hành động | Topview (Seedance, MiniMax) | token riêng, dè xẻn |

Ảnh thở, tầng rẻ nhất:

```bash
PYTHONUTF8=1 python .claude/skills/creature-motion/scripts/render.py --input public/img/<ep>/<shot>.jpg --spec .claude/skills/creature-motion/assets/<spec>.json --output out/<shot>.gif --contact-sheet experiments/creature-motion/<shot>-contact.jpg
npx remotion ffmpeg -y -i out/<shot>.gif -c:v libx264 -crf 19 -pix_fmt yuv420p public/video/<ep>/<shot>-breath.mp4
```

Chi tiết và giới hạn: [experiments/creature-motion](../experiments/creature-motion/README.md).

Rồi: `npm run scaffold -- <slug>` (timing ước lượng, audio câm) → `npm run registry` → `npm run studio`.

**Hai đường xem, đừng lẫn:**

| | Xem cái gì | Khi nào |
|---|---|---|
| `npm run studio` | bản dựng **trực tiếp** trong trình duyệt, tua được, không render | sửa hình, canh bố cục — vòng lặp nhanh |
| `tools/review.py` | một bản **đã render**, kèm phụ đề, ghi chú được tại chỗ | soát lần cuối ở chặng 10 |

Studio không tải Chrome Headless Shell nên không dính lỗi chứng chỉ của mạng công ty; render thì có
— xem phần gotcha trong [CLAUDE.md](../CLAUDE.md).

> **Cổng:** xem hết một lượt ở **cả 16:9 lẫn 9:16**. Bản dọc là nơi chữ tràn và cảnh rộng chết.
> Ảnh thở: xem contact sheet ở cỡ thật — sọ, chân chạm đất và vật cứng (trứng, đá) phải đứng yên.

## 9 · Tiếng và giọng ✋🤖

**Tiếng động** — [SOUND.md](SOUND.md): ghép ba lớp (thân / giọng / chi tiết), mỗi lớp một loài thật.
Nguồn chỉ Pixabay và Freesound CC0.

**Nhạc** — ghép từ thư viện mẫu của kênh, không sinh mới mỗi tập.

**Giọng** — hai track cho cùng một video:
- VI: VBee, đọc từ `out/<slug>/script-tts.txt`. Nghe lại toàn bộ trước khi ghép — phiên âm sai một
  tên loài là phải thu lại cả beat.
- EN: nhà cung cấp **chưa chốt** (xem [BUSINESS-FLOW.md](BUSINESS-FLOW.md)).

Có giọng thật rồi thì chạy lại timing và phụ đề: `npm run align -- <slug>` rồi
`python tools/export-subs.py <slug>`.

> **Cổng:** timing trong `timings.json` là timing **thật**. Mọi cue trong `sfx.json` có file thật,
> và không cue nào đè lên một câu quan trọng.

## 10 · Soát ✋🤖

```bash
PYTHONUTF8=1 python tools/check-episode.py <slug>
```

Máy soát được: khung tập, chữ làm lộ khung, nguồn canon, tên nhân vật khớp CAST.md, chữ tràn, file
hình/tiếng thiếu, ảnh sinh ra mà không dùng, timing và phụ đề cũ, thumbnail thiếu field, phiên âm
thiếu, beat VI lệch thời lượng so với EN, và **cảnh bị ngắt sớm**.

Luật cảnh ngắn đo **hai kiểu**, vì một kiểu không đủ:

- **Tuyệt đối** — dưới 1,2s là ✗, dưới 2,5s là ⚠. Moment còn phải nuốt 12 khung hoà vào cảnh sau.
- **Tương đối** — dưới 25% trung vị của **chính tập đó** là ⚠. Tập có nhịp trung vị 15s thì cảnh 3s
  vẫn hẫng, dù 3s nghe chẳng ngắn. Ngưỡng tuyệt đối không bắt được cái đó.

Sửa bằng cách tăng `w` của moment hoặc bỏ bớt một moment trong beat — đừng kéo dài lời dẫn cho vừa hình.

Và **nhịp hình**: một loại cảnh chiếm quá 75% thì tập đơn điệu; bốn beat liền cùng một công thức hình
thì khán giả thấy y hệt nhau. Năm loại cảnh tràn khung là năm "động từ" khác nhau — `world` mở ra,
`specimen` soi vào, `clip` cho chuyển động thật, `notepage` dừng lại ghi chép, `anatomy` nhìn xuyên
qua. Dùng mãi một động từ thì câu chuyện mất nhịp dù lời dẫn vẫn đúng.

Rồi **người xem một lượt trên bản dựng, có tiếng, không tua** — ghi chú ngay tại chỗ:

```bash
PYTHONUTF8=1 python tools/review.py <slug>
```

Trang này có hai mặt: trái là bản render **kèm phụ đề bật/tắt được** (tạm dừng, gõ ghi chú, lưu kèm
mốc thời gian và beat), phải là ảnh gốc (bấm lên ảnh → toạ độ callout).

**Đọc lời bằng mắt trước khi trả tiền giọng.** `npm run build -- <slug> --skip-audio` ra mp4 câm,
`python tools/export-subs.py <slug>` ra `.srt`, rồi mở trang này và bật phụ đề. Sai một câu phát hiện
ở đây mất ba phút; phát hiện sau khi đã thu giọng thì phải thu lại cả beat. Tách hai mặt là bắt buộc — khung video đã bị `camera`
zoom/pan nên bấm lên đó không ra được toạ độ trên ảnh gốc. Ghi ra `videos/<slug>/review-notes.json`.

Toạ độ đo **trên ảnh thật**, sau khi ảnh đã chốt; sinh lại ảnh là phải đo lại.

> **Cổng:** không còn ✗. Mỗi ⚠ đều đã được đọc và cố ý bỏ qua.

## 11 · Render, gói đăng, sao lưu ✋🤖

```bash
npm run thumb -- <slug>
npm run build -- <slug> --skip-audio
```

**Short làm riêng** — hook riêng, tiêu đề riêng. Shorts có multi-audio nhưng **không có thumbnail
theo ngôn ngữ**, nên ảnh bìa Short phải không chữ hoặc chọn một thứ tiếng.

**Gói đăng** — skill **`episode-publish`** soạn `videos/<slug>/PUBLISH.md`: 3 tiêu đề, mô tả SEO,
chapters, comment ghim, hashtag — **hai ngôn ngữ**. Thumbnail ra vài phương án để chọn.

Lên YouTube: bật khai báo **nội dung tổng hợp bằng AI**, gắn phụ đề, nạp **track giọng thứ hai** và
tiêu đề/mô tả/thumbnail bản địa hoá, credit **Tuấn La**.

**Sao lưu** — đẩy một chiều lên Drive những thứ **không tái tạo được**: ảnh đã đo toạ độ, giọng đã
duyệt, nhạc đã chọn. Ảnh đổi từ "tái tạo được" sang "không tái tạo được" đúng lúc chặng 10 đo xong
toạ độ.

> **Cổng:** xem lại bản render cuối **có tiếng**, từ đầu tới cuối, một lần. Không tua.

---

## Thứ hay bị miss

Mười lỗi đã thật sự xảy ra, chứ không phải lo xa:

1. Thiếu beat `short-outro` → không có bản Short, phát hiện lúc render.
2. Đặt tên nhân vật theo một dấu tích **chưa có ảnh** → cái tên rơi vào hư không.
3. `atWord` neo vào một từ ở **cuối câu** → cảnh chỉ hiện một giây rồi chuyển.
4. Đo toạ độ callout trên ảnh nháp, sau đó sinh lại ảnh → lệch hết.
5. Sửa `content.py` mà quên chạy lại `scaffold` → timing và phụ đề nói chuyện của bản cũ.
6. Chữ vừa khít ở 16:9, tràn ở 9:16.
7. Dấu ngoặc kép tiếng Việt trong `_note` của `scenes.json` → hỏng JSON, `export-subs` chết.
8. Ảnh sinh ra 11 cái, dùng 5 cái, quên mất 6 cái đã trả tiền.
9. `PRON` thiếu tên loài → VBee đọc "Bulbasaur" thành thứ không ai hiểu.
10. Giọng thu xong mới phát hiện một câu vi phạm luật kênh.

Chín trong mười cái đó `check-episode.py` bắt được. Cái còn lại (số 4) thì chỉ có thói quen:
**sinh ảnh xong hẳn rồi mới đo toạ độ.**

Hai cái mới, sinh ra từ việc đổi sang EN-trước và một-kênh-multi-audio:

11. Sửa bản EN sau khi đã tinh chỉnh tay bản VI, rồi dịch lại → mất sạch phần đã chỉnh.
12. Bản VI dịch dài hơn bản EN ở một beat → hai track giọng lệch nhau trên cùng một dòng thời gian.
