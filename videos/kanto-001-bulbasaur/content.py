# Creature Field Guide — Kanto #001–003 · "Chọn Nắng"
#
# Người kể: Tuấn, nhà sinh vật học thực địa của thế giới chúng ta, khảo sát Rừng Gió Gập ở Kanto.
# Nhân vật (đặt tên theo vết tích hoặc hành vi, kèm vai diễn — xem skills/.../subject-naming-and-evidence.md):
#   K7 "Kẻ Chọn Nắng" (gọi tắt: Chọn Nắng) — hành vi: luôn chiếm vệt nắng sáng nhất · vai: KẺ YẾU THẾ VƯƠN LÊN
#   "Vai Rách"     — đặt theo vết tích: mảng da rách bên sườn · vai: HÀNG XÓM
#   "Mắt Tro"      — đặt theo vết tích: một con mắt màu tro · vai: KẺ SĂN CHUYÊN MỘT CON MỒI
#   "Lưng Rêu"     — đặt theo vết tích: rêu và dương xỉ mọc trên lưng · con cái già · vai: BÀ LÃO CỦA VÙNG
# Bí ẩn xuyên suốt: cái hạt trên lưng là ký sinh hay cộng sinh? -> trả bài ở beat 15.
#
# Luật (docs/CREATURE-LENS.md + skills/creature-field-guide-scriptwriter):
#   - Không nhắc game. Pokédex = cuốn danh lục của người bản xứ; tên đòn đánh = tên người ta đặt.
#   - Ba nhãn không trộn: 📖 danh lục (có nguồn) · 👁 quan sát · 🔬 giả thuyết (kèm loài có thật).
#   - CẢNH TIẾN HOÁ: không có lột da. Chỉ dùng sưng nở, sức nặng, ánh sáng, bóng dáng, dấu vết.
#   - Mọi khả năng phải nêu CÁI GIÁ.
# Giọng đọc VBee ghép sau -> không dùng [tag]. "\n" = một nhịp ngắt.

ORDER = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]

