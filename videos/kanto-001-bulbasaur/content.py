# Creature Field Guide — Kanto #001 · "Ai đang nuôi ai?" · V4
#
# Luồng: 2-skeleton.md (Claude) → 3-script-gemini.md (Gemini) → bản này (Claude chuẩn hoá).
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
"Ngày đầu tiên tôi gặp nó, nó nằm bất động giữa lối mòn dưới nắng trưa.\n"
"Tôi tưởng nó đã chết.\n"
"Rồi cái hạt trên lưng nó khẽ co lại. Nó đang thở, và không phải chỉ bằng phổi.",

"01":
"Tôi mang theo một câu hỏi từ nhiều năm nay: có những sinh vật mà sự sống và năng lượng không thể tách rời.\n"
"Nên tôi làm cái việc ở quê tôi người ta vẫn làm với sói và voi: chọn một con, đi theo nó, xem điều gì thay đổi.\n"
"Cuốn danh lục gọi loài này là Bulbasaur. Sổ của tôi gọi nó là K-01.\n"
"Suốt mấy tuần đầu, nó chỉ có chừng ấy: một chữ cái và một con số.",

"02":
"Viridian là nơi rừng già chạm vào đồng cỏ. Giữa hai thứ ấy có một lối mòn cỏ rạp, và chính chúng đã dẫm ra nó.\n"
"Trảng này có bảy con. K-01 nhỏ nhất, và lúc nào cũng đi sau cùng. Vậy mà nó lại là con đập vào mắt đầu tiên.\n"
"Da nó màu vàng xanh nhạt, ấm, trong khi những con kia xanh lam. Và cái củ trên lưng nó sẫm hơn củ của chúng.\n"
"Suốt bảy ngày, tôi vẽ lại chỗ từng con nằm lúc giữa trưa. Ngày nào K-01 cũng chiếm vệt nắng sáng nhất.\n"
"Người ở đây gọi những con như thế là “shiny”. Trong sổ tôi, nó vẫn chỉ là K-01.",

# ---- HỒI 2 · CÁI DẠ DÀY THỨ HAI ---------------------------------------------------
"03":
"Giữa trưa, K-01 thôi kiếm ăn và nằm im. Có lần tôi mất dấu nó hẳn, phải bò qua bụi dương xỉ hai mươi phút mới tìm ra.\n"
"Ba tiếng sau, cái hạt trên lưng nó căng tròn. Còn bụng thì vẫn phẳng.\n"
"Nó không nhịn đói. Nó đang ăn một thứ khác.\n"
"Cuốn danh lục có hai dòng ghi rời nhau: nắng làm cái hạt lớn lên, và con vật nhịn ăn được nhiều ngày nhờ phần dự trữ trong củ. Tôi mất gần một tháng mới ghép được hai dòng ấy lại.\n"
"Thứ trên lưng nó là một cái dạ dày thứ hai.",

"04":
"Nhưng chỉ có nắng thì chưa đủ. Một cái cây còn cần nước và khoáng, và tôi mất thêm ba tuần mới thấy K-01 lấy chúng ở đâu.\n"
"Cuối chiều, nó lội ra mép ao, đứng rất lâu, hai chân trước lún trong bùn. Nó không hề cúi xuống uống.\n"
"Còn khoáng, tôi ngờ là đến từ bên trong. Ở quê tôi, loài tảo sống trong mô san hô lấy chính chất thải của vật chủ làm thức ăn.\n"
"Nếu cái củ cũng vậy, thì nó đang được bón bằng thứ mà cơ thể K-01 thải ra. Một vòng khép kín. Không rơi mất giọt nào.",

"05":
"Tới đây, cuốn sổ của tôi rẽ sang hướng khác.\n"
"Ban đầu tôi viết: vật ký sinh. Một thứ bám vào, hút, và lớn lên bằng những gì vật chủ kiếm được. Rồi tôi gạch đi. Ký sinh không làm vật chủ no, mà K-01 lại khoẻ nhất vào những ngày nắng gắt nhất.\n"
"Con thú đang nuôi cái hạt, hay cái hạt đang nuôi con thú?\n"
"Ở quê tôi, ranh giới giữa hai lối sống chung ấy mỏng như sợi tóc. Địa y là nấm và tảo gắn chặt tới mức người ta từng tưởng là một loài. Còn cây tầm gửi cắm rễ vào thân cây chủ, cho tới khi cây chủ chết đứng.",

