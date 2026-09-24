# Bảng nhân vật · Cast sheet

Kênh làm **hai bản: tiếng Việt và tiếng Anh** trên cùng một video. Luật:

1. **Không đặt tên riêng cho con vật.** Cá thể trung tâm gọi bằng **đặc điểm canon + mã thực địa**:
   `Shiny Bulbasaur · K-01`. Mọi con khác gọi bằng **tên loài**: "một con Fearow", "con Venusaur cái
   già". Vì sao:
   - Tên tự đặt đã ping-pong bốn vòng ở tập 001 (Búp Lệch → Saur → Crookedbud → chưa chốt), và vòng
     nào cũng kéo theo sửa kịch bản, CAST và luật.
   - "Shiny" và "K-01" **giống hệt nhau ở hai thứ tiếng** — không phải dịch, không phải chia "màn hình
     tên EN / giọng tên VI", VBee không phải đọc tên tự bịa.
   - Đặt tên là một kiểu sở hữu; mã số là quan sát. Dr. Holth là nhánh *buông* (xem
     [NARRATOR.md](NARRATOR.md)).
2. **Đặc điểm của cá thể trung tâm lấy từ canon, ưu tiên Shiny.** Chốt một đặc điểm duy nhất, ghi vào
   `bible/creatures/<loài>.json` → `individuals.<mã>.trait`. Loài không có Shiny đáng kể thì chọn một
   đặc điểm canon khác nhìn thấy được.
3. **Đặc điểm chỉ được gọi ra sau khi khán giả đã thấy nó.** Chữ "Shiny" chỉ được nói sau cảnh cho
   thấy màu khác thường. Nói trước khi thấy là chữ rơi vào hư không.
4. **"Shiny" là từ của người bản xứ, không phải thuật ngữ game.** Người trong thế giới Pokémon vẫn gọi
   những con khác màu như thế. Xử lý như Pokédex → "cuốn danh lục": nói **một lần** như cách người
   bản xứ gọi (*"người ở đây gọi những con khác màu như vậy là shiny"*), sau đó dùng mã thực địa.
   Cần `PRON` cho VBee: "Shiny" → "sai-ni".
5. **Con thứ yếu gọi bằng tên loài.** Chỉ khi một con thứ yếu **quay lại nhiều lần** và dễ lẫn với
   con cùng loài thì mới cho nó một mã thực địa (`K-04`) — vẫn không đặt tên. Mã thì không cần dẫn chứng.
6. **Địa danh vẫn phải có dẫn chứng canon** — không bịa địa danh khi canon đã có. Xem
   `bible/locations/`.
7. **Người kể là Dr. Holth, và không có tên trong lời đọc.** Ông xưng "tôi" và chỉ thế. Tên chỉ hiện
   bằng chữ trên bìa sổ và chữ ký trang ghi chép — **chỉ `Dr. Holth`, không bao giờ "Gilbert"**.
   **Tuấn La không xuất hiện trong video**, chỉ ở mô tả YouTube.

## Kanto #001–003 · dòng Bulbasaur

| Vai | Gọi là (cả hai bản) | Đặc điểm nhìn thấy được | Dẫn chứng |
|---|---|---|---|
| Cá thể trung tâm | **Shiny Bulbasaur · K-01** | thân xanh vàng, củ sẫm hơn con thường | 📖 Bulbapedia — Shiny Pokémon. Tỉ lệ 1/8192 (Gen II–V), 1/4096 (từ Gen VI) |
| Con lớn nằm cạnh *(quay lại ở beat 13)* | **một con Bulbasaur lớn · K-04** | mảng da rách bên sườn | 👁 quan sát của người kể — mã vì nó quay lại và dễ lẫn với cả đàn |
| Kẻ săn | **một con Fearow** | một bên mắt phủ màng đục màu tro | 👁 quan sát của người kể. Loài 📖 Fearow — Bulbapedia, phân bố Kanto |
| Con trưởng thành già | **con Venusaur cái già** | rêu và dương xỉ mọc trên lưng; cấu trúc nhỏ giống hạt giữa hoa | 👁 quan sát. Dị hình giới tính 📖 Bulbapedia — Venusaur gender differences |
| Người kể | **Dr. Holth** *(không đọc lên, xưng "tôi")* | nhà sinh vật học thực địa | Blightfall — IP riêng. Xem [NARRATOR.md](NARRATOR.md) |
| Tác giả | **Tuấn La** | người làm phim thật — **không xuất hiện trong video** | chỉ ở mô tả YouTube |
| Địa danh | **Viridian Forest** | rừng Kanto nơi Bulbasaur sống hoang dã | 📖 Pokémon Let's Go Pikachu/Eevee. *(Gen 1 KHÔNG có Bulbasaur hoang dã)* |
| Nơi bầy tụ họp | **The Mysterious Garden** | lòng chảo khuất, nơi cả bầy cùng đổi hình | 🎬 Anime tập 51 — kể như truyền thuyết người bản xứ, không gắn 📖 |

> **Ô "Dẫn chứng" không được để trống, và không được ghi một lời khẳng định thay cho nguồn.**
> Cá thể do người kể đặt tên thì ghi thẳng là 👁 — đó là câu trả lời trung thực, không phải chỗ trống.
> `check-episode.py` soát ô này.

Người kể **không bao giờ nói tên mình**. Mở bằng "Tôi là…" là biến phim tư liệu thành vlog, và kéo
sự chú ý ra khỏi khu rừng. Ông chỉ là một ống kính biết ngẫm. Tên đi bằng đường chữ: bìa sổ ghi
`DR. HOLTH · FIELD NOTES`, chữ ký cuối trang `— H.`

## Quy ước cho tập sau

- Mỗi tập tối đa **bốn** con được theo dõi riêng (một trung tâm + tối đa ba mã phụ). Nhiều hơn thì khán giả không nhớ nổi.
- Một tập luôn có **đúng một** cá thể trung tâm mang mã thực địa.
- Tên loài (Bulbasaur, Venusaur) **không dịch** ở cả hai bản.
- Tên đòn đánh và đặc tính **không bao giờ đọc thành tên game**; hai bản đều gọi theo nghĩa sinh học
  (xem bảng quy đổi trong [CREATURE-LENS.md](CREATURE-LENS.md)).