BEATS = {
# ---- mở đầu ------------------------------------------------------------------
"00":
"Ngày đầu tiên tôi gặp Chọn Nắng, nó đang nằm giữa lối mòn, bất động dưới nắng trưa.\n"
"Tôi tưởng nó đã chết.\n"
"Rồi cái hạt trên lưng nó khẽ co lại.\n"
"Nó đang thở. Và không phải chỉ bằng phổi.",

"01":
"Tôi là Tuấn. Tôi tới Rừng Gió Gập để làm một việc mà ở quê tôi người ta làm với sói và với voi:\n"
"chọn một con, đi theo nó đủ lâu, rồi xem cái gì thay đổi.\n"
"Trong sổ của người bản xứ, con vật này được ghi là Bulbasaur. Trong sổ của tôi, nó là cá thể K7.\n"
"Suốt mấy tuần đầu, nó chỉ có chừng ấy: một chữ và một con số.",

# ---- chương 1: con yếu nhất --------------------------------------------------
"02":
"Rừng Gió Gập là chỗ rừng già chạm vào đồng cỏ. Giữa hai thứ đó có một lối mòn nhỏ, cỏ bị đè rạp,\n"
"và lối mòn ấy do chúng đi.\n"
"Ở trảng này tôi đếm được bảy cá thể. Chọn Nắng là con nhỏ nhất, và lúc nào cũng đi sau.\n"
"Nếu chỉ nhìn qua, nó là con yếu nhất trong bảy con.\n"
"Nhưng suốt một tuần đầu tiên, tôi ghi lại chỗ nằm của từng con vào mỗi buổi trưa.\n"
"Và K7 luôn nằm đúng vệt nắng sáng nhất trong trảng. Không phải một hôm. Là cả bảy hôm.\n"
"Ở đây người ta không gọi con vật bằng số. Họ gọi theo cái nó hay làm, hoặc theo dấu nó mang trên người.\n"
"Từ hôm ấy, trong sổ tôi, K7 thành Kẻ Chọn Nắng. Về sau, viết tắt dần, tôi chỉ còn ghi là Chọn Nắng.",

# ---- chương 2: cái hạt không phải vật trang trí -------------------------------
"03":
"Mỗi buổi trưa, Chọn Nắng bỏ ăn.\n"
"Nó nằm yên tới mức có hôm tôi tưởng mình đã mất dấu, và bò vòng qua bụi dương xỉ để tìm.\n"
"Nhưng sau vài giờ, cái hạt trên lưng nó căng lên, còn cái bụng thì vẫn phẳng.\n"
"Nó không nhịn đói. Nó đang ăn một thứ khác.\n"
"Cuốn danh lục ghi hai dòng rời nhau, và tôi mất gần một tháng mới ghép được chúng lại:\n"
"cái hạt lớn lên nhờ hút ánh mặt trời, và con vật này nhịn ăn được nhiều ngày liền\n"
"nhờ phần dự trữ nằm trong củ.\n"
"Nói cách khác, thứ trên lưng nó không phải đồ trang trí, mà là một cái dạ dày thứ hai.",

"04":
"Nhưng ăn nắng thôi thì chưa đủ. Một cái cây còn cần nước và khoáng.\n"
"Tôi mất thêm ba tuần mới thấy Chọn Nắng lấy hai thứ đó ở đâu.\n"
"Cuối buổi chiều, nó ra mép ao, đứng lún hai chân trước trong lớp bùn nhão, rất lâu, và không uống ngụm nào.\n"
"Ở quê tôi, ếch nhái gần như không uống bằng miệng. Chúng hút nước qua một vùng da mỏng ở bụng.\n"
"Còn phần khoáng, tôi ngờ nó không đến từ bên ngoài chút nào.\n"
"Dưới rạn san hô, tảo sống trong mô con vật chủ dùng lại chính chất thải của nó để lớn.\n"
"Nếu cái củ này cũng vậy, thì nó đang được bón bằng thứ mà cơ thể Chọn Nắng thải ra.\n"
"Một vòng khép kín. Không rơi mất giọt nào.",

# ---- chương 3: một sinh vật sống chung ---------------------------------------
"05":
"Tới đây thì câu hỏi trong sổ tôi đổi hẳn.\n"
"Ban đầu tôi viết: cái hạt này là vật ký sinh.\n"
"Nó bám trên lưng, nó hút, nó lớn lên bằng thứ con vật kiếm được.\n"
"Nhưng ký sinh thì không làm cho vật chủ no.\n"
"Còn Chọn Nắng thì những ngày nắng gắt lại là những ngày nó khoẻ nhất.\n"
"Vậy Chọn Nắng đang nuôi cái hạt, hay cái hạt đang nuôi Chọn Nắng?\n"
"Ở quê tôi, hai kiểu sống chung này chỉ cách nhau một sợi tóc.\n"
"Địa y là nấm và tảo dính vào nhau tới mức người ta từng tưởng là một loài.\n"
"Còn cây tầm gửi thì cắm vòi vào thân cây chủ, rồi rút dần cho tới khi cây chủ chết đứng.",

# ---- chương 4: bầy đàn --------------------------------------------------------
"06":
"Bảy con trong trảng không bao giờ nằm sát nhau.\n"
"Mỗi con giữ một khoảng trống đủ rộng để nắng chạm được xuống lưng mình.\n"
"Chiều xuống, khi bóng rừng bò ra, những vệt nắng còn lại co rất nhanh, và lúc đó thì có chen lấn.\n"
"Không con nào cắn con nào. Chúng ép vai, đẩy nhau, rồi con thua bỏ đi tìm vệt khác.\n"
"Chọn Nắng thường ngủ cách một con lớn hơn chừng hai thân người. Đêm nào cũng vậy, cùng một khoảng cách.\n"
"Hai con ấy chưa bao giờ chạm vào nhau.\n"
"Hôm con lớn kia bị rách một mảng da bên sườn, tôi mới đặt được tên cho nó: Vai Rách.\n"
"Ở đây người ta đặt tên như thế. Cái tên đến sau vết thương.\n"
"Và cả trảng đổi chỗ nằm. Tới tối, bốn con đã nằm quanh Vai Rách.",

"07":
"Chúng cũng chạm vào nhau, chỉ là không nằm cạnh nhau.\n"
"Hai sợi dây leo thò ra từ dưới củ, gặp nhau giữa không trung, cuộn lấy nhau vài giây, rồi thả.\n"
"Tôi đứng nhìn cảnh đó hai mươi phút và không ghi nổi chữ nào.\n"
"Vì thứ tôi vừa thấy không phải một cái roi. Nó gần với cái vòi con voi hơn.\n"
"Để cầm, để chạm, để chào.\n"
"Và để gãi. Lưng là điểm mù: một con vật bốn chân, cổ ngắn, không thể tự quay lại chỗ cái củ.\n"
"Chiều hôm đó tôi thấy Chọn Nắng vẩy một sợi dây leo qua lưng, gạt phắt một con sâu đang bò lên mép lá,\n"
"đúng động tác cái đuôi ngựa xua ruồi trâu.",

# ---- chương 5: Mắt Tro --------------------------------------------------------
"08":
"Con chim xuất hiện vào ngày thứ hai mươi hai.\n"
"Một con chim lớn, mỏ dài, bay vòng rất cao. Nó không săn cả trảng. Nó chỉ theo Chọn Nắng.\n"
"Một bên mắt nó phủ một lớp màng đục màu tro, dấu của một vết thương cũ.\n"
"Người bản xứ gọi nó theo đúng cái mắt ấy: Mắt Tro.\n"
"Lần bổ nhào đầu tiên, Chọn Nắng không chạy.\n"
"Nó ép sát người xuống nền đất ẩm dưới một tán dương xỉ, và đứng im.\n"
"Đây là lúc tôi hiểu ra bộ da của nó.\n"
"Màu xanh lam với những đốm sẫm không đều, nhìn gần thì kỳ quặc, nhưng nằm dưới tán lá thì\n"
"những đốm ấy trùng khít với các mảng nắng lọt qua kẽ lá rọi xuống đất.\n"
"Mắt Tro sượt qua cách chừng một sải tay, rồi bay vòng lại.\n"
"Lần thứ hai, cái củ trên lưng Chọn Nắng hé ra ở đỉnh, và một màn bào tử mịn bung lên.\n"
"Con chim đảo cánh, mất hướng, rồi bỏ đi.",

# ---- chương 6: cái giá của sức mạnh ------------------------------------------
"09":
"Nhưng cái tôi ghi đậm nhất hôm đó không phải màn bào tử.\n"
"Sau khi Mắt Tro bỏ đi, Chọn Nắng nằm im gần hết buổi chiều. Không ăn, không đổi chỗ, không phản ứng khi tôi lại gần.\n"
"Và cái củ trên lưng nó nhỏ lại thấy rõ.\n"
"Thứ vừa cứu mạng nó được lấy ra từ đúng cái kho mà nó phơi nắng cả tháng để tích.\n"
"Từ hôm đó tôi thôi ghi những thứ này vào mục khả năng.\n"
"Tôi chuyển hết sang mục thu và chi.",

# ---- chương 6b: trong thị trấn ------------------------------------------------
"10":
"Ở vùng đất này có một thứ mà quê tôi không có. Người ta đấu với nhau bằng chính những con vật này.\n"
"Tối hôm ấy tôi xuống thị trấn, đứng ở vòng ngoài một sân đất, và xem một trận.\n"
"Trong sân, hai sợi dây leo không còn để chào nhau nữa. Chúng quật.\n"
"Cùng một cơ quan: ngoài rừng để hái quả và gạt sâu, trong sân để đánh.\n"
"Tôi không thấy điều đó đáng lên án. Cái vòi voi ở quê tôi cũng vừa vuốt ve con non, vừa quật gãy được xương người.\n"
"Nhưng có một cú làm tôi ngồi viết tới gần sáng.\n"
"Con vật trong sân không bắn ngay. Nó đứng yên một nhịp, cái củ trên lưng sáng lên,\n"
"rồi mới phóng ra một luồng sáng.\n"
"Khán giả quanh tôi coi nhịp chờ ấy là điểm yếu. Tôi thì nhận ra mình vừa nhìn thấy cái kho ban trưa,\n"
"bị rút cạn trong một hơi thở.",

# ---- chương 6c: hai cái nết ---------------------------------------------------
"11":
"Những người nuôi lâu năm ở đây nói mỗi loài có một nết riêng. Với loài này thì có hai.\n"
"Nết thứ nhất tôi tự đo được trước khi nghe ai nói.\n"
"Giữa trưa nắng gắt, Chọn Nắng đi nhanh hơn hẳn chính nó lúc trời râm. Tôi bấm giờ trên cùng một quãng đường,\n"
"và con số gần như gấp đôi.\n"
"Ở quê tôi, thằn lằn và rắn phải phơi nắng cho ấm người đã, rồi mới chạy nhanh được.\n"
"Một cỗ máy chạy bằng nắng thì nắng càng gắt, máy càng khoẻ.\n"
"Nết thứ hai tôi chỉ thấy trong sân đấu, và nó làm tôi khó chịu hơn là thán phục.\n"
"Khi con vật đã bị thương nặng, gần như không đứng nổi, những cú đánh của nó đột nhiên mạnh hẳn lên.\n"
"Tôi không nghĩ nó khoẻ hơn. Tôi nghĩ nó đang dốc nốt chỗ dự trữ. Một lần. Và hết.\n"
"Ở quê tôi, cây thùa sống mấy chục năm chỉ để dồn tất cả vào một lần trổ hoa, rồi chết.",

# ---- chương 7: trước khi đổi ---------------------------------------------------
"12":
"Tháng thứ tư, Chọn Nắng đổi nếp.\n"
"Nó nằm ngoài nắng lâu hơn hẳn, bỏ cả nhịp trú trưa trong bóng râm, và ăn nhiều hơn trước.\n"
"Nó cũng đi chậm lại. Hai sợi dây leo dày lên, cử động nặng nề, có lần vươn ra rồi rơi xuống\n"
"như chính nó cũng không điều khiển nổi.\n"
"Có một buổi sáng tôi ngồi đúng ba tiếng chỉ để ghi một chi tiết.\n"
"Đầu Chọn Nắng quay về hướng nam, nằm im. Nhưng cái củ trên lưng thì vặn chậm về phía đông, theo mặt trời.\n"
"Hai thứ trên cùng một cơ thể, quay về hai hướng khác nhau, trong cùng một buổi sáng.\n"
"Ở quê tôi, hoa hướng dương non cũng quay theo mặt trời suốt ngày. Tới khi nở hẳn thì đứng yên,\n"
"và đứng mãi về một hướng.",

"13":
"Cuối tháng ấy, Chọn Nắng rời đàn.\n"
"Nó bỏ trảng nắng, đi sâu vào phía rừng già, và tôi mất dấu nó bốn ngày.\n"
"Đêm thứ năm tôi tìm thấy nó trong một hõm đất khuất sau vành cây, cùng hơn mười con khác, đứng thành vòng.\n"
"Không con nào chạm vào con nào. Không con nào phát ra tiếng.\n"
"Người bản xứ nói mỗi năm chúng tụ về đây một lần.\n"
"Lúc đó tôi nghĩ nó sắp chết. Tôi đã viết nguyên một trang về chuyện ấy.\n"
"Sau này tôi mới hiểu, nó chỉ đang chuẩn bị không còn là Chọn Nắng nữa.",

# ---- chương 8: Ivysaur --------------------------------------------------------
"14":
"Tôi không nhìn thấy khoảnh khắc ấy. Tôi ngủ quên sau hai đêm thức trắng, và khi tỉnh dậy thì trời đã sáng.\n"
"Cái hõm đất trống không.\n"
"Nhưng nó để lại đủ thứ cho một người có nghề đọc.\n"
"Đất bị cày lên thành những rãnh ngắn, chỗ bốn cái chân đã bấu xuống để chống đỡ một sức nặng mới.\n"
"Cỏ quanh đó bẹp thành một vòng tròn. Quanh cổ củ, những bẹ lá già bong ra, khô, cuộn lại như vỏ hành.\n"
"Và cả hõm đất sực mùi hoa, thứ mùi mà trước đó tôi chưa từng ngửi thấy ở loài này.\n"
"Phía bên kia bãi cỏ, trong sương, có một cái bóng lớn hơn cái bóng tôi đã theo suốt một năm.\n"
"Nó bước ra khỏi vùng sáng, và để lại những dấu chân sâu hơn hẳn, có một vệt kéo lê phía sau.\n"
"Thứ đứng đó không còn là con vật tôi từng ghi chép.\n"
"Nhưng khi tôi mở sổ, nó vẫn nghiêng đầu về phía tiếng bút.",

"15":
"Cái nụ trên lưng nó bây giờ nặng tới mức nó không đứng bằng hai chân sau được nữa.\n"
"Chân và thân đã dày lên để đỡ. Ở quê tôi, voi và rùa khổng lồ trả đúng cái giá ấy:\n"
"mang nặng thì chân phải thành cột.\n"
"Mùa mưa cuối cùng trong cuốn sổ này, tôi gặp một con trưởng thành già sống ở bìa rừng.\n"
"Thân nó đã hoá gỗ, dương xỉ nhỏ và rêu mọc luôn trên lưng, bông hoa to và hơi bạc màu.\n"
"Người bản xứ gọi con này là Lưng Rêu, và họ bảo nó ở bìa rừng ấy từ trước khi họ sinh ra.\n"
"Chính giữa bông hoa của Lưng Rêu có một cái nhụy. Ở những con khác tôi từng gặp thì không có.\n"
"Lưng Rêu là con cái. Và đó là lần đầu tiên tôi phân biệt được giới tính của loài này bằng mắt thường.\n"
"Còn Chọn Nắng thì chưa. Cái nụ của nó chưa nở, nên tôi vẫn chưa biết mình đã theo một con đực hay con cái.\n"
"Sau mỗi trận mưa, hương hoa của nó đậm hẳn lên, và tôi đã ngồi nhìn hai con vật đang gầm gừ nhau\n"
"cùng ngồi xuống, cách nhau vài bước, trong làn hương ấy.\n"
"Tôi vẫn không biết cái hạt trên lưng Chọn Nắng là một phần của nó, hay một sinh vật khác sống nhờ nó.\n"
"Có lẽ câu trả lời không nằm ở chỗ ta gọi nó là gì.\n"
"Có lẽ một cơ thể có thể bắt đầu từ hai sự sống, và vẫn thành một cá thể duy nhất.\n"
"Ở trang sau của cuốn danh lục có một loài mang lửa ở chóp đuôi.\n"
"Nếu ngọn lửa ấy tắt khi trời mưa, nó sống sót bằng cách nào?",

"short-outro":
"Cái hạt ấy là một phần của nó, hay một sinh vật khác đang sống nhờ nó?\n"
"Sau mười bốn tháng ngoài đồng, tôi vẫn chưa trả lời được.",
}

