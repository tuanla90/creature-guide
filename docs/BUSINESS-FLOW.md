# Quy trình vận hành kênh · bản để góp ý

Đây là bản **nghiệp vụ**, không phải bản kỹ thuật. Mỗi bước trả lời: *làm gì, ra cái gì, ai làm,
bằng công cụ gì, và đã tự động tới đâu*. Bản kỹ thuật tương ứng là [PIPELINE.md](PIPELINE.md).

Cột **Tự động**: 🔴 làm tay hoàn toàn · 🟡 nửa tay nửa máy · 🟢 máy làm, người chỉ duyệt.
Cột **Ghi chú của bạn** để trống cho chủ dự án điền kinh nghiệm và công nghệ muốn dùng.

---

## A · Chiến lược và kế hoạch

| # | Bước | Ra cái gì | Ai | Công nghệ hiện tại | Tự động | Ghi chú của bạn |
|---|---|---|---|---|---|---|
| A1 | Định vị kênh, khán giả, điểm khác biệt | tuyên bố định vị | người | — (đang nằm trong đầu, chưa ghi ở đâu) | 🔴 | |
| A2 | Kho ý tưởng | `docs/IDEA-BANK.md` | người + máy | markdown | 🟡 | |
| A3 | Chọn tập tiếp theo, xếp lịch phát hành | lịch + tập đang làm | người | chưa có | 🔴 | |
| A4 | Ngân sách một tập (credit ảnh, giọng, nhạc) | hạn mức trước khi bắt đầu | người | chưa có — credit đang tiêu tới đâu biết tới đó | 🔴 | |

## B · Tiền kỳ

| # | Bước | Ra cái gì | Ai | Công nghệ hiện tại | Tự động | Ghi chú của bạn |
|---|---|---|---|---|---|---|
| B1 | Tra canon của loài | bảng `NGUON` | máy | Bulbapedia + đọc tay | 🟡 | |
| B2 | Tìm loài thật đối chiếu | cột 🔬 trong IDEA-BANK | máy | tra cứu web | 🟡 | |
| B3 | Hồ sơ hình dáng loài | `bible/creatures/<loài>.json` | máy | JSON viết tay | 🟡 | |
| B4 | Đặt tên nhân vật, hai ngôn ngữ | `docs/CAST.md` | máy + người duyệt | luật trong skill + CAST.md | 🟡 | |
| B5 | Viết kịch bản VI | `content.py` | máy | skill `creature-field-guide-scriptwriter` | 🟢 | |
| B6 | **Duyệt kịch bản** | quyết định đi tiếp | **người** | `episode-checklist.md` | 🔴 | |
| B7 | Bản EN | *chưa có* | — | **chưa có gì** | 🔴 | |
| B8 | Bảng shot | `bible/shots/<ep>.json` | máy | JSON + `build-prompts.mjs` | 🟢 | |

## C · Sản xuất tài sản

| # | Bước | Ra cái gì | Ai | Công nghệ hiện tại | Tự động | Ghi chú của bạn |
|---|---|---|---|---|---|---|
| C1 | Sinh ảnh | `public/img/<ep>/*.jpg` | người bấm, máy soạn | Google Flow (Nano Banana Pro) + tool Batch Studio | 🟡 | |
| C2 | Nhập ảnh, gỡ watermark | ảnh sạch | máy | `import-flow.py`, `unwatermark.py` | 🟢 | |
| C3 | Cho ảnh thở | `*-breath.mp4` | máy | skill `creature-motion` (OpenCV) + `remotion ffmpeg` | 🟢 | |
| C4 | Clip quay thật / video AI | `public/video/<ep>/*.mp4` | người | Veo trong Flow — **chưa thử** | 🔴 | |
| C5 | Tách lớp cho parallax | `layers/*.png` | người | cắt tay | 🔴 | |
| C6 | Đo toạ độ callout trên ảnh thật | số trong `scenes.json` | người | đọc toạ độ bằng mắt | 🔴 | |
| C7 | Nhạc nền | `public/audio/music/` | máy | `tools/build-music.py` — 20 đoạn cùng tông La thứ theo 10 chặng của khung tập · `import-music.py` cho nhạc sinh bằng Lyria / YouTube Audio Library | 🟢 | |
| C8 | Tiếng động, tiếng sinh vật | `public/audio/sfx/<ep>/` | máy + người đi tìm | `sfx.json` + `tools/build-sfx.py` — máy dựng bản tổng hợp ngay, người thay dần lớp giọng bằng Pixabay/Freesound CC0 ([SOUND.md](SOUND.md)) | 🟡 | |
| C9 | Giọng đọc VI | mp3 theo beat | người | VBee Pro | 🟡 | |
| C10 | Giọng đọc EN | *chưa có* | — | **chưa chọn nhà cung cấp** | 🔴 | |