# ---- HỒI 3 · CHẠM ---------------------------------------------------------------
"06":
"Bảy con không bao giờ nằm sát nhau. Con nào cũng giữ một khoảng trống đủ để nắng chạm xuống lưng mình.\n"
"Chiều xuống, bóng rừng bò dần qua trảng, những vệt nắng co lại rất nhanh, và cuộc chen lấn bắt đầu. Chúng ép vai, không bao giờ cắn. Con thua bỏ đi.\n"
"K-01 ngủ cách một con lớn hơn chừng hai thân. Đêm nào cũng đúng khoảng ấy. Hai con chưa bao giờ chạm vào nhau.\n"
"Hôm con lớn kia bị rách một mảng da bên sườn, tôi cho nó một mã: K-04. Một con vật chỉ có mã khi tôi phân biệt được nó.\n"
"Đêm ấy, bốn con dời chỗ nằm quanh K-04. K-01 vẫn nằm đúng chỗ cũ.",

"07":
"Chúng có chạm vào nhau. Chỉ là không phải lúc nằm nghỉ.\n"
"Hai sợi dây leo thò ra từ dưới củ, gặp nhau giữa không trung, quấn lấy nhau vài giây rồi buông. Tôi đứng nhìn hai mươi phút mà không viết nổi một chữ.\n"
"Đó không phải cái roi. Đó là một cơ quan để cầm, để chạm, để chào.\n"
"Và để giữ mình sạch sẽ. Lưng là điểm mù của một con vật bốn chân, cổ ngắn. Chiều hôm ấy, K-01 vẩy một sợi dây leo qua vai, gạt phắt con sâu đang bò ở chân củ, y như con ngựa quất đuôi đuổi ruồi.",

# ---- HỒI 4 · CÁI GIÁ ------------------------------------------------------------
"08":
"Màu da ấy có cái giá của nó.\n"
"Ngày thứ năm mươi ba, một con chim lớn bắt đầu lượn vòng trên cao. Danh lục ghi nó là Fearow. Một bên mắt nó đục màu tro vì một vết thương cũ. Nó chỉ bám theo K-01.\n"
"Dưới tán dương xỉ, bộ da xanh lam lốm đốm của những con kia tan vào bóng nắng loang lổ. Còn da nhạt màu của K-01 thì không.\n"
"Ở quê tôi, những con bướm đêm màu nhạt đậu trên vỏ cây ám khói bị chim bắt nhiều hơn hẳn những con sẫm màu.\n"
"Cú bổ nhào đầu tiên, K-01 không chạy. Nó ép sát mình dưới một bụi dương xỉ và đứng im. Bụi dương xỉ che nó, chứ không phải bộ da. Con chim trượt qua cách một sải tay.\n"
"Cú thứ hai, đỉnh củ hé ra và một làn bột mịn bung lên. Con chim chao đảo, mất hướng, rồi bỏ đi.",

"09":
"Điều tôi gạch chân lại đến sau đó.\n"
"K-01 nằm im suốt buổi chiều. Không ăn, không nhúc nhích, không phản ứng khi tôi lại gần.\n"
"Và cái củ nhỏ đi thấy rõ.\n"
"Thứ vừa cứu mạng nó được trả bằng đúng cái kho mà nó đã phơi nắng hàng tuần để tích.\n"
"Từ hôm ấy, tôi thôi ghi những thứ này vào mục khả năng. Tôi mở một cuốn sổ: thu, và chi.",

