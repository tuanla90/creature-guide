# Quy trình vận hành kênh · bản nghiệp vụ

Bản **nghiệp vụ**, không phải bản kỹ thuật. Mỗi bước trả lời: *làm gì, ra cái gì, bằng công cụ gì,
tự động tới đâu, và bao lâu làm một lần*. Bản kỹ thuật tương ứng là [PIPELINE.md](PIPELINE.md).

**Cột Auto** — 🔴 làm tay, chưa ai tự động hoá · 🟡 nửa tay nửa máy · 🟢 máy làm, người duyệt ·
✋ **cố ý là người, không bao giờ nên tự động hoá**.

**Cột Nhịp** — `1×` làm một lần rồi thôi · `tập` mỗi tập một lần · `kỳ` định kỳ, không theo tập.

Phân biệt 🔴 với ✋ là quan trọng: 🔴 là **nợ**, ✋ là **chỗ bạn chịu trách nhiệm**. Đếm nợ thì chỉ
đếm 🔴.

---

## Những gì đã chốt

Ghi lại để sáu tháng sau không ai phải hỏi lại "vì sao hồi đó quyết thế".

| Quyết định | Chốt là | Vì sao |
|---|---|---|
| Chủ thể kênh | Sinh vật đã có trong văn hoá: Pokémon → thần thoại, cổ tích, HP/LOTR/GoT | Lõi kênh là **góc nhìn**, không phải Pokémon |
| Lộ trình | Đi hết Kanto (~70–80 tập, 8–9 tháng) rồi rẽ sang nhóm phạm vi công cộng | Fan Pokémon kéo sub nhanh cho kênh mới |
| Điều kiện rẽ nhánh | **Sự kiện, không phải ngày**: dính tín hiệu IP, hoặc đủ sub | Phải có người theo dõi — xem A5 |
| Kênh | **Một kênh, YouTube multi-audio** | Gộp sub và view; 2 lượt đăng/tuần thay vì 4 |
| Ngôn ngữ gốc | **Viết EN trước → dịch VI → người tinh chỉnh** | AI viết EN tự nhiên hơn viết VI |
| Cái giá của multi-audio | Giọng VI phải **khít từng beat** với bản dựng theo EN | Một video, một dòng thời gian |
| Nhịp | 2 tập/tuần, cuốn chiếu, WIP = 1 | Ưng mới làm tiếp |
| Nút thắt thật | **Duyệt ý tưởng và script** (4–5h/tập), không phải sinh ảnh | Nên đầu tư vào *rút ngắn vòng duyệt*, không phải *tăng tốc sinh ảnh* |
| Sao lưu | Google Drive, **chép một chiều**; git giữ phần chữ | Git không chứa nổi 7–14GB ảnh |
| Đăng | Đăng tay, máy soạn sẵn gói đăng | Tường không phải code mà là xác minh app Google |
| Sửa sau đăng | Ghim comment đính chính | Nội dung hư cấu, không cần gỡ video |
| Luồng kịch bản | **Gemini liệt kê ý → Claude chọn, dựng khung → Gemini dựng lại và viết lời → Claude chuẩn hoá → người duyệt trên trang** | Gemini nghĩ rộng, Claude giữ luật. Lần chạy đầu Gemini phạm bốn luật mà tự khai là không — bước chuẩn hoá là bắt buộc |
| Quyền của Gemini | Bố cục thả, **sự kiện khoá** (canon chỉ từ bảng nguồn của khung) | Gemini giỏi bố cục, hay bịa canon |
| Gọi con vật | **Không đặt tên riêng**: đặc điểm canon + mã (`Shiny Bulbasaur · K-01`); "shiny" nói một lần, sau khi đã thấy | Tên tự đặt ping-pong bốn vòng ở tập 001 |
| Loài Trái Đất | Tối đa **3 cú dừng hình, 2 ảnh quê nhà** mỗi tập, còn lại chỉ nói; **không sinh bằng AI**, lấy từ nguồn không đòi ghi tên tác giả | Sai về loài thật bị bắt ngay; cắt sang ảnh thật tràn khung làm vỡ nhập vai |
| Bàn giao | **Tên file mang id**, bạn chỉ nói "xong <việc>" | Mỗi câu hỏi "file này là gì" là một vòng qua lại |
| Duyệt | Trên một **trang** có Duyệt / Cần sửa từng beat, Claude đọc lại được | Nút thắt là duyệt — bớt chép ghi chú qua chat |
| Clip | Veo trong Flow **15 token/clip** — coi như không giới hạn; Seedance chỉ cho hành động | Đã đo |

