---
name: creature-field-guide-production
description: Turn a finished Creature Field Guide script into a rendered episode — shot bible, Google Flow image batches, scenes.json staging with world/specimen/clip, timing, subtitles and the pre-render lint. Use after the script exists; the scriptwriter skill covers the writing itself.
---

# Creature Field Guide — production

Kịch bản xong rồi mới dùng skill này. Việc của nó là biến `content.py` thành một tập render được,
không miss chặng nào. Bản đồ tổng: `docs/PIPELINE.md`.

## Repo nằm ở đâu

```
bible/style.json                 văn phong ảnh dùng chung (style, creatureTreatment, forbidden, output)
bible/creatures/<loài>.json      anchor + appearance + sexDifferences + individuals + forbidden
bible/shots/<ep>.json            danh sách shot của tập
prompts/<ep>.{txt,flow.txt,jsonl,md}   sinh ra, đừng sửa tay
videos/<slug>/content.py         lời dẫn (ORDER, BEATS, PRON, NGUON)
videos/<slug>/scenes.json        hình từng beat
public/img/<ep>/                 ảnh đã import + gỡ watermark
docs/                            CAST · CREATURE-LENS · EPISODE-FRAME · IDEA-BANK · SOUND · PIPELINE
```

## Soạn shot

Một shot:

```json
{ "id": "n08-raptor-strike", "beat": "08", "kind": "scene",
  "creatures": ["bulbasaur:K7"],
  "scene": "chuyện gì đang xảy ra, nói như tả một bức ảnh thật",
  "framing": "góc máy, ánh sáng, khoảng cách" }
```

- `kind` chọn khối style trong `bible/style.json`:

  | `kind` | Là gì | Ghi chú |
  |---|---|---|
  | `plate` | ảnh mẫu, nền trơn, cả thân | sinh **trước**, mọi cảnh khác lấy nó làm `[ref]` |
  | `scene` | cảnh thật | mặc định |
  | ~~`real`~~ | **ngừng dùng** | loài Trái Đất lấy ảnh/video thật, xem `docs/SCENE-TYPES.md` mục B2 |
  | `anatomy` | X-quang mô phỏng, nền xanh, xương và mạch năng lượng | thân **nguyên vẹn, khép kín** — không máu me, nội tạng, mổ xẻ |
  | `fieldnote` | trang sổ thực địa: giấy + hình vẽ chì/mực | chừa trống **một phần ba bên phải** |
  | `location` | **địa điểm trống**, không một sinh vật nào | ảnh mẫu địa điểm — sinh trước, mọi cảnh cùng nơi lấy làm `[ref]` |

  Trường thêm của shot: `size` · `angle` · `motion` · `location` (`"viridian-forest:clearing"`) ·
  `studies` (cho `fieldnote`, `"footprint"` lấy dấu chân canon). Chuỗi tham chiếu ba lớp — ảnh tham
  chiếu → ảnh mẫu → cảnh — và luật hai ảnh mẫu (con thường / con được chọn): `docs/SCENE-TYPES.md`
  mục A2, A3.

  `anatomy` và `fieldnote` **không lấy `[ref]`** từ ảnh mẫu — ref là ảnh chụp, nó sẽ kéo bản x-quang
  và bản vẽ tay ngược về thành ảnh chụp. Cái giá: hai kind này dễ lệch hình hơn, nên tả `scene` kỹ hơn.

  **`fieldnote` không có một chữ nào, cũng không có một mũi tên nào.** Chữ do element `notepage`
  của engine vẽ lên sau:

  ```json
  { "el": "notepage", "src": "img/kanto-001/x02-fieldnote.jpg",
    "notes": [
      { "x": 0.72, "y": 0.22, "text": "củ nghiêng hẳn sang trái", "atWord": "nghiêng" },
      { "x": 0.72, "y": 0.41, "text": "ba lớp bẹ, lớp ngoài đã khô", "atWord": "bẹ" }
    ] }
  ```

  Toạ độ `x`,`y` là toạ độ **trên ảnh** (0..1), đo bằng `tools/review.py` như callout. Ghi chú hiện
  dần theo từ trong giọng đọc và **tích lại** tới hết cảnh. Font là PatrickHand — một trong số ít
  font viết tay của Google Fonts có tiếng Việt. AI sinh chữ ra ký tự méo (tiếng Việt có dấu méo nặng hơn), còn mũi tên AI vẽ thì chỉ
  sai chỗ mà không sửa được. Đổi lại được ba thứ: chữ luôn đọc được, sửa lời không phải sinh lại ảnh,
  và bản EN dùng chung y hệt tấm giấy — chỉ đổi lớp chữ.
