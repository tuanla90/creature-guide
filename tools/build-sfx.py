"""Tiếng của một tập: từ công thức trong sfx.json ra file wav.

    PYTHONUTF8=1 python tools/build-sfx.py kanto-001-bulbasaur
    PYTHONUTF8=1 python tools/build-sfx.py kanto-001-bulbasaur --only powder-burst
    PYTHONUTF8=1 python tools/build-sfx.py kanto-001-bulbasaur --list

Mỗi lớp lấy file thật ở assets/sfx-src/<cue>/<synth>.wav nếu có (Pixabay hoặc Freesound CC0 —
luật ở docs/SOUND.md), không có thì dựng tạm bằng bộ tổng hợp dưới đây.

Máy dựng được cái gì, và không dựng được cái gì — đã nghe thử cả 17 cue rồi mới viết:

  ✔ CHẤT LIỆU (vật va vào vật): bẻ, xé, vò lá khô, trượt vải ướt, bùn, roi vút, bước chân.
    Dùng được ngay. Vì tiếng của chúng ĐÚNG LÀ nhiễu qua bộ lọc cộng hưởng rồi tắt dần —
    mô phỏng bằng numpy không phải bắt chước, mà là làm đúng cái vật lý ấy.

  ✘ GIỌNG (ếch, cóc, vạc, quạ): nghe ra ngay là đồ giả. Tai người có phần chuyên trách cho
    tiếng sinh vật, và nó bắt được những thứ chuỗi xung + formant cố định không có: hơi rung
    thất thường, formant trôi trong một tiếng kêu, tạp âm của mô sống.

  ✘ KHÔNG GIAN (lớp nền: rừng trưa, rạng sáng, mưa, đám đông): nghe ra là NHIỄU, không ra
    một CHỖ. Một khu rừng là hàng trăm sự kiện rời nhau ở những khoảng cách khác nhau, cộng
    tiếng vang và độ hút của không khí. Không có bản thu thật thì không có chiều sâu.

Nên tám cue thuộc hai nhóm dưới BẮT BUỘC phải có file thật (Pixabay hoặc Freesound CC0). Tool
vẫn dựng tạm để bạn canh nhịp, nhưng nó đếm riêng và nhắc riêng — đừng đem lên YouTube.

Ra: public/audio/sfx/<ep>/<cue>.wav, 48 kHz 16 bit, đỉnh −3 dBFS. Độ lớn thật nằm ở "volume"
trong sfx.json, chép sang scenes.json.
"""

import json
import sys
import zlib
from pathlib import Path

import numpy as np
from scipy import signal

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolab as al
from audiolab import SR, n

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent


# ---- nguyên liệu dùng lại ------------------------------------------------------

def crackle(sec, rng, density, band, q=1.0, tau=0.004, shape=None):
    """Chất liệu vụn: lá khô, vỏ măng, mưa — mật độ quyết định nó là gì."""
    ln = n(sec)
    x = np.zeros(ln)
    count = max(2, int(density * sec))
    pos = rng.integers(0, ln, count)
    amp = rng.random(count) ** 2.2
    if shape is not None:
        amp = amp * shape(pos / ln)
    np.add.at(x, pos, amp)
    grain = np.exp(-np.arange(n(tau * 6)) / (tau * SR)) * rng.normal(size=n(tau * 6))
    x = signal.fftconvolve(x, grain)[:ln]
    return al.bandpass(x, band, q)


def voice(sec, rng, f0, f_end, bands, am=None, noisiness=0.0, jitter=0.02):
    """Một tiếng có dây thanh: xung thanh môn -> formant -> rung -> bao hình."""
    x = al.impulses(sec, f0, rng, jitter=jitter, f_end=f_end)
    x = al.resonators(x, bands)
    if noisiness:
        x = x * (1 - noisiness) + noisiness * al.bandpass(al.noise(sec, rng), bands[0][0], 1.2) * 0.5
    if am:
        x = al.tremolo(x, am[0], am[1])
    return x


