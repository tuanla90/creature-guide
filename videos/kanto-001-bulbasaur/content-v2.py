# Creature Field Guide — Kanto #001 · "Saur" (Version 2 - Master Production Script)
#
# Bối cảnh CANON: Viridian Forest, Kanto (Game Canon: Let's Go / Anime Ep 51)
# Định danh cá thể: Specimen K-01 "Saur" (Trainer Red Alignment - Manga Pokémon Adventures)
# Kẻ bảo trợ: Scar-Shoulder (K-04) | Kẻ săn mồi: Ash-Eye (Fearow già) | Cổ thụ: Moss-Back (Venusaur cái)
#
# Đạo diễn âm thanh & thị giác:
#   - Hook phong cách BBC Earth / Dynasties: Đẩy nghịch lý sinh học và nhịp thở của củ lên giây 0.
#   - 100% Chuyển động (Full-Animation):
#       + Tầng 1: creature-motion (OpenCV offline) cho cảnh thở, phơi nắng, ngủ, canh tổ.
#       + Tầng 2: Google Flow cho sinh hoạt dã sinh, lội bùn, chạm dây leo, sương sớm.
#       + Tầng 3: Seedance cho hành động nhanh, Fearow vồ mồi, nổ bào tử, SolarBeam.
#   - Cắt bỏ phần hứa hẹn video sau: Kết thúc độc lập, sâu sắc, hoàn toàn làm chủ lịch phát hành.
#   - Luật text 9:16: caption <= 68 ký tự, text <= 52 ký tự.

ORDER = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]