- `creatures`: `"<loài>"`, `"<loài>:male|female"` (lấy `sexDifferences`), `"<loài>:<mã cá thể>"`
  (lấy thêm `individuals[mã].marks` — dấu riêng của cá thể có tên trong tập).
- `dropAppearance`: bỏ vài dòng mô tả chung chọi với cảnh (vd con non chưa có củ).
- `allow`: bỏ vài mục khỏi danh sách cấm chung (vd cảnh trận đấu cần có bóng người xem).

Rồi `node tools/build-prompts.mjs <ep>`. File `.flow.txt` là thứ dán vào Batch Studio: mỗi block mở
bằng `[id: …]`, cảnh nào có sinh vật đã có ảnh mẫu thì tự thêm `[ref: <id ảnh mẫu>]`.

**Luật quan trọng nhất:** đặc điểm nhận dạng của cá thể trung tâm (vd màu Shiny) phải có **một cảnh
rõ riêng**, và cảnh ấy đứng **trước** chỗ lời dẫn gọi nó ra. Gọi ra một đặc điểm khán giả chưa nhìn
thấy là chữ rơi vào hư không. Kênh không đặt tên riêng cho con vật — xem `docs/CAST.md`.

## Sinh ảnh trong Google Flow

Project "Creature" trên flow.google.com. Hai đường:

- **Vài ảnh lẻ**: gõ thẳng vào ô prompt của project. Nút Settings chọn model (Nano Banana Pro / 2 /
  2 Lite), tỉ lệ, số bản. Ô này ở trang gốc nên gõ vào bình thường.
- **Cả loạt**: Tools → Batch Image Studio Pro, dán `.flow.txt`.

Bẫy đã dính, đừng dính lại:

- Phím tắt **không vào được iframe** của tool — chỉ gõ chữ được. Muốn thay nội dung ô thì click đầu
  rồi Shift+click cuối, gõ đè. Ctrl+A vô tác dụng.
- Click vào ảnh trên thẻ có thể trúng nút "Tạo lại" → mất credit.
- **Pane trình duyệt bị ẩn thì tab treo I/O**: console hiện `ERR_NETWORK_IO_SUSPENDED`, ảnh báo
  "Failed to load image". Nhờ người dùng mở lại pane trước khi kết luận lỗi phía Google.
- Cùng `[id]` + cùng prompt thì Flow giữ kết quả cũ, không tốn credit thêm.

Tải ZIP về rồi:

```bash
python tools/import-flow.py <ep>        # ZIP -> public/img/<ep>/<id>.jpg
python tools/unwatermark.py <ep>        # gỡ sao Gemini góc dưới-phải
```

SynthID vẫn còn sau khi gỡ watermark nhìn thấy được. Đó là lý do phải khai báo nội dung AI khi đăng.

## Dựng cảnh

`scenes.json`, mỗi beat:

```json
"08": { "bg": "CHƯƠNG 5 · MẮT TRO", "holdSec": 1.3, "moments": [ … ] }
```

Ba element làm gần hết việc:

| | Dùng khi | Nhớ |
|---|---|---|
| `world` | cảnh tràn khung, camera tự lia/phóng | nhiều `layers` + `depth` thì có parallax; `fx` cho hạt |
| `specimen` | soi từng điểm trên một ảnh mẫu | **toạ độ đo trên ảnh thật**, `atWord` neo theo lời đọc |
| `clip` | nguồn là video | `from`/`to` tính bằng giây trong file gốc, `speed`, tự lặp |
| `specimen` + `video` | **dừng hình để phân tích** | video chạy tới callout đầu rồi đứng; `callout.media` kẹp ảnh quê nhà. Tối đa 3 cú dừng, 2 ảnh quê nhà mỗi tập |

Luật chữ của kênh (khác mặc định của engine):

- `text` size ≤ **4.2**, `caption` ≤ **2.7** — to hơn là thành tiêu đề quảng cáo, không phải lower-third.
- `text` ≤ ~52 ký tự, `caption` ≤ ~68. Dài hơn thì bản dọc 9:16 tràn.
- Chữ trên ảnh tự canh trái, có vạch accent và dải tối mép. Không bật gradient.

Neo thời gian: `atWord` khớp **một từ xuất hiện sớm trong câu**. Neo vào từ cuối câu thì cảnh chỉ kịp
hiện một giây rồi beat chuyển.

Xong thì:

```bash
npm run scaffold -- <slug>      # timing ước lượng + audio câm
npm run registry                # sinh lại src/videos.gen.ts
npm run studio                  # xem ở cả 16:9 lẫn 9:16
```

## Cho ảnh thở

Cảnh đứng lâu mà ảnh chết thì người xem thấy ngay. Skill `creature-motion` biến một ảnh thành vòng
lặp 4 giây (thở, mắt khép, lá lay), chạy offline bằng OpenCV, không tốn credit. Xuất GIF rồi đổi sang
mp4 bằng ffmpeg đi kèm Remotion (`npx remotion ffmpeg`), dùng như `clip` bình thường.

Ba điều quyết định kết quả:

- Đặt **mỏ neo** trước: sọ, chỗ chân chạm đất, gốc của từng bộ phận. Rồi mới cho cái gì lay.
- `composite_mode: warp_only` cho nền phức tạp (tổ, trứng, lá chồng nhau); `cutout` chỉ hợp khi con
  vật nằm trên nền trơn.
- `output_width` và `fps` trong spec mặc định là 1032 px / 12 fps — **luôn đặt lại bằng chiều rộng
  thật của ảnh và 25 fps**, không thì clip mờ hơn ảnh gốc.

Đã dựng sẵn ba clip cho tập 1, xem `experiments/creature-motion/README.md`.

## Trước khi thu giọng và render

```bash
python tools/check-episode.py <slug>
```

Không còn ✗ thì mới đi tiếp. Mỗi ⚠ phải đọc và cố ý bỏ qua, không được lướt.

Phần máy không soát được thì theo
`.claude/skills/creature-field-guide-scriptwriter/references/episode-checklist.md`.

## Gotcha của dự án này

- `scenes.json` có `_note` tiếng Việt — **đừng đặt dấu ngoặc kép** trong đó, hỏng JSON và
  `export-subs.py` chết ngay.
- Sửa `content.py` thì **phải** chạy lại `scaffold` rồi `export-subs.py`, không thì phụ đề kể chuyện
  của bản cũ.
- Console Windows là cp1252: chạy script Python phải có `PYTHONUTF8=1`, không thì `UnicodeEncodeError`.
- Engine nối bằng `file:` trỏ vào worktree; sửa engine xong phải `npm run build:lib` bên engine.
- Element `sfx` lấy file trong `public/<audio.sfxDir>` (kênh này: `public/audio/sfx/`), tên có dấu
  chấm thì dùng nguyên văn nên đặt theo tập được. `volume` mặc định 0.1 là quá nhỏ cho tiếng sinh vật.