# ---- HỒI 5 · CÙNG MỘT CƠ QUAN ----------------------------------------------------
"10":
"Vùng đất này có một thứ mà quê tôi không có: người ta cho những con vật này đấu với nhau.\n"
"Tôi xuống một thị trấn, đứng ở vòng ngoài một sân đất, xem một trận.\n"
"Trong sân, dây leo không chào nhau nữa. Chúng quất.\n"
"Cùng một cơ quan: trong rừng để hái quả và gạt sâu, trong sân để đánh. Tôi không phán xét điều đó. Ở quê tôi, vòi voi vừa vuốt ve voi con, vừa bẻ gãy được cả một cành cây.\n"
"Có một khoảnh khắc làm tôi ngồi viết tới sáng. Con vật đứng im một nhịp, cái củ sáng lên từ bên trong, rồi mới phóng ra một luồng sáng.\n"
"Đám đông coi nhịp chờ ấy là điểm yếu. Tôi thì thấy cả kho nắng ban trưa bị tiêu sạch trong một hơi thở.\n"
"Sáng hôm sau về lại rừng, K-01 đã nằm sẵn trong vệt nắng đầu tiên.",

"11":
"Những người nuôi loài này lâu năm bảo mỗi loài có một nết. Loài này có hai.\n"
"Nết thứ nhất tôi tự đo được trước khi ai kể. Dưới nắng gắt giữa trưa, K-01 đi hết cùng một quãng đường nhanh gần gấp đôi lúc trời râm. Tôi đã bấm giờ. Một cơ thể chạy bằng nắng thì nắng càng gắt, nó càng khoẻ.\n"
"Nết thứ hai tôi chỉ thấy trong sân đấu, và nó làm tôi khó chịu hơn là thán phục. Khi con vật đã bị thương nặng, gần như không đứng nổi, những cú đánh của nó bỗng mạnh hẳn lên.\n"
"Tôi không nghĩ nó khoẻ hơn. Tôi nghĩ nó đang dốc nốt phần dự trữ cuối cùng. Một lần. Rồi hết.\n"
"Ở quê tôi, cây thùa tích mấy chục năm chỉ để dồn cả vào một lần trổ hoa, rồi chết.",

# ---- HỒI 6 · ĐỔI HÌNH -----------------------------------------------------------
"12":
"Sang tháng thứ tư, K-01 đổi nếp.\n"
"Nó nằm ngoài nắng lâu hơn hẳn, bỏ cả nhịp trú trưa, và ăn nhiều hơn. Nó đi chậm lại. Hai sợi dây leo dày lên, trĩu xuống, như thể nó không còn điều khiển được chúng.\n"
"Có một buổi sáng tôi ngồi ba tiếng chỉ để ghi một chi tiết.\n"
"Đầu K-01 quay về hướng nam và không nhúc nhích. Nhưng cái củ trên lưng thì xoay chậm về hướng đông, theo mặt trời.\n"
"Hai phần của cùng một cơ thể, quay về hai hướng, trong cùng một buổi sáng.\n"
"Đó là dấu hiệu rõ nhất tôi có được rằng trong thân thể này có hai sự sống. Vậy mà tôi vẫn không nói được con nào đang nuôi con nào.\n"
"Ở quê tôi, hoa hướng dương non quay theo mặt trời suốt ngày. Tới khi nở hẳn thì đứng yên, nhìn mãi về hướng đông.",

"13":
"Cuối tháng ấy, K-01 rời đàn, đi vào rừng già. Tôi mất dấu nó bốn ngày.\n"
"K-04 ở lại. Sáng nào nó cũng nằm đúng chỗ cũ, cạnh một khoảng trống bằng hai thân. Không con nào vào nằm chỗ ấy.\n"
"Đêm thứ năm, tôi tìm thấy K-01 trong một hõm đất sau vành cây cổ thụ, đứng thành vòng cùng mười một con khác, lặng im, không con nào chạm con nào. K-01 là con nhạt màu duy nhất.\n"
"Người ở đây kể rằng mỗi năm chúng tụ về đây một lần. Họ gọi nơi này là Khu Vườn Kỳ Bí.\n"
"Lúc ấy tôi tưởng nó đến đó để chết. Tôi đã viết nguyên một trang về chuyện ấy.",