### Ba thứ chưa chốt

1. **Giọng EN.** ElevenLabs free ≈ 10.000 ký tự/tháng; một tập ≈ 10.700 ký tự. Gói free đọc được
   **một tập mỗi tháng**, nhu cầu là tám. Phải trả tiền, đổi nhà, hoặc giảm nhịp bản EN.
2. **Track gốc của video là VI hay EN.** Ảnh hưởng tới ngôn ngữ mặc định và cách YouTube phân phối.
3. **Ranh giới IP với HP / LOTR / GoT** — chưa tới lúc, nhưng phải quyết trước khi làm tập đầu
   thuộc nhóm đó, không phải sau.

---

## 0 · Dựng kênh · làm một lần

Cụm này chưa từng có trong bảng cũ. Nó tồn tại vì kênh sẽ lập mới từ đầu, và vì **thứ tự bên trong
nó có ràng buộc**: multi-audio cần Advanced features, Advanced features cần xác minh số điện thoại.
Làm sai thứ tự thì phát hiện lúc sắp đăng tập đầu.

| # | Bước | Ra cái gì | Công nghệ | Auto | Nhịp |
|---|---|---|---|---|---|
| 0.1 | Lập kênh: tên, handle, avatar, banner, mô tả, ngôn ngữ kênh | kênh sống | [CHANNEL-SETUP.md](CHANNEL-SETUP.md) | ✋ | 1× |
| 0.2 | Xác minh danh tính → **bật Advanced features** | multi-audio dùng được | [CHANNEL-SETUP.md](CHANNEL-SETUP.md) | ✋ | 1× |
| 0.3 | Chốt track gốc VI hay EN | quyết định | — | ✋ | 1× |
| 0.4 | ✅ Khung tập thứ hai (so sánh 2–3 chủ thể) | `EPISODE-FRAME.md` khung B | markdown | 🟢 | 1× |
| 0.5 | ✅ `CREATURE-LENS.md` trung lập với Pokémon | nguồn hai tầng · trục 12 · bẫy từ vựng kỳ ảo | 🟢 | 1× |
| 0.6 | Thư viện nhạc mẫu — **21 bản nguồn đã có, chưa dựng ra `public/audio/music/`** | xem [SOUND.md](SOUND.md) | 🟡 | 1× |
| 0.7 | ✅ Bê 3 skill từ `semantix-docs`, cắt 3 luật của `stop-slop` | `episode-plan` · `episode-review` · `episode-publish` · `stop-slop` | 🟢 | 1× |
| 0.8 | ✅ Công cụ xem-và-ghi-chú trên bản dựng | `tools/review.py` → `review-notes.json` | 🟢 | 1× |
| 0.9 | ✅ Script sao lưu một chiều — *còn phải chọn thư mục Drive* | `tools/backup-episode.py` | 🟡 | 1× |

> **Cổng:** 0.2 xong thì mới có nghĩa để làm tiếp cụm D và E.

---

## A · Chiến lược

| # | Bước | Ra cái gì | Công nghệ | Auto | Nhịp |
|---|---|---|---|---|---|
| A1 | Định vị kênh | tuyên bố định vị (đã có, xem dưới) | markdown | ✋ | 1× |
| A2 | Kho ý tưởng | `docs/IDEA-BANK.md` | markdown + máy đề xuất | 🟡 | kỳ |
| A3 | Lịch: tập nào ở chặng nào, phát ngày nào | [SLATE.md](SLATE.md) | skill `episode-plan` | 🟢 | kỳ |
| A4 | Hạn mức mỗi chu kỳ | biết một tháng làm được mấy tập | đo thử 1 tháng | 🔴 | kỳ |
| A5 | **Theo dõi tín hiệu IP + ngưỡng rẽ nhánh** | sổ rà trong [SLATE.md](SLATE.md) | ✋ | kỳ |

**A1 · Định vị.** Phim tài liệu sinh học giả định (*speculative biology documentary*) kết hợp ký hoạ
thực địa. Khán giả: ban đầu fan Pokémon, sau là cộng đồng fantasy & sci-fi hardcore, 15–40 tuổi.
Điểm khác biệt: **nhân vật chính là con vật hoang dã, người chỉ đứng ngoài quan sát**; bàn giải phẫu,
chuyển hoá năng lượng, tập tính bầy đàn và cái giá sinh học — **không** bàn chiêu thức, cấp độ, hệ
khắc hệ, cốt truyện game. Tôn trọng đúng lore của sinh vật, rồi soi nó bằng sinh lý học.

