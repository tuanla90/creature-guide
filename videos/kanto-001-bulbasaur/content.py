# Creature Field Guide — Kanto #001 · "Ai đang nuôi ai?" · V4
#
# Luồng: 2-skeleton.md (Claude) → 3-script-gemini.md (Gemini) → bản này (Claude chuẩn hoá).
# Vòng 2 (2026-09-24): viết lại theo docs/VOICE.md sau góp ý duyệt — mở cảnh, câu nối, bớt câu cụt,
# đại từ có chủ ("nó" chỉ cho K-01), giải nghĩa mã K-01.
# Đã sửa gì của Gemini và vì sao: drafts/4-review.md.
#
# Người kể: Dr. Holth (docs/NARRATOR.md) — xưng "tôi", KHÔNG bao giờ nói tên mình.
# Không đặt tên riêng cho con vật (docs/CAST.md):
#   K-01 · Shiny Bulbasaur → Shiny Ivysaur — đặc điểm: thân vàng-xanh nhạt, củ sẫm; sau đổi hình: nụ VÀNG
#   K-04 · con Bulbasaur lớn, rách một mảng da bên sườn — quay lại ở beat 13
#   một con Fearow, một bên mắt đục màu tro · con Venusaur cái già ở bìa rừng
# "shiny" là từ của người bản xứ, nói ĐÚNG MỘT LẦN ở beat 02, sau khi đã thấy màu.
# Câu hỏi xương sống, không bao giờ trả lời: con thú nuôi cái hạt, hay cái hạt nuôi con thú?
#
# Luật: không nhắc game · ba nhãn 📖 👁 🔬 (+🎬 lời người bản xứ) · không lột da · mọi khả năng có giá ·
# không bịa số. Giọng đọc VBee ghép sau -> không dùng [tag]. "\n" = một nhịp ngắt.
#
# BEATS là bản VI (track giọng VBee). BEATS_EN là bản gốc EN — engine chưa đọc, giữ ở đây để hai bản
# đi cùng một file và soát lệch thời lượng được.

ORDER = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]