BEATS = {
# ---- HOOK: NGHỊCH LÝ CỦA SỰ SỐNG -------------------------------------------
"00":
"Ở rìa Rừng Viridian, ranh giới giữa động vật và thực vật không tồn tại.\n"
"Thoạt nhìn, con vật này như một tảng đá phủ rêu bất động dưới nắng trưa.\n"
"Nhưng cái bọc trên lưng nó... đang thở.\n"
"Nó là con thú mang trên lưng một cái cây, hay một cái cây đang mượn đôi chân của con thú?",

# ---- CHƯƠNG 1: ĐỊNH DANH SAUR ---------------------------------------------
"01":
"Cuốn danh lục của người bản xứ gọi loài này là Bulbasaur. Trong sổ thực địa của tôi, nó mang mã K-01.\n"
"Tôi đến Viridian làm một việc mà ở quê nhà người ta làm với bầy sói:\n"
"chọn một cá thể, bám dấu đủ lâu, và đợi tự nhiên lên tiếng.\n"
"Suốt một tháng đầu, nó chỉ có bấy nhiêu: một mã số và một vệt nắng.",

"02":
"Trảng cỏ Viridian này có bảy cá thể. K-01 nhỏ bé nhất, luôn đi sau cùng.\n"
"Nhưng bảy ngày liền, nó luôn giành được vệt nắng chói nhất trảng.\n"
"Khác với đồng loại có củ mọc thẳng đứng, cái củ trên lưng nó vặn nghiêng hẳn sang một bên—\n"
"hậu quả của những ngày dài vặn mình đón nắng.\n"
"Từ hôm ấy, trong sổ tôi, K-01 có một cái tên: Saur.",

# ---- CHƯƠNG 2: CHIẾC DẠ DÀY THỨ HAI ---------------------------------------
"03":
"Mỗi buổi trưa, Saur bỏ ăn hoàn toàn.\n"
"Nó phơi mình hàng giờ liền dưới nắng gắt, mắt khép hờ, lá củ khẽ động.\n"
"Khi đứng dậy, khoang bụng nó vẫn phẳng lì, nhưng cái củ trên lưng đã căng mọng dịch lỏng.\n"
"Nó không nhịn đói. Nó đang ăn nắng.\n"
"Thứ trên lưng Saur không phải vật ký sinh, mà là một chiếc dạ dày thứ hai,\n"
"chuyển hóa trực tiếp quang năng thành sinh khối.",

"04":
"Nhưng quang hợp cần nước và muối khoáng.\n"
"Cuối chiều, Saur lội xuống đầm lầy, cắm sâu bốn chân vào bùn nhão nửa giờ liền mà không uống một ngụm nào.\n"
"Da chân của nó hoạt động như loài lưỡng cư: hút ẩm và khoáng chất trực tiếp từ bùn.\n"
"Còn chất đạm để nuôi củ, nó lấy từ chính chất thải bài tiết của con vật.\n"
"Tương tự như loài sên lục Elysia ở biển: một vòng tuần hoàn khép kín tuyệt đối, không lọt mất một giọt năng lượng.",

# ---- CHƯƠNG 3: LIÊN MINH BẮT BUỘC -----------------------------------------
"05":
"Đây không phải là ký sinh. Đây là một liên minh sinh tồn hoàn hảo.\n"
"Cái cây cho Saur năng lượng vô tận để không bao giờ chết đói.\n"
"Đổi lại, Saur cho cái cây một bộ khung xương để di chuyển tìm ánh sáng.\n"
"Ở quê tôi, địa y là nấm và tảo bện chặt vào nhau tới mức người ta từng tưởng là một loài duy nhất.\n"
"Saur và hạt mầm trên lưng nó cũng vậy: hai sự sống tách rời đã hòa làm một.",

# ---- CHƯƠNG 4: NGÔN NGỮ CỦA DÂY LEO ---------------------------------------
"06":
"Bảy con trong trảng giữ khoảng cách nghiêm ngặt để không che bóng của nhau.\n"
"Chiều tà, khi vệt nắng co lại, chúng dùng vai huých đẩy nhưng tuyệt nhiên không cắn xé.\n"
"Saur thường nằm cách con đực lớn nhất hai thân người.\n"
"Con lớn ấy mang một vết sẹo dài bên sườn sau một trận kịch chiến cũ.\n"
"Tôi gọi nó là Scar-Shoulder. Ở đây, tên gọi luôn đến sau vết thương.",

"07":
"Chúng cũng chạm vào nhau, nhưng bằng một cách rất khác.\n"
"Hai sợi dây leo thò ra từ nách củ, vươn cao, xoắn lấy nhau giữa không trung vài giây rồi buông lơi.\n"
"Đó không phải vũ khí để quất. Đó là xúc tu cảm giác.\n"
"Chúng chạm để nhận diện đồng loại, và để vệ sinh vùng lưng—\n"
"điểm mù giải phẫu mà bốn cái chân ngắn không thể nào tự với tới.",

# ---- CHƯƠNG 5: MẮT ĐỤC VÀ MÀN BÀO TỬ --------------------------------------
"08":
"Ngày thứ hai mươi hai, một bóng đen xé toạc bầu trời Viridian.\n"
"Đó là Ash-Eye—con chim Fearow già với một bên mắt mờ đục màu tro, chuyên săn lùng con non.\n"
"Khi bóng chim bổ nhào, Saur không chạy trốn. Nó ép sát bụng xuống rêu ẩm.\n"
"Bộ da hoa văn xanh lốm đốm tan biến hoàn toàn vào những mảng nắng tán xạ qua kẽ lá.\n"
"Cú sà xuống lần hai, đỉnh củ của Saur nứt mở.\n"
"Một làn sương bào tử vàng mịn bung ra mù mịt. Con chim hoảng loạn, mất hướng rồi vội vã tháo lui.",

# ---- CHƯƠNG 6: CÁI GIÁ CỦA SỨC MẠNH ---------------------------------------
"09":
"Nhưng cái giá của sự sống sót hiện rõ ngay buổi chiều hôm đó.\n"
"Sau khi Ash-Eye biến mất, Saur nằm bẹp suốt nhiều giờ, kiệt sức.\n"
"Cái củ trên lưng nó teo tóp lại thấy rõ, lớp bẹ nhăn nheo như quả khô.\n"
"Màn bào tử vừa cứu mạng nó đã đốt sạch lượng dinh dưỡng mà nó phơi nắng cả tháng trời để tích lũy.\n"
"Trong tự nhiên, không có món quà nào là miễn phí.",

# ---- CHƯƠNG 7: VŨ KHÍ TRONG SỚI ĐẤU ---------------------------------------
"10":
"Ở các thị trấn quanh Viridian, con người dùng chính những con vật này trong các sới đấu đất nện.\n"
"Dây leo ở đây không còn để chải chuốt hay chào nhau—chúng quất mạnh như roi thép xé toạc mặt đất.\n"
"Nhưng đáng sợ nhất là cú phóng quang SolarBeam:\n"
"con vật đứng khựng lại, củ trên lưng hút cạn quang năng xung quanh rồi phóng ra một luồng nhiệt chói lòa.\n"
"Khán giả reo hò trước uy lực. Còn tôi thấy một kho dự trữ bị vắt kiệt tới tế bào cuối cùng.",

"11":
"Loài này có hai nết sinh lý đặc biệt.\n"
"Thứ nhất: giữa trưa nắng gắt, Saur di chuyển nhanh gấp đôi lúc trời râm—\n"
"nhiệt lượng mặt trời kích hoạt toàn bộ cơ bắp của nó như một cỗ máy sinh học hoàn hảo.\n"
"Thứ hai: khi kiệt sức vì thương tích, đòn đánh của nó đột nhiên mạnh bất thường.\n"
"Nó đang dốc nốt chút sinh lực cuối cùng. Giống như loài thùa sa mạc:\n"
"gom góp cả đời chỉ để bung nở một lần duy nhất trước khi tàn lụi.",

# ---- CHƯƠNG 8: DẤU HIỆU BIẾN THÁI ----------------------------------------
"12":
"Tháng thứ tư, Saur thay đổi nếp sống.\n"
"Nó nằm lì ngoài nắng, ăn mùn đất không ngừng nghỉ. Bước đi của nó bắt đầu nặng nề.\n"
"Có những buổi sớm, đầu Saur hướng về phía nam, nhưng cái củ lại vặn gắt về phía đông đón nắng.\n"
"Hai phần trên một cơ thể quay về hai hướng khác nhau.\n"
"Cái củ nghiêng mà tôi lấy làm tên cho nó, chính là vết tích của bản năng hướng dương mãnh liệt này.",

"13":
"Rồi một đêm trăng khuyết, Saur rời bỏ trảng cỏ, đi sâu vào rừng thẳm.\n"
"Tôi lần theo dấu vết đến một hõm đất bí mật khuất sau vành đá cổ thụ.\n"
"Hơn mười cá thể Bulbasaur đang đứng ken đặc thành một vòng tròn im lìm.\n"
"Ánh lân tinh xanh biếc bốc lên từ những đỉnh củ, hòa vào màn sương đêm.\n"
"Đó là nghi lễ biến thái thiêng liêng của cả giống loài.",

# ---- CHƯƠNG 9: SỨC NẶNG CỦA IVYSAUR ---------------------------------------
"14":
"Sáng hôm sau, thung lũng chỉ còn lại hiện trường:\n"
"đất bị cày nát thành những rãnh sâu bởi bốn cái chân vừa phải chống đỡ một sức nặng tăng vọt.\n"
"Những bẹ lá khô bong tróc nằm cuộn tròn như vỏ hành già. Và không khí sực nức mùi hương hoa lạ.\n"
"Từ trong sương mù, một bóng hình sừng sững bước ra.\n"
"Bốn chân nó to dày như những cây cột đá để nâng đỡ cái nụ hoa hồng rực nặng trĩu trên lưng.\n"
"Nó đã trở thành Ivysaur.\n"
"Nhưng khi tôi mở sổ tay, con thú to lớn ấy vẫn khẽ nghiêng đầu về phía tiếng ngòi bút của tôi.",

# ---- CHƯƠNG 10: MOSS-BACK VÀ VÒNG KHÉP KÍN --------------------------------
"15":
"Mang nụ hoa nặng nề khiến Ivysaur vĩnh viễn mất khả năng đứng bằng hai chân sau. Chân phải thành cột.\n"
"Mùa mưa cuối, tôi bắt gặp Moss-Back—cá thể Venusaur khổng lồ canh giữ lối vào rừng già Viridian.\n"
"Lưng nó đã hóa gỗ nứt nẻ, rêu phong phủ đầy mai. Ở tâm hoa nhô lên một chiếc nhụy hạt: một con cái cổ thụ.\n"
"Hương hoa sau mưa của Moss-Back làm dịu đi cơn hung hăng của những con thú dữ tợn nhất.\n"
"Rời khỏi Viridian, tôi vẫn không có câu trả lời: hạt mầm là một phần cơ thể hay là một sinh vật sống cộng sinh?\n"
"Nhưng có lẽ thiên nhiên không cần một định nghĩa rạch ròi.\n"
"Hai sự sống đã nương tựa vào nhau, để cùng tạo nên một thực thể hoàn mỹ.",

# ---- SHORT OUTRO (Dành riêng cho bản Short cắt từ Beat 00) -------------------
"short-outro":
"Cái hạt ấy là một phần của nó, hay một sự sống khác đang mượn cơ thể nó?\n"
"Rời khỏi Rừng Viridian sau mười bốn tháng, tôi vẫn chọn để câu hỏi ấy mở.",
}

