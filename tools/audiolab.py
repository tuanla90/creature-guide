"""Bộ đồ nghề âm thanh dùng chung cho build-sfx.py và build-music.py.

Không phụ thuộc ffmpeg: bản ffmpeg đi kèm Remotion đã cắt gần hết filter audio
(không có lowpass, bandpass, tremolo, aecho), nên mọi thứ ở đây làm bằng numpy.

Quy ước: tín hiệu là mảng float32 mono trong khoảng [-1, 1], 48 kHz.
"""

import wave
from pathlib import Path

import numpy as np
from scipy import signal

SR = 48000


# ---- nền tảng ----------------------------------------------------------------

def n(sec):
    return max(1, int(round(sec * SR)))


def t(sec):
    """Trục thời gian, dùng cho mọi thứ dao động."""
    return np.arange(n(sec), dtype=np.float64) / SR


def noise(sec, rng, color="white"):
    """Nhiễu tô màu trong miền tần số — 1/f^a, a = 0 trắng, 0.5 hồng, 1 nâu."""
    a = {"white": 0.0, "pink": 0.5, "brown": 1.0}[color]
    ln = n(sec)
    spec = rng.normal(size=ln // 2 + 1) + 1j * rng.normal(size=ln // 2 + 1)
    f = np.arange(len(spec))
    f[0] = 1
    spec *= f ** (-a)
    spec[0] = 0
    x = np.fft.irfft(spec, ln)
    return _norm(x)


def sine(f, sec, phase=0.0):
    return np.sin(2 * np.pi * f * t(sec) + phase)


def impulses(sec, f0, rng, jitter=0.015, f_end=None):
    """Chuỗi xung thanh môn — nguyên liệu của mọi tiếng có dây thanh.

    f0 -> f_end cho tiếng rơi giọng (vạc, quạ, bò rống cuối hơi).
    """
    ln = n(sec)
    x = np.zeros(ln)
    f_end = f0 if f_end is None else f_end
    pos, i = 0.0, 0
    while pos < ln - 2:
        k = pos / max(ln - 1, 1)
        f = f0 * (1 - k) + f_end * k
        idx = int(pos)
        frac = pos - idx
        x[idx] += 1 - frac
        x[idx + 1] += frac
        pos += SR / f * (1 + rng.normal(0, jitter))
        i += 1
    return x


def resonators(x, bands):
    """Đưa nguyên liệu thô qua vài hộp cộng hưởng — chỗ quyết định 'con gì'.

    bands: [(tần số, Q, độ lớn)] — formant của cơ thể phát ra tiếng.
    """
    out = np.zeros_like(x)
    for f, q, g in bands:
        f = float(np.clip(f, 20, SR / 2 - 100))
        b, a = signal.iirpeak(f / (SR / 2), q)
        out += g * signal.lfilter(b, a, x)
    return out


# ---- lọc ---------------------------------------------------------------------

def _sos(kind, freq, q=0.707):
    if kind == "bandpass":
        lo = float(np.clip(freq / (1 + 1 / (2 * q)), 20, SR / 2 - 200))
        hi = float(np.clip(freq * (1 + 1 / (2 * q)), lo + 20, SR / 2 - 100))
        return signal.butter(2, [lo, hi], btype="bandpass", fs=SR, output="sos")
    freq = float(np.clip(freq, 20, SR / 2 - 100))
    return signal.butter(2, freq, btype=kind, fs=SR, output="sos")


def lowpass(x, freq):
    return signal.sosfilt(_sos("lowpass", freq), x)


def highpass(x, freq):
    return signal.sosfilt(_sos("highpass", freq), x)


def bandpass(x, freq, q=0.707):
    return signal.sosfilt(_sos("bandpass", freq, q), x)


# ---- bao hình ----------------------------------------------------------------

def env(sec, attack, release, curve=2.0):
    """Bao hình attack/release đơn giản — attack ngắn là 'gắt', dài là 'thở'."""
    ln = n(sec)
    a = min(n(attack), ln)
    e = np.ones(ln)
    e[:a] = np.linspace(0, 1, a) ** (1 / curve)
    r = min(n(release), ln - a) if ln > a else 0
    if r > 0:
        e[ln - r:] *= np.linspace(1, 0, r) ** curve
    return e


def decay(sec, tau):
    return np.exp(-t(sec) / tau)


def tremolo(x, f, depth):
    return x * (1 - depth + depth * (0.5 + 0.5 * np.sin(2 * np.pi * f * np.arange(len(x)) / SR)))


def echo(x, delay, feedback, taps=3):
    out = x.astype(np.float64).copy()
    d = n(delay)
    for i in range(1, taps + 1):
        g = feedback ** i
        if g < 0.02:
            break
        out[i * d:] += g * x[: len(x) - i * d]
    return out


def fade(x, fin, fout):
    x = x.astype(np.float64).copy()
    a, b = min(n(fin), len(x)), min(n(fout), len(x))
    col = (slice(None), None) if x.ndim == 2 else (slice(None),)   # chạy được cả với stereo
    if a:
        x[:a] *= (np.linspace(0, 1, a) ** 1.5)[col]
    if b:
        x[len(x) - b:] *= (np.linspace(1, 0, b) ** 1.5)[col]
    return x


# ---- đổi cao độ và độ dài ----------------------------------------------------

def resample(x, ratio):
    """Kiểu asetrate: dịch cả formant -> nghe như một con vật TO HƠN.

    ratio < 1 là hạ giọng và kéo dài. Đây là thứ sinh vật hư cấu gần như luôn muốn.
    """
    ln = int(len(x) / ratio)
    src = np.linspace(0, len(x) - 1, ln)
    return np.interp(src, np.arange(len(x)), x)


def semitones(x, st):
    return resample(x, 2 ** (st / 12))


def stretch(x, target_sec, win=4096):
    """Paulstretch rút gọn — kéo dài chất liệu mà không thành tiếng vặn băng."""
    out_len = n(target_sec)
    hop = win // 2
    w = np.hanning(win)
    out = np.zeros(out_len + win)
    rng = np.random.default_rng(7)
    steps = max(1, out_len // hop)
    for i in range(steps):
        src = int(i * (max(len(x) - win, 1) / steps) + rng.integers(-win // 8, win // 8))
        src = int(np.clip(src, 0, max(len(x) - win, 0)))
        grain = x[src:src + win]
        if len(grain) < win:
            grain = np.pad(grain, (0, win - len(grain)))
        out[i * hop:i * hop + win] += grain * w
    return out[:out_len]


# ---- ghép ---------------------------------------------------------------------

def pad_to(x, ln):
    if len(x) >= ln:
        return x[:ln]
    return np.pad(x, (0, ln - len(x)))


def place(out, seg, at):
    """Đặt một mẩu vào đúng chỗ, cắt gọn nếu tràn đuôi."""
    i = max(0, int(at))
    seg = seg[: max(len(out) - i, 0)]
    out[i:i + len(seg)] += seg
    return out


def mix(parts, length=None):
    """Cộng nhiều lớp. (tín hiệu, độ lớn, lệch bao nhiêu giây so với mốc 0)."""
    ln = length or max(len(x) + n(at) for x, _, at in parts)
    out = np.zeros(ln)
    for x, g, at in parts:
        i = n(at) if at else 0
        seg = x[: max(ln - i, 0)]
        out[i:i + len(seg)] += g * seg
    return out


def repeat(x, times, gap):
    step = len(x) + n(gap)
    out = np.zeros(step * (times - 1) + len(x))
    for i in range(times):
        out[i * step:i * step + len(x)] += x
    return out


def loopify(x, cross):
    """Gấp đuôi chồng lên đầu — nghe liền mạch khi lặp, không có cú nhảy."""
    c = min(n(cross), len(x) // 3)
    head, tail = x[:c].copy(), x[len(x) - c:].copy()
    ramp = np.linspace(0, 1, c)
    out = x[: len(x) - c].copy()
    out[:c] = head * ramp + tail * (1 - ramp)
    return out


def _norm(x, peak=1.0):
    m = float(np.max(np.abs(x))) if len(x) else 0.0
    return x * (peak / m) if m > 1e-9 else x


def normalize(x, peak_db=-3.0):
    return _norm(x, 10 ** (peak_db / 20))


def normalize_rms(x, rms_db=-24.0, peak_db=-3.0):
    """Chuẩn theo độ lớn cảm nhận được, không theo đỉnh.

    Tiếng nền thưa (chim rạng sáng, sương rơi) nếu chuẩn theo đỉnh thì một giọt nước
    to nhất sẽ kéo cả lớp nền xuống gần như không nghe thấy.
    """
    r = float(np.sqrt(np.mean(np.square(x)))) if len(x) else 0.0
    if r > 1e-9:
        x = x * (10 ** (rms_db / 20) / r)
    ceiling = 10 ** (peak_db / 20)
    if np.max(np.abs(x)) > ceiling:          # chỉ ghìm khi vượt trần, không thì giữ nguyên
        x = normalize(soft_clip(x), peak_db)  # độ lớn — nếu kéo lên trần thì hỏng mục đích
    return x


def soft_clip(x):
    return np.tanh(x * 1.2) / np.tanh(1.2)


def stereo(x, width=0.35, sec_delay=0.011):
    """Hai kênh lệch nhau một chút — chỉ dùng cho tiếng nền, cue thì để mono."""
    d = n(sec_delay)
    left = x
    right = np.concatenate([x[d:], x[:d]])          # dịch vòng, vẫn lặp liền
    return np.stack([left * (1 - width) + right * width,
                     right * (1 - width) + left * width], axis=1)


BED_RMS = -20.0     # mọi bản nhạc nền của kênh về cùng độ lớn này, dù dựng hay tải về


def finish_bed(x):
    """Bước cuối chung cho mọi bản nền: cùng độ lớn, cùng độ rộng, cùng trần đỉnh.

    Nhờ vậy đổi bản giữa tập, hay chồng hai bản ở chỗ chuyển chương, đều không nhảy âm lượng.
    """
    return stereo(normalize_rms(x, BED_RMS, -6.0), 0.4, 0.013)


# ---- đọc ghi -------------------------------------------------------------------

def write_wav(path, x, sr=SR):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    x = np.asarray(x)
    data = (np.clip(x, -1, 1) * 32767).astype("<i2")
    with wave.open(str(path), "wb") as f:
        f.setnchannels(2 if x.ndim == 2 else 1)
        f.setsampwidth(2)
        f.setframerate(sr)
        f.writeframes(data.tobytes())
    return path


NOTE_NAMES = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]


def pitch_profile(x):
    """Bản nhạc này đang ở nốt nào — để biết hai bản có ghép được với nhau không.

    Trả (tên nốt trầm nhất, tần số của nó, bốn nốt mạnh nhất). Dồn cả phổ về 12 bán cung
    nên hoà âm bậc cao không làm lệch kết quả.
    """
    X = np.abs(np.fft.rfft(x * np.hanning(len(x))))
    f = np.fft.rfftfreq(len(x), 1 / SR)
    m = (f > 40) & (f < 1200)
    f, X = f[m], X[m]
    pc = np.zeros(12)
    np.add.at(pc, np.round(69 + 12 * np.log2(f / 440.0)).astype(int) % 12, X ** 2)
    pc /= max(pc.max(), 1e-12)
    top = [NOTE_NAMES[i] for i in np.argsort(pc)[::-1][:4] if pc[i] > 0.08]
    strong = X ** 2 > 0.02 * (X ** 2).max()
    hz = float(f[strong][0]) if strong.any() else 0.0
    name = NOTE_NAMES[int(round(69 + 12 * np.log2(hz / 440.0))) % 12] if hz else "?"
    return name, hz, top


# La thứ tính từ La = 0: La Si Do Re Mi Fa Sol
A_MINOR = {0, 2, 3, 5, 7, 8, 10}


def pitch_classes(x):
    """Năng lượng dồn về 12 bán cung, lấy La làm mốc 0."""
    X = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    f = np.fft.rfftfreq(len(x), 1 / SR)
    m = (f > 40) & (f < 1600)
    pc = np.zeros(12)
    np.add.at(pc, (np.round(69 + 12 * np.log2(f[m] / 440.0)).astype(int) - 9) % 12, X[m])
    return pc / max(pc.sum(), 1e-12)


def best_shift(x):
    """Kéo bao nhiêu bán cung thì bản nhạc này rơi gọn nhất vào bảy nốt của La thứ.

    Chuyển tông là phép nhân tần số, nên thử hết mười hai khoảng dịch là biết được **trần**
    của việc kéo: dịch được bao nhiêu thì tốt nhất chỉ tới đó. Chấm theo thứ tự:

      1. bao nhiêu năng lượng rơi vào bảy nốt — đây mới là thứ quyết định hai bản có chồng
         lên nhau được không;
      2. hoà nhau (chênh dưới 2%) thì lấy khoảng dịch NHỎ hơn, vì dịch bằng cách lấy mẫu lại
         thì kéo theo cả tốc độ và formant — dịch 5 bán cung là nhạc chậm đi một phần tư;
      3. vẫn hoà thì lấy bản có bè trầm rơi vào La hoặc Mi.

    Cái phép nhân này KHÔNG sửa được thể: bản nào viết ở trưởng, hay có chuyển hợp âm giữa
    chừng, thì xoay kiểu gì cũng còn nốt lạc — lúc ấy phải sinh lại, không cứu bằng máy được.
    """
    pc = pitch_classes(x)
    X = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    f = np.fft.rfftfreq(len(x), 1 / SR)
    m = (f > 35) & (f < 130)
    bass = int((round(69 + 12 * np.log2(f[m][np.argmax(X[m])] / 440.0)) - 9) % 12)

    cand = []
    for s in range(12):
        s = s - 12 if s > 6 else s                 # +10 và −2 là một, lấy đường ngắn
        fit = sum(pc[(i - s) % 12] for i in A_MINOR)
        cand.append((fit, s, (bass + s) % 12 in (0, 7)))
    top = max(c[0] for c in cand)
    near = [c for c in cand if c[0] >= top - 0.02]
    near.sort(key=lambda c: (abs(c[1]), not c[2]))
    return near[0][1], near[0][0]


def read_wav(path, secs=None):
    """Đọc file thật tải về từ Pixabay / Freesound, trả mono float 48 kHz."""
    with wave.open(str(path), "rb") as f:
        ch, w, sr, ln = f.getnchannels(), f.getsampwidth(), f.getframerate(), f.getnframes()
        raw = f.readframes(ln)
    dtype = {1: np.uint8, 2: "<i2", 4: "<i4"}.get(w)
    if dtype is None:
        raise ValueError(f"{path}: chưa đọc được wav {w * 8} bit — xuất lại ở 16 bit")
    x = np.frombuffer(raw, dtype=dtype).astype(np.float64)
    x = (x - 128) / 128 if w == 1 else x / float(2 ** (8 * w - 1))
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    if sr != SR:
        x = np.interp(np.linspace(0, len(x) - 1, int(len(x) * SR / sr)), np.arange(len(x)), x)
    return x[: n(secs)] if secs else x