def sweep(sec, rng, f_from, f_to, q=1.2, color="white", curve=1.0, bands=9):
    """Nhiễu có tâm lọc chạy — nền của mọi thứ trượt, hút, vút.

    Làm bằng một dàn lọc cố định rồi chuyển dần độ lớn giữa chúng: mượt hơn và
    không có tiếng "bậc thang" như khi đổi hệ số lọc giữa chừng.
    """
    src = al.noise(sec, rng, color)
    ln = len(src)
    k = np.linspace(0, 1, ln) ** curve
    logf = np.log(f_from * (1 - k) + f_to * k)
    centers = np.geomspace(min(f_from, f_to), max(f_from, f_to), bands)
    width = np.log(centers[1] / centers[0])
    out = np.zeros(ln)
    for c in centers:
        w = np.maximum(0.0, 1 - np.abs(logf - np.log(c)) / width)
        if w.max() > 1e-3:
            out += al.bandpass(src, c, q) * w
    return out


SYNTH = {}


def synth(name):
    def deco(fn):
        SYNTH[name] = fn
        return fn
    return deco


# ---- nền ------------------------------------------------------------------------

@synth("cicada_far")
def _(sec, rng):
    x = al.bandpass(al.noise(sec, rng), 4500, 7)
    x = al.tremolo(x, 82, 0.55)
    return x * (0.7 + 0.3 * np.sin(2 * np.pi * 0.08 * al.t(sec)))


@synth("grass_wind")
def _(sec, rng):
    x = al.bandpass(al.noise(sec, rng, "pink"), 1100, 0.5)
    lfo = 0.55 + 0.45 * np.sin(2 * np.pi * 0.125 * al.t(sec) + 1.1)
    return x * lfo


@synth("birds_sparse_dawn")
def _(sec, rng):
    ln = n(sec)
    out = np.zeros(ln)
    for _ in range(max(2, int(sec * 0.7))):
        d = rng.uniform(0.05, 0.12)
        f0 = rng.uniform(2400, 4200)
        chirp = np.sin(2 * np.pi * np.cumsum(np.linspace(f0, f0 * rng.uniform(0.7, 1.4), n(d))) / SR)
        chirp *= al.env(d, 0.008, d * 0.7)
        al.place(out, chirp * rng.uniform(0.3, 1.0), rng.integers(0, max(1, ln - len(chirp))))
    return out


@synth("dew_drip")
def _(sec, rng):
    ln = n(sec)
    out = np.zeros(ln)
    for _ in range(max(2, int(sec * 0.6))):
        d = 0.05
        f = rng.uniform(700, 1500)
        ping = np.sin(2 * np.pi * np.cumsum(np.linspace(f * 0.8, f * 1.25, n(d))) / SR) * al.decay(d, 0.012)
        al.place(out, ping * rng.uniform(0.4, 1.0), rng.integers(0, max(1, ln - len(ping))))
    return out


@synth("rain_on_leaves")
def _(sec, rng):
    drops = crackle(sec, rng, 950, 4200, 0.9, 0.0015)
    bed = al.bandpass(al.noise(sec, rng, "pink"), 2200, 0.5) * 0.35
    return drops + bed


@synth("crowd_distant")
def _(sec, rng):
    x = al.resonators(al.noise(sec, rng, "pink"), [(420, 3, 1.0), (900, 2.5, 0.5), (1800, 2, 0.2)])
    swell = 0.6 + 0.4 * np.sin(2 * np.pi * 0.07 * al.t(sec)) * np.sin(2 * np.pi * 0.023 * al.t(sec))
    return al.lowpass(x * swell, 1400)


# ---- thân (40–150 Hz): con vật to cỡ nào -----------------------------------------

@synth("cow_bellow")
def _(sec, rng):
    x = voice(sec, rng, 112, 78, [(165, 11, 1.0), (430, 8, 0.55), (880, 6, 0.2)], jitter=0.012)
    return x * al.env(sec, 0.14, sec * 0.5)


@synth("pig_grunt")
def _(sec, rng):
    d = min(sec, 0.18)
    x = voice(d, rng, 145, 105, [(300, 10, 1.0), (720, 7, 0.45)], jitter=0.03)
    return al.pad_to(x * al.env(d, 0.006, d * 0.75), n(sec))