PRON = {
    "Bulbasaur": "bôn-ba-xo",
    "Ivysaur": "ai-vi-so",
    "Venusaur": "ve-nu-so",
    "Viridian": "vi-ri-đi-ân",
    "Kanto": "can-tô",
    "SolarBeam": "sô-la-bim",
    "Saur": "so",
}

NGUON = {
    "Bulbasaur hoang dã tại Kanto": "Pokémon Let's Go, Pikachu! & Eevee! (Spawn duy nhất tại Viridian Forest)",
    "Nghi lễ biến thái tại khu vườn bí mật": "Anime Pokémon Tập 51 (Bulbasaur's Mysterious Garden)",
    "Hạt hấp thụ ánh nắng để lớn, nhịn ăn nhiều ngày": "Pokédex Red/Blue/Yellow/Ruby/Emerald",
    "Hai nết sinh lý (quang hợp tăng tốc, dốc sức khi nguy cấp)": "Chlorophyll & Overgrow abilities — Bulbapedia",
    "Ivysaur mất khả năng đứng 2 chân sau, chân to như cột": "Pokédex Red/LeafGreen/Sword",
    "Venusaur cái có nhụy hoa giữa tâm": "Bulbapedia Venusaur Gender Differences",
    "Hương hoa làm dịu cơn giận dữ": "Pokédex Venusaur Ruby/Sapphire/FireRed",
    "ĐỐI CHIẾU TRÁI ĐẤT": "Sên lục Elysia chlorotica quang hợp · Biểu mô hút nước ở chân ếch · Tảo và nấm trong địa y · Cây thùa dồn nhựa trổ hoa trước khi chết · Voi và rùa khổng lồ chân cột",
}
