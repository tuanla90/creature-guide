# DNA của kênh · bài học rút từ các vòng duyệt

Mỗi lần người duyệt chỉ ra một lỗi, lỗi ấy phải thành **một luật có chỗ ép**, để tập sau không vấp lại.
File này gom các luật ấy. Mỗi mục ghi rõ nó được ép ở đâu:

- **B** · bản giao Gemini ([briefs/core.md](briefs/core.md), mục *Lessons from review*), để lỗi không
  sinh ra ngay từ bản nháp;
- **M** · bộ soát máy: `tools/dna_lint.py` (mã D…), `tools/voice_lint.py`, `check-episode.py`,
  `handoff.py --draft`;
- **R** · checklist của skill [`episode-review`](../.claude/skills/episode-review/SKILL.md), mục 1.8,
  cho những thứ máy không đọc ra.

Máy bắt được thì để máy bắt. Chỉ những gì cần mắt người mới nằm ở checklist.

**Thêm một bài học mới:** viết một mục ở đây (lỗi → luật → chỗ ép). Nếu bắt được bằng mẫu chữ thì
thêm vào `TERMS` trong `dna_lint.py`. Nếu là luật viết thì thêm một dòng vào mục *Lessons* của
`core.md`. Còn lại thì thêm một ô vào mục 1.8 của `episode-review`. Ghi vòng duyệt vào
`drafts/4-review.md` của tập.

---

## D1 · Chữ canon: gọi đúng tên thứ game đã đặt

| Lỗi đã gặp (tập 001) | Luật | Ép ở |
|---|---|---|
| "hai **nết**" | Ability gọi là **đặc tính**, vì game thủ Việt quen gọi thế. EN: *trait*. | M `TERMS` · B |
| Một con mang cả Chlorophyll lẫn Overgrow | **Mỗi cá thể mang một đặc tính.** Loài có hai (hay ba, kể cả đặc tính ẩn) thì kể là "người ta kể về hai đặc tính ở loài này", và gắn mỗi đặc tính với **một con khác nhau**. | B · R |
| "những cú đánh bỗng mạnh lên" | Nói đúng **phạm vi** canon. Overgrow chỉ tăng **đòn hệ Cỏ**, nên phải nói "những đòn dùng dây leo và năng lượng của củ", không phải mọi cú đánh. | B · R |
| "cái **nhụy**" giữa hoa Venusaur cái | Canon chỉ vẽ ra một thứ, không gọi tên nó. Tả đúng cái được thấy: "một **cấu trúc nhỏ giống hạt**" (*seed-like structure*). Đừng nâng một nét vẽ lên thành một thuật ngữ thực vật. | M `TERMS` · B |
| — | Màu Shiny **giữ qua đổi hình**, nhưng mỗi dạng có bảng màu riêng: Shiny Ivysaur có nụ vàng. Tra màu của từng dạng. | R |

## D2 · Dè dặt: mắt thấy thì nói thấy, đầu nghĩ thì nói ngờ

Lỗi đã gặp: "thứ vừa cứu mạng nó **đã phải trả** bằng chính cái kho…" và "tôi thấy cả một kho nắng bị
tiêu sạch". Người kể không nhìn được vào trong củ.

**Luật:** câu nào nói về cơ chế bên trong (kho, dự trữ, tiêu, cạn) mà không phải trích danh lục thì
là 🔬, và phải có chữ rào: *tôi ngờ rằng · có lẽ · tôi không chứng minh được, nhưng…* Câu 👁 chỉ tả
được cái mắt thấy: củ xẹp, con vật nằm lâu hơn, bước chậm hơn.

Ép ở **M** (`lint_hedge`, mã D2) và **B**.

## D3 · Chữ theo giai đoạn: hạt · củ · nụ · hoa

Lỗi đã gặp: "cái hạt" được dùng lẫn với "cái củ" suốt tập, nên người xem không biết mình đang nhìn
cái gì.

**Luật:** chữ của câu hỏi xương sống ("con thú nuôi **cái hạt**, hay cái hạt nuôi con thú?") là chữ
**dành riêng**. Chỉ dùng nó ở ba chỗ: câu hỏi xương sống, câu trích danh lục, và beat cuối. Mọi chỗ
khác gọi theo thứ đang hiện trên hình: **củ** (Bulbasaur), **nụ** (Ivysaur), **hoa** (Venusaur).