@synth("wood_low_snap")
def _(sec, rng):
    d = min(sec, 0.25)
    imp = np.zeros(n(d))
    imp[0] = 1.0
    imp[n(0.004)] = 0.6
    x = al.resonators(imp + al.noise(d, rng) * 0.25, [(115, 14, 1.0), (295, 9, 0.5), (640, 6, 0.2)])
    return al.pad_to(x * al.decay(d, 0.05), n(sec))


def _thump(f):
    def fn(sec, rng):
        d = min(sec, 0.3)
        ph = np.cumsum(np.linspace(f * 1.35, f, n(d))) / SR
        x = np.sin(2 * np.pi * ph) * al.decay(d, 0.055)
        click = al.lowpass(al.noise(0.006, rng), 900) * 0.4
        return al.pad_to(al.mix([(x, 1.0, 0), (click, 1.0, 0)], n(d)), n(sec))
    return fn


SYNTH["thump_45"] = _thump(45)
SYNTH["thump_38"] = _thump(38)


@synth("earth_settle")
def _(sec, rng):
    d = min(sec, 0.7)
    x = al.lowpass(al.noise(d, rng, "brown"), 120)
    return al.pad_to(x * al.env(d, 0.02, d * 0.9), n(sec))


@synth("wind_suck_low")
def _(sec, rng):
    x = sweep(sec, rng, 210, 65, q=0.8, color="brown", curve=1.6)
    return x * al.env(sec, sec * 0.45, sec * 0.4)


# ---- giọng (200–1200 Hz): nó là loài gì -------------------------------------------

@synth("frog_uong")
def _(sec, rng):
    d = min(sec, 0.55)
    x = voice(d, rng, 96, 88, [(430, 12, 1.0), (910, 9, 0.45), (1750, 7, 0.18)],
              am=(33, 0.7), jitter=0.03)
    return al.pad_to(x * al.env(d, 0.02, d * 0.55), n(sec))


@synth("toad_low")
def _(sec, rng):
    d = min(sec, 0.32)
    x = voice(d, rng, 82, 78, [(350, 13, 1.0), (790, 9, 0.35)], am=(22, 0.75), jitter=0.025)
    return al.pad_to(x * al.env(d, 0.015, d * 0.6), n(sec))


@synth("night_heron")
def _(sec, rng):
    d = min(sec, 0.35)
    x = voice(d, rng, 330, 210, [(700, 6, 1.0), (1500, 5, 0.6), (2800, 4, 0.28)],
              noisiness=0.3, jitter=0.05)
    return al.pad_to(x * al.env(d, 0.004, d * 0.7), n(sec))


@synth("crow_caw")
def _(sec, rng):
    d = min(sec, 0.4)
    x = voice(d, rng, 430, 295, [(800, 5, 1.0), (1900, 4, 0.5), (3300, 3, 0.22)],
              noisiness=0.35, jitter=0.045)
    return al.pad_to(x * al.env(d, 0.008, d * 0.65), n(sec))


# ---- chi tiết (2–8 kHz): ướt hay khô, gần hay xa ------------------------------------

@synth("breath_nostril_wet")
def _(sec, rng):
    air = al.bandpass(al.noise(sec, rng, "pink"), 780, 1.3)
    wet = crackle(sec, rng, 26, 520, 1.6, 0.006) * 0.5
    shape = al.env(sec, sec * 0.35, sec * 0.5)
    return (air + wet) * shape


@synth("breath_puff")
def _(sec, rng):
    d = min(sec, 0.35)
    x = al.bandpass(al.noise(d, rng, "pink"), 1300, 0.9)
    return al.pad_to(x * al.env(d, 0.01, d * 0.85), n(sec))


@synth("powder_hiss")
def _(sec, rng):
    x = sweep(sec, rng, 5200, 3000, q=0.6, curve=0.6)
    return x * al.env(sec, 0.012, sec * 0.85)


@synth("leaf_dry_crush")
def _(sec, rng):
    return crackle(sec, rng, 420, 3800, 0.8, 0.002, shape=lambda k: np.exp(-3.0 * k))


@synth("leaf_tear_slow")
def _(sec, rng):
    return crackle(sec, rng, 260, 3000, 0.9, 0.0035, shape=lambda k: 0.2 + 1.6 * k)


@synth("bamboo_split")
def _(sec, rng):
    cracks = crackle(sec, rng, 22, 2200, 1.5, 0.008)
    ring = al.resonators(cracks, [(880, 9, 0.5), (1700, 7, 0.25)])
    return cracks + ring