**A4 · Ngân sách không phải tiền mà là trần.** Mọi thứ đã trả thuê bao (Claude Ultra, Gemini Ultra,
Google Flow, VBee Pro), nên câu hỏi đúng là *"một tháng làm được mấy tập trước khi đụng trần, và trần
nào đụng trước"*. Hai con số đáng đo trong tháng đầu: **giờ người mỗi tập** (đang ước 4–5h, chủ yếu ở
khâu duyệt) và **token Topview / ElevenLabs đã tiêu**. Chưa dựng hệ thống — chạy vài tập rồi đánh giá.

**A5 · Đang trống hoàn toàn.** "Rẽ nhánh khi dính IP hoặc đủ sub" chỉ là câu nói nếu không ai theo
dõi claim, strike, video bị gỡ, và con số sub. Đây là bước rẻ nhất trong cụm A và đang không tồn tại.

---

## B · Tiền kỳ · viết EN trước

Thứ tự ở đây đã đảo so với bản cũ: **EN là bản gốc**, VI là bản dịch. Khoảng trống "B7 · bản EN —
chưa có gì" của bảng cũ biến mất, vì EN không còn là phái sinh.

| # | Bước | Ra cái gì | Công nghệ | Auto | Nhịp |
|---|---|---|---|---|---|
| B0 | **Gemini liệt kê sáu ý** → Claude chấm, chọn một, giữ dự phòng | `drafts/1-ideas-gemini.md` → ý đã chọn | `handoff.py --brief ideas` | 🟢 | tập |
| B1 | **Chọn khung tập**: một cá thể, hay so sánh 2–3 chủ thể | quyết định | `EPISODE-FRAME.md` | 🟡 | tập |
| B2 | Tra canon, ghi rõ **phiên bản nào được chọn** | bảng `NGUON` | Bulbapedia / nguồn lore | 🟡 | tập |
| B3 | Tìm loài thật đối chiếu — **phải có nguồn tra được** | cột 🔬 | tra cứu web | 🟡 | tập |
| B4 | Hồ sơ hình dáng **mọi loài lên hình** (hai đường, xem dưới) + ảnh tham chiếu | `bible/creatures/<loài>.json` · `bible/refs/<loài>/` | JSON · tải tay | 🟡 | mỗi loài |
| B5 | Chốt đặc điểm cá thể trung tâm (không đặt tên) | `docs/CAST.md` · `individuals.<mã>.trait` | luật trong skill | 🟢 | tập |
| B6 | **Claude dựng khung → Gemini dựng lại và viết lời EN + VI nháp** | `drafts/2-skeleton.md` → `3-script-gemini.md` | `handoff.py --brief script` · bố cục thả, sự kiện khoá | 🟢 | tập |
| B7 | Soát máy + Claude chuẩn hoá: logic, nhãn, nguồn, luật | `content.py` + `drafts/4-review.md` | `handoff.py --draft` · `check-episode.py` | 🟢 | tập |
| B8 | Soát văn: giọng, sức ép kể chuyện | ghi chú sửa | Gemini + `stop-slop` đã cắt 3 luật | 🟢 | tập |
| B9 | **Người duyệt kịch bản + cảnh dự kiến** trên trang | Duyệt / Cần sửa từng beat | `drafts/4-scene-plan.json` → `tools/review-page.py` → Artifact (`db`) | ✋ | tập |
| B10 | ~~Bản VI theo hạn mức thời lượng từng beat~~ → **gộp vào B6/B7**: Gemini viết EN + VI cùng lúc, `--draft` soát lệch | bản VI | — | 🟢 | tập |
| B11 | ~~Người tinh chỉnh VI~~ → **gộp vào B9**: VI duyệt ngay trên trang; đủ Duyệt là đóng băng | bản VI chốt | trang duyệt | ✋ | tập |
| B12 | Bảng shot, **từ cảnh dự kiến đã duyệt** | `bible/shots/<ep>.json` → `prompts/` | `build-prompts.mjs` | 🟢 | tập |

> **Cổng B9:** không câu nào mà bạn không chỉ được ra nó là 📖 danh lục, 👁 quan sát hay 🔬 giả thuyết.
> Soát trước khi sinh ảnh — script quyết định ảnh, sửa script sau khi có ảnh là đắt gấp mười.

**B2 · Nguồn có hai tầng.** IP còn sống (Pokémon, HP, LOTR, GoT) thì bám canon chặt và ghi nguồn
chính xác. Thần thoại, cổ tích, dân gian thì lỏng hơn — nhưng nhiều dị bản nên **phải ghi rõ chọn bản
nào**. Tập so sánh (rồng phương Đông vs phương Tây, Hydra vs Yamata no Orochi) chính là cách biến
mâu thuẫn dị bản thành nội dung thay vì giấu nó đi.

