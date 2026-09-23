"""Nhạc của kênh — hai mươi đoạn cùng tông, mỗi đoạn một bối cảnh trong khung tập.

    PYTHONUTF8=1 python tools/build-music.py
    PYTHONUTF8=1 python tools/build-music.py --only strike
    PYTHONUTF8=1 python tools/build-music.py --group C --sec 48
    PYTHONUTF8=1 python tools/build-music.py --creature charmander
    PYTHONUTF8=1 python tools/build-music.py --list
    PYTHONUTF8=1 python tools/build-music.py --check          # đo tông của thứ đang có

Ra public/audio/music/. Bảng bối cảnh và câu lệnh sinh bản có nhạc cụ thật:
docs/MUSIC-PROMPTS.md. Luật: docs/SOUND.md.

**Cả bộ nằm trong một tông: La thứ (A minor), trục La–Mi.** Đây là điều kiện để ghép: hai đoạn
khác tâm trạng nhưng cùng tông thì chồng lên nhau ở chỗ chuyển chương vẫn thuận tai, còn khác
tông thì chỗ nối nghe như hai đài phát cùng lúc. Mỗi đoạn chỉ được dùng nốt trong La thứ
(La Si Do Re Mi Fa Sol) — khác nhau ở chỗ *chọn nốt nào*, *ở quãng nào*, *tiếng gì*, *động tới
đâu*, chứ không ở chỗ đổi tông.

Không giai điệu, không bộ gõ: nhạc chạy dưới lời dẫn, mà cái gì có nốt đi lên đi xuống hay có
nhịp gõ đều thì tai bám theo nó và rời khỏi lời.

Mười sáu đoạn nền là **vòng lặp liền mạch**: mọi tần số và mọi nhịp phồng đều là bội của 1/L,
nhiễu dựng thẳng trong miền tần số, bộ lọc chạy trên hai vòng rồi lấy vòng sau — nên chỗ nối
không có cú nhảy. Bốn đoạn chơi một lần (mở tập, kết tập, cú ra đòn, nhịp nạp) thì ngược lại:
chúng sống bằng đúng cái mở và cái kết của mình.

Đây là nhạc dựng bằng máy tại chỗ: kênh sở hữu toàn bộ, không vướng license, không dính
Content ID, và dựng lại bao nhiêu lần cũng ra đúng file cũ.
"""

import sys
import zlib
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolab as al
from audiolab import SR

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent

TONIC = 55.0          # La1. Mọi đoạn nhạc của kênh mọc lên từ nốt này.
KEY = "La thứ · A minor"

# Nốt tính bằng bán cung so với La1. Chỉ được lấy trong La thứ:
#   La 0 · Si 2 · Do 3 · Re 5 · Mi 7 · Fa 8 · Sol 10  (cộng 12 cho mỗi quãng tám)
LA, SI, DO, RE, MI, FA, SOL = 0, 2, 3, 5, 7, 8, 10
OCT = 12

