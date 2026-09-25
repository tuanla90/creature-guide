# AGENTS.md · đọc file này trước tiên

Đây là "README cho AI": trợ lý nào (Claude, Gemini, Codex, Cursor, Copilot…) vào dự án cũng đọc file này
trước, rồi theo **bản đồ đọc** bên dưới để biết đọc gì tiếp. `CLAUDE.md` và `GEMINI.md` chỉ nhúng file
này và thêm phần riêng của từng công cụ. Có luật chung mới thì sửa **ở đây**, không sửa ở hai file kia.

**Dự án:** kênh YouTube *Creature Field Guide*, phim tài liệu tự nhiên về sinh vật hư cấu (bắt đầu bằng
Pokémon), dựng bằng Remotion qua engine `blog2video`. Mỗi tập làm **hai bản Việt và Anh** trên cùng một
video (YouTube multi-audio).

---

## 1 · Vào phiên: bốn bước, theo đúng thứ tự

1. Đọc hết file này.
2. `git pull`, rồi xem tập đang ở đâu: `PYTHONUTF8=1 python tools/handoff.py <slug>`. Tập đang làm là
   `kanto-001-bulbasaur`; lịch các tập ở [docs/SLATE.md](docs/SLATE.md).
3. Đọc `videos/<slug>/drafts/4-review.md`. Đây là nhật ký các vòng duyệt, **vòng mới nhất nằm cuối file**:
   quyết định gần nhất và việc còn treo đều ở đó.
4. Đọc [docs/DNA.md](docs/DNA.md): mọi lỗi từng lọt qua duyệt, mỗi lỗi kèm luật và chỗ ép luật ấy.

## 2 · Bản đồ đọc theo việc

| Bạn đến để… | Đọc |
|---|---|
| Hiểu toàn cảnh, biết chỗ nào còn làm tay | [README.md](README.md) · [docs/BUSINESS-FLOW.md](docs/BUSINESS-FLOW.md) (mục *Rà soát* ở cuối) |
| Làm một tập từ đầu đến cuối | [docs/PIPELINE.md](docs/PIPELINE.md) (mười một chặng) · [docs/HANDOFF.md](docs/HANDOFF.md) (từ khoá "xong", luật đặt tên file) |
| Viết hoặc sửa lời dẫn | [docs/NARRATOR.md](docs/NARRATOR.md) · [docs/VOICE.md](docs/VOICE.md) · [docs/DNA.md](docs/DNA.md) · [docs/CAST.md](docs/CAST.md) · [docs/briefs/core.md](docs/briefs/core.md) |
| Nghĩ ý tưởng, chọn góc | [docs/IDEA-BANK.md](docs/IDEA-BANK.md) · [docs/CREATURE-LENS.md](docs/CREATURE-LENS.md) · [docs/EPISODE-FRAME.md](docs/EPISODE-FRAME.md) · [docs/competitor-research.md](docs/competitor-research.md) |
| Soát kịch bản trước khi sinh ảnh | `.claude/skills/episode-review/SKILL.md` · [docs/DNA.md](docs/DNA.md) |
| Hình: cảnh, ảnh mẫu, trang sổ | [docs/SCENE-TYPES.md](docs/SCENE-TYPES.md) · [docs/JOURNAL-STYLE.md](docs/JOURNAL-STYLE.md) · `bible/style.json` · `bible/shots/<ep>.json` |
| Clip (Veo / Seedance) | `bible/clips/<ep>.json` → `node tools/build-motion-prompts.mjs <ep>` |
| Âm thanh, nhạc | [docs/SOUND.md](docs/SOUND.md) |
| Sang máy mới, sao lưu | [docs/BACKUP.md](docs/BACKUP.md) |
| Sửa engine dựng video | repo `blog2video`, nhánh `feat/specimen-freeze-media` (xem *Gotcha*) |

## 3 · Luật của kênh, không thương lượng

- Người dẫn là **Dr. Holth**, nhà sinh vật học thực địa của *thế giới chúng ta*
  ([docs/NARRATOR.md](docs/NARRATOR.md)). Xưng "tôi", **không bao giờ nói tên mình**; tên chỉ hiện bằng chữ
  trên bìa sổ và chữ ký. ⛔ **Không bao giờ hiện "Gilbert"**: "Gilbert D. Holth" là đảo chữ của "Blight
  Lord". "Tuấn La" **không xuất hiện trong video**, chỉ ở mô tả YouTube.
- Không nhắc game, không nhắc AI, không nhắc đoàn làm phim. Pokédex gọi là "cuốn danh lục". Tên đòn,
  tên hệ, tên nguồn game không lên lời dẫn và không lên hình.
- Ba nhãn bằng chứng không được trộn: 📖 danh lục (phải có nguồn trong `NGUON`) · 👁 quan sát · 🔬 giả
  thuyết (phải kèm một loài có thật ở Trái Đất).
