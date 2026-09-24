# Bàn giao · bạn nói "xong", máy biết phải làm gì

Mỗi việc tay trong [PIPELINE.md](PIPELINE.md) kết thúc bằng **một file đặt đúng tên ở đúng chỗ**. Khi
tên file đã nói hết, bạn chỉ cần nhắn **`xong`** (hoặc `xong <việc>` cho nhanh), rồi Claude chạy:

```bash
PYTHONUTF8=1 python tools/handoff.py <slug>            # cái gì đã tới, còn thiếu gì, bước tiếp
PYTHONUTF8=1 python tools/handoff.py <slug> --take     # nạp file mới vào đúng chỗ
```

Chạy ở **thư mục chính của repo** (nơi có ảnh thật), không chạy trong worktree.

## Chỗ thả file

Thả vào **`inbox/`** ở gốc repo, hoặc để nguyên trong **Downloads**. Tool quét cả hai và nhận file bằng
nội dung, không bằng đuôi tên, nên file `.tmp` do trình duyệt trong app lưu cũng nhận được, **miễn là
tên đúng**. Nạp xong thì file **rời khỏi** inbox/Downloads (chuyển chứ không chép). Tool không xoá
gì: ảnh bị thay được đổi tên thành `<tên>.prev1.jpg`, còn ZIP đã giải nén thì cất vào `inbox/done/`.

`inbox/` không vào git.

## Bảng từ khoá

| Bạn nói | Bạn đã làm | File phải tên là | Tool đặt vào | Claude làm tiếp |
|---|---|---|---|---|
| `xong ý tưởng` | dán `drafts/1-ideas-brief.md` vào Gemini | `videos/<slug>/drafts/1-ideas-gemini.md` (dán thẳng, không qua inbox) | — | chấm sáu ý, chọn một kèm lý do và một ý dự phòng, dựng `2-skeleton.md`, ghép `3-script-brief.md` |
| `xong kịch bản` (hoặc `xong gemini`) | dán `drafts/3-script-brief.md` vào Gemini | `drafts/3-script-gemini.md` (vòng sau `-2`, `-3`) | — | `--draft` → chuẩn hoá vào `content.py` → ghi `4-review.md` → báo chỗ bạn phải chốt |
| `duyệt` | đọc `4-review.md` và bản dựng câm | — | — | ghi `Đã duyệt: <ngày>` vào `4-review.md`, rồi soạn shot |
| `xong refs` | tải ảnh tham chiếu theo danh sách tool in ra | `<ref-id>.png` (vd `ref-bulbasaur-shiny.png`) | `bible/refs/<loài>/<file>`, đánh dấu “đã tải” trong `refs.json` | gắn vào ảnh mẫu, sinh lại `prompts/` |
| `xong ảnh mẫu` | chạy loạt ảnh mẫu trong Batch Studio, tải ZIP | ZIP **tên gì cũng được** | `public/img/<ep>/<shot-id>.jpg` | gỡ watermark, mở cho bạn xem, rồi mới ra loạt cảnh |
| `xong ảnh` | chạy loạt cảnh, tải ZIP | như trên | như trên | gỡ watermark, đo toạ độ callout, dựng `scenes.json` |
| — | sinh lại **một** ảnh lẻ ngoài batch | `<shot-id>.jpg` hoặc `.png` | `public/img/<ep>/<shot-id>.jpg` | như trên, đo lại toạ độ của riêng ảnh ấy |
| `xong clip` | tải clip Veo / Seedance | `<shot-id>.mp4` (nhiều bản thì `<shot-id>-2.mp4`) | `public/video/<ep>/` | cắt `from`/`to`, gắn vào `scenes.json` |
| `xong earth` | tải ảnh/video loài Trái Đất từ nguồn sạch ([SCENE-TYPES.md](SCENE-TYPES.md) mục B2) | `earth-<loài>-<bộ phận>.mp4` hoặc `.jpg`, và **một dòng** trong `videos/<slug>/earth.json` | `public/video/<ep>/` hoặc `public/img/<ep>/` | soát giấy phép, gắn vào `callout.media` |
| `xong giọng` | thu VBee từng beat | `beat-00.mp3` … `beat-15.mp3`, `short-outro.mp3` | `public/audio/<slug>/` | `npm run align` → `export-subs.py` → soát lệch |
| `xong âm` | tải nhạc / tiếng động | theo [SOUND.md](SOUND.md) | `assets/` | chạy `/nap-am` (tool riêng: `tools/intake.py`) |
| `xong duyệt` | xem bản dựng trong `tools/review.py`, ghi chú tại chỗ | tự lưu `videos/<slug>/review-notes.json` | — | sửa theo từng ghi chú, báo lại cái nào chưa sửa được |
| `xong đăng` | đăng lên YouTube | điền link vào `docs/SLATE.md` | — | chạy `backup-episode.py`, mở tập sau |