# ---- trục thứ hai: bộ tiếng theo loài -------------------------------------------------
# Bảng PIECES dưới đây là **bối cảnh** — nó đến từ mười chặng của khung tập nên loài nào cũng
# giống nhau. Nhưng *tiếng* và *nhịp* thì không được giống nhau, và đó là luật 3 của SOUND.md
# ("giải phẫu quyết định âm sắc") áp cho nhạc:
#
#   vật liệu cơ thể chọn bộ nhạc cụ · nhịp sống chọn tempo
#
# Bộ mặc định là của dòng Bulbasaur: một con vật ăn nắng, nằm im, tích trữ — nên chậm và đầy
# tiếng kéo vĩ. Đem nguyên bộ ấy sang một con vật chạy bằng lửa là sai, dù từng đoạn vẫn hay.
#
# timbre: pad = nốt trơn ấm · bowed = kéo vĩ, hoạ âm dày dần · glass = thuỷ tinh và kim loại,
#         bồi âm lệch · brass = kèn đồng, càng to càng sáng
CREATURES = {
    "bulbasaur": {
        "desc": "thực vật, gỗ ẩm, ăn nắng — chậm, dây kéo vĩ (bộ gốc)",
        "swap": {}, "tempo": 1.0, "tilt": 1.0, "air": 1.0, "breath": 1.0,
    },
    "charmander": {
        "desc": "lửa và khí nóng — nhanh hơn, sáng hơn, hơi thổi và kim loại thay cho vĩ",
        "swap": {"bowed": "brass", "pad": "brass"},
        "tempo": 1.35, "tilt": 1.35, "air": 1.6, "breath": 0.8,
    },
    "squirtle": {
        "desc": "nước và vỏ — ống cộng hưởng, trầm tròn, trôi chứ không cọ",
        "swap": {"bowed": "pad", "brass": "pad"},
        "tempo": 1.1, "tilt": 0.9, "air": 1.2, "breath": 1.2,
    },
    "caterpie": {
        "desc": "côn trùng, cánh mỏng — rung nhanh, mỏng và cao, gần như không có bè trầm",
        "swap": {"bowed": "glass", "pad": "glass", "brass": "glass"},
        "tempo": 1.7, "tilt": 1.4, "air": 1.5, "breath": 0.5,
    },
    "pikachu": {
        "desc": "điện — kim loại, tắt nhanh, đứt đoạn; sáng và gấp",
        "swap": {"bowed": "glass", "pad": "glass"},
        "tempo": 1.5, "tilt": 1.3, "air": 1.4, "breath": 0.7,
    },
    "diglett": {
        "desc": "dưới mặt đất — trầm, bịt kín, cắt gần hết dải cao",
        "swap": {"glass": "brass", "bowed": "brass"},
        "tempo": 0.8, "tilt": 0.5, "air": 0.4, "breath": 1.5,
    },
}


def apply_creature(cfg, cre):
    """Giữ nguyên bối cảnh và nguyên bộ nốt — chỉ đổi tiếng và nhịp.

    Nốt không đụng tới, nên bộ của loài nào cũng vẫn nằm trong La thứ và vẫn ghép được
    với bộ của loài khác. Đó là chỗ việc khoá tông trả bài lần thứ hai.
    """
    c = dict(cfg)
    c["timbre"] = cre["swap"].get(cfg.get("timbre", "pad"), cfg.get("timbre", "pad"))
    c["motion"] = cfg.get("motion", 1.0) * cre["tempo"]
    c["tilt"] = cfg.get("tilt", 7000) * cre["tilt"]
    c["air"] = min(cfg["air"] * cre["air"], 0.6)
    c["breath"] = cfg["breath"] * cre["breath"]
    for k in ("pulse", "tremolo"):
        if cfg.get(k):
            c[k] = cfg[k] * cre["tempo"]
    return c


