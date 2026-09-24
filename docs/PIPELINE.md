# Dây chuyền một tập · từ ý tưởng tới bản upload

Mười một chặng. Mỗi chặng có **một cổng**: không qua cổng thì đừng đi tiếp, vì mọi lỗi lọt qua cổng
đều đắt gấp mười ở chặng sau — sửa một câu thoại tốn ba phút, sửa nó sau khi đã thu giọng và dựng
hình tốn ba tiếng.

Đây là bản **kỹ thuật**, chỉ nói việc làm một tập. Việc dựng kênh (làm một lần) và việc vận hành
(lịch, sao lưu, đọc số) nằm ở [BUSINESS-FLOW.md](BUSINESS-FLOW.md).

Ô 🤖 là chặng máy làm được gần hết, ✋ là chặng phải có người quyết.

| # | Chặng | | Ra cái gì |
|---|---|---|---|
| 1 | Ý tưởng: Gemini liệt kê, Claude chọn | 🤖✋ | `drafts/1-ideas-gemini.md` → ý đã chọn + khung A/B |
| 2 | Tra canon, dựng khung | 🤖 | `drafts/2-skeleton.md` (bảng nguồn + beat) + `bible/creatures/<loài>.json` |
| 3 | Gemini dựng lại khung và viết lời EN + VI nháp | 🤖 | `drafts/3-script-gemini.md` |
| 4 | Claude chuẩn hoá, người duyệt | 🤖✋ | `content.py` + `drafts/4-review.md` · “Đã duyệt” |
| 5 | Tinh chỉnh VI, khít beat | ✋🤖 | bản VI đóng băng trong `content.py` |
| 6 | Soạn shot | 🤖 | `bible/shots/<ep>.json` → `prompts/<ep>.flow.txt` |
| 7 | Sinh ảnh | ✋🤖 | `public/img/<ep>/*.jpg` |
| 8 | Dựng hình và chuyển động | 🤖 | `videos/<slug>/scenes.json` + `public/video/<ep>/*.mp4` |
| 9 | Tiếng và giọng | ✋🤖 | sfx, nhạc, hai track giọng |
| 10 | Soát | ✋🤖 | `check-episode.py` sạch + một lượt xem của người |
| 11 | Render, gói đăng, sao lưu | ✋🤖 | mp4 Long + Short, thumbnail, `<slug>.PUBLISH.md` |

---

## 1 · Ý tưởng: Gemini liệt kê, Claude chọn 🤖✋

Luồng kịch bản chia việc theo đúng sở trường, đã thử thật ở tập 001: **Gemini nghĩ rộng** (ý tưởng,
bố cục, câu chữ), **Claude giữ kỷ luật** (chọn, canon, luật), **người chốt**. File và từ khoá bàn
giao: [HANDOFF.md](HANDOFF.md).

1. `tools/handoff.py <slug> --brief ideas "<loài>"` ghép `drafts/1-ideas-brief.md` — lõi luật
   ([briefs/core.md](briefs/core.md)) + đề bài ([briefs/ideas.md](briefs/ideas.md)) + những gì
   IDEA-BANK và SLATE đã ghi về loài. Gemini trả **sáu ý**, trải ít nhất bốn trục của
   [CREATURE-LENS.md](CREATURE-LENS.md), mỗi ý một câu hỏi xương sống.
2. Claude chấm từng ý theo năm tiêu chí — canon đủ dày · cá thể trung tâm có đặc điểm nhìn thấy được
   (ưu tiên Shiny) · có đối chiếu Trái Đất mạnh · câu hỏi treo được cả tập · hook — rồi **chọn một,
   nêu lý do, giữ một ý dự phòng**. Bạn chỉ cần nói "đổi" nếu không ưng.

Khung trong [EPISODE-FRAME.md](EPISODE-FRAME.md):
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

**Tải ảnh tham chiếu** cho mỗi loài chính — `bible/refs/<loài>/refs.json`: kích thước so với người,
dấu chân Pokédex, màu Shiny. AI biết dáng Pokémon phổ biến nhưng không biết chắc tiểu tiết. Ghi nguồn
từng tấm. Ảnh là của bên thứ ba: chỉ để tham chiếu, không đăng, không đưa vào git.

**Chốt địa điểm** — `bible/locations/<id>.json`, có dẫn chứng canon.

Ra `drafts/2-skeleton.md`: đặc điểm cá thể trung tâm, địa danh, câu hỏi xương sống, **bảng nguồn**
(thứ duy nhất Gemini được lấy làm 📖), so sánh lõi / tuỳ chọn, chỗ gợi ý dừng hình, các beat gợi ý kèm
thời lượng, và giá trị `who` / `loc` được dùng. Dòng `<!-- handoff: trait=… central=… -->` ở đầu file
cho bộ soát biết đặc điểm nào phải gọi đúng một lần.

