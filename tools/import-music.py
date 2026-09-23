"""Một bản nhạc tải về -> bản nền lặp được của kênh.

    PYTHONUTF8=1 python tools/import-music.py assets/music-src/gemini-lyria-field-bed.mp3
    PYTHONUTF8=1 python tools/import-music.py <file> --name field-bed-lyria --cross 6 --shift -2
    PYTHONUTF8=1 python tools/import-music.py <file> --name music-strike --once

Nhạc sinh ra từ Gemini (Lyria) hay tải từ YouTube Audio Library luôn có mở đầu và có kết —
nó là một bản nhạc. Bản nền thì không được có kết: engine lặp nó suốt cả tập, và tai bắt ngay
chỗ nối. Tool này cắt phần mở phần tắt, rồi gấp đuôi chồng lên đầu để vòng lặp khép kín.

Nguồn phải ghi lại: file gốc để nguyên trong assets/music-src/, đừng ghi đè. Nhạc là thứ dễ
dính Content ID nhất trong cả tập — xem docs/SOUND.md.
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolab as al
from audiolab import SR

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent


def decode(src):
    """mp3 / m4a / opus -> mảng mono 48 kHz, qua ffmpeg đi kèm Remotion."""
    if src.suffix.lower() == ".wav":
        return al.read_wav(src)
    npx = shutil.which("npx") or shutil.which("npx.cmd")
    if not npx:
        raise SystemExit("không thấy npx — cần ffmpeg đi kèm Remotion để giải mã, hoặc tự xuất ra .wav")
    tmp = Path(tempfile.gettempdir()) / f"{src.stem}-48k.wav"
    subprocess.run([npx, "remotion", "ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                    "-ar", str(SR), "-ac", "1", "-c:a", "pcm_s16le", str(tmp)],
                   check=True, timeout=600)
    return al.read_wav(tmp)


def trim_ends(x, floor=0.6):
    """Bỏ đoạn mở dần và đoạn tắt dần — chỗ duy nhất nói ra rằng bản nhạc có đầu có cuối."""
    w = al.n(0.25)
    c = np.cumsum(np.abs(x))                       # trung bình trượt bằng tổng tích luỹ:
    env = (c[w:] - c[:-w]) / w                     # np.convolve trên 8 triệu mẫu thì treo máy
    live = np.flatnonzero(env > floor * np.median(env))
    if len(live) < 2:
        return x
    return x[live[0]:live[-1]]


def main():
    argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        return
    src = Path(argv[0])
    name = argv[argv.index("--name") + 1] if "--name" in argv else src.stem
    cross = float(argv[argv.index("--cross") + 1]) if "--cross" in argv else 6.0
    shift = argv[argv.index("--shift") + 1] if "--shift" in argv else 0.0

    once = "--once" in argv          # đoạn chơi một lần (cú ra đòn, trả bài, kết tập)
    x = decode(src)
    raw = len(x) / SR
    if shift == "auto":                  # tự tìm khoảng lệch so với La thứ
        shift, fit = al.best_shift(x[: al.n(60)])
        print(f"    tự dò tông: kéo {shift:+d} bán cung, {fit * 100:.0f}% năng lượng rơi vào La thứ")
    shift = float(shift)
    if shift:
        x = al.semitones(x, shift)       # kéo về tông của kênh; dịch cả formant, nhạc cụ nghe to hơn
    if once:
        x = al.fade(x, 0.15, 1.2)    # giữ nguyên đầu đuôi: đoạn này CÓ mở và CÓ kết
    else:
        x = al.loopify(trim_ends(x), cross)

    # Khoét dải lời dẫn, chỉ khi bản nhạc thật sự có gì ở đó.
    probe = x[: al.n(30)]
    f = np.fft.rfftfreq(len(probe), 1 / SR)
    X = np.abs(np.fft.rfft(probe)) ** 2
    speech = X[(f >= 1800) & (f < 4500)].sum() / max(X.sum(), 1e-9)
    if speech > 0.02:
        x = x - 0.5 * al.bandpass(x, 2600, 0.6)
        note = f"khoét dải 2–4 kHz (đang chiếm {speech * 100:.0f}% năng lượng)"
    else:
        note = "dải 2–4 kHz vốn đã trống, để nguyên"

    key, hz, top = al.pitch_profile(x[: al.n(45)])
    out = al.write_wav(ROOT / "public" / "audio" / "music" / f"{name}.wav", al.finish_bed(x))
    seam = abs(x[0] - x[-1]) / max(np.percentile(np.abs(np.diff(x)), 99.9), 1e-9)
    print(f"  ✓ {out.name}")
    how = "chơi một lần, giữ nguyên mở và kết" if once else f"chồng {cross:.0f}s ở chỗ nối"
    print(f"    {raw:.0f}s -> {len(x) / SR:.0f}s, {how} · {note}")
    if not once:
        print(f"    chỗ nối lệch {seam:.2f} lần một bước sóng thường (dưới 1 là tai không nghe ra)")
    print(f"    tông: bè trầm {hz:.1f} Hz = {key} · nốt mạnh {' '.join(top)}")
    print(f"    kênh đi theo La thứ (La–Mi). Lệch tông thì dựng lại, hoặc --shift <bán cung>.")
    print(f"    dùng: video.config.json -> \"bed\": \"audio/music/{name}.wav\"")


if __name__ == "__main__":
    main()
