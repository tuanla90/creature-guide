# Giọng văn lời dẫn

Lời dẫn phải **đọc thầm vẫn hấp dẫn**. Nếu tắt tiếng, bỏ hình, chỉ còn trang giấy mà người ta vẫn
muốn đọc tiếp, thì lên giọng mới hay. Sinh ra từ góp ý duyệt tập 001: lời V4 đúng luật nhưng khô
như biên bản — thiếu cảnh, thiếu chuyển tiếp, câu cụt, đại từ trôi nổi.

Bộ soát máy bắt được một phần (mục cuối). Phần còn lại là tay nghề.

## Học gì từ ai

Đọc để học **cách làm**, không chép câu nào.

- **Tô Hoài — *Dế Mèn phiêu lưu ký*.** Tả cận cảnh bằng động từ chính xác và từ láy (lũn cũn,
  phành phạch, im phăng phắc); câu dài nối bằng dấu phẩy mà vẫn có nhịp; người kể ngôi thứ nhất vừa
  kể vừa tự nhận xét. Đây là giọng gần nhất với Dr. Holth: một người quan sát tỉ mỉ, có chút hóm.
- **Nguyễn Đình Thi — *Cái Tết của Mèo Con*.** Mở mỗi đoạn bằng cảnh — trời, đất, giờ, mùa —
  rồi mới tới chuyện. Nhân vật nào cũng được giới thiệu rõ trước khi được gọi tắt.
- **Nguyễn Nhật Ánh — *Tôi là Bêtô*.** Người kể nói *với* người đọc; giữa hai sự việc có một câu
  bình, một câu tự hỏi. Chữ giản dị nhưng có tình.

## Bảy luật

1. **Mở cảnh trước khi kể việc.** Mỗi beat, và mỗi khi đổi chỗ hay đổi giờ, có một câu dựng cảnh:
   giờ nào, ánh sáng thế nào, nghe gì, ngửi thấy gì. "Chiều nào cũng vậy, khi nắng đã ngả vàng, nó
   lững thững lội ra mép ao…" chứ không phải "Cuối chiều, nó ra mép ao."
2. **Có cầu nối giữa các câu và các beat.** Thời gian (rồi, từ hôm ấy, đến đêm thứ năm), nguyên
   nhân (bởi, vì thế, hoá ra), đối lập (thế nhưng, vậy mà, còn). Đầu beat móc vào cuối beat trước.
3. **Câu cụt là gia vị, không phải cơm.** Tối đa **một** câu ngắn (≤ 6 tiếng) mỗi beat, đặt ở chỗ
   cần cú đập. Hai câu ngắn liền nhau là nhịp báo cáo. "Chúng quất." → "Chúng vụt ra nhanh như gió,
   quất xuống nền đất nện nghe chát chúa như tiếng roi da."
4. **Động từ hành động phải có hình và tiếng.** Mọi hành động mạnh (quất, bổ nhào, bung, cày) đi kèm
   một so sánh, một âm thanh, hay một hệ quả nhìn thấy được.
5. **Đại từ có chủ.**
   - **"Nó" chỉ dành cho cá thể trung tâm (K-01).** Con khác gọi bằng danh từ: "con chim ấy",
     "con Venusaur già", "con vật trong sân".
   - **"Chúng" chỉ dùng ngay sau khi vừa nêu một danh từ số nhiều** trong cùng đoạn ("đàn
     Bulbasaur… Chúng…"). Mở beat bằng "chúng" là sai.
   - Không "con đấy", "con đó", "con kia" trơ trọi. Con nào cũng được **giới thiệu một lần bằng
     danh từ đầy đủ, đúng lúc nó có trên hình**, rồi mới được gọi tắt.
6. **Từ lạ phải được dựng.** Lần đầu dùng một từ ít gặp (trảng cỏ, bẹ lá, nhụy) thì câu ấy tự giải
   nghĩa: "một khoảng đất trống cỏ mọc thấp, người ta gọi là trảng cỏ". Sau đó luôn viết đủ "trảng
   cỏ", không cắt còn "trảng". Không dịch sát kiểu Tây ("điều tôi gạch chân" → "điều khiến tôi phải
   ghi đậm vào sổ").
7. **Mã số phải có nghĩa.** Lần đầu gọi K-01, nói K là gì (Kanto — tên vùng đất) và 01 là gì (con
   đầu tiên được chọn theo). Mã chỉ gán sau khi khán giả đã thấy con vật.

Bản EN theo cùng bảy luật, với giọng Attenborough — câu dài uyển chuyển, không nhịp điện tín.

## Máy bắt được gì

`tools/voice_lint.py`, chạy trong `check-episode.py` và `handoff.py --draft`:
- beat có hơn một câu ngắn, hoặc hai câu ngắn liền nhau (VI ≤ 6 tiếng, EN ≤ 5 từ);
- beat mở bằng "chúng"/"they" chưa có danh từ số nhiều đứng trước;
- "con đấy / con đó / con kia";
- "trảng" không kèm "cỏ";
- từ dịch sát trong danh sách `CALQUES`.

Máy không biết câu nào hay. Mở cảnh, cầu nối, hình và tiếng của động từ — người đọc thành tiếng
một lượt mới biết.