**B4 · Hai đường ngược nhau.**
- *Hình cố định* (Pokémon): hình có sẵn → suy ra câu chuyện.
- *Hình không cố định* (rồng, kỳ lân): **câu chuyện trước** → suy ra hình tượng cá thể (khiếm khuyết
  hay nét nổi bật trên ngoại hình) → rồi mới sinh ảnh.

**B5 · Không đặt tên.** Cá thể trung tâm = đặc điểm canon + mã thực địa (`Shiny Bulbasaur · K-01`); con khác gọi bằng tên loài. Tên tự đặt đã ping-pong bốn vòng ở tập 001 — bỏ hẳn tầng quyết định ấy. Tên canon (Smaug, Buckbeak) vẫn giữ nguyên.

**B10 · Luật mới, sinh ra từ multi-audio.** Một video, một dòng thời gian, hai track giọng — nên bản
dịch VI không được dài ngắn tuỳ ý. Mỗi beat có hạn mức thời lượng lấy từ bản EN; lệch quá ngưỡng thì
`check-episode.py` báo. Đây là **cái giá của việc gộp một kênh**, và là việc của máy chứ không phải
việc tay.

**B11 · Bẫy mất công.** Sau khi bạn tinh chỉnh VI, **bản VI đóng băng**. Sửa EN sau thời điểm đó rồi
dịch lại là xoá sạch phần bạn đã chỉnh — phải sửa tay cả hai bên. Đây là loại lỗi chỉ lộ ra ở tập thứ năm.

---

## C · Sản xuất tài sản

| # | Bước | Ra cái gì | Công nghệ | Auto | Nhịp |
|---|---|---|---|---|---|
| C1 | Sinh ảnh — **ảnh mẫu trước**, rồi cảnh; không tốn credit | `public/img/<ep>/*.jpg` | Google Flow (Nano Banana Pro) + Batch Studio | 🟡 | tập |
| C2 | Nhập ảnh, gỡ watermark | ảnh sạch | `handoff.py --take` (thay `import-flow.py`), `unwatermark.py` | 🟢 | tập |
| C3 | Chuyển động — **ba tầng, xem bảng dưới** | mp4 | tuỳ tầng | 🟡 | tập |
| C4 | Cảnh giải phẫu | ảnh nền xanh, xương, mạch năng lượng | `kind: "anatomy"` trong shot bible | 🟢 | tập |
| C5 | Trang sổ thực địa | giấy + hình vẽ, **chữ để trống** | `kind: "fieldnote"` + `el: "notepage"` | 🟢 | tập |
| C6 | Nhạc nền | `public/audio/music/` | `tools/build-music.py` — 20 đoạn cùng tông La thứ theo 10 chặng của khung tập · `import-music.py` cho nhạc sinh bằng Lyria / YouTube Audio Library · nạp bằng `/nap-am` | 🟢 | tập |
| C7 | Tiếng động, tiếng sinh vật | `public/audio/sfx/<ep>/` | `sfx.json` + `tools/build-sfx.py` — máy dựng bản tổng hợp ngay, người thay dần lớp giọng bằng file thật ([SOUND.md](SOUND.md)) · nạp bằng `/nap-am` | 🟡 | tập |
| C8 | Giọng EN | mp3 theo beat | **chưa chốt nhà cung cấp** | 🔴 | tập |
| C9 | Giọng VI, khít beat của bản EN | mp3 theo beat | VBee Pro | 🟡 | tập |
| C10 | Ảnh / video loài Trái Đất (≤ 2 mỗi tập) | `public/{img,video}/<ep>/earth-*` + `videos/<slug>/earth.json` | Pexels, Pixabay, NOAA/USFWS/NPS, Biodiversity Heritage Library | ✋ | tập |
| C11 | Nạp mọi file bàn giao vào đúng chỗ | ảnh, clip, giọng, tham chiếu, loài Trái Đất | `tools/handoff.py --take` (`/xong`) · âm thanh: `tools/intake.py` (`/nap-am`) | 🟢 | tập |

**C3 · Luật phân tầng chuyển động.** Trước giờ chưa ai viết ra:

| Loại cảnh | Công nghệ | Chi phí |
|---|---|---|
| Cảnh đứng, tĩnh | `creature-motion` (OpenCV) | miễn phí, offline |
| Sinh hoạt thường | Veo / Nano Banana | trong 25k token/tháng |
| Hành động | Topview (Seedance, MiniMax) | token riêng, dè xẻn |