> **Cổng:** không có câu nào trong tập mà bạn không chỉ được ra nó là 📖 danh lục, 👁 quan sát,
> hay 🔬 giả thuyết. Mỗi 📖 và mỗi 🔬 đều có một dòng nguồn.

## 3 · Gemini dựng lại khung và viết lời 🤖

**Bản gốc của kênh là tiếng Anh**, và bản EN quyết định bố cục, timing và ảnh. Gemini viết EN kèm
một bản VI nháp cùng nhịp.

`tools/handoff.py <slug> --brief script` ghép `drafts/3-script-brief.md` — lõi luật + khung +
đề bài ([briefs/script.md](briefs/script.md)). Quyền của Gemini:

- **Bố cục thả:** thêm, bớt, gộp, tách, đổi thứ tự beat; co giãn thời lượng (tổng giữ trong ±5%);
  chọn so sánh tuỳ chọn và chỗ dừng hình; thêm chi tiết giác quan và quan sát nhỏ (gắn `👁 (new)`).
  Mọi thay đổi bố cục liệt kê ở mục `CHANGES`.
- **Sự kiện khoá:** 📖 chỉ lấy từ bảng nguồn của khung. Muốn thêm thì ghi ở `PROPOSED`, không vào lời.
- **Luật cứng khoá**, cùng đặc điểm cá thể trung tâm, câu hỏi xương sống không được trả lời, câu
  móc sang tập sau.

Vòng sau: `--brief script --round 2` → `3-script-gemini-2.md`.

**Không đặt tên riêng cho con vật** ([CAST.md](CAST.md)):
- Cá thể **có tên canon** (Smaug, Buckbeak) → giữ tên gốc.
- Cá thể trung tâm vô danh → **đặc điểm canon + mã thực địa**: `Shiny Bulbasaur · K-01`. Ưu tiên Shiny.
  Đặc điểm chỉ gọi ra **sau khi** khán giả đã thấy nó.
- Con khác gọi bằng tên loài; con phụ quay lại nhiều lần thì có mã (`K-04`), không có tên.

> **Cổng:** mỗi beat có đúng một việc để kể, và bạn chỉ được ra nhãn bằng chứng của từng câu.

## 4 · Claude chuẩn hoá, người duyệt 🤖✋

1. **Máy soát** — `tools/handoff.py <slug> --draft`: đủ mục, từ cấm EN lẫn VI, tên riêng cũ, đặc
   điểm gọi đúng một lần và sau cảnh cận, giá trị `who`/`loc` trong khung, hạn mức dừng hình và ảnh
   quê nhà, tổng thời lượng, hai track lệch nhau, bố cục đổi so với khung.
2. **Claude chuẩn hoá** theo skill **`episode-review`** (gọi `stop-slop`): nhãn bằng chứng từng câu,
   nguồn, số khớp TIMELINE, tuyến bỏ dở, quan sát mới có hợp lý không, cái giá của mỗi khả năng. Ghi
   vào `content.py` (`ORDER`, `BEATS`, `short-outro`, `PRON`, `NGUON`), và ghi `drafts/4-review.md`:
   **đã sửa gì của Gemini và vì sao**, đề xuất nào trong `PROPOSED` / `CHANGES` được nhận hay bị bỏ.
   Rồi `check-episode.py`.
3. **Claude soạn cảnh dự kiến** — `drafts/4-scene-plan.json`: mỗi beat mấy cảnh, lúc lời đọc tới
   chữ nào, trên hình có gì, ai trong khung (K-01 có mặt không), cỡ cảnh / góc máy, ảnh lấy từ đâu
   (**có sẵn · sinh lại · sinh mới · tải về**), chuyển động tầng nào, chỗ nào dừng hình. Kèm danh sách
   ảnh mẫu phải sinh trước. Đây là bản nháp của shot bible — duyệt nó rẻ hơn duyệt ảnh.
4. **Người duyệt trên trang** — `PYTHONUTF8=1 python tools/review-page.py <slug>` ghép cảnh dự kiến
   + lời EN cạnh lời VI thành `out/<slug>/review.html`; Claude đăng thành Artifact (capability `db`).
   Mỗi beat có nút **Duyệt / Cần sửa** và ô ghi chú; Claude đọc lại bằng collection `review`, không
   phải chép qua chat. Soát theo
   [episode-checklist.md](../.claude/skills/creature-field-guide-scriptwriter/references/episode-checklist.md).
   Mọi beat "Duyệt" thì Claude ghi `Đã duyệt: <ngày>` vào `4-review.md`; beat "Cần sửa" thì Claude
   sửa, đăng lại trang (cùng link), bạn duyệt lại riêng beat ấy.

