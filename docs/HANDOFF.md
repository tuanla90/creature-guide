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
| `xong gemini` | dán `drafts/vN-brief.md` vào Gemini, chép câu trả lời | `videos/<slug>/drafts/vN-gemini.md` (dán thẳng, không qua inbox) | — | `--draft vN` → ép luật từng beat → chuyển vào `content.py` → báo chỗ phải chốt |
| `xong refs` | tải ảnh tham chiếu theo danh sách tool in ra | `<ref-id>.png` (vd `ref-bulbasaur-shiny.png`) | `bible/refs/<loài>/<file>`, đánh dấu “đã tải” trong `refs.json` | gắn vào ảnh mẫu, sinh lại `prompts/` |
| `xong ảnh mẫu` | chạy loạt ảnh mẫu trong Batch Studio, tải ZIP | ZIP **tên gì cũng được** | `public/img/<ep>/<shot-id>.jpg` | gỡ watermark, mở cho bạn xem, rồi mới ra loạt cảnh |
| `xong ảnh` | chạy loạt cảnh, tải ZIP | như trên | như trên | gỡ watermark, đo toạ độ callout, dựng `scenes.json` |
| — | sinh lại **một** ảnh lẻ ngoài batch | `<shot-id>.jpg` hoặc `.png` | `public/img/<ep>/<shot-id>.jpg` | như trên, đo lại toạ độ của riêng ảnh ấy |
| `xong clip` | tải clip Veo / Seedance | `<shot-id>.mp4` (nhiều bản thì `<shot-id>-2.mp4`) | `public/video/<ep>/` | cắt `from`/`to`, gắn vào `scenes.json` |
| `xong giọng` | thu VBee từng beat | `beat-00.mp3` … `beat-15.mp3`, `short-outro.mp3` | `public/audio/<slug>/` | `npm run align` → `export-subs.py` → soát lệch |
| `xong âm` | tải nhạc / tiếng động | theo [SOUND.md](SOUND.md) | `assets/` | chạy `/nap-am` (tool riêng: `tools/intake.py`) |
| `xong duyệt` | xem bản dựng trong `tools/review.py`, ghi chú tại chỗ | tự lưu `videos/<slug>/review-notes.json` | — | sửa theo từng ghi chú, báo lại cái nào chưa sửa được |
| `xong đăng` | đăng lên YouTube | điền link vào `docs/SLATE.md` | — | chạy `backup-episode.py`, mở tập sau |

**ID lấy ở đâu:** id ảnh nằm trong `prompts/<ep>*.jsonl` và ở dòng `[id: …]` của file `.flow.txt`.
Id ảnh tham chiếu nằm trong `bible/refs/<loài>/refs.json`. Không nhớ thì chạy tool không kèm cờ, nó
in ra từng id còn thiếu.

## Bản nháp kịch bản

```
videos/<slug>/drafts/
  v4-brief.md      Claude viết: luật + khung + định dạng trả về. Bạn dán cho Gemini.
  v4-gemini.md     Bạn dán nguyên văn câu trả lời của Gemini.
```

Mỗi vòng mới là một số mới (`v5-brief.md` …), không ghi đè vòng cũ, để còn so được hai vòng với
nhau. Bản brief có ba phần **lõi dùng lại cho mọi tập** (thế giới và người dẫn · luật cứng · định dạng
trả về) và ba phần riêng từng tập (tập này · khung beat · chỗ cần hay hơn). Tập mới thì chép brief của
tập trước rồi thay ba phần riêng.

`--draft vN` chỉ soát **phần có luật**: đủ beat, độ dài so với đích, hai track VI/EN lệch nhau, từ
cấm (game, đoàn phim, lột da), tên riêng cũ, “shiny” đúng một lần ở beat 02, giá trị cỡ cảnh/góc máy
hợp lệ, có X-quang, có trang sổ, màu K-01 được thấy trước khi được gọi. Nhãn bằng chứng có đúng
không, số liệu có khớp TIMELINE không, câu có hay không thì Claude đọc tiếp.

## Vì sao đặt tên chặt thế

Mỗi lần phải hỏi "file này là cái gì" là một vòng hỏi qua lại. Tên file mang id thì máy tự trả lời
được, và một id sai thì tool báo ngay, không lặng lẽ đặt nhầm chỗ.