Đã đo: một clip Veo trong Flow tốn **15 token** — 25k/tháng là hơn một nghìn clip, coi như không giới
hạn. Trần thật là thời gian duyệt, không phải token.

**C4 · Ranh giới giải phẫu.** Được: dạng X-quang mô phỏng phục vụ nghiên cứu — nền xanh, xương, mạch
năng lượng chạy trong thân; vết thương nhỏ trên da. Không được: máu me, nội tạng, mổ xẻ. Luật này đã
được sửa lại cho khớp ở `CLAUDE.md` và `IDEA-BANK.md` — bản cũ cấm rộng hơn ý thật.

**C5 · Vì sao chữ để trống.** `style.json` đang cấm `text` và `caption` vì AI sinh chữ ra ký tự méo,
tiếng Việt có dấu thì méo nặng hơn. Nên tách đôi: **AI sinh giấy và nét phác hoạ, chừa chỗ trống;
Remotion vẽ chữ viết tay lên**. Được ba thứ: chữ luôn đọc được, sửa lời không phải sinh lại ảnh, và
bản EN dùng chung y hệt tấm giấy — chỉ đổi lớp chữ.

**Đã bỏ: tách lớp parallax.** Bốn file trong `public/img/kanto-001/layers/` **không được tham chiếu ở
đâu trong `scenes.json`** — cắt tay xong rồi để đó. Với bảng phân tầng C3 thì việc này thừa. Giữ lại
trong `experiments/` làm ghi chép, không làm nữa.

---

## D · Hậu kỳ

| # | Bước | Ra cái gì | Công nghệ | Auto | Nhịp |
|---|---|---|---|---|---|
| D1 | Dựng hình từng beat — kể cả dừng hình và ảnh quê nhà | `scenes.json` | skill production · engine `specimen` + `video` / `callout.media` | 🟢 | tập |
| D2 | Timing ước lượng để xem trước | `timings.json` | `npm run scaffold` | 🟢 | tập |
| D3 | Timing thật theo giọng | `timings.json` | `npm run align` (whisper) | 🟢 | tập |
| D4 | Phụ đề EN + VI | `out/<slug>/*.srt` | `export-subs.py` | 🟢 | tập |
| D5 | Soát máy | báo cáo ✗/⚠ | `check-episode.py` | 🟢 | tập |
| D6 | **Soát người trên bản dựng, có tiếng, không tua** | ghi chú + toạ độ callout | công cụ dựng ở 0.8 | ✋ | tập |
| D7 | Render Long | mp4 | Remotion | 🟢 | tập |
| D8 | **Short làm riêng**: hook riêng, tiêu đề riêng | mp4 dọc | Remotion | 🟡 | tập |
| D9 | Thumbnail — **vài phương án**, hai ngôn ngữ | 1280×720 × 2 | `npm run thumb` | 🟡 | tập |
| D10 | Gói đăng: 3 tiêu đề, mô tả SEO, chapters, comment ghim, hashtag — hai ngôn ngữ | `videos/<slug>/PUBLISH.md` | skill `episode-publish` | 🟡 | tập |
| D11 | Sổ tài sản: ghi **từng file**, xem **theo tập** | manifest tập | sinh từ `prompts/<ep>.jsonl` | 🔴 | tập |

**D6 · Bước quan trọng nhất của cả cụm.** Nút thắt của kênh là duyệt, nên chỗ này đáng đầu tư công
cụ. Đã dựng: `PYTHONUTF8=1 python tools/review.py <slug>` mở một trang cục bộ có **hai mặt**, ghi ra
`videos/<slug>/review-notes.json`.

- **Trái · bản render.** Tạm dừng ở chỗ sai, gõ ghi chú → lưu kèm mốc thời gian và beat đoán được.
- **Phải · ảnh gốc.** Bấm lên ảnh → toạ độ callout đã chuẩn hoá.

Hai mặt tách nhau là **bắt buộc**, không phải cho đẹp: khung video đã bị `camera` zoom/pan nên bấm
lên đó không suy ngược ra được toạ độ trên ảnh gốc. Video cho biết *chỗ nào sai*, ảnh cho biết *toạ
độ bao nhiêu*. Gộp được việc "đo toạ độ callout" (~10 cái/tập) vốn là thuế tay nặng nhất.

Có công cụ mã nguồn mở cùng loại (FreeFrame, Clapshot) nhưng chúng là công cụ cho đội nhóm và chỉ
nhả ra *bình luận*, không ghi ngược được toạ độ vào `scenes.json`. Tự dựng rẻ hơn.