# shape:  None = vòng lặp · build = dày dần rồi đứng · fade = tan dần · gesture = một cú ·
#         charge = nén rồi cắt
PIECES = {
    # ---- A · khung tập -------------------------------------------------------------
    "open": {
        "file": "music-open.wav", "group": "A", "sec": 72, "shape": "build", "build": 20,
        "desc": "mở tập — một nốt dày dần thành quãng năm rồi đứng yên",
        "use": "chặng 0, câu hỏi mở màn (beat 00–01)",
        "notes": [(LA, 0.60), (MI, 0.30), (LA + OCT, 0.22), (MI + OCT, 0.10), (LA + 2 * OCT, 0.06)],
        "timbre": "bowed", "air": 0.14, "breath": 0.22, "motion": 0.9, "detune": 5, "tilt": 6500,
    },
    "bridge": {
        "file": "field-bed-bridge.wav", "group": "A",
        "desc": "chuyển chặng — mỏng tới mức gần như không có mặt",
        "use": "chỗ nối giữa hai chặng, lúc người kể lật sổ",
        "notes": [(LA, 0.45), (MI + OCT, 0.16), (LA + OCT, 0.10)],
        "timbre": "bowed", "air": 0.10, "breath": 0.10, "motion": 1.1, "detune": 3, "tilt": 5000,
    },
    "reveal": {
        "file": "field-bed-reveal.wav", "group": "A",
        "desc": "trả bài — sáng dần và mở ra, nhưng không thắng lợi",
        "use": "chặng 9, chỗ câu hỏi mở màn được trả lời",
        "notes": [(LA, 0.45), (MI, 0.28), (LA + OCT, 0.24), (MI + OCT, 0.20),
                  (LA + 2 * OCT, 0.14), (MI + 2 * OCT, 0.08)],
        "timbre": "bowed", "air": 0.24, "breath": 0.16, "motion": 0.7, "detune": 6, "tilt": 8500,
    },
    "close": {
        "file": "music-close.wav", "group": "A", "sec": 40, "shape": "fade", "fade": 26,
        "desc": "kết tập — các bè rụng dần, cuối cùng còn một nốt và không khí",
        "use": "short-outro và đuôi bản Long, chỗ đặt logo",
        "notes": [(LA, 0.55), (MI, 0.30), (LA + OCT, 0.22), (MI + OCT, 0.12)],
        "timbre": "pad", "air": 0.18, "breath": 0.20, "motion": 0.8, "detune": 4, "tilt": 7000,
    },

    # ---- B · vùng đất và đời thường -------------------------------------------------
    "calm": {
        "file": "field-bed-calm.wav", "group": "B",
        "desc": "nền chung, nhẹ nhàng — quãng năm để ngỏ, không buồn không vui",
        "use": "mặc định; chương kể chuyện, quan sát bình thường",
        "notes": [(LA, 0.55), (MI, 0.34), (LA + OCT, 0.26), (MI + OCT, 0.12),
                  (LA + 2 * OCT, 0.07), (MI + 2 * OCT, 0.035)],
        "timbre": "pad", "air": 0.16, "breath": 0.20, "motion": 1.0, "detune": 4, "tilt": 7000,
    },
    "vista": {
        "file": "field-bed-vista.wav", "group": "B",
        "desc": "cảnh rộng — cùng một nốt trải khắp các quãng tám, cao và trống",
        "use": "chặng 1, vùng đất: khí hậu, địa hình, cảnh mở toàn vùng",
        "notes": [(LA, 0.50), (LA + OCT, 0.30), (MI + OCT, 0.22), (LA + 2 * OCT, 0.20),
                  (MI + 2 * OCT, 0.14), (LA + 3 * OCT, 0.08)],
        "timbre": "bowed", "air": 0.28, "breath": 0.22, "motion": 0.5, "detune": 7, "tilt": 9000,
    },
    "warm": {
        "file": "field-bed-warm.wav", "group": "B",
        "desc": "thư giãn — thêm nốt ba thứ, đủ bộ hợp âm, mềm và có hơi",
        "use": "chặng 3, ban ngày, đàn nằm phơi nắng",
        "notes": [(LA, 0.50), (MI, 0.30), (DO + OCT, 0.26), (MI + OCT, 0.20),
                  (LA + 2 * OCT, 0.12), (SI + 2 * OCT, 0.05)],
        "timbre": "pad", "air": 0.22, "breath": 0.18, "motion": 0.8, "detune": 6, "tilt": 8000,
    },
    "still": {
        "file": "field-bed-still.wav", "group": "B",
        "desc": "tĩnh lặng — gần như không có gì chuyển động",
        "use": "cận cảnh, lúc chờ, con vật nằm im; chỗ cần nghe thấy tiếng thở",
        "notes": [(LA, 0.75), (MI, 0.38), (LA + OCT, 0.16), (MI + OCT, 0.04)],
        "timbre": "pad", "air": 0.05, "breath": 0.14, "motion": 0.45, "detune": 2, "tilt": 3600,
    },
    "alive": {
        "file": "field-bed-alive.wav", "group": "B",
        "desc": "náo nhiệt — hợp âm bảy, nhiều bè, có nhịp phồng chậm",
        "use": "chặng 4, đàn đông; tranh chỗ nằm, chen lấn",
        "notes": [(LA, 0.45), (MI, 0.28), (DO + OCT, 0.22), (SOL + OCT, 0.20),
                  (MI + OCT, 0.16), (DO + 2 * OCT, 0.10), (MI + 2 * OCT, 0.06)],
        "timbre": "pad", "air": 0.20, "breath": 0.12, "motion": 2.4, "detune": 8, "tilt": 9000,
        "pulse": 0.75,        # nhịp phồng, KHÔNG phải tiếng trống
    },
    "mystic": {
        "file": "field-bed-mystic.wav", "group": "B",
        "desc": "thần bí — nốt sáu thứ chà nhẹ vào quãng năm, bè cao trôi",
        "use": "chặng 6, đêm và sương; mọi chỗ còn là 🔬 giả thuyết",
        "notes": [(LA, 0.34), (MI, 0.30), (FA + OCT, 0.22), (SI + 2 * OCT, 0.15),
                  (MI + 2 * OCT, 0.12), (LA + 3 * OCT, 0.05)],
        "timbre": "glass", "air": 0.30, "breath": 0.10, "motion": 0.6, "detune": 14, "tilt": 9500,
    },

    # ---- C · kẻ địch và trận đấu ----------------------------------------------------
    "stalk": {
        "file": "field-bed-stalk.wav", "group": "C",
        "desc": "kẻ săn đang theo — Mi và Fa nằm cạnh nhau, nặng, không có bè cao",
        "use": "chặng 5, kẻ săn bay vòng, chưa ra tay",
        "notes": [(LA, 0.70), (MI, 0.32), (FA, 0.18), (DO + OCT, 0.12), (LA + OCT, 0.10)],
        "timbre": "brass", "air": 0.06, "breath": 0.32, "motion": 0.7, "detune": 5, "tilt": 2800,
    },
    "chase": {
        "file": "field-bed-chase.wav", "group": "C",
        "desc": "rượt đuổi — vĩ rung không nghỉ, gấp mà không có một tiếng gõ nào",
        "use": "chặng 5, lúc con mồi vỡ chạy",
        "notes": [(LA, 0.50), (MI, 0.22), (LA + OCT, 0.26), (DO + 2 * OCT, 0.22),
                  (MI + 2 * OCT, 0.18)],
        "timbre": "bowed", "air": 0.12, "breath": 0.26, "motion": 3.2, "detune": 9, "tilt": 7500,
        "tremolo": 14.0,      # vĩ rung: gấp gáp mà không đếm thành nhịp được
        "pulse": 1.87,        # 112 BPM chia đôi — phồng chứ không gõ
    },
    "strike": {
        "file": "music-strike.wav", "group": "C", "sec": 16, "shape": "gesture", "hit": 9.5,
        "desc": "cú ra đòn — nén, một nhát, rồi im hẳn; không có đuôi vang",
        "use": "cú bổ nhào, cú quật dây leo",
        "notes": [(LA, 0.60), (MI, 0.30), (FA, 0.20), (LA + OCT, 0.22), (MI + OCT, 0.14)],
        "timbre": "bowed", "air": 0.10, "breath": 0.30, "motion": 1.6, "detune": 10, "tilt": 8000,
    },
    "charge": {
        "file": "music-charge.wav", "group": "C", "sec": 14, "shape": "charge",
        "desc": "nhịp nạp — dâng và đặc dần rồi CẮT, không có hợp âm trả bài",
        "use": "chặng 5b, đứng yên một nhịp, cái củ sáng lên, rồi mới phóng",
        "notes": [(LA, 0.55), (MI, 0.30), (LA + OCT, 0.26), (MI + OCT, 0.20),
                  (SI + 2 * OCT, 0.10)],
        "timbre": "brass", "air": 0.16, "breath": 0.24, "motion": 1.2, "detune": 7, "tilt": 7000,
    },
    "arena": {
        "file": "field-bed-arena.wav", "group": "C",
        "desc": "sân đấu — dây dày, một bè trầm đi dưới; máy quay đứng ngoài vòng",
        "use": "chặng 5b, trận đấu của người bản xứ",
        "notes": [(LA, 0.48), (MI, 0.30), (DO + OCT, 0.24), (MI + OCT, 0.18), (SOL + OCT, 0.14),
                  (LA + 2 * OCT, 0.08)],
        "timbre": "bowed", "air": 0.14, "breath": 0.24, "motion": 2.0, "detune": 8, "tilt": 6000,
        "pulse": 1.4,
    },
    "aftermath": {
        "file": "field-bed-aftermath.wav", "group": "C",
        "desc": "sau trận — những bè vừa dày đặc giờ chỉ còn một hai nốt",
        "use": "chặng 8, cơ thể kiệt, cái kho bị rút cạn",
        "notes": [(LA, 0.55), (MI, 0.14), (DO + OCT, 0.10)],
        "timbre": "bowed", "air": 0.08, "breath": 0.26, "motion": 0.35, "detune": 4, "tilt": 3200,
    },

    # ---- D · vòng đời ---------------------------------------------------------------
    "birth": {
        "file": "field-bed-birth.wav", "group": "D",
        "desc": "tổ và con non — nhỏ và sáng ở trên, trầm giữ rất xa ở dưới",
        "use": "chặng 2, trứng, ổ, lúc chào đời",
        "notes": [(LA, 0.30), (MI + 2 * OCT, 0.22), (LA + 3 * OCT, 0.20), (DO + 3 * OCT, 0.16),
                  (MI + 3 * OCT, 0.10)],
        "timbre": "glass", "air": 0.26, "breath": 0.12, "motion": 1.0, "detune": 5, "tilt": 10000,
    },
    "threshold": {
        "file": "field-bed-threshold.wav", "group": "D",
        "desc": "ngưỡng đổi hình — căng và nín; KHÔNG có tiếng biến hình, không lấp lánh",
        "use": "chặng 7, đêm cả đàn đứng thành vòng",
        "notes": [(LA, 0.68), (MI, 0.30), (SI + OCT, 0.12), (MI + 3 * OCT, 0.08)],
        "timbre": "bowed", "air": 0.10, "breath": 0.30, "motion": 0.3, "detune": 6, "tilt": 4200,
    },
    "courtship": {
        "file": "field-bed-courtship.wav", "group": "D",
        "desc": "mùa sinh sản — ấm và có màu hơn mọi đoạn khác, nhưng kiềm chế",
        "use": "chặng 9, mùa mưa, hương đậm, phô diễn và làm tổ",
        "notes": [(LA, 0.48), (MI, 0.28), (DO + OCT, 0.24), (SOL + OCT, 0.16),
                  (MI + OCT, 0.18), (DO + 2 * OCT, 0.10)],
        "timbre": "pad", "air": 0.24, "breath": 0.16, "motion": 0.9, "detune": 7, "tilt": 8500,
    },
    "elegy": {
        "file": "field-bed-elegy.wav", "group": "D",
        "desc": "cái chết — dây trầm giữ nốt rất dài, một nốt cao ở xa; không nốt nào rơi xuống",
        "use": "trục 16, xác một cá thể trả khoáng lại cho đất",
        "notes": [(LA, 0.62), (MI, 0.28), (DO + OCT, 0.16), (MI + 2 * OCT, 0.10)],
        "timbre": "bowed", "air": 0.16, "breath": 0.26, "motion": 0.4, "detune": 5, "tilt": 5200,
    },
}