"14":
"Tôi không được thấy khoảnh khắc ấy. Sau hai đêm thức trắng tôi thiếp đi, và khi tỉnh dậy lúc rạng sáng, hõm đất đã trống không.\n"
"Nhưng nó để lại đủ cho một người biết đọc mặt đất.\n"
"Đất bị cày thành những rãnh ngắn, chỗ bốn bàn chân đã bấu xuống để đỡ một sức nặng mới. Cỏ bẹp thành một vòng tròn. Trên mặt đất rải rác những bẹ lá già khô, bong ra, cuộn lại như vỏ hành. Và cả hõm đất sực mùi hoa, thứ mùi tôi chưa từng ngửi thấy ở loài này.\n"
"Bên kia bãi cỏ, trong sương, có những cái bóng lớn. Những con kia mang nụ màu hồng.\n"
"Một con mang nụ màu vàng.\n"
"Da nó giờ đã xanh lá, không còn nhạt màu nữa, nhưng cái nụ thì vàng óng, và tôi biết.\n"
"Thứ đứng đó không còn là con vật tôi từng ghi chép. Nhưng khi tôi mở sổ, nó vẫn nghiêng đầu về phía tiếng bút.",

# ---- HỒI 7 · KHÔNG CÓ CÂU TRẢ LỜI ------------------------------------------------
"15":
"Cái nụ giờ nặng tới mức K-01 không đứng lên bằng hai chân sau được nữa. Chân và thân nó đã dày ra để đỡ.\n"
"Mùa mưa cuối cùng trong cuốn sổ này, tôi gặp một con Venusaur cái rất già ở bìa rừng. Thân nó đã hoá gỗ. Rêu và dương xỉ nhỏ mọc kín lưng, bông hoa lớn đã phai màu. Người ở đây bảo nó ở bìa rừng ấy từ trước khi ông bà họ ra đời.\n"
"Chính giữa bông hoa có một cái nhụy. Những con khác tôi gặp đều không có. Nó là con cái, và đó là lần đầu tôi phân biệt được giới tính loài này bằng mắt thường.\n"
"Nụ của K-01 thì chưa nở. Sau mười bốn tháng, tôi vẫn chưa biết mình đã theo một con đực hay một con cái.\n"
"Sau mỗi trận mưa, hương hoa của con cái già đậm hẳn lên. Có lần tôi thấy hai con vật đang gầm gừ nhau cùng nằm xuống, cách nhau vài bước, trong làn hương ấy, và nằm yên.\n"
"Tôi vẫn không biết cái hạt trên lưng K-01 là một phần của nó, hay một sự sống khác đang sống nhờ nó. Có lẽ câu trả lời không nằm ở cách ta gọi tên. Có lẽ một cơ thể có thể bắt đầu từ hai sự sống, mà vẫn thành một.\n"
"Ở trang sau của cuốn danh lục là một loài mang ngọn lửa ở chóp đuôi. Nếu ngọn lửa ấy tắt trong mưa, nó sống sót bằng cách nào?",

"short-outro":
"Con thú đang nuôi cái hạt, hay cái hạt đang nuôi con thú?\n"
"Sau mười bốn tháng ngoài đồng, tôi vẫn chưa trả lời được.",
}

