# Creature Field Guide

Phim tài liệu tự nhiên về những sinh vật không có thật — dựng như Discovery, đi theo thứ tự danh lục,
làm hai bản Việt và Anh.

Trợ lý AI (Claude, Gemini, Codex, Cursor, Copilot…) đọc **[AGENTS.md](AGENTS.md)** trước: bản đồ đọc theo việc, luật kênh,
cách làm việc. `CLAUDE.md` và `GEMINI.md` chỉ nhúng file đó.

Bắt đầu ở đây: **[docs/PIPELINE.md](docs/PIPELINE.md)** — mười chặng từ ý tưởng tới bản upload, mỗi
chặng một cổng.

| Tài liệu | Trả lời câu hỏi |
|---|---|
| [PIPELINE.md](docs/PIPELINE.md) | làm một tập thì đi qua những chặng nào, cổng ở đâu |
| [CREATURE-LENS.md](docs/CREATURE-LENS.md) | soi một sinh vật bất kỳ qua những trục nào |
| [IDEA-BANK.md](docs/IDEA-BANK.md) | tập này kể chuyện gì, tập sau kể chuyện gì |
| [EPISODE-FRAME.md](docs/EPISODE-FRAME.md) | một tập có mấy chương, mỗi chương làm gì |
| [CAST.md](docs/CAST.md) | nhân vật tên gì ở bản VI và bản EN, đặt theo luật nào |
| [SOUND.md](docs/SOUND.md) | tiếng kêu ghép từ những loài thật nào, nhạc nền theo tông nào |
| [MUSIC-PROMPTS.md](docs/MUSIC-PROMPTS.md) | hai mươi câu lệnh sinh nhạc, theo mười chặng của khung tập |
| [JOURNAL-STYLE.md](docs/JOURNAL-STYLE.md) | visual spec sổ thực địa Dr. Holth — aesthetic Gravity Falls, nội dung bio-energy |

Máy làm được phần nào thì nằm ở `.claude/`:

| | |
|---|---|
| `/tap-moi <loài>` | mở tập mới: ý tưởng → canon → kịch bản → shot, dừng trước khi tốn tiền ảnh |
| `/soat-tap <slug>` | soát trước khi thu giọng: máy soát rồi tới người soát |
| `/nghi-y-tuong <loài>` | khai phá 6 hướng nội dung và chọn một ý mạnh, chưa mở tập hay sửa pipeline |
| `/review-noi-dung <file hoặc slug>` | review canon, speculative biology, câu chuyện và lời dẫn; bỏ qua UI/code |
| `/nap-am` | nạp âm thanh vừa tải về: đổi tên, cắt, vào đúng chỗ, không để bản sao |
| skill `creature-field-guide-scriptwriter` | luật viết lời |
| skill `creature-field-guide-production` | bible → ảnh → `scenes.json` → render |
| skill `creature-motion` | biến một ảnh tĩnh thành vòng lặp động nhẹ — xem [experiments/creature-motion](experiments/creature-motion/README.md) |

## Lệnh hay dùng

```bash
node tools/build-prompts.mjs <ep>          # bible -> prompt cho Google Flow
python tools/import-flow.py <ep>           # ZIP tải về -> public/img/
python tools/unwatermark.py <ep>           # gỡ watermark Gemini
python tools/build-sfx.py <slug>           # sfx.json -> tiếng của tập
python tools/build-music.py                # 20 đoạn nhạc, cùng tông La thứ
python tools/import-music.py <file>        # nhạc tải về -> bản nền lặp được
python tools/intake.py --status            # bản gốc / bản dựng, nặng bao nhiêu
npm run scaffold -- <slug>                 # timing ước lượng + audio câm
npm run studio                             # xem thử
python tools/check-episode.py <slug>       # soát trước khi thu giọng / render
python tools/export-subs.py <slug>         # phụ đề .srt
npm run build -- <slug> --skip-audio       # render Long + Short
```

Engine dựng video là [blog2video](https://github.com/tuanla90/blog-to-video), nối bằng `file:` trong
`package.json`. Nội dung của kênh nằm ở đây; thứ gì dùng chung cho mọi kênh thì thuộc về engine.

Nội dung sinh bằng AI, có khai báo khi đăng. Đây là phim tài liệu giả tưởng, không phải sản phẩm
chính thức của chủ sở hữu các sinh vật được nhắc tới.