**D8 · Short là sản phẩm thật.** Lưu ý: Shorts có multi-audio nhưng **không có thumbnail theo ngôn
ngữ** — nên ảnh bìa Short phải không chữ, hoặc chọn một thứ tiếng.

---

## E · Phát hành và vận hành

| # | Bước | Ra cái gì | Công nghệ | Auto | Nhịp |
|---|---|---|---|---|---|
| E1 | Đăng video, **khai báo nội dung tổng hợp bằng AI** | video công khai | YouTube Studio | ✋ | tập |
| E2 | Nạp track giọng thứ hai + tiêu đề/mô tả/thumbnail bản địa hoá | video hai thứ tiếng | YouTube multi-audio | ✋ | tập |
| E3 | Sao lưu một chiều lên Drive | bản sao ngoài máy | `backup-episode.py` | 🟡 | tập |
| E4 | Đọc số → ra hành động (bảng dưới) | việc cần làm cho tập sau | YouTube Analytics | 🔴 | kỳ |
| E5 | Đính chính sau khi đăng | comment ghim | YouTube Studio | ✋ | — |
| E6 | **Quét mã nguồn mở xem có gì dùng được** | ghi chú công nghệ | tìm kiếm | 🔴 | kỳ |

**E4 · Số nào dẫn tới việc gì.** Không mở Analytics ngồi đọc — chỉ cần bảng này:

| Chỉ số yếu | Sửa cái gì |
|---|---|
| CTR thumbnail thấp | đổi thumbnail + tiêu đề |
| Tỉ lệ giữ chân tụt sớm | đổi hook, sửa kịch bản mở màn |
| Giữ chân tụt giữa bài | cắt đoạn thừa, xem lại nhịp beat |

**E3 · Đừng dùng Drive đồng bộ hai chiều.** Xoá nhầm dưới máy là Drive xoá theo. Phải là chép một
chiều theo tập. Nhóm cần cứu nhỏ hơn bạn tưởng — chỉ những gì **không tái tạo được**:

| Tái tạo được | Không tái tạo được → phải sao lưu |
|---|---|
| Ảnh chưa đo toạ độ (còn prompt là sinh lại được, không tốn credit) | **Ảnh đã đo toạ độ callout** — sinh lại ra ảnh khác là hỏng cả `scenes.json` |
| Timing, phụ đề (máy chạy lại) | Giọng đã duyệt bằng tai |
| Prompt (sinh từ `bible/`) | Nhạc đã chọn · lớp cắt tay |

Ảnh **đổi nhóm** đúng lúc D6 đo xong toạ độ. Đó là mốc để đẩy bản sao.

---

## Rà soát 2026-09-24 · bước nào đang ở đâu

Rà lại sau khi tập 001 đi hết vòng kịch bản V4 (năm vòng duyệt). Mỗi bước được xếp vào **đúng một** nhóm:

- **Một lần**: làm xong thì thôi. Còn mở thì là việc phải làm, không phải việc phải thiết kế.
- **Đã chốt**: có công cụ và có quy trình, mỗi tập chỉ việc chạy. Người chỉ duyệt.
- **Tự động một phần**: máy làm được một khúc. Ghi rõ khúc nào còn tay, và bước nhỏ tiếp theo nếu muốn đẩy thêm.
- **Còn mở**: chưa có lời giải, hoặc chưa quyết.

### Một lần

| # | Việc | Trạng thái |
|---|---|---|
| 0.4 · 0.5 · 0.7 · 0.8 · A1 | khung B · CREATURE-LENS · bốn skill · `review.py` · định vị | ✅ xong |
| — | trang duyệt + luồng kịch bản năm bước + DNA (`review-page.py`, `handoff.py --brief/--draft`, `dna_lint.py`) | ✅ xong trong đợt tập 001 |
| 0.6 | thư viện nhạc | 🟡 21 bản nguồn đã có ở `assets/music-src/`; **chưa chạy** `build-music.py` ra `public/audio/music/` và chưa chọn nền cho tập 001 |
| 0.9 | sao lưu Drive | 🔴 script có, **`CFG_BACKUP_DIR` chưa đặt**, chưa chạy thử. Ảnh vẫn chỉ nằm trên một máy |
| mới | **git remote** | 🔴 repo **không có remote**: cả phần chữ (kịch bản, bible, tool) cũng chỉ nằm trên một máy. Rẻ nhất, gấp nhất |
| mới | gộp engine | 🔴 `feat/specimen-freeze-media` (notepage · dừng hình · ảnh quê nhà · thẻ chương) **chưa vào `main` của engine**; kênh đang nối vào worktree |
| 0.1 · 0.2 | lập kênh, bật Advanced features | ✋ chưa làm, chặn multi-audio ([CHANNEL-SETUP.md](CHANNEL-SETUP.md)) |
| 0.3 | track gốc VI hay EN | ✋ chưa quyết (xem *Còn mở*) |
| mỗi loài | bible loài + ảnh tham chiếu | 🟡 một lần **cho mỗi loài**, không phải mỗi tập. Bài học Fearow: loài nào lên hình cũng phải có bible (DNA D12) |