> **Cổng:** duyệt **trước khi soạn shot và sinh ảnh**. Script quyết định ảnh; sửa script sau khi đã
> có ảnh là hỏng cả loạt ảnh đã trả credit.

## 5 · Tinh chỉnh VI, khít beat ✋🤖

Một video mang **hai track giọng** trên **một dòng thời gian** (YouTube multi-audio). Nên bản VI
không được dài ngắn tuỳ ý: mỗi beat có hạn mức thời lượng lấy từ bản EN.

Gemini đã viết sẵn bản VI nháp cùng nhịp ở chặng 3, Claude đưa vào `content.py` ở chặng 4 và soát
độ lệch thời lượng từng beat. Nhớ `PRON` cho VBee (tên loài, `K-01` đọc "ca không một", `Shiny`).

Rồi bạn **tinh chỉnh tay** bản VI. Sau lúc đó **bản VI đóng băng**: sửa EN nữa thì phải sửa tay cả
hai bên, đừng dịch lại — dịch lại là xoá sạch phần đã chỉnh.

> **Cổng:** `python tools/check-episode.py <slug>` không còn ✗, và không beat nào lệch thời lượng
> quá ngưỡng so với bản EN.

## 6 · Soạn shot 🤖

Skill: **`creature-field-guide-production`** (phần "Soạn shot").

Đầu vào là `drafts/4-scene-plan.json` **đã duyệt** — mỗi cảnh "sinh lại / sinh mới" thành một shot,
"có sẵn" giữ nguyên id (đổi ảnh là phải đo lại toạ độ callout), "tải về" thành một dòng chờ trong
`earth.json`. `bible/shots/<ep>.json` → `node tools/build-prompts.mjs <ep>` → bốn file trong `prompts/`.

Cảnh **lẫn đối tượng** (đàn thường + đúng một con được chọn) khai cả hai: `"creatures": ["bulbasaur",
"bulbasaur:K-01"]` — builder tả loài một lần với màu thường rồi thêm "đúng một con khác: …". Chỉ khai
`bulbasaur:K-01` cho cảnh cả đàn thì cả đàn sẽ mang màu Shiny (`check-episode.py` bắt).

**Sinh ảnh mẫu TRƯỚC, theo đúng thứ tự:** địa điểm trống (`kind: location`) → con thường của loài →
con được chọn. Mọi cảnh khác lấy chúng làm `[ref]`. Chuỗi đầy đủ: [SCENE-TYPES.md](SCENE-TYPES.md) mục A3.

Kịch bản đã **chốt một đặc điểm** của cá thể trung tâm (ưu tiên Shiny nếu loài có) — ghi vào
`individuals.<mã>.trait`. Mỗi shot khai `size`, `angle`, và `location`. Bắt buộc có ít nhất một
`anatomy` và một `fieldnote`.
Cá thể có dấu riêng thì khai ở `individuals` trong `bible/creatures/<loài>.json` và gọi bằng
`"creatures": ["bulbasaur:K7"]`.

Hồ sơ hình dáng có **hai đường ngược nhau**:
- *Hình cố định* (Pokémon): hình có sẵn → suy ra câu chuyện.
- *Hình không cố định* (rồng, kỳ lân): **câu chuyện trước** → suy ra hình tượng cá thể (một khiếm
  khuyết hay một nét nổi bật trên ngoại hình) → rồi mới sinh ảnh.

> **Cổng:** mỗi beat trong `ORDER` có ít nhất một shot; đặc điểm của cá thể trung tâm có **một
> cảnh rõ riêng** — gọi ra một đặc điểm khán giả chưa nhìn thấy là chữ rơi vào hư không.

## 7 · Sinh ảnh ✋🤖

Google Flow, project "Creature". Một hai ảnh lẻ thì gõ thẳng vào ô prompt của project; cả loạt thì
mở Tools → Batch Image Studio Pro, dán `prompts/<ep>.flow.txt`.

Thứ tự, và **hỏi trước mỗi loạt tốn credit**:
1. **Ảnh mẫu** (địa điểm → con thường → con được chọn), kèm ảnh tham chiếu đã tải (`xong refs`).
   Xem bằng mắt trước khi đi tiếp: ảnh mẫu sai màu thì mọi cảnh ăn theo đều sai.
