---
description: Nạp âm thanh vừa tải về — tự đổi tên, cắt, đưa vào đúng chỗ, không để lại bản sao
argument-hint: (để trống = quét Downloads) · <cue>/<lớp> cho một file tiếng · status
---

Nạp âm thanh vừa tải về: **$ARGUMENTS**

Luật đứng sau mọi bước dưới đây: **một file gốc chỉ được nằm ở đúng một chỗ.** `assets/` giữ bản
gốc — đó là thứ duy nhất không dựng lại được, và là thứ duy nhất phải sao lưu. Mọi thứ trong
`public/audio/` là bản dựng ra, xoá lúc nào cũng được. Không bao giờ chép thêm "cho chắc".

## Không có tham số — nạp nhạc

```bash
PYTHONUTF8=1 python tools/intake.py --dry-run
```

Xem trước rồi mới chạy thật (bỏ `--dry-run`). Tool tự khớp tên file tải về với bảng bối cảnh
trong `tools/build-music.py`, chuyển bản gốc vào `assets/music-src/`, rồi dựng ra
`public/audio/music/<tên>-lyria.wav`: kéo về La thứ, cắt đoạn mở/tắt dần, gấp đuôi chồng lên đầu
cho vòng lặp khép kín — riêng bốn đoạn chơi một lần thì giữ nguyên mở và kết.

File nào không khớp tên thì tool bỏ qua và nói rõ. Lúc tải từ Gemini nhớ đặt đúng tên ở cột cuối
mỗi mục trong [docs/MUSIC-PROMPTS.md](../../docs/MUSIC-PROMPTS.md), ví dụ `field-bed-stalk.mp3`.

**Báo lại cho chủ dự án:** đoạn nào vừa nạp, tông đo được bao nhiêu phần trăm nằm trong La thứ,
và đoạn nào rớt ngưỡng (≥95% nếu sẽ chồng lên đoạn khác, ≥80% nếu chạy một mình). Dưới 80% thì nói
thẳng là phải sinh lại, đừng để lẫn vào bộ.

## `<cue>/<lớp>` — nạp một lớp tiếng

```bash
PYTHONUTF8=1 python tools/intake.py --sfx $ARGUMENTS
```

Lấy **file âm thanh mới nhất** trong Downloads (nhận cả `.tmp` mà trình duyệt trong app hay lưu,
vì tool soi mấy byte đầu chứ không tin đuôi tên), đổi sang wav 48 kHz mono, đặt vào
`assets/sfx-src/<cue>/<lớp>.wav`, rồi dựng lại riêng cue ấy.

Không nhớ đang thiếu lớp nào thì chạy `PYTHONUTF8=1 python tools/build-sfx.py <slug>` — nó in sẵn
danh sách kèm từ khoá đi tìm.

**Nếu loài tải về khác loài đã ghi trong bảng** (hay gặp: không có bản CC0 nào của vạc, phải lấy
tiếng ngỗng), thì sửa trường `species` của lớp ấy trong `videos/<slug>/sfx.json` cho khớp con vật
thật sự đã dùng. Bảng đó là chỗ trả lời "tiếng này ở đâu ra" — sai là mất luôn sổ giấy phép.

## `status` — đang nặng bao nhiêu, trùng ở đâu

```bash
PYTHONUTF8=1 python tools/intake.py --status
```

In ra dung lượng bản gốc (phải sao lưu) so với bản dựng (xoá được), và cảnh báo nếu còn file sót
lại trong Downloads sau khi đã nạp.

`public/` bị Remotion đóng gói mỗi lần render, nên mỗi MB nằm trong đó là thuế phải trả cho mọi
lần render. Thấy `public/audio/music` phình lên thì xoá bản không dùng — một lệnh là dựng lại.

## Luật không được quên

- **Chuyển, không chép.** Nạp xong mà Downloads vẫn còn file ấy là sai; tool đã chuyển thì thư mục
  tải về phải sạch.
- **Nguồn tiếng chỉ ba nơi**, đều không đòi ghi nguồn: Freesound lọc CC0 · Pixabay · Sonniss GDC.
  Không CC-BY, không xeno-canto, không BBC — luật đầy đủ ở [docs/SOUND.md](../../docs/SOUND.md).
- **Không đẩy `assets/` lên repo công khai.** Giấy phép Sonniss cấm phát tán lại chính file tiếng.