BEATS_EN = {
"00":
"On the first day, I found it lying on the trail under the midday sun.\n"
"I thought it was dead.\n"
"Then the seed on its back contracted. It was breathing, and not only with its lungs.",

"01":
"I came with a question I have carried for years: there are creatures in which life and energy cannot be pulled apart.\n"
"So I did what we do back home with wolves and elephants. Choose one animal, follow it, see what changes.\n"
"The catalogue calls this species Bulbasaur. My notebook calls it K-01.\n"
"For weeks, that was all it was: a letter and a number.",

"02":
"Viridian is where the old forest meets the grassland. Between them runs a trail of flattened stems, and they are the ones who made it.\n"
"Seven animals live in this clearing. K-01 is the smallest, and it always walks last. Yet it is the one you notice first.\n"
"Its skin is a warm, pale yellow-green where the others are blue-green, and the bulb on its back is darker than theirs.\n"
"For seven days I mapped where each animal lay at noon. K-01 took the brightest patch every single day.\n"
"People here call animals like this “shiny”. In my notebook, it is still just K-01.",

"03":
"At noon, K-01 stops feeding and lies still. Once I lost it completely, and spent twenty minutes crawling through the bracken to find it.\n"
"Three hours later, the seed on its back was taut and swollen. Its belly was still flat.\n"
"It was not fasting. It was eating something else.\n"
"The catalogue keeps two separate notes: sunlight makes the seed grow, and the animal can go for days without food on what the bulb has stored. It took me nearly a month to put them together.\n"
"The thing on its back is a second stomach.",

"04":
"But sunlight is not enough. A plant also needs water and minerals, and it took me another three weeks to see where K-01 finds them.\n"
"Late in the afternoon it wades to the edge of the pond and stands there a long time, front feet sunk in the mud. It never lowers its head to drink.\n"
"The minerals, I suspect, come from inside. Back home, the algae living in coral tissue feed on their host's waste.\n"
"If the bulb works the same way, it is fed by what K-01's own body throws away. A closed loop. Nothing lost.",

"05":
"Here my notebook changed course.\n"
"At first I wrote: parasite. Something that clings, drinks, and grows on whatever its host finds. Then I crossed it out. Parasites do not leave their host well fed, and K-01 is strongest on the fiercest days of sun.\n"
"Is the animal feeding the seed, or is the seed feeding the animal?\n"
"Back home, the line between those two ways of living is a hair thin. A lichen is a fungus and an alga bound so tightly we once took them for one species. A mistletoe drives its roots into a tree until the tree dies standing.",

"06":
"The seven never sleep pressed together. Each keeps enough space for the sun to reach its back.\n"
"At dusk, as the forest's shadow crawls across the clearing, the patches of light shrink fast, and the shoving begins. Shoulders, never teeth. The loser walks away.\n"
"K-01 sleeps about two body-lengths from a larger animal. Every night, the same distance. They never touch.\n"
"The day that larger one tore open its flank, I gave it a code: K-04. An animal earns a code once I can tell it apart.\n"
"That night, four animals moved to lie around K-04. K-01 stayed where it always was.",

"07":
"They do touch. Just never while they rest.\n"
"Two vines slide out from under the bulbs, meet in the air, wind around each other for a few seconds, and let go. I watched for twenty minutes and did not write a word.\n"
"This is not a whip. It is an organ for holding, for touching, for greeting.\n"
"And for keeping clean. The back is a blind spot for a short-necked animal on four legs. That afternoon, K-01 flicked a vine over its shoulder and knocked a caterpillar off the base of its bulb, the way a horse swats a fly with its tail.",

"08":
"The colour has a price.\n"
"On the fifty-third day, a large bird began to circle overhead. The catalogue lists it as Fearow. One of its eyes was clouded ash-grey from an old wound. It followed only K-01.\n"
"Under the ferns, the others' blotched blue-green skin melts into the broken shade. K-01's pale skin does not.\n"
"Back home, pale moths resting on soot-darkened bark were taken by birds far more often than dark ones.\n"
"On the first dive, K-01 did not run. It pressed itself flat under a fern and froze. The fern hid it, not its skin. The bird missed by an arm's length.\n"
"On the second dive, the top of the bulb split open and a fine pale powder burst out. The bird rolled, lost its line, and was gone.",

"09":
"What I underlined came afterwards.\n"
"K-01 lay still for the rest of the afternoon. It did not eat, did not move, did not react when I came close.\n"
"And the bulb was visibly smaller.\n"
"What had saved its life was paid out of the store it had spent weeks filling in the sun.\n"
"From then on, I stopped writing these things under abilities. I started a ledger: income, and expense.",

"10":
"This land has something my home does not. People set these animals against each other.\n"
"I went down to a town and watched one match from the edge of a dirt yard.\n"
"In the yard, the vines do not greet. They lash.\n"
"The same organ that picks fruit and brushes off pests in the forest is used here to strike. I do not judge it. Back home, an elephant's trunk can caress a newborn calf, and it can tear a branch from a tree.\n"
"One moment kept me writing until dawn. The animal held perfectly still for a beat, the bulb lit from within, and only then came the beam of light.\n"
"The crowd called that pause a weakness. I saw the day's stored sun spent in a single breath.\n"
"By morning, back in the forest, K-01 was already lying in the first patch of light.",

"11":
"People who have raised these animals for years say each kind has a temperament. This one has two.\n"
"The first I had measured myself before anyone told me. Under the harsh noon sun, K-01 covered the same stretch of ground almost twice as fast as in the shade. I timed it. A body that runs on sunlight runs harder when the sun is fierce.\n"
"The second I saw only in the yard, and it troubled me more than it impressed me. When an animal is badly hurt, barely standing, its blows suddenly grow stronger.\n"
"I do not think it has become stronger. I think it is spending the last of its reserve. Once.\n"
"Back home, the agave stores for decades for a single flowering, and then it dies.",

"12":
"In the fourth month, K-01 changed its habits.\n"
"It stayed out in the open sun long past noon, gave up its midday shade, and ate more than before. It walked more slowly. Its vines thickened and hung heavy, as if it could no longer quite steer them.\n"
"One morning I sat for three hours to record a single detail.\n"
"K-01's head faced south and did not move. But the bulb on its back turned, slowly, toward the east, following the sun.\n"
"Two parts of one body, facing two ways, on the same morning.\n"
"It is the clearest sign I have that two lives share this body. And still I cannot say which one is feeding the other.\n"
"Back home, young sunflowers follow the sun all day. Once they bloom, they stop, and face the east for good.",

"13":
"At the end of that month, K-01 left the herd and went into the old forest. For four days I lost it.\n"
"K-04 stayed. Every morning it lay in its usual place, beside the same two-body gap. No one took that spot.\n"
"On the fifth night I found K-01 in a hollow behind a ring of old trees, standing in a silent circle with eleven others, none of them touching. K-01 was the only pale one.\n"
"People here say they gather in this place once a year. They call it the Mysterious Garden.\n"
"I thought it had gone there to die. I wrote a whole page about it.",

"14":
"I did not see the moment itself. After two sleepless nights I fell asleep, and when I woke at dawn, the hollow was empty.\n"
"But it had left enough for anyone who reads the ground.\n"
"The soil was ploughed into short furrows, where four feet had braced under a sudden new weight. The grass lay flattened in a ring. Old dry bracts lay scattered on the ground, come loose and curled like onion skin. And the whole hollow smelled of flowers, a scent I had never known this species to carry.\n"
"Across the grass, in the mist, stood large shapes. The others carried pink buds.\n"
"One carried a yellow bud.\n"
"Its skin was leaf-green now, no longer pale, but the bud was gold, and I knew.\n"
"What stood there was no longer the animal I had recorded. But when I opened my notebook, it tilted its head toward the sound of the pen.",

"15":
"The bud is so heavy now that K-01 can no longer rise onto its hind legs. Its legs and body have thickened to carry it.\n"
"In the last rainy season of this notebook, I met a very old female Venusaur at the edge of the forest. Her trunk had turned to bark. Moss and small ferns covered her back, and her great flower had faded. People here say she was there before their grandparents were born.\n"
"At the centre of her flower was a pistil. The others I had met had none. She was female, the first time I could tell the sexes of this species apart by eye.\n"
"K-01's bud has not opened. After fourteen months, I still do not know whether I have followed a male or a female.\n"
"After rain, her scent grows stronger. Once I watched two animals that had been snarling at each other lie down a few steps apart inside it, and stay there.\n"
"I still do not know whether the seed on K-01's back is part of it, or another life living on it. Perhaps the answer is not in what we call it. Perhaps a body can begin as two lives, and still become one.\n"
"On the next page of the catalogue is a creature that carries a flame at the tip of its tail. If that flame goes out in the rain, how does it survive?",

"short-outro":
"Is the animal feeding the seed, or is the seed feeding the animal?\n"
"After fourteen months in the field, I still cannot say.",
}

# Phiên âm cho TTS (VBee): chữ trên màn hình vẫn giữ chính tả gốc. Nghe thử rồi chỉnh.
PRON = {
    "Bulbasaur": "bôn-ba-xo",
    "Venusaur": "vi-nu-xo",
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