2. **Thử một cảnh lẫn đối tượng** trước cả loạt. Flow không giữ được "đúng một con khác màu" thì
   đường lùi là ghép: sinh cảnh đàn thường, rồi đặt K-01 vào bằng ảnh mẫu.
3. **Cả loạt cảnh.**
4. **Clip**: Veo trong Flow dựng từ chính ảnh đã chốt (15 token/clip — trong hạn mức 25k/tháng coi
   như không giới hạn); Seedance chỉ cho cảnh hành động. Nguồn của mỗi cú **dừng hình** phải là clip.
5. **Loài Trái Đất** (tối đa 2 mỗi tập) **không sinh** — tải từ nguồn không đòi ghi tên tác giả, ghi
   một dòng vào `earth.json`, nói `xong earth` ([SCENE-TYPES.md](SCENE-TYPES.md) mục B2).

Tải ZIP về (tên gì cũng được, để trong Downloads) rồi nói **"xong ảnh"** → `tools/handoff.py <slug> --take`
nạp vào đúng chỗ → `python tools/unwatermark.py <ep>`. Luật đặt tên mọi file bàn giao: [HANDOFF.md](HANDOFF.md).

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
Bảng tra đầy đủ các loại cảnh và tuỳ chọn: [SCENE-TYPES.md](SCENE-TYPES.md).

`scenes.json`: `world` cho cảnh tràn khung, `specimen` cho cảnh soi từng điểm, `clip` cho video.
Chữ lower-third: `text` ≤ 4.2, `caption` ≤ 2.7.

**Dừng hình để phân tích** — `specimen` với `video` thay cho `src`: clip chạy tới đúng chữ neo của
callout đầu tiên rồi đứng hình, tối nền, soi. **Ảnh quê nhà** — `callout.media`: ảnh hoặc video loài
Trái Đất kẹp trong thẻ như tấm ảnh in. Tối đa 3 cú dừng, 2 ảnh quê nhà mỗi tập
([SCENE-TYPES.md](SCENE-TYPES.md) mục B, B2).

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

```bash
PYTHONUTF8=1 python tools/build-sfx.py <slug>     # công thức trong sfx.json -> public/audio/sfx/<ep>/
PYTHONUTF8=1 python tools/build-music.py          # nhạc nền -> public/audio/music/
```

Lớp nào chưa có file thật thì tool dựng tạm một tiếng tổng hợp, đủ để dựng hình và canh nhịp.
Tải được file thật về `assets/sfx-src/<cue>/<lớp>.wav` thì chạy lại, công thức giữ nguyên.

Nhạc đi theo hai trục: **hai mươi bối cảnh** (từ khung tập) × **bộ tiếng của loài** (vật liệu cơ
thể chọn nhạc cụ, nhịp sống chọn tempo). Loài mới thì chọn bộ tiếng trước, đừng dùng lại bộ của
loài trước. Chặng nào trong kịch bản không có đoạn nhạc hợp thì **thêm đoạn mới**, đừng ép đoạn
có sẵn — vòng lặp ấy ở [SOUND.md](SOUND.md).

> **Cổng:** mọi cue trong `sfx.json` đều có file, không cue nào đè lên một câu quan trọng,
> **lớp giọng đã là loài thật** (tiếng tổng hợp dùng để dựng thì được, để đăng thì không), và
> mỗi chặng trong `ORDER` đều có một đoạn nhạc thuộc về nó — không có chặng nào đang mượn tạm.

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
tiêu đề/mô tả/thumbnail bản địa hoá. Tên tác giả **Tuấn La** chỉ ở mô tả, không có trong video.

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

Bốn cái mới, từ lần đầu chạy luồng Gemini → Claude ở tập 001 (bộ soát `handoff.py --draft` đã học cả bốn):

13. **Mục tự soát của Gemini nói sai.** Nó ghi "tối đa một so sánh mỗi beat" ngay trong bản có hai
    beat mỗi beat hai so sánh. Không tin SELF-CHECK — soát lại bằng máy và bằng mắt.
14. **Số bịa trốn trong chỗ không phải lời** — ghi chú trang sổ "2.1 m/s", chữ "gấp đôi" cho một
    nết canon là ×1,5. Soát cả SHOTS và notes, không chỉ VO.
15. **Mốc thời gian vênh** — ngày 22 bị tấn công nhưng kho dự trữ "tích cả tháng". Bắt Gemini viết
    TIMELINE, rồi đọc mọi con số trong lời đối chiếu với nó.
16. **Tên cũ sống lại** trong TIMELINE khi lời đã sạch — dấu hiệu Gemini vẫn nghĩ bằng tên cũ.