def circular(fn, x):
    """Lọc mà không để lại cú nhảy ở chỗ nối: chạy hai vòng, lấy vòng sau."""
    return fn(np.concatenate([x, x]))[len(x):]


def quantize(f, sec):
    """Kéo tần số về bội của 1/L — điều kiện để sóng khép kín đúng một vòng."""
    return max(round(f * sec), 1) / sec


# ---- tiếng của từng bè ---------------------------------------------------------------
# Mỗi hàm trả về một bè ở tần số f. Vì f đã là bội của 1/L nên mọi hoạ âm k·f cũng vậy,
# và cả bè vẫn khép kín đúng một vòng.

def _pair(f, t, rng, detune, sec):
    """Hai sóng lệch nhau vài cent — chỗ đẻ ra độ dày, không phải chỗ đẻ ra nốt mới."""
    d = quantize(f * 2 ** (detune / 1200), sec)
    return (np.sin(2 * np.pi * f * t + rng.uniform(0, 6.28))
            + 0.6 * np.sin(2 * np.pi * d * t + rng.uniform(0, 6.28)))


# Hoạ âm tự nhiên của nốt La không nằm gọn trong La thứ: bậc 5 và bậc 10 là **Do#**, tức quãng
# ba TRƯỞNG. Để nguyên thì mọi bè kéo vĩ đều lén mang theo một nốt ngoài tông, và nó chỏi thẳng
# với nốt Do của những đoạn có đủ bộ hợp âm thứ. Nên hai bậc ấy bị ghìm xuống. Bậc 7 là Sol —
# có trong La thứ, chỉ thấp hơn 31 cent, giữ lại nhưng bớt đi một nửa.
HARMONIC_TRIM = {5: 0.18, 7: 0.5, 10: 0.15}