# Phiên âm cho TTS (VBee): caption trên màn hình vẫn giữ chính tả gốc.
PRON = {
    "Bulbasaur": "bôn-ba-xo",
    "Kanto": "can-tô",
}

# Nguồn cho từng câu canon — soát lại trước khi thu giọng.
NGUON = {
    "hạt được gieo trên lưng từ lúc chào đời": "Pokédex Red/Blue",
    "ngủ dưới nắng, hạt hấp thụ nắng mà lớn": "Pokédex Ruby/Sapphire/Emerald",
    "nhịn ăn nhiều ngày, dự trữ trong củ": "Pokédex Yellow",
    "7 đực : 1 cái (không còn đọc thành số trong lời thoại, để dành cho tập khác)": "Bulbapedia",
    "hai nết: nắng gắt → nhanh gấp đôi; kiệt sức → đòn mạnh hơn": "Chlorophyll; Overgrow — Bulbapedia",
    "nụ hút năng lượng từ chính cơ thể": "Pokédex Yellow (Ivysaur)",
    "mất khả năng đứng bằng hai chân sau; chân và thân dày lên": "Pokédex Red/LeafGreen/Sword; Ruby/Emerald",
    "phơi nắng nhiều hơn thường lệ = sắp nở; toả hương khi sắp nở": "Pokédex Ruby; Blue/Silver (Ivysaur)",
    "con cái có nhụy giữa hoa": "Bulbapedia — Venusaur, gender differences",
    "sau mưa hương đậm hơn; hương làm nguôi kẻ đang giao chiến": "Pokédex Venusaur; Ruby/Sapphire; FireRed",
    "mỗi năm tụ về một chỗ khuất rồi cùng đổi hình": "anime — Bulbapedia, mục Biology (kể như lời người bản xứ)",
    "ĐỐI CHIẾU TRÁI ĐẤT (soát lại trước khi thu)": "ếch hút nước qua da bụng · tảo cộng sinh trong mô san hô dùng lại chất thải đạm của vật chủ · địa y cộng sinh · cây tầm gửi ký sinh · đuôi ngựa xua ruồi · màu gây nhiễu dưới ánh nắng lọt tán lá · thằn lằn phơi nắng mới chạy nhanh · cây thùa dồn cả đời vào một lần trổ hoa · hoa hướng dương non quay theo mặt trời rồi đứng cố định khi nở · voi và rùa khổng lồ: mang nặng thì chân thành cột",
}