**ID lấy ở đâu:** id ảnh nằm trong `prompts/<ep>*.jsonl` và ở dòng `[id: …]` của file `.flow.txt`.
Id ảnh tham chiếu nằm trong `bible/refs/<loài>/refs.json`. Không nhớ thì chạy tool không kèm cờ, nó
in ra từng id còn thiếu.

## Luồng kịch bản — năm bước

```
videos/<slug>/drafts/
  1-ideas-brief.md     bản dán cho Gemini: liệt kê sáu ý          (tool ghép)
  1-ideas-gemini.md    Gemini trả                                   → “xong ý tưởng”
  2-skeleton.md        Claude chọn ý, tra canon, dựng khung
  3-script-brief.md    bản dán cho Gemini: dựng lại khung + viết lời (tool ghép)
  3-script-gemini.md   Gemini trả (vòng sau: -2, -3)                → “xong kịch bản”
  4-review.md          Claude chuẩn hoá: đã sửa gì, vì sao, đề xuất nào nhận / bỏ
                       + content.py                                 → bạn nói “duyệt”
```

Bản dán **không viết tay**: `tools/handoff.py <slug> --brief ideas "<loài>"` hoặc `--brief script`
ghép từ ba mảnh — [briefs/core.md](briefs/core.md) (thế giới, người dẫn, luật cứng, luật so sánh Trái
Đất, dùng chung mọi tập) · đề bài của bước ([briefs/ideas.md](briefs/ideas.md),
[briefs/script.md](briefs/script.md)) · và `2-skeleton.md` riêng của tập. Luật kênh đổi thì sửa một
chỗ, ghép lại là mọi bản dán sau đều theo. Mỗi bản dán tự dặn Gemini lưu vào đâu.

Quyền của Gemini ở bước 3: **bố cục thả, sự kiện khoá** — xem [PIPELINE.md](PIPELINE.md) chặng 3.

`--draft` chỉ soát **phần có luật**: đủ mục, từ cấm (game, đoàn phim, lột da) cả EN lẫn VI, tên
riêng cũ, đặc điểm cá thể trung tâm gọi đúng một lần và sau cảnh cận, `who`/`loc` nằm trong khung,
hạn mức dừng hình và ảnh quê nhà, tổng thời lượng, hai track lệch nhau, bố cục đổi so với khung.
Nhãn bằng chứng có đúng không, số có khớp TIMELINE không, câu có hay không thì Claude đọc tiếp.

Tập 001 bỏ qua bước 1 (ý đã chốt trước khi có luồng này), đi thẳng từ `2-skeleton.md`. Bản Gemini lưu
theo tên cũ `v4-gemini.md` vẫn được nhận.

## Vì sao đặt tên chặt thế

Mỗi lần phải hỏi "file này là cái gì" là một vòng hỏi qua lại. Tên file mang id thì máy tự trả lời
được, và một id sai thì tool báo ngay, không lặng lẽ đặt nhầm chỗ.