Ép ở **M**: `content.py` khai `RESERVED = {"hạt": "củ · nụ · hoa"}` và `SPINE_KEY`, còn `lint_reserved`
(mã D3) bắt những chỗ dùng sai. Tập khác khai chữ riêng của loài mình (ví dụ "ngọn lửa" của
Charmander).

## D4 · Giữ chân: sự cố sớm, câu hứa cuối hồi 1

Lỗi đã gặp: mối nguy đầu tiên (Fearow) tới ở phút thứ 6,5. Suốt sáu phút đầu chỉ có quan sát, và
người xem không có lý do nào để ở lại.

**Luật:**
- **Sự cố đầu tiên trước phút thứ 4.** Không cần là trận chiến. Một cái bóng lướt qua, một lần hụt
  chân cũng tính, miễn là con vật gặp nguy. Đánh dấu `"incident": true` ở beat đó trong
  `4-scene-plan.json`.
- **Câu hứa ở cuối hồi 1** (trong 30% đầu tập): một câu báo trước cái sẽ tới mà không nói hết. Ví
  dụ ở tập 001: *"Nhưng màu da khiến tôi nhận ra nó giữa cả đàn cũng sẽ khiến một thứ khác nhận ra
  nó."* Đánh dấu `"promise": true`.

Ép ở **M** (`lint_story`, mã D4: ước thời điểm theo 3,3 tiếng/giây, cộng quãng đen của thẻ chương)
và **B**.

## D5 · Cài thì phải trả; con có mã phải quay lại

Lỗi đã gặp: Fearow tấn công mà không có gì báo trước. K-04 có mã nhưng biến mất trước khi K-01 đổi
hình, nên cuộc tái ngộ người xem chờ không bao giờ tới.

**Luật:**
- Mọi mối nguy lớn phải được **cài** trước ít nhất một beat: cái bóng, tiếng kêu, một dấu vết. Trong
  plan, ghi `"sets": ["<khoá>"]` ở beat cài và `"pays": ["<khoá>"]` ở beat trả. Máy báo chỗ cài
  không trả, trả không cài, và trả trước khi cài.
- Mọi con có mã (K-04…) phải có mặt ít nhất hai lần, và **quay lại sau lần cá thể trung tâm đổi
  hình** (plan đánh dấu `"change": true`). Cuộc tái ngộ nên **lặp lại một bố cục cũ** (tập 001:
  khoảng cách hai thân) để người xem tự nhận ra điều đã thay đổi.

Ép ở **M** (`lint_story`, `lint_codes`, mã D5) và **R**.

## D6 · Màu: một chữ, đúng canon, dùng suốt

Lỗi đã gặp: "xanh lam lốm đốm", trong khi Bulbasaur thường có màu **xanh lục lam** (teal).

**Luật:** tra màu canon của từng dạng, chọn **một** chữ, ghi vào `bible/creatures/<loài>.json`, và
dùng đúng chữ ấy suốt tập. Đừng rút gọn màu.

Ép ở **M** (`TERMS`, mã D6; thêm mẫu khi gặp màu mới) và **R**.

## D7 · Lời mở màn phải khớp với hình mở màn

Lỗi đã gặp: lời nói củ "phồng lên xẹp xuống **đều đặn như một lồng ngực**", còn ý của cảnh (và clip
thở) lại là củ thở **lệch nhịp** với lồng ngực. Chính cái lệch mới là điều lạ, là cái móc.

**Luật:** câu móc phải nói đúng điều **lạ** mà hình cho thấy, không nói điều bình thường. Soát câu
đầu tiên cạnh cảnh đầu tiên trên trang duyệt.

Ép ở **R**.

## D8 · Mỗi mẹo dùng một lần

Lỗi đã gặp: beat 00 "tưởng nó đã chết", rồi beat 03 "tưởng đã lạc mất nó". Cả hai là cùng một mẹo:
người kể nhầm vì con vật nằm quá im.

**Luật:** mỗi mẹo kể chuyện (người kể nhầm, tưởng chết, lạc mất, một con số gây sốc) chỉ dùng **một
lần** mỗi tập. Lần thứ hai thì cắt, hoặc đổi sang mẹo khác.

Ép ở **R**.

## D9 · Hình không được trông giống lúc đổi hình

Lỗi đã gặp: cảnh phun bột viết là "đỉnh củ **hé mở**, một làn bột tung ra". Trên hình, cảnh ấy rất dễ
trông như cái nụ đang nở, tức là như đang đổi hình, trong khi đổi hình là cao trào của hồi 6.