@synth("celery_snap_wet")
def _(sec, rng):
    x = crackle(sec, rng, 95, 1800, 1.2, 0.006, shape=lambda k: 0.4 + 1.2 * np.sin(np.pi * k))
    return x + al.resonators(x, [(620, 8, 0.4)])


@synth("wood_tension")
def _(sec, rng):
    """Vặn: dính rồi trượt, dính rồi trượt — tần số đi bộ ngẫu nhiên, biên độ giật cục."""
    ln = n(sec)
    walk = np.cumsum(rng.normal(0, 6.0, ln))
    walk = walk - walk.mean()
    f = np.clip(270 + walk, 140, 460)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR)
    grip = np.abs(rng.normal(size=ln))
    grip = al.lowpass(grip, 14) ** 2
    return al.bandpass(x * grip, 900, 0.9)


@synth("wet_cloth_slide")
def _(sec, rng):
    x = sweep(sec, rng, 700, 1700, q=1.1, color="pink", curve=0.8)
    wob = 0.55 + 0.45 * np.sin(2 * np.pi * 2.6 * al.t(sec))
    return x * wob * al.env(sec, sec * 0.25, sec * 0.45)


@synth("rope_soft")
def _(sec, rng):
    return crackle(sec, rng, 40, 620, 1.4, 0.01) * al.env(sec, sec * 0.2, sec * 0.5)


@synth("rope_whip")
def _(sec, rng):
    d = min(sec, 0.45)
    x = sweep(d, rng, 500, 3200, q=1.4, curve=1.8)
    return al.pad_to(x * al.env(d, d * 0.7, d * 0.25), n(sec))


@synth("wing_wind")
def _(sec, rng):
    ln = n(sec)
    out = np.zeros(ln)
    flaps = max(2, int(sec * 3.5))
    for i in range(flaps):
        d = 0.16
        flap = sweep(d, rng, 260, 900, q=1.0, color="pink") * al.env(d, 0.02, d * 0.7)
        al.place(out, flap, i * (ln / flaps) + rng.integers(0, n(0.03)))
    return out + al.bandpass(al.noise(sec, rng, "pink"), 1800, 0.5) * 0.25


@synth("mud_suck")
def _(sec, rng):
    d = min(sec, 0.6)
    pull = sweep(d, rng, 190, 950, q=2.2, color="pink", curve=1.4)
    pops = crackle(d, rng, 55, 700, 1.8, 0.01, shape=lambda k: 0.3 + 1.4 * k)
    x = al.mix([(pull, 1.0, 0), (pops, 0.7, 0)], n(d))
    return al.pad_to(x * al.env(d, 0.02, d * 0.5), n(sec))


# ---- áp công thức ------------------------------------------------------------------

def apply_fx(x, ops):
    for op in ops:
        k, a = op[0], op[1:]
        if k == "rate":
            x = al.resample(x, a[0])
        elif k == "semitones":
            x = al.semitones(x, a[0])
        elif k == "tremolo":
            x = al.tremolo(x, a[0], a[1])
        elif k == "lowpass":
            x = al.lowpass(x, a[0])
        elif k == "highpass":
            x = al.highpass(x, a[0])
        elif k == "bandpass":
            x = al.bandpass(x, a[0], a[1] if len(a) > 1 else 0.707)
        elif k == "echo":
            x = al.echo(x, a[0], a[1])
        elif k == "stretch":
            x = al.stretch(x, a[0])
        elif k == "env":
            x = x * al.env(len(x) / SR, a[0], a[1])
        elif k == "fade":
            x = al.fade(x, a[0], a[1])
        elif k == "trim":
            x = x[: n(a[0])]
        elif k == "repeat":
            x = al.repeat(x, int(a[0]), a[1])
        elif k == "gain_db":
            x = x * 10 ** (a[0] / 20)
        elif k == "loop":
            x = al.loopify(x, a[0])
        elif k == "mono":
            pass                                   # mọi thứ ở đây vốn đã mono
        else:
            raise ValueError(f"phép xử lý lạ: {k}")
    return x