def timbre_pad(f, t, rng, cfg, sec):
    return _pair(f, t, rng, cfg.get("detune", 4), sec)


def timbre_bowed(f, t, rng, cfg, sec):
    """Kéo vĩ: hoạ âm rơi theo 1/k, thêm một chút rung tay trái."""
    x = np.zeros(len(t))
    for k in range(1, 9):
        fk = quantize(f * k, sec)
        if fk > SR / 2.2:
            break
        x += HARMONIC_TRIM.get(k, 1.0) * (1.0 / k ** 1.1) * _pair(fk, t, rng, cfg.get("detune", 4) * 0.5, sec)
    return x * (1 + 0.004 * np.sin(2 * np.pi * quantize(5.0, sec) * t))


def timbre_glass(f, t, rng, cfg, sec):
    """Thuỷ tinh và kim loại: bồi âm lệch khỏi bội số nguyên, nên trong mà không ấm."""
    x = _pair(f, t, rng, cfg.get("detune", 8), sec)
    for r, g in ((2.01, 0.45), (3.04, 0.22), (4.21, 0.12), (5.43, 0.06)):
        fk = quantize(f * r, sec)
        if fk < SR / 2.2:
            x += g * np.sin(2 * np.pi * fk * t + rng.uniform(0, 6.28))
    return x