BEATS = {
# ---- HỒI 1 · NGHỊCH LÝ ----------------------------------------------------------
"00":
"Đó là một buổi trưa đầu hạ ở rừng Viridian. Nắng đổ xuống lối mòn trắng loá, gió cũng lười chẳng buồn lay ngọn cỏ, và giữa lối mòn ấy có một con vật nhỏ nằm sấp, bốn chân duỗi thẳng, cái củ xanh sẫm trên lưng im lìm như một hòn đá phủ rêu.\n"
"Tôi đứng nhìn nó rất lâu, và tin chắc rằng nó đã chết.\n"
"Thế rồi cái củ trên lưng nó khẽ phồng lên, rồi xẹp xuống, chậm rãi như một lồng ngực. Con vật ấy đang thở, mà hình như không chỉ thở bằng phổi.",

"01":
"Tôi đến vùng đất này mang theo một câu hỏi đã theo tôi nhiều năm: liệu có những sinh vật mà sự sống và năng lượng quấn chặt vào nhau đến mức không thể gỡ ra được hay không.\n"
"Để trả lời, tôi làm theo cách các nhà nghiên cứu ở quê tôi vẫn làm với bầy sói hay đàn voi: chọn lấy một cá thể, lặng lẽ đi theo nó thật lâu, rồi xem năm tháng thay đổi nó ra sao.\n"
"Người ở đây ghi loài vật ấy trong cuốn danh lục của họ dưới cái tên Bulbasaur. Còn trong sổ của tôi, con vật nằm giữa lối mòn hôm ấy mang một mã số, K-01: chữ K là Kanto, tên của cả vùng đất này, còn số 01 vì nó là con đầu tiên tôi chọn để theo.\n"
"Suốt mấy tuần đầu, tôi chỉ biết về nó được chừng ấy: một cái tên loài và một mã số trong sổ.",

"02":
"Viridian là nơi rừng già giáp với đồng cỏ. Ở chỗ giáp ranh ấy có một khoảng đất trống cỏ mọc thấp, người ta gọi là trảng cỏ, và băng ngang trảng cỏ là một lối mòn nhỏ, cỏ rạp cả xuống, do chính đàn Bulbasaur ngày ngày đi qua đi lại mà thành.\n"
"Đàn ở trảng cỏ này có bảy con. K-01 bé nhất đàn, lúc nào cũng lũn cũn đi sau cùng, vậy mà lại là con người ta nhìn thấy trước tiên. Sáu con còn lại khoác lớp da xanh lam lốm đốm như rêu trên đá, còn da K-01 lại màu vàng xanh nhàn nhạt, ấm như lá non đầu mùa, và cái củ trên lưng nó cũng sẫm màu hơn hẳn củ của các bạn cùng đàn.\n"
"Suốt bảy ngày liền, cứ đúng giữa trưa, tôi lại vẽ vào sổ chỗ nằm của từng con. Bảy ngày như một, K-01 đều nằm gọn trong vệt nắng sáng nhất trảng cỏ.\n"
"Người ở đây gọi những con vật mang màu lạ như thế là “shiny”. Nhưng trong sổ của tôi, nó vẫn chỉ là K-01.",

# ---- HỒI 2 · CÁI DẠ DÀY THỨ HAI ---------------------------------------------------
"03":
"Cứ đến giữa trưa, khi nắng lên đỉnh đầu, K-01 lại thôi kiếm ăn mà nằm dài ra, im phăng phắc. Có lần nó nằm im đến mức tôi tưởng mình đã lạc mất nó, phải bò lổm ngổm vòng qua cả một bụi dương xỉ suốt hai mươi phút mới tìm lại được.\n"
"Ba tiếng đồng hồ sau, cái củ trên lưng nó đã căng mọng lên trông thấy, trong khi cái bụng vẫn lép kẹp sát đất như lúc đầu.\n"
"Hoá ra nó chẳng hề nhịn đói, mà đang ăn, chỉ là ăn một thứ khác hẳn cỏ lá.\n"
"Cuốn danh lục của người ở đây có ghi hai dòng nằm cách xa nhau: một dòng nói cái hạt trên lưng lớn lên nhờ nắng, một dòng nói con vật có thể nhịn ăn nhiều ngày liền nhờ phần dự trữ cất trong củ. Tôi mất gần một tháng mới nhận ra hai dòng ấy đang nói về cùng một chuyện.\n"
"Thứ nằm trên lưng nó, nếu được phép gọi theo cách của tôi, chính là một cái dạ dày thứ hai.",

"04":
"Thế nhưng chỉ có nắng thì chưa đủ. Cây cối nào cũng cần thêm nước và khoáng, và tôi phải theo thêm ba tuần nữa mới biết K-01 kiếm hai thứ ấy ở đâu.\n"
"Chiều nào cũng vậy, khi nắng đã ngả vàng, nó lững thững lội ra mép cái ao nhỏ cạnh trảng cỏ, rồi đứng yên rất lâu, hai chân trước lún sâu trong lớp bùn mát lạnh. Mặt nước gợn lên từng vòng, vậy mà chẳng lần nào tôi thấy nó cúi đầu uống lấy một ngụm.\n"
"Còn khoáng, tôi ngờ rằng nó lấy ngay từ bên trong mình. Ở quê tôi, dưới những rạn san hô, có loài tảo sống lẫn trong mô san hô và lấy chính chất thải của vật chủ làm thức ăn.\n"
"Nếu cái củ này cũng sống theo cách ấy, thì nó đang được bón bằng chính những gì cơ thể K-01 thải ra: một vòng tròn khép kín, không rơi rớt đi đâu lấy một giọt.",

"05":
"Đến đây, những trang sổ của tôi bắt đầu rẽ sang một hướng khác.\n"
"Thoạt đầu, tôi đã viết hai chữ “ký sinh”: một thứ bám vào lưng con vật, hút lấy những gì con vật kiếm được mà lớn lên. Rồi tôi gạch đi, vì vật ký sinh thì làm vật chủ gầy mòn, trong khi K-01 lại khoẻ khoắn, nhanh nhẹn nhất vào đúng những ngày nắng gắt nhất.\n"
"Vậy thì con thú đang nuôi cái hạt, hay chính cái hạt đang nuôi con thú?\n"
"Ở quê tôi, ranh giới giữa hai lối sống chung ấy mong manh như sợi tóc. Địa y là nấm và tảo quấn quýt vào nhau chặt đến mức người ta từng ngỡ là một loài, còn cây tầm gửi thì cắm rễ vào thân cây chủ, rút dần rút mòn cho đến khi cây chủ chết khô mà vẫn đứng.",

# ---- HỒI 3 · CHẠM ---------------------------------------------------------------
"06":
"Bảy con Bulbasaur trong đàn chẳng bao giờ nằm sát vào nhau. Con nào cũng giữ riêng cho mình một khoảng trống, vừa đủ rộng để nắng rọi thẳng xuống cái củ trên lưng.\n"
"Chiều xuống, bóng rừng già bò dần ra trảng cỏ, những vệt nắng còn sót lại co lại nhanh như vũng nước bốc hơi, và bấy giờ mới có chuyện chen lấn. Mấy con Bulbasaur ép vai, huých sườn, đẩy nhau dùng dằng, nhưng tuyệt nhiên không con nào cắn con nào, và con nào thua thì lẳng lặng bỏ đi tìm vệt nắng khác.\n"
"Đêm nào K-01 cũng nằm cách một con Bulbasaur to lớn hơn chừng hai thân mình, không xa hơn, cũng không gần hơn, và hai con chưa bao giờ chạm vào nhau.\n"
"Rồi một hôm, con to lớn ấy bị rách một mảng da bên sườn, và từ hôm đó tôi mới phân biệt được con vật ấy giữa đàn. Tôi ghi cho nó một mã số riêng: K-04.\n"
"Đêm ấy, cả đàn dời chỗ nằm, bốn con xích lại quanh K-04 như người ta quây quanh một người ốm, riêng K-01 vẫn nằm nguyên chỗ cũ, cách đúng hai thân mình.",

"07":
"Nói vậy không có nghĩa là những con Bulbasaur ấy chẳng bao giờ chạm vào nhau. Chỉ là chúng không chạm nhau bằng cách nằm cạnh nhau.\n"
"Có những buổi chiều, từ dưới gốc củ của hai con Bulbasaur, hai sợi dây leo thong thả vươn ra, gặp nhau giữa không trung, quấn lấy nhau vài giây như hai bàn tay nắm lấy nhau, rồi buông ra. Tôi đứng xem suốt hai mươi phút mà không viết nổi một chữ nào vào sổ.\n"
"Bởi thứ tôi vừa thấy không phải một cái roi, mà là một cơ quan để cầm nắm, để sờ chạm, để chào hỏi.\n"
"Và còn để giữ mình sạch sẽ nữa. Tấm lưng là chỗ khuất của một con vật bốn chân cổ ngắn, và chiều hôm ấy tôi thấy K-01 vắt một sợi dây leo qua vai, gạt phắt con sâu đang bò lên chân củ, gọn gàng y như con ngựa quất đuôi đuổi ruồi.",

# ---- HỒI 4 · CÁI GIÁ ------------------------------------------------------------
"08":
"Thế nhưng màu da khác lạ ấy cũng có cái giá của nó.\n"
"Vào ngày thứ năm mươi ba, một con chim lớn bắt đầu lượn vòng trên nền trời phía trên trảng cỏ. Cuốn danh lục gọi loài chim ấy là Fearow, và con chim này có một bên mắt đục mờ màu tro, dấu vết của một vết thương cũ. Nó bỏ qua cả đàn, chỉ nhằm theo một mình K-01.\n"
"Nằm dưới tán dương xỉ, lớp da xanh lam lốm đốm của những con Bulbasaur khác tan biến vào những mảng bóng nắng loang lổ, còn lớp da nhàn nhạt của K-01 thì không.\n"
"Ở quê tôi, những con bướm đêm màu nhạt đậu trên thân cây ám khói bồ hóng bị chim bắt nhiều hơn hẳn những con màu sẫm.\n"
"Lần bổ nhào thứ nhất, K-01 không chạy. Nó ép sát người xuống dưới một bụi dương xỉ rồi nằm yên như chết, và chính bụi dương xỉ đã che cho nó, chứ không phải bộ da. Con chim sà xuống, sượt qua chỉ cách một sải tay.\n"
"Đến lần thứ hai, đỉnh củ trên lưng K-01 bỗng hé mở, và một làn bột mịn màu nhạt tung ra, lan toả như khói. Con chim chao đảo, cánh đập loạn xạ, mất hướng, rồi bỏ đi mất hút.",

"09":
"Nhưng điều khiến tôi phải ghi đậm vào sổ lại là những gì xảy ra sau đó.\n"
"Suốt cả buổi chiều hôm ấy, K-01 nằm bẹp dưới bóng râm, không ăn, không nhúc nhích, cũng chẳng buồn ngẩng lên khi tôi lại gần.\n"
"Và cái củ trên lưng nó xẹp hẳn đi, nhìn thấy rõ bằng mắt thường.\n"
"Thứ vừa cứu mạng nó đã phải trả bằng chính cái kho mà nó mất bao nhiêu tuần phơi nắng mới tích được.\n"
"Từ hôm ấy, tôi thôi không ghi những chuyện như thế vào mục “khả năng” nữa, mà mở hẳn một trang mới, kẻ làm hai cột: thu, và chi.",

# ---- HỒI 5 · CÙNG MỘT CƠ QUAN ----------------------------------------------------
"10":
"Vùng đất này có một điều mà quê tôi không có: người ta cho những con vật như thế này đấu với nhau.\n"
"Một buổi chiều, tôi xuống một thị trấn nhỏ dưới chân rừng, chen vào đứng ở vòng ngoài một sân đất nện, và xem trọn một trận.\n"
"Trong sân, những sợi dây leo không còn vươn ra để chào nhau nữa. Chúng vụt ra nhanh như gió, quất xuống nền đất nện nghe chát chúa như tiếng roi da, bụi đất tung lên thành từng vệt.\n"
"Vẫn là cơ quan ấy: trong rừng thì hái quả và gạt sâu, vào sân thì thành vũ khí. Tôi không phán xét chuyện đó, bởi ở quê tôi, cái vòi voi cũng vừa âu yếm được voi con, vừa bẻ gãy được cả một cành cây lớn.\n"
"Nhưng có một khoảnh khắc khiến tôi ngồi viết đến tận sáng. Con vật trong sân bỗng đứng khựng lại một nhịp, cái củ trên lưng rực sáng lên từ bên trong như ngọn đèn lồng, rồi mới phóng ra một luồng sáng chói loà.\n"
"Đám đông quanh tôi chê nhịp chờ ấy là điểm yếu. Còn tôi thì thấy cả một kho nắng tích từ ban trưa bị tiêu sạch chỉ trong một hơi thở.\n"
"Sáng hôm sau trở về rừng, tôi đã thấy K-01 nằm sẵn trong vệt nắng đầu tiên.",

"11":
"Những người nuôi loài vật này lâu năm bảo rằng loài nào cũng có một nết riêng, riêng loài này thì có đến hai.\n"
"Nết thứ nhất, tôi đã tự mình đo được trước khi có ai kể. Dưới cái nắng gắt giữa trưa, K-01 đi hết cùng một quãng đường nhanh gần gấp đôi so với lúc trời râm, và tôi đã cầm đồng hồ bấm giờ không biết bao nhiêu lần. Một cơ thể chạy bằng nắng thì nắng càng gắt, nó càng khoẻ.\n"
"Nết thứ hai thì tôi chỉ thấy trong sân đấu, và nó khiến tôi bứt rứt hơn là thán phục. Khi một con Bulbasaur đã bị thương nặng, lảo đảo gần như không đứng vững, những cú đánh của con vật ấy bỗng mạnh lên một cách lạ lùng.\n"
"Tôi không nghĩ con vật ấy khoẻ thêm. Tôi nghĩ nó đang dốc cạn chút dự trữ cuối cùng, dồn hết vào một lần duy nhất.\n"
"Ở quê tôi, cây thùa tích góp suốt mấy chục năm trời chỉ để dồn hết vào một lần trổ hoa, rồi lặng lẽ chết đi.",

# ---- HỒI 6 · ĐỔI HÌNH -----------------------------------------------------------
"12":
"Sang tháng thứ tư, K-01 bắt đầu đổi nếp.\n"
"Nó nằm phơi nắng lâu hơn hẳn, bỏ cả giấc trú trưa quen thuộc dưới bóng râm, và ăn nhiều hơn trước. Bước chân nó chậm lại, nặng nề, còn hai sợi dây leo thì dày lên, trĩu xuống, như thể chính nó cũng không còn điều khiển nổi.\n"
"Có một buổi sáng, tôi ngồi yên suốt ba tiếng đồng hồ chỉ để ghi lại đúng một chi tiết.\n"
"Cái đầu của K-01 quay về hướng nam và nằm im, không nhúc nhích. Nhưng cái củ trên lưng nó thì cứ chầm chậm xoay về hướng đông, bám theo mặt trời đang lên.\n"
"Hai phần của cùng một cơ thể, quay về hai phía khác nhau, trong cùng một buổi sáng.\n"
"Đó là dấu hiệu rõ ràng nhất tôi từng có rằng trong thân thể nhỏ bé ấy đang có hai sự sống. Vậy mà tôi vẫn không dám nói bên nào đang nuôi bên nào.\n"
"Ở quê tôi, những bông hướng dương non cũng quay theo mặt trời suốt ngày, đến khi nở hẳn thì đứng yên, và mãi mãi hướng về phía đông.",

"13":
"Cuối tháng ấy, K-01 rời đàn, một mình đi sâu vào rừng già, và tôi mất dấu nó suốt bốn ngày.\n"
"Ở lại trảng cỏ, sáng nào K-04 cũng nằm đúng chỗ cũ, bên cạnh một khoảng trống rộng bằng hai thân mình, và không con nào trong đàn vào nằm chỗ trống ấy.\n"
"Đến đêm thứ năm, tôi tìm thấy K-01 trong một hõm đất khuất sau vòng cây cổ thụ. Nó đứng thành một vòng tròn cùng mười một con Bulbasaur khác, lặng im, không con nào chạm vào con nào, và giữa những lớp da xanh lam dưới ánh trăng, chỉ có mình nó là nhạt màu.\n"
"Người ở đây kể rằng mỗi năm, loài vật này lại tụ về chốn ấy một lần. Họ gọi nơi đó là Khu Vườn Kỳ Bí.\n"
"Đêm ấy, tôi đã tin rằng nó tìm đến đó để chết, và tôi đã ngồi viết kín cả một trang sổ về chuyện ấy.",

"14":
"Tôi không được tận mắt thấy giây phút ấy. Sau hai đêm thức trắng, tôi thiếp đi lúc nào không biết, và khi tỉnh dậy thì trời đã rạng, hõm đất đã trống trơn.\n"
"Thế nhưng cái đêm ấy vẫn để lại đủ dấu vết cho một người quen đọc mặt đất.\n"
"Đất bị cày lên thành những rãnh ngắn, chỗ bốn bàn chân đã bấu chặt xuống để gánh một sức nặng mới. Cỏ bẹp dí thành một vòng tròn, rải rác trên mặt đất là những bẹ lá già khô queo, bong ra và cuộn tròn như vỏ hành, và khắp hõm đất sực nức một mùi hương hoa mà trước đó tôi chưa từng ngửi thấy ở loài này.\n"
"Bên kia bãi cỏ, trong làn sương sớm, thấp thoáng những bóng hình to lớn. Đó là những con Ivysaur, con nào trên lưng cũng mang một nụ hoa màu hồng.\n"
"Riêng một con mang trên lưng một nụ hoa màu vàng.\n"
"Da nó giờ đã chuyển sang màu xanh lá, không còn nhàn nhạt như trước, nhưng cái nụ thì vàng óng, và tôi biết ngay đó là ai.\n"
"Sinh vật đứng trước mặt tôi không còn là con vật tôi từng ghi chép. Vậy mà khi tôi mở sổ ra, nó vẫn nghiêng đầu về phía tiếng ngòi bút sột soạt, như bao lần trước.",

# ---- HỒI 7 · KHÔNG CÓ CÂU TRẢ LỜI ------------------------------------------------
"15":
"Giờ đây, cái nụ trên lưng K-01 đã nặng đến mức nó không thể đứng lên bằng hai chân sau được nữa. Bốn chân và thân mình nó đã dày ra, chắc nịch như những cây cột nhỏ, để gánh lấy sức nặng ấy.\n"
"Vào mùa mưa cuối cùng được ghi trong cuốn sổ này, tôi gặp một con Venusaur cái rất già sống ở bìa rừng. Thân con Venusaur ấy đã hoá gỗ sần sùi, rêu và dương xỉ con mọc kín cả lưng, bông hoa to trên lưng đã phai màu theo năm tháng. Người ở đây bảo con Venusaur già đã ở bìa rừng từ trước khi ông bà họ ra đời.\n"
"Chính giữa bông hoa ấy có một cái nhụy, thứ mà những con khác tôi từng gặp đều không có. Đó là một con cái, và cũng là lần đầu tiên tôi phân biệt được giới tính của loài này bằng mắt thường.\n"
"Còn nụ hoa của K-01 thì vẫn chưa nở. Sau mười bốn tháng ròng, tôi vẫn chưa biết mình đã theo một con đực hay một con cái.\n"
"Sau mỗi trận mưa, hương hoa của con Venusaur già lại đậm hẳn lên. Có lần, tôi thấy hai con Bulbasaur đang gầm gừ giành nhau một chỗ nằm bỗng dịu hẳn lại, rồi cùng nằm xuống cách nhau vài bước, trong làn hương ấy, và cứ thế nằm yên.\n"
"Đến tận bây giờ, tôi vẫn không biết cái hạt trên lưng K-01 là một phần của nó, hay là một sự sống khác đang nương nhờ nó. Có lẽ câu trả lời không nằm ở cách chúng ta gọi tên. Có lẽ một cơ thể có thể bắt đầu từ hai sự sống, mà rồi vẫn thành một.\n"
"Ở trang sau của cuốn danh lục là một loài mang ngọn lửa ở chóp đuôi. Nếu ngọn lửa ấy tắt đi trong mưa, con vật ấy sẽ sống sót bằng cách nào?",

"short-outro":
"Con thú đang nuôi cái hạt, hay chính cái hạt đang nuôi con thú?\n"
"Sau mười bốn tháng ròng rã ngoài thực địa, tôi vẫn chưa tìm được câu trả lời.",
}