**Luật:** hành động nào trước lần đổi hình cũng không được có những nét của lần đổi hình: củ mở ra,
sáng lên, phồng to, bóng dáng đổi khác. Bột thì phụt ra **từ khe giữa các bẹ**, còn củ giữ nguyên
hình. Viết điều đó thẳng vào `scene` của shot.

Ép ở **R** (soát shot trước khi sinh ảnh).

## D10 · Giọng văn

Tám luật trong [VOICE.md](VOICE.md): cảnh trước, cầu nối, nhịp một câu thong thả một câu gọn, tả rồi
mới làm, đại từ có chủ, dựng từ lạ, mã có nghĩa, không kịch.

Ép ở **M** (`voice_lint.py`: câu ngắn, câu dài, "chúng" không chủ, từ cộc, so sánh chồng, cầu nối ở
chỗ đổi hồi) · **B** (Narration craft 1–8) · **R** (đọc to).

## D11 · Beat giới thiệu phải gọn

Lỗi đã gặp: beat 01 (vì sao theo con này, mã K-01 là gì) dài gần 30 giây, nằm ngay sau câu móc, và
làm nguội cái móc.

**Luật:** beat giới thiệu **≤ 20–25 giây**: câu hỏi, lựa chọn, ý nghĩa của mã. Bỏ ví dụ và bỏ câu kết
nói lại điều đã nói.

Ép ở **R**. Nếu tái diễn thì thêm vào `dna_lint`.

## D13 · Chữ tổng quát, không chữ tự chế

Lỗi đã gặp (vòng 5): "tiêu nắng" và cột sổ "thu, và chi". Đó là những chữ người kể tự chế ra, và
người xem phải dừng lại để giải nghĩa.

**Luật:** gọi bằng chữ tổng quát, ai nghe cũng hiểu ngay: **tiêu hao năng lượng**, **năng lực · cái
giá phải trả**. Ẩn dụ sổ sách (thu, chi, lãi, lỗ) không dùng làm khung cho tập.

Ép ở **M** (`TERMS`, mã D13) và **B**.

## D14 · Điều lạ nào cũng cần một lẽ, và đoán thì phải có căn cứ

Lỗi đã gặp (vòng 5):
- Beat 04 nói nó không bao giờ uống nước, rồi bỏ lửng. Nêu điều lạ thì phải đưa kèm một giả thuyết:
  nước đi lên qua bàn chân ngập trong bùn.
- Beat 06 nói bảy con phải sống chung một trảng cỏ, nhưng không nói vì sao. Hành vi bầy đàn nào cũng
  cần **lý do sinh thái**: đây là khoảng nắng trống duy nhất; một con rạp xuống thì cả đàn rạp theo.
- Beat 13 để người kể "tin rằng nó tìm đến để chết", trong khi không có căn cứ nào cho chuyện đó.
  Người kể được phép sai, nhưng cái sai phải **có lý do**. Không có lý do thì để người kể **tò mò**
  và đặt câu hỏi.

**Luật:** nêu một điều lạ thì kèm một lẽ (📖, hoặc 🔬 có rào). Người kể chỉ đoán điều mình có căn cứ
để đoán.

Ép ở **R** và **B**.

## D15 · Con số vật lý: được nói, nhưng chỉ khi tính ra được

Nguồn: nghiên cứu đối thủ + CREATURE-LENS trục 17 (2026-09-25). Luật cũ cấm hẳn số; nay chốt lại.

**Luật:** số lực / năng lượng / công suất chỉ được dùng khi **suy từ chiều cao, cân nặng canon**, luôn
viết là ước lượng (`~`, "khoảng", "about"), gắn 🔬, và **cách tính ghi trên trang sổ**. Lời dẫn nói **tối
đa hai con số cả tập**, ưu tiên dạng quy đổi cảm được ("cả một buổi sáng nắng, tiêu trong nửa giây").
Không phần trăm, không chỉ số.

Ép ở **M** (`lint_numbers` mã D15 trong lời dẫn; `handoff.py --draft` nhận số có `~` trong ghi chú trang
sổ, số không `~` vẫn là lỗi) và **B** (luật cứng 4).

## D16 · Chữ trên hình không mang tên game

Lỗi đã gặp (spec trang sổ mẫu): nhãn `VINE WHIP: ~6J`, nguồn `Bulbapedia · Gen I` ghi ngay trên trang.