def timbre_brass(f, t, rng, cfg, sec):
    """Kèn đồng: hoạ âm dày và đều — chỗ nó doạ người là ở mấy bậc trên."""
    x = np.zeros(len(t))
    for k in range(1, 11):
        fk = quantize(f * k, sec)
        if fk > SR / 2.2:
            break
        x += HARMONIC_TRIM.get(k, 1.0) * (1.0 / k ** 0.85) * np.sin(2 * np.pi * fk * t + rng.uniform(0, 6.28))
    return x


TIMBRES = {"pad": timbre_pad, "bowed": timbre_bowed, "glass": timbre_glass, "brass": timbre_brass}


# ---- bao hình của cả đoạn -------------------------------------------------------------

def shape_env(cfg, sec, t):
    """Đoạn chơi một lần thì hình dáng của nó chính là nội dung của nó."""
    kind = cfg.get("shape")
    if not kind:
        return np.ones(len(t))
    if kind == "build":
        b = cfg.get("build", 20.0)
        k = np.clip(t / b, 0, 1)
        return 0.12 + 0.88 * (k * k * (3 - 2 * k))                # dày dần rồi đứng yên
    if kind == "fade":
        f = cfg.get("fade", 26.0)
        return (1 - np.clip((t - (sec - f)) / f, 0, 1)) ** 2.2    # rụng dần từng bè
    if kind == "gesture":
        hit, ln = cfg.get("hit", 9.5), len(t)
        e = 0.10 + 0.32 * np.clip(t / hit, 0, 1) ** 2.0           # nén dần
        i, rise, fall = al.n(hit), al.n(0.045), al.n(0.5)
        e[i:] = 0.0
        e[i:i + rise] = np.linspace(0.42, 1.0, rise)              # một nhát
        e[i + rise:i + rise + fall] = np.linspace(1.0, 0.04, fall)
        tail = ln - i - rise - fall
        if tail > 0:
            e[i + rise + fall:] = np.linspace(0.04, 0.0, tail) ** 2
        return e
    if kind == "charge":
        cut = sec - 0.25
        e = 0.08 + 0.92 * np.clip(t / cut, 0, 1) ** 2.4           # dâng và đặc dần
        return np.where(t >= cut, 0.0, e)                         # rồi CẮT, không trả bài
    raise ValueError(f"hình dáng lạ: {kind}")