## D · Hậu kỳ

| # | Bước | Ra cái gì | Ai | Công nghệ hiện tại | Tự động | Ghi chú của bạn |
|---|---|---|---|---|---|---|
| D1 | Dựng hình từng beat | `scenes.json` | máy | skill `creature-field-guide-production` | 🟢 | |
| D2 | Timing ước lượng để xem trước | `timings.json` | máy | `npm run scaffold` | 🟢 | |
| D3 | Timing thật theo giọng | `timings.json` | máy | `npm run align` (whisper) | 🟢 | |
| D4 | Phụ đề VI | `out/<slug>/long.srt` | máy | `export-subs.py` | 🟢 | |
| D5 | Phụ đề EN | *chưa có* | — | **chưa có** | 🔴 | |
| D6 | Soát máy | báo cáo ✗/⚠ | máy | `check-episode.py` | 🟢 | |
| D7 | **Soát người, xem hết một lượt có tiếng** | quyết định phát hành | **người** | mắt và tai | 🔴 | |
| D8 | Render Long + Short | mp4 | máy | Remotion | 🟢 | |
| D9 | Thumbnail | 1280×720 | máy | `npm run thumb` | 🟢 | |
| D10 | Tiêu đề, mô tả, tag, chương | metadata | người | **chưa lưu ở đâu cả** | 🔴 | |

## E · Phát hành và vận hành

| # | Bước | Ra cái gì | Ai | Công nghệ hiện tại | Tự động | Ghi chú của bạn |
|---|---|---|---|---|---|---|
| E1 | Đăng YouTube, khai báo nội dung AI | video công khai | người | YouTube Studio | 🔴 | |
| E2 | Bản EN: kênh riêng hay multi-audio | quyết định | người | **chưa quyết** | 🔴 | |
| E3 | Sổ tài sản và giấy phép | ai sinh cái gì, license gì | *chưa có* | **chưa có** | 🔴 | |
| E4 | Sổ chi phí | tiền/credit mỗi tập | *chưa có* | **chưa có** | 🔴 | |
| E5 | Sao lưu ảnh và clip | bản sao ngoài máy | *chưa có* | **`public/img` nằm ngoài git — mất máy là mất hết** | 🔴 | |
| E6 | Đọc số liệu, rút bài học về IDEA-BANK | ý tưởng tập sau | người | YouTube Analytics | 🔴 | |
| E7 | Sửa sau khi đăng | bản vá | người | chưa có quy ước | 🔴 | |

---

## Chỗ trống lớn nhất, xếp theo mức đau

1. **E5 · Sao lưu.** Ảnh và clip không nằm trong git (đúng, vì nặng), nhưng cũng **không nằm ở đâu khác**.
   Một tập là ~40 ảnh đã trả credit. Đây là rủi ro lớn nhất trong toàn bộ danh sách và rẻ nhất để vá.
2. **B7 / C10 / D5 · Cả nhánh tiếng Anh.** Kênh định làm song ngữ nhưng chưa có một bước nào cho bản EN.
3. **E3 · Sổ tài sản và giấy phép.** Kênh có kiếm tiền thì phải trả lời được "file này ở đâu ra, ai cho
   phép dùng" cho **từng** file. Hiện thông tin ấy nằm rải rác trong chat và trong đầu.
4. **D10 · Metadata.** Tiêu đề và mô tả quyết định lượt xem, mà đang không được lưu, không được soát,
   không có phiên bản.
5. **A4 / E4 · Tiền.** Không biết một tập tốn bao nhiêu thì không biết kênh có sống được không.
6. **C6 · Đo toạ độ bằng mắt.** Việc tay lặp lại nhiều nhất trong cả dây chuyền.
7. **A3 · Lịch phát hành.** Một tập thì nhớ được; năm tập song song thì không.
