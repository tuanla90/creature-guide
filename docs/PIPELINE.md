# Dây chuyền một tập · từ ý tưởng tới bản upload

Mười chặng. Mỗi chặng có **một cổng**: không qua cổng thì đừng đi tiếp, vì mọi lỗi lọt qua cổng
đều đắt gấp mười ở chặng sau — sửa một câu thoại tốn ba phút, sửa nó sau khi đã thu giọng và dựng
hình tốn ba tiếng.

Ô 🤖 là chặng máy làm được gần hết, ✋ là chặng phải có người quyết.

| # | Chặng | | Ra cái gì |
|---|---|---|---|
| 1 | Chọn ý tưởng | ✋ | một dòng trong `docs/IDEA-BANK.md` |
| 2 | Tra canon | 🤖 | bảng `NGUON` + `bible/creatures/<loài>.json` |
| 3 | Viết kịch bản | 🤖 | `videos/<slug>/content.py` |
| 4 | Soạn shot | 🤖 | `bible/shots/<ep>.json` → `prompts/<ep>.flow.txt` |
| 5 | Sinh ảnh | ✋🤖 | `public/img/<ep>/*.jpg` |
| 6 | Dựng hình | 🤖 | `videos/<slug>/scenes.json` |
| 7 | Tiếng | 🤖 | `public/audio/sfx/<ep>/*.wav` |
| 8 | Giọng | ✋ | `videos/<slug>/audio/*.mp3` + timing thật |
| 9 | Soát | 🤖 | `python tools/check-episode.py <slug>` sạch |
| 10 | Render & đăng | ✋🤖 | mp4 Long + Short, thumbnail, phụ đề |

---

## 1 · Chọn ý tưởng ✋

Lấy từ [IDEA-BANK.md](IDEA-BANK.md), hoặc soi loài mới qua 16 trục của [CREATURE-LENS.md](CREATURE-LENS.md).

Một tập cần **một câu hỏi sinh tồn** và **một cá thể trung tâm**, không phải một danh sách sự thật.

> **Cổng:** viết được câu hỏi mở màn trong đúng một câu, và trả lời được "cá thể này muốn gì, cái gì
> cản nó". Chưa viết được thì chưa có tập.

## 2 · Tra canon 🤖

Bulbapedia cho từng mục danh lục. Mọi câu lấy từ danh lục phải vào `NGUON` trong `content.py` kèm
tên bản game/nguồn. Mọi suy đoán phải kèm **một loài có thật ở Trái Đất**.

> **Cổng:** không có câu nào trong tập mà bạn không chỉ được ra nó là 📖 danh lục, 👁 quan sát,
> hay 🔬 giả thuyết.

## 3 · Viết kịch bản 🤖

Skill: **`creature-field-guide-scriptwriter`** (luật kể chuyện, giọng, nhãn bằng chứng, cách đặt tên).
Ghi tên nhân vật vào [CAST.md](CAST.md) — cả bản VI và EN.

Nhớ: `ORDER`, `BEATS`, beat `"short-outro"` (thiếu là không có bản Short), `PRON` cho VBee, `NGUON`.

> **Cổng:** `python tools/check-episode.py <slug>` không còn ✗ ở phần lời dẫn.

## 4 · Soạn shot 🤖

Skill: **`creature-field-guide-production`** (phần "Soạn shot").

`bible/shots/<ep>.json` → `node tools/build-prompts.mjs <ep>` → bốn file trong `prompts/`.
Ảnh mẫu (`kind: "plate"`) sinh trước, mọi cảnh khác lấy nó làm `[ref]` để con vật không đổi hình.
Cá thể có dấu riêng thì khai ở `individuals` trong `bible/creatures/<loài>.json` và gọi bằng
`"creatures": ["bulbasaur:K7"]`.