def build(cfg, sec, rng):
    ln = al.n(sec)
    t = np.arange(ln) / SR
    motion = cfg.get("motion", 1.0)
    timbre = TIMBRES[cfg.get("timbre", "pad")]

    # Vĩ rung — CHỈ cho bè từ La2 trở lên. Rung một nốt trầm bằng cách nhân biên độ ở 14 Hz thì
    # đẻ ra dải biên f±14, và với nốt La1 (55 Hz) cái dải biên ấy rơi đúng vào 69 Hz = Do#, một
    # nốt ngoài La thứ. Ngoài đời dàn dây cũng làm đúng thế: bè giữa và bè cao rung vĩ, còn
    # contrabass thì giữ nguyên nốt.
    trem = None
    if cfg.get("tremolo"):
        trem = 0.55 + 0.45 * np.sin(2 * np.pi * quantize(cfg["tremolo"], sec) * t)

    # Dàn bè: mỗi nốt một bè, mỗi bè phồng xẹp theo một chu kỳ riêng.
    pad = np.zeros(ln)
    for i, (semitone, gain) in enumerate(cfg["notes"]):
        f = quantize(TONIC * 2 ** (semitone / 12), sec)
        m = quantize((i + 1) * motion / 7.0, sec)
        lfo = 0.55 + 0.45 * np.sin(2 * np.pi * m * t + rng.uniform(0, 6.28))
        voice = gain * lfo * timbre(f, t, rng, cfg, sec)
        if trem is not None and semitone >= OCT:
            voice = voice * trem
        pad += voice

    # Hơi: dải cao rất khẽ, để đoạn nhạc không thành một khối đặc.
    air = circular(lambda z: al.bandpass(z, 3400, 0.5), al.noise(sec, rng, "pink"))
    air *= 0.5 + 0.5 * np.sin(2 * np.pi * quantize(motion / 23.0, sec) * t)

    # Nhịp thở của cả đoạn: phồng rất chậm, đúng ba lần trong một vòng.
    low = circular(lambda z: al.lowpass(z, 90), al.noise(sec, rng, "brown"))
    low *= 0.4 + 0.6 * (0.5 + 0.5 * np.sin(2 * np.pi * quantize(3 / sec, sec) * t))

    x = al._norm(pad) + cfg["air"] * al._norm(air) + cfg["breath"] * al._norm(low)

    if cfg.get("pulse"):
        p = quantize(cfg["pulse"], sec)
        x *= 0.78 + 0.22 * (0.5 + 0.5 * np.sin(2 * np.pi * p * t)) ** 2

    # Khoét bớt dải 2–4 kHz: đây là chỗ lời dẫn nằm, nhạc tránh ra cho giọng có đường đi.
    x -= 0.55 * circular(lambda z: al.bandpass(z, 2600, 0.6), x)
    x = circular(lambda z: al.lowpass(z, cfg.get("tilt", 7000)), x)
    x = circular(lambda z: al.highpass(z, 32), x)

    x = x * shape_env(cfg, sec, t)
    if cfg.get("shape"):
        x = al.fade(x, 0.05, 0.05)        # đoạn chơi một lần: chặn cú bụp ở hai đầu
    return al.finish_bed(al._norm(x, 0.9))