BEATS_EN = {
"00":
"It was an early-summer noon in Viridian Forest. The sun beat down on the trail until it glared white, the air too lazy even to stir the grass, and in the middle of that trail lay a small animal, flat on its belly, legs stretched out, the dark green bulb on its back as still as a moss-covered stone.\n"
"I watched it for a long time, and I was certain it was dead.\n"
"Then the bulb on its back swelled, very slightly, and sank again, slow as a ribcage. The animal was breathing, and not, it seemed, only with its lungs.",

"01":
"I came to this land carrying a question that had followed me for years: whether there are creatures in which life and energy are wound together so tightly that they can no longer be pulled apart.\n"
"To answer it, I did what researchers back home do with a pack of wolves or a herd of elephants: choose a single animal, follow it quietly for a long time, and see what the months do to it.\n"
"The people here list the species in their catalogue under the name Bulbasaur. In my notebook, the animal lying on the trail that day was given a field code, K-01: K for Kanto, the name of this whole region, and 01 because it was the first animal I chose to follow.\n"
"For the first few weeks, that was all I knew of it: the name of a species, and a code in a notebook.",

"02":
"Viridian is where the old forest meets the grassland. Along that border lies an open patch of short grass, a clearing, and across the clearing runs a narrow trail of flattened stems, worn there by the herd of Bulbasaur walking the same way, day after day.\n"
"There are seven of them in this herd. K-01 is the smallest, always trotting along at the back, and yet it is the one you notice first. The other six wear a blotched blue-green skin, like moss on stone, while K-01's skin is a pale, warm yellow-green, the colour of a new leaf, and the bulb on its back is darker than any of theirs.\n"
"For seven days running, at exactly noon, I sketched where each animal lay. On every one of those seven days, K-01 lay curled in the brightest patch of sun in the whole clearing.\n"
"People here call animals with such unusual colouring “shiny”. In my notebook, it was still simply K-01.",

"03":
"Every day at noon, when the sun stood straight overhead, K-01 stopped foraging and stretched out, perfectly still. Once it lay so still that I thought I had lost it, and I spent twenty minutes crawling on my elbows around a clump of ferns before I found it again.\n"
"Three hours later, the bulb on its back had visibly filled out and tightened, while its belly still lay as flat against the ground as when it began.\n"
"So it was not going hungry at all; it was eating, only eating something that was neither grass nor leaf.\n"
"The people's catalogue holds two lines written far apart: one says the seed on its back grows by taking in sunlight, the other that the animal can go for days without food by living on what the bulb has stored. It took me nearly a month to see that the two lines were describing the same thing.\n"
"The thing on its back, if I may put it my own way, is a second stomach.",

"04":
"Yet sunlight alone is not enough. Every plant needs water and minerals as well, and it took me another three weeks of following K-01 to learn where it finds them.\n"
"Every afternoon, once the light had turned golden, it would amble down to the edge of a small pond beside the clearing and stand there for a long while, both front feet sunk deep in the cool mud. Rings spread slowly across the water, and yet not once did I see it lower its head to drink.\n"
"As for the minerals, I suspect they come from inside the animal itself. Back home, beneath the coral reefs, there are algae that live inside the coral's own tissue and feed on the waste of their host.\n"
"If this bulb lives the same way, then it is being fed on whatever K-01's body throws away: a closed circle, in which not a single drop is lost.",

"05":
"From here on, the pages of my notebook began to turn in a different direction.\n"
"At first I had written one word, “parasite”: something that clings to an animal's back and grows on whatever the animal manages to find. Then I crossed it out, because a parasite leaves its host thin and worn, while K-01 was at its liveliest and quickest on the very fiercest days of sun.\n"
"So is the animal feeding the seed, or is the seed feeding the animal?\n"
"Back home, the line between those two ways of living together is as thin as a hair. A lichen is a fungus and an alga bound so closely that we once took them for a single species, while a mistletoe drives its roots into its host and drains it, little by little, until the tree dies standing.",

"06":
"The seven Bulbasaur of the herd never lie pressed together. Each one keeps a space of its own, just wide enough for the sun to fall straight onto the bulb on its back.\n"
"As evening comes and the shadow of the old forest creeps out across the clearing, the last patches of sunlight shrink as fast as puddles drying in the heat, and only then does the jostling begin. The animals lean shoulder against shoulder and shove one another back and forth, yet not one of them ever bites, and whichever gives way simply wanders off in search of another patch of light.\n"
"Every night, K-01 lies about two body-lengths from a much larger Bulbasaur, never nearer and never farther, and the two of them have never once touched.\n"
"Then one day that larger animal tore a strip of skin from its flank, and from then on I could pick it out from the rest of the herd. I gave it a field code of its own: K-04.\n"
"That night the whole herd rearranged itself: four animals shuffled in close around K-04, the way people gather round someone who is ill, while K-01 stayed exactly where it always lay, two body-lengths away.",

"07":
"That is not to say these Bulbasaur never touch one another. They simply do not touch by lying side by side.\n"
"On some afternoons, two vines would slip out from beneath the bulbs of two Bulbasaur, meet in the air, and wind around each other for a few seconds, like two hands clasping, before letting go. I stood watching for twenty minutes and could not write a single word.\n"
"Because what I had just seen was not a whip, but an organ for holding, for feeling, for greeting.\n"
"And for keeping clean as well. The back is out of reach for a short-necked animal on four legs, and that afternoon I watched K-01 swing a vine over its shoulder and flick a caterpillar off the base of its bulb, as neatly as a horse swishing its tail at a fly.",

"08":
"And yet that unusual colour has its price.\n"
"On the fifty-third day, a large bird began to circle high over the clearing. The catalogue calls this kind of bird Fearow, and this one had an eye clouded ash-grey, the mark of some old wound. The bird paid no attention to the rest of the herd; it followed K-01 alone.\n"
"Lying beneath the ferns, the blotched blue-green skin of the other Bulbasaur melts away into the broken patches of shade, while K-01's pale skin does not.\n"
"Back home, pale moths resting on bark blackened with soot were taken by birds far more often than the dark ones.\n"
"On the first dive, K-01 did not run. It pressed itself flat beneath a clump of ferns and lay as still as death, and it was the ferns that hid it, not its skin. The bird swept down and passed by barely an arm's length away.\n"
"On the second dive, the top of the bulb on K-01's back split open and a fine, pale powder burst out, spreading like smoke. The bird lurched, wings beating wildly, lost its line, and was gone.",

"09":
"But what made me press hardest on my pencil that day was what came afterwards.\n"
"All through that afternoon, K-01 lay flattened in the shade, not eating, not moving, not even lifting its head when I came close.\n"
"And the bulb on its back had shrunk, plainly, to the naked eye.\n"
"What had just saved its life had been paid for out of the very store it had spent weeks of sunshine filling.\n"
"From that day on, I stopped writing such things under the heading “abilities”, and instead opened a fresh page and ruled it into two columns: income, and expense.",

"10":
"This land has something that my home does not: people set animals like these to fight one another.\n"
"One afternoon I went down to a small town at the foot of the forest, squeezed into the outer ring of a yard of beaten earth, and watched a whole match.\n"
"In that yard, the vines no longer reached out to greet. They shot out fast as the wind and cracked down onto the hard earth with a sound as sharp as a whip, throwing up streaks of dust.\n"
"It was the same organ: in the forest it picks fruit and brushes off caterpillars, and in the yard it became a weapon. I pass no judgement on that, for back home an elephant's trunk can caress a newborn calf, and it can also tear a great branch from a tree.\n"
"But one moment kept me writing until dawn. The animal in the yard suddenly stood stock-still for a beat, the bulb on its back glowing from within like a lantern, and only then did it release a blinding beam of light.\n"
"The crowd around me jeered at that pause as a weakness. What I saw was a whole noon's store of sunlight spent in a single breath.\n"
"The next morning, back in the forest, I found K-01 already lying in the first patch of sun.",

"11":
"People who have raised these animals for years say that every kind has a temperament of its own, and that this kind has two.\n"
"The first I had measured for myself before anyone told me of it. Under the harsh noon sun, K-01 covered the same stretch of ground almost twice as fast as it did when the sky was overcast, and I timed it with a stopwatch more times than I can count. A body that runs on sunlight runs harder the fiercer the sun.\n"
"The second I saw only in the fighting yard, and it unsettled me more than it impressed me. When a Bulbasaur has been badly hurt and is swaying, barely able to stand, its blows suddenly grow strangely strong.\n"
"I do not believe the animal grows stronger. I believe it is pouring out the very last of its reserve, all of it, at once.\n"
"Back home, the agave gathers its strength for decades, only to spend it all on a single flowering, and then quietly dies.",

"12":
"In the fourth month, K-01 began to change its ways.\n"
"It lay out in the sun far longer than before, gave up its familiar midday rest in the shade, and ate more than it ever had. Its steps grew slow and heavy, and its two vines thickened and hung down, as if it could no longer quite steer them.\n"
"One morning I sat without moving for three hours, just to record a single detail.\n"
"K-01's head was turned to the south and lay perfectly still. But the bulb on its back was turning, slowly, toward the east, following the rising sun.\n"
"Two parts of one body, facing two different ways, on the very same morning.\n"
"It is the clearest sign I have ever had that two lives share that small body. And still I dare not say which one is feeding the other.\n"
"Back home, young sunflowers turn to follow the sun all day long, until, once they are in full bloom, they stop, and face the east for good.",

"13":
"At the end of that month, K-01 left the herd and wandered alone, deep into the old forest, and for four days I lost all trace of it.\n"
"Back in the clearing, K-04 lay every morning in exactly the same place, beside an empty space two body-lengths wide, and not one animal in the herd ever lay down in that space.\n"
"On the fifth night, I found K-01 in a hollow hidden behind a ring of ancient trees. It stood in a circle with eleven other Bulbasaur, silent, none of them touching, and among all that blue-green skin under the moon, it alone was pale.\n"
"The people here say that once every year, these animals gather in that place. They call it the Mysterious Garden.\n"
"That night I believed K-01 had come there to die, and I sat and filled an entire page of my notebook about it.",

"14":
"I did not witness the moment itself. After two nights without sleep I drifted off without knowing it, and when I woke the sky was already light and the hollow stood empty.\n"
"And yet that night had left enough behind for someone used to reading the ground.\n"
"The earth was churned into short furrows where four feet had braced themselves to carry a new weight. The grass lay crushed flat in a circle, old dry bracts lay scattered over the ground, come loose and curled up like onion skin, and the whole hollow was steeped in the scent of flowers, a scent I had never once smelled on this species.\n"
"Across the grass, in the early mist, large shapes loomed. They were Ivysaur, and every one of them carried a pink flower bud on its back.\n"
"All except one, which carried a bud of yellow.\n"
"Its skin had turned leaf-green now, no longer pale as before, but the bud was a shining gold, and I knew at once who it was.\n"
"The creature before me was no longer the animal I had been recording. And yet, when I opened my notebook, it tilted its head toward the scratch of my pen, just as it always had.",

"15":
"By now the bud on K-01's back has grown so heavy that it can no longer rise onto its hind legs. Its legs and body have thickened, sturdy as little pillars, to carry the weight.\n"
"In the last rainy season recorded in this notebook, I met a very old female Venusaur living at the edge of the forest. Her trunk had turned to rough bark, moss and young ferns had grown all over her back, and the great flower she carried had faded with the years. The people here say the old Venusaur was at the forest edge before their grandparents were born.\n"
"At the very centre of her flower was a pistil, something none of the others I had met possessed. She was female, and it was the first time I could tell the sexes of this species apart with my own eyes.\n"
"K-01's bud, though, has not yet opened. After fourteen long months, I still do not know whether I have been following a male or a female.\n"
"After every rain, the old Venusaur's scent grows heavier. Once, I watched two Bulbasaur that had been snarling over a place to lie suddenly soften, then lie down a few steps apart inside that fragrance, and stay there, quite still.\n"
"To this day, I do not know whether the seed on K-01's back is a part of it, or another life taking shelter on it. Perhaps the answer does not lie in what we choose to call it. Perhaps a body can begin as two lives, and still become one.\n"
"On the next page of the catalogue is a creature that carries a flame at the tip of its tail. If that flame goes out in the rain, how does it survive?",

"short-outro":
"Is the animal feeding the seed, or is the seed feeding the animal?\n"
"After fourteen long months in the field, I still have not found the answer.",
}