> **Cổng:** mỗi beat trong `ORDER` có ít nhất một shot; mỗi dấu tích dùng để đặt tên đều có **một
> shot cận cảnh riêng** — tên đặt theo thứ khán giả không nhìn thấy là tên chết.

## 5 · Sinh ảnh ✋🤖

Google Flow, project "Creature". Một hai ảnh lẻ thì gõ thẳng vào ô prompt của project; cả loạt thì
mở Tools → Batch Image Studio Pro, dán `prompts/<ep>.flow.txt`.

Tải ZIP về → `python tools/import-flow.py <ep>` → `python tools/unwatermark.py <ep>`.

> **Cổng:** ảnh nào định zoom ≥ 2× phải từ 2000 px trở lên, và watermark đã sạch. Zoom vào ảnh vỡ
> thì cả cảnh hỏng, mà lúc đó bạn đã đo toạ độ callout xong rồi.

## 6 · Dựng hình 🤖

Skill: **`creature-field-guide-production`** (phần "Dựng cảnh").

`scenes.json`: `world` cho cảnh tràn khung, `specimen` cho cảnh soi từng điểm, `clip` cho video.
**Toạ độ callout đo trên ảnh thật**, không đoán. Chữ lower-third: `text` ≤ 4.2, `caption` ≤ 2.7.

Rồi: `npm run scaffold -- <slug>` (timing ước lượng, audio câm) → `npm run registry` → `npm run studio`.

> **Cổng:** xem hết một lượt ở **cả 16:9 lẫn 9:16**. Bản dọc là nơi chữ tràn và cảnh rộng chết.

## 7 · Tiếng 🤖

[SOUND.md](SOUND.md): ghép ba lớp (thân / giọng / chi tiết), mỗi lớp một loài thật.
Nguồn chỉ Pixabay và Freesound CC0.

> **Cổng:** mọi cue có trong `sfx.json` đều có file thật, và không cue nào đè lên một câu quan trọng.

## 8 · Giọng ✋

VBee, đọc từ `out/<slug>/script-tts.txt`. Nghe lại toàn bộ trước khi ghép: phiên âm sai một tên loài
là phải thu lại cả beat.

Có giọng thật rồi thì chạy lại timing và phụ đề: `npm run align -- <slug>` rồi
`python tools/export-subs.py <slug>`.

> **Cổng:** timing trong `timings.json` là timing **thật**, không còn là ước lượng của scaffold.

## 9 · Soát 🤖

```bash
python tools/check-episode.py <slug>
```

Máy soát được: khung tập, chữ làm lộ khung (game, AI, đoàn phim, "lột da"), nguồn canon, tên nhân vật
khớp CAST.md, chữ tràn, file hình/tiếng thiếu, ảnh sinh ra mà không dùng, timing và phụ đề cũ,
thumbnail thiếu field, phiên âm thiếu.

Máy **không** soát được, người phải tự xem — dùng
[episode-checklist.md](../.claude/skills/creature-field-guide-scriptwriter/references/episode-checklist.md):
câu chuyện có sức ép không, cái tên có đến sau quan sát không, cảnh tiến hoá có đúng luật không,
có chỗ nào giả thuyết bị kể như sự thật không.

> **Cổng:** không còn ✗. Mỗi ⚠ đều đã được đọc và cố ý bỏ qua.

## 10 · Render & đăng ✋🤖

```bash
npm run thumb -- <slug>
npm run build -- <slug> --skip-audio
```

Lên YouTube: bật khai báo **nội dung tổng hợp bằng AI**, gắn phụ đề `out/<slug>/long.srt`, mô tả ghi
rõ đây là phim tài liệu giả tưởng về sinh vật hư cấu, credit **Tuấn La**.

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
10. Giọng thu xong mới phát hiện một câu vi phạm luật kênh (ví dụ "lột da").

Chín trong mười cái đó `check-episode.py` bắt được. Cái còn lại (số 4) thì chỉ có thói quen:
**sinh ảnh xong hẳn rồi mới đo toạ độ.**