def report(path):
    """Đo một file: bao nhiêu phần năng lượng nằm trong bảy nốt của La thứ.

    Không chấm theo nốt trầm: Do trưởng và La thứ dùng chung đúng bảy nốt, nên một bản đứng
    trên Do vẫn chồng được với một bản đứng trên La. Cái phải đo là **bộ nốt**.
    """
    x = al.read_wav(path, secs=60)
    name, hz, _ = al.pitch_profile(x)
    pc = al.pitch_classes(x)
    fit = sum(pc[i] for i in al.A_MINOR)
    stray = sorted(((pc[i], al.NOTE_NAMES[(i + 9) % 12]) for i in range(12) if i not in al.A_MINOR),
                   reverse=True)
    lạc = " ".join(f"{n} {100 * v:.0f}%" for v, n in stray if v > 0.04) or "—"
    return f"{100 * fit:3.0f}% trong tông {'✓' if fit >= 0.90 else '✗'} · trầm {name:3} · nốt lạc: {lạc}"


def main():
    argv = sys.argv[1:]
    sec_cli = float(argv[argv.index("--sec") + 1]) if "--sec" in argv else None
    only = argv[argv.index("--only") + 1] if "--only" in argv else None
    group = argv[argv.index("--group") + 1].upper() if "--group" in argv else None
    cname = argv[argv.index("--creature") + 1] if "--creature" in argv else "bulbasaur"
    if cname not in CREATURES:
        raise SystemExit(f"chưa có bộ tiếng cho '{cname}'. Đang có: {', '.join(CREATURES)}\n"
                         f"Thêm một mục vào CREATURES, luật ở docs/SOUND.md.")
    cre = CREATURES[cname]
    outdir = ROOT / "public" / "audio" / "music"
    if cname != "bulbasaur":
        outdir = outdir / cname            # bộ của loài khác nằm riêng, không đè lên bộ gốc

    if "--list" in argv:
        for k, c in PIECES.items():
            kind = "một lần" if c.get("shape") else "vòng lặp"
            print(f"  {c['group']} {k:11} {kind:8} {c['file']:28} {c['use']}")
        print("\nBộ tiếng theo loài (--creature):")
        for k, c in CREATURES.items():
            print(f"  {k:12} {c['desc']}  · tempo ×{c['tempo']}")
        return

    if "--check" in argv:
        print(f"Tông của kênh: {KEY} (La1 = {TONIC:.1f} Hz)\n")
        for p in sorted(outdir.glob("*.wav")):
            print(f"  {p.name:28} {report(p)}")
        return

    print(f"Tông của kênh: {KEY} (La1 = {TONIC:.1f} Hz) — cả bộ ghép được với nhau\n")
    made = 0
    for key, cfg in PIECES.items():
        if (only and key != only) or (group and cfg["group"] != group):
            continue
        sec = cfg.get("sec") or sec_cli or 60.0
        rng = np.random.default_rng(zlib.crc32(key.encode()))
        al.write_wav(outdir / cfg["file"], build(cfg, sec, rng))
        kind = "một lần" if cfg.get("shape") else "vòng lặp"
        print(f"  ✓ {cfg['group']} {cfg['file']:28} {sec:3.0f}s {kind:8} {cfg['desc']}")
        made += 1

    print(f"\n{made} đoạn -> public/audio/music/   (nền cho tập: video.config.json -> audio.bed)")
    print("Câu lệnh sinh bản có nhạc cụ thật: docs/MUSIC-PROMPTS.md")
    print("Trộn: bedVolume 0.12–0.15. Lời dẫn luôn là thứ to nhất; nhạc chỉ để đỡ, không để nghe.")


if __name__ == "__main__":
    main()