# Phiên âm cho TTS (VBee): chữ trên màn hình vẫn giữ chính tả gốc. Nghe thử rồi chỉnh.
PRON = {
    "Bulbasaur": "bôn-ba-xo",
    "Ivysaur": "ai-vi-xo",
    "Venusaur": "vi-nu-xo",
    "Kanto": "can-tô",
    "Fearow": "phia-râu",
    "Viridian": "vi-ri-đi-an",
    "K-01": "ca không một",
    "K-04": "ca không bốn",
    "shiny": "sai-ni",
}

# Nguồn cho từng câu canon — soát lại trước khi thu giọng. Khoá theo nghĩa, không theo chữ.
NGUON = {
    "hạt trên lưng; ngủ dưới nắng, hạt hấp thụ nắng mà lớn": "Pokédex Ruby/Sapphire/Emerald",
    "nhịn ăn nhiều ngày, dự trữ trong củ": "Pokédex Yellow",
    "màu Shiny: thân vàng-xanh nhạt, củ sẫm; Shiny Ivysaur nụ vàng; giữ qua đổi hình": "Bulbapedia — Shiny Pokémon",
    "bung bột mịn làm kẻ tấn công lả đi (không gọi tên)": "Sleep Powder, Gen I — Bulbapedia",
    "nạp sáng trong củ, đứng im một nhịp rồi phóng (không gọi tên)": "Solar Beam, lượt nạp — Bulbapedia",
    "hai nết: nắng gắt → nhanh gấp đôi; kiệt sức → đòn mạnh hơn (không gọi tên, không nói hệ số)": "Chlorophyll; Overgrow — Bulbapedia",
    "phơi nắng nhiều hơn thường lệ = sắp nở; toả hương khi sắp nở": "Pokédex Ruby; Blue/Silver (Ivysaur)",
    "mất khả năng đứng bằng hai chân sau; chân và thân dày lên": "Pokédex Red/LeafGreen/Sword; Ruby/Emerald",
    "con cái có nhụy giữa hoa": "Bulbapedia — Venusaur, gender differences",
    "sau mưa hương đậm hơn; hương làm nguôi kẻ đang giao chiến": "Pokédex Venusaur; Ruby/Sapphire; FireRed",
    "mỗi năm tụ về một chỗ khuất rồi cùng đổi hình (🎬, kể như lời người bản xứ)": "anime tập 51 — Bulbapedia, mục Biology",
    "Viridian Forest": "Pokémon: Let's Go, Pikachu!/Eevee!",
    "ĐỐI CHIẾU TRÁI ĐẤT (soát nguồn trước khi thu)":
        "lõi: tảo cộng sinh trong mô san hô dùng lại chất thải của vật chủ · địa y cộng sinh / cây tầm gửi ký sinh · "
        "vòi voi (vuốt ve và bẻ cành) · bướm sâu đo Biston betularia, dạng nhạt trên vỏ cây ám khói bị chim bắt nhiều hơn "
        "(Kettlewell 1955; Cook et al. 2012) · hướng dương non quay theo mặt trời, nở rồi đứng yên hướng đông "
        "(Atamian et al. 2016) — tuỳ chọn (2/2): đuôi ngựa xua ruồi · cây thùa dồn cả đời vào một lần trổ hoa",
}