- **Cảnh đổi hình không có lột da.** Chỉ sưng nở, sức nặng, ánh sáng, bóng dáng, dấu vết.
- Mọi khả năng phải nêu **cái giá** của nó.
- **Không đặt tên riêng cho con vật.** Cá thể trung tâm = đặc điểm canon + mã thực địa
  (`Shiny Bulbasaur · K-01`). Đặc điểm chỉ được gọi **sau khi** khán giả đã thấy nó.
- Địa danh phải có dẫn chứng canon; **không bịa** khi canon đã có.
- Giải phẫu chỉ theo lối nghiên cứu: X-quang mô phỏng, nền xanh, xương, mạch năng lượng. Không máu me,
  không nội tạng, không mổ xẻ. Cảnh ghép đôi dừng ở phô diễn, làm tổ, chăm con.
- Con số vật lý chỉ là ước lượng suy từ canon, có `~` và 🔬; lời dẫn tối đa hai con số cả tập (DNA D15).

## 4 · Cách làm việc

- **Luôn** chạy `PYTHONUTF8=1 python tools/check-episode.py <slug>` trước khi thu giọng hoặc render.
- Luồng kịch bản năm bước: Gemini liệt kê ý → Claude dựng khung → Gemini viết lời → Claude chuẩn hoá →
  người duyệt trên trang. Bản dán cho Gemini ghép bằng `tools/handoff.py <slug> --brief ideas|script`,
  **không viết tay**. Không tin mục SELF-CHECK của Gemini: soát lại bằng `handoff.py --draft`.
- Góp ý duyệt lộ ra lỗi mới thì **đóng gói vào [docs/DNA.md](docs/DNA.md)** (lỗi → luật → chỗ ép: brief · máy
  · checklist), không chỉ sửa chữ rồi thôi.
- **Không tự đăng, không tự render bản cuối, không tự tải lên.** Sinh ảnh Flow không tốn credit; clip
  Veo / Seedance thì phải hỏi trước.
- Ảnh tham chiếu (`bible/refs/**`) là ảnh của bên thứ ba: chỉ dùng để tham chiếu, không đăng, không đưa
  vào git.
- Engine `blog2video` là repo **công khai**: không đưa nội dung Pokémon sang đó.
- Git: làm trên nhánh hoặc worktree rồi fast-forward `master`, rồi push `origin`
  (`github.com/tuanla90/creature-guide`). Thư mục chính có sửa dở thì cất vào một nhánh `wip/…`, **đừng
  stash, đừng ghi đè**.

## 5 · Bố cục

```
AGENTS.md          file này · CLAUDE.md / GEMINI.md nhúng nó
videos/<slug>/     content.py (lời VI + EN, NGUON) · scenes.json (hình) · thumb.json · timings.json
                   drafts/ (luồng năm bước · 4-review.md · 4-scene-plan.json · 5-review.html/.md)
bible/             style.json · creatures/<loài>.json · shots/<ep>.json · clips/<ep>.json
                   locations/<nơi>.json · refs/<loài>/refs.json   (ảnh tham chiếu KHÔNG nằm trong git)
prompts/           sinh ra từ bible, đừng sửa tay
public/            img/<ep>/ · video/<ep>/ · audio/…   (ảnh, clip, âm KHÔNG nằm trong git → docs/BACKUP.md)
docs/              xem bản đồ đọc ở mục 2
tools/             handoff.py · check-episode.py · dna_lint.py · voice_lint.py · review-page.py
                   build-prompts.mjs · build-motion-prompts.mjs · unwatermark.py · backup-all.py …
```

## 6 · Gotcha hay cắn

- Console Windows là cp1252 → mọi lệnh Python phải có `PYTHONUTF8=1`.
- Viết script bằng heredoc trong shell mà có `\n` hay chữ Việt trong mẫu `sed` là dễ hỏng: dùng công cụ
  ghi / sửa file.
- Sửa `content.py` thì phải `npm run scaffold -- <slug>` rồi `python tools/export-subs.py <slug>`.
- `_note` trong `scenes.json` **không được chứa dấu ngoặc kép**.
- Toạ độ callout đo **trên ảnh thật**, sau khi ảnh đã chốt. Sinh lại ảnh là phải đo lại.
- Render chết ở `SELF_SIGNED_CERT_IN_CHAIN` là do mạng công ty chặn TLS: đặt biến `CHROME` trỏ tới
  Chrome đã cài (`remotion.config.ts` có sẵn móc).
- Google Flow: pane trình duyệt bị ẩn thì tab treo, mọi ảnh báo "Failed to load image". Batch Image
  Studio Pro V3.0 có *thư viện ref*: SDK không tìm được ảnh trong project theo tên, nên ảnh cũ phải gán
  một lần bằng nút *Gán ảnh* ([docs/PIPELINE.md](docs/PIPELINE.md) chặng 7).
- Engine đang nối vào worktree `blog2video/.claude/worktrees/specimen-media` (nhánh
  `feat/specimen-freeze-media`), **chưa gộp vào `main`, chưa lên GitHub**. Bản sao nằm trong gói sao lưu
  (`git/blog2video.bundle`). Sửa engine xong phải chạy `node scripts/build-lib.mjs` bên đó.