**Luật:** trang sổ, nhãn, chú thích tả **việc cơ quan làm** (`VINE STRIKE`, `BEAM`). Nguồn thật
(Bulbapedia, bản game) chỉ nằm trong `NGUON`; trên trang ghi `📖 danh lục`. Ba dấu 📖 👁 🔬 vẽ tay bằng
mực sepia, không phải emoji ([JOURNAL-STYLE.md](JOURNAL-STYLE.md) mục G).

Ép ở **M** (`lint_onscreen` mã D16 quét mọi trường chữ trong `scenes.json`) và **B**.

## D17 · Mở tập bốn shot, hai shot đầu không lời

**Luật** ([SCENE-TYPES.md](SCENE-TYPES.md)): shot 1 establish (cực rộng hoặc cực cận, chưa thấy con vật) ·
shot 2 reveal · shot 3 chi tiết / câu móc — **lời vào ở đây** · shot 4 thẻ tên loài. Thẻ tên chỉ ghi loài +
nơi; mã và chữ Shiny hiện khi lời đã giải nghĩa và khán giả đã thấy màu (luật CAST).

Ép ở **M** (`lint_opening_guests` mã D17: hai cảnh đầu của beat mở phải có `"silent": <giây>` trong plan).
Engine cần hỗ trợ khoảng im lặng đầu beat.

## D18 · Loài khách có vai sinh thái

**Luật:** mỗi tập 2–4 loài khách, mỗi loài một vai: **predator · prey · competitor · mutualist**. Kẻ săn
không có mã. Loài tương hỗ quay lại quá hai lần thì cho mã. Khai trong plan: `"guests": [{species, role}]`.

Ép ở **M** (mã D18) và **R**.

## D19 · Trang sổ: một tấm giấy, hai ngôn ngữ

Rủi ro chỉ ra khi rà SCENE-TYPES (2026-09-25): trang sổ dùng chung ảnh nhưng vẽ chữ hai thứ tiếng, và
chưa có giới hạn chữ, chưa có ngữ pháp diagram, `chip` phát sáng lại va với trang vẽ tay.

**Luật** ([SCENE-TYPES.md](SCENE-TYPES.md) các mục *Style bắt buộc*, *Diagram khoa học*, *Bằng chứng và
tham chiếu*, *Giới hạn chữ trên trang sổ*): mọi chữ khai `{vi, en}` và giới hạn tính theo bản dài hơn · note
≤ 80 ký tự, ≤ 5 mỗi trang (trang đôi ≤ 8) · nhãn IN HOA ≤ 22 ký tự, ≤ 6 mỗi trang · số có `~` · diagram chỉ
trong 7 kiểu · tham chiếu chỉ `page:<n>` / `species:<loài>` / `catalogue` · `chip` không lên trang sổ, bằng
chứng là `mark` vẽ tay · chữ không đè `keepout`.

Ép ở **M** (`lint_notepage` mã D19, quét `scenes.json`) và **R** (chữ có đè hình không, 9:16 có đọc được không).

## D12 · Bàn giao và công cụ

| Lỗi đã gặp | Luật | Ép ở |
|---|---|---|
| Ảnh giữ chỗ (khung xám) được tính là "đã có ảnh" | Ảnh giữ chỗ không phải là ảnh | M `imgcheck.py` |
| Tin mục SELF-CHECK của Gemini | Không tin. Chạy `handoff.py --draft` (có cả DNA D1, D2) rồi đọc bằng mắt | M · R |
| Số đo bịa trong ghi chú trang sổ ("2.1 m/s") | Trang sổ chỉ ghi quan sát, không ghi số đo | M `--draft` |
| Ảnh AI của loài Trái Đất | Không sinh. Dừng hình ≤ 3, ảnh quê nhà ≤ 2, nguồn sạch ghi trong `earth.json` | M `check-episode` |
| Loài phụ chỉ có một dòng `extraCreatures` → Flow vẽ ra chim thật (ảnh mắt đục Fearow: mỏ dày có rãnh, đầu trọc) | Loài nào **lên hình** cũng phải có `bible/creatures/<loài>.json` (dáng đầu, mỏ, mào, `forbidden` chặn các loài thật nó dễ bị nhầm), một ảnh mẫu, và một ảnh tham chiếu | R · shot bible |
| Viết script Python bằng heredoc có `\n` hoặc chữ Việt trong mẫu `sed` | Dùng tool Write/Edit; khớp chữ Việt trong Python file, không trong `sed` | (ghi cho Claude) |