### Đã chốt · chạy mỗi tập, người chỉ duyệt

| # | Bước | Chốt bằng |
|---|---|---|
| B0 | Gemini liệt kê sáu ý | `handoff.py --brief ideas` (hoặc `/nghi-y-tuong` nếu chỉ muốn nghĩ) |
| B5 | gọi cá thể: đặc điểm + mã, không đặt tên | luật + `check-episode.py` đối chiếu CAST |
| B6 | Claude dựng khung → Gemini viết EN + VI | `handoff.py --brief script`; **gộp luôn B10**: Gemini viết hai bản cùng nhịp |
| B7 | soát máy + chuẩn hoá | `handoff.py --draft` · `check-episode.py` · `voice_lint` · `dna_lint` (D1–D6, D13) |
| B9 | duyệt kịch bản + cảnh dự kiến | ✋ trang Artifact `db`: Duyệt / Cần sửa từng beat, Claude đọc lại được. **Gộp luôn B11**: bản VI được duyệt ngay trên trang |
| B9+ | góp ý lộ ra lỗi mới → đóng gói | `docs/DNA.md` (lỗi → luật → chỗ ép: brief · máy · checklist) |
| B12 | cảnh dự kiến → shot → prompt | `bible/shots` + `build-prompts.mjs`; ảnh mẫu trước, ảnh mẫu riêng cho mỗi con có mã |
| C2 · C11 | nạp file bàn giao, gỡ watermark | `handoff.py --take` (thay `import-flow.py`; bỏ qua ZIP cũ hơn ảnh đang có) · `unwatermark.py` |
| C4 · C5 | cảnh X-quang, trang sổ để trống chữ | `kind: anatomy / fieldnote` + element `notepage` |
| C10 | loài Trái Đất | luật: ≤3 dừng hình, ≤2 ảnh quê nhà, không sinh AI, ghi `earth.json`. Tải về là ✋ |
| D1–D5 · D7 | dựng, timing, align, phụ đề, soát máy, render | engine + `scaffold` / `align` / `export-subs.py` / `check-episode.py` |
| A3 | lịch | skill `episode-plan` |

### Tự động một phần

| # | Bước | Máy làm | Còn tay | Bước nhỏ tiếp theo |
|---|---|---|---|---|
| A2 | kho ý tưởng | `/nghi-y-tuong` chấm sáu ý | chọn | — (chọn là việc của người) |
| B1–B3 | khung · canon · loài đối chiếu | Claude đề xuất trong `2-skeleton.md` kèm nguồn | soát nguồn loài thật | — |
| B4 | bible loài + ảnh tham chiếu | Claude viết JSON, `refs.json` liệt kê ảnh cần tải | **tải ảnh tham chiếu** (bên thứ ba, người tải) | `check-episode` đã báo loài thiếu bible |
| C1 | sinh ảnh | prompt + tờ batch (`out/flow/…`, nút "Tạo script batch" trên trang) | chạy Batch Studio, tải ZIP. **Không tốn credit**: sai thì sinh lại | tự chạy batch qua CDP như `animate_flow_cdp.py` đang làm cho clip |
| C3 | chuyển động | tầng 1 `creature-motion` + `motion-studio.py` (khoanh vùng bằng chuột); tầng 2 Veo qua `animate_flow_cdp.py` | Seedance (tầng 3), duyệt clip | soát `animate_flow_cdp.py` còn chạy với Flow hiện tại không |
| C6 | nhạc | `build-music.py` 20 đoạn theo chặng | chọn nền | chạy lần đầu (xem 0.6) |
| C7 | tiếng động | `sfx.json` + `build-sfx.py` dựng bản tổng hợp | thay dần lớp giọng sinh vật bằng file thật | — |
| C9 | giọng VI | `out/<slug>/script-tts.txt`, nạp mp3 bằng `--take`, `align` | dán từng beat vào VBee, nghe duyệt | ⚠ `public/audio/kanto-001-bulbasaur/` đang là bản thu **V3** (còn beat 11b, 16, 17): V4 phải thu lại |
| D6 | soát bản dựng | `review.py`: ghi chú theo mốc + toạ độ callout | xem có tiếng, không tua | — |
| D8 · D9 | Short · thumbnail | engine dựng, `npm run thumb` | chọn hook, chọn phương án | — |
| D10 | gói đăng | skill `episode-publish` | duyệt | **chưa chạy thật lần nào** (chưa có `PUBLISH.md`) |
| E3 | sao lưu | `backup-episode.py` | chọn thư mục Drive | xem 0.9 |