def must_be_real(cue):
    """Cue này có thuộc loại máy không dựng nổi không?

    Suy ra từ chính dữ liệu, không cần đánh dấu tay: có lớp GIỌNG (role "voice") là có dây
    thanh, còn cue lặp (loop) là một KHÔNG GIAN. Hai loại ấy phải là bản thu thật.
    """
    return bool(cue.get("loop")) or any(L["role"] == "voice" for L in cue["layers"])


def build_cue(cid, cue, srcdir):
    rng = np.random.default_rng(zlib.crc32(cid.encode()))
    sec = float(cue["sec"])
    parts, real = [], []
    for L in cue["layers"]:
        name = L["synth"]
        f = srcdir / cid / (L.get("file") or f"{name}.wav")
        if f.exists():
            x = al.read_wav(f)
            x = al.pad_to(x, n(sec)) if len(x) < n(sec) else x[: n(sec)]
            real.append(f"{L['role']}:{L['species']}")
        else:
            if name not in SYNTH:
                raise KeyError(f"{cid}: chưa có công thức tổng hợp '{name}'")
            x = SYNTH[name](sec, rng)
        parts.append((al._norm(x), float(L.get("gain", 1.0)), float(L.get("at", 0.0))))

    x = al.mix(parts)                              # ba lớp bắt đầu cùng một khoảnh khắc
    x = apply_fx(x, cue.get("fx", []))
    if cue.get("loop"):
        x = al.stereo(al.normalize_rms(x, -24.0), 0.3)   # nền: chuẩn theo độ lớn nghe được
    else:
        x = al.normalize(al.soft_clip(al._norm(x, 0.95)), -3.0)
    return x, real


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    slug = args[0] if args else "kanto-001-bulbasaur"
    only = args[1] if "--only" in flags and len(args) > 1 else None

    spec = json.loads((ROOT / "videos" / slug / "sfx.json").read_text(encoding="utf-8"))
    ep = spec["ep"]
    outdir = ROOT / "public" / "audio" / "sfx" / ep
    srcdir = ROOT / "assets" / "sfx-src"

    if "--list" in flags:
        for cid, cue in spec["cues"].items():
            lay = " · ".join(f"{l['role']}={l['species']}" for l in cue["layers"])
            print(f"{cid:16} beat {','.join(cue['beat']):8} {lay}")
        return

    made, synthed, cho_thay = 0, 0, []
    for cid, cue in spec["cues"].items():
        if only and cid != only:
            continue
        x, real = build_cue(cid, cue, srcdir)
        al.write_wav(outdir / f"{cid}.wav", x)
        n_layers = len(cue["layers"])
        if len(real) == n_layers:
            tag = "thật"
        elif must_be_real(cue):
            tag = "PHẢI THAY"
            cho_thay.append((cid, cue))
        else:
            tag = "tổng hợp"
            synthed += n_layers - len(real)
        made += 1
        print(f"  ✓ {cid:16} {len(x) / SR:5.1f}s  vol {cue['volume']:.2f}  [{tag:9}] {cue['desc']}")

    print(f"\n{made} cue -> public/audio/sfx/{ep}/")
    if synthed:
        print(f"  {synthed} lớp chất liệu đang là tiếng tổng hợp — dùng tạm được, thay dần thì hơn.")
    if cho_thay:
        print(f"\n⚠ {len(cho_thay)} cue máy KHÔNG dựng nổi: giọng thì tai người bắt bài ngay, lớp nền"
              f" thì ra\n  nhiễu chứ không ra một chỗ. Đang là bản tạm để canh nhịp, PHẢI thay trước"
              f" khi đăng.\n  Từ khoá đi tìm (Pixabay / Freesound lọc CC0):\n")
        for cid, cue in cho_thay:
            for L in cue["layers"]:
                if L["role"] == "voice" or cue.get("loop"):
                    print(f"    {cid:15} {L['role']:8} {L['species']:24} → \"{L['query']}\"")
        print("\n  Tải về assets/sfx-src/<cue>/<tên lớp>.wav rồi chạy lại — công thức giữ nguyên.")
    print("Neo vào scenes.json:  "
          '{ "el": "sfx", "name": "%s/<cue>.wav", "atWord": "...", "volume": ... }' % ep)


if __name__ == "__main__":
    main()