### Còn mở

| # | Việc | Loại | Đề xuất |
|---|---|---|---|
| C8 | **giọng EN** | quyết + tiền | chặn bản EN của mọi tập. Ba đường: trả ElevenLabs · đổi nhà · ra EN sau VI. Nên chốt trước khi thu VI tập 001, vì bản VI phải khít nhịp EN |
| 0.3 | track gốc VI hay EN | quyết | khó đổi sau khi đã đăng tập đầu |
| A4 | giờ người mỗi tập | đo | **đo được rồi, rẻ**: trang duyệt ghi mốc giờ từng lần bấm. Vòng 5 tập 001 duyệt 16 beat trong ~10 phút, duyệt lại 6 beat trong ~2 phút. Ghi mốc vào `4-review.md` mỗi vòng |
| A5 | rà IP + ngưỡng rẽ nhánh | kỳ | bảng rà trong SLATE còn trống. Chưa có kênh thì chưa có gì để rà; đặt **ngưỡng sub** ngay |
| D11 | sổ tài sản | tool | sinh từ `prompts/*.jsonl` + `earth.json` + `CREDITS`; chỉ giấy phép nhạc và tiếng là tay |
| E4 | đọc số → hành động | kỳ | chờ có kênh; bảng quy đổi ở trên là đủ |
| E6 | quét mã nguồn mở | kỳ | — |
| — | ranh giới IP với HP / LOTR / GoT | quyết | chưa tới lúc |

**Đếm nợ thật** (🔴 không kể ✋): git remote · sao lưu Drive · gộp engine · sổ tài sản · giọng EN. Ba
việc đầu là việc một lần, mỗi việc dưới một giờ. Nên làm trước khi tập 001 có giọng và toạ độ callout,
vì đó là những thứ đầu tiên **không tái tạo được**.

---

## Phụ lục · bê gì từ `semantix-docs`

`D:\Users\tuanla2\semantix-docs\.claude\skills\` có sẵn thứ đã chạy thật:

| Skill | Vá bước nào | Sửa gì khi bê sang |
|---|---|---|
| `content-plan` | `A3` | Hay ở chỗ **không giữ lịch riêng** mà quét trạng thái thật từ file rồi đối chiếu slate. Giữ nguyên cách đó, đổi đường dẫn. |
| `content-check` + `stop-slop` | `B7` `B8` | **Cắt 3 luật của stop-slop** — xem dưới. |
| `content-publish` | `D10` `E1` | Giữ khuôn `<slug>.PUBLISH.md` và guardrail "không tự đăng/render". Bỏ phần OAuth. |

**Ba luật của `stop-slop` phải cắt, vì chúng chống lại giọng kênh này:**

1. *"Every sentence needs a human subject doing something"* — kênh cố ý lấy **con vật** làm chủ ngữ,
   người chỉ đứng ngoài quan sát. Luật này đảo ngược đúng định vị A1.
2. *"Put the reader in the room, 'You' beats 'People'"* — người dẫn ngồi trong lều quan sát, xưng
   "tôi", không gọi "bạn". Xưng hô kiểu đó phá khung phim tài liệu.
3. *"Cut quotables"* — phim tài liệu thiên nhiên sống bằng câu kết.

Phần còn lại của `stop-slop` giữ được, và giờ còn hợp hơn trước: nó được viết cho **văn tiếng Anh**,
mà từ nay bản gốc của kênh là tiếng Anh.

`content-publish` cũng đã dò sẵn tường của việc đăng tự động, ghi lại đây để khỏi dò lại:
`videos.insert` tốn 1600 unit, quota 10k/ngày → tối đa 6 video/ngày (nhịp 2 tập/tuần không chạm trần).
Tường thật là: app ở chế độ **Testing thì refresh token hết hạn sau 7 ngày** và video bị khoá private
tới khi app được Google verify. Nên `E1` đăng tay là lựa chọn đúng cho tới khi nhịp tăng.
