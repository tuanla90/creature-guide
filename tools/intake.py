"""Nhận file vừa tải về: đổi tên, cắt, đưa vào đúng chỗ — và không để lại bản sao nào.

    PYTHONUTF8=1 python tools/intake.py                          # quét Downloads, nạp hết
    PYTHONUTF8=1 python tools/intake.py --dry-run                # xem trước, không đụng file
    PYTHONUTF8=1 python tools/intake.py --sfx call-k7-soft/frog_uong
    PYTHONUTF8=1 python tools/intake.py --status                 # đang nặng bao nhiêu, trùng ở đâu

**Chuyển chứ không chép.** Một file tải về chỉ được nằm ở đúng một chỗ: `assets/`. Mọi thứ trong
`public/audio/` là bản dựng ra từ nó, xoá lúc nào cũng được và dựng lại bằng một lệnh. Chép thêm
một bản "cho chắc" là cách nhanh nhất để sáu tháng sau không ai biết bản nào là bản thật.

Nhận ra file bằng ruột chứ không bằng đuôi tên: trình duyệt trong app lưu file thành `.tmp` với
tên là một chuỗi ngẫu nhiên, nên cứ soi mấy byte đầu.

Nhạc thì tự khớp tên: tải về đặt đúng tên bối cảnh (`field-bed-stalk.mp3`) là tool biết đường đi.
Tiếng thì phải chỉ chỗ, vì tên file tải về không nói được nó là lớp nào của cue nào.
"""

import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
PY = [sys.executable]

# Vài byte đầu của từng định dạng — đuôi tên có thể sai, ruột thì không.
MAGIC = {b"ID3": "mp3", b"\xff\xfb": "mp3", b"\xff\xf3": "mp3", b"\xff\xf2": "mp3",
         b"RIFF": "wav", b"OggS": "ogg", b"fLaC": "flac"}


def sniff(p):
    """File này có phải audio không, và là loại gì."""
    try:
        head = p.open("rb").read(12)
    except OSError:
        return None
    for m, kind in MAGIC.items():
        if head.startswith(m):
            return kind
    return "m4a" if head[4:8] == b"ftyp" else None


def mb(n):
    return f"{n / 1048576:.0f} MB"


def pieces():
    """Bảng bối cảnh nhạc, đọc thẳng từ build-music.py để hai bên không lệch nhau."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("bm", ROOT / "tools" / "build-music.py")
    bm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bm)
    return {c["file"][:-4]: c for c in bm.PIECES.values()}


def newest_audio(src_dir):
    found = [(p.stat().st_mtime, p) for p in src_dir.iterdir() if p.is_file() and sniff(p)]
    if not found:
        raise SystemExit(f"không thấy file âm thanh nào trong {src_dir}")
    return max(found)[1]


def take_music(src_dir, dry):
    """Mọi file tải về có tên khớp một bối cảnh -> assets/music-src/ rồi dựng ra wav."""
    known = pieces()
    done = 0
    for p in sorted(src_dir.iterdir()):
        if not p.is_file() or p.stem not in known or sniff(p) is None:
            continue
        dest = ROOT / "assets" / "music-src" / f"{p.stem}.mp3"
        cue = known[p.stem]
        once = ["--once"] if cue.get("shape") else []
        print(f"  {p.name}  ({mb(p.stat().st_size)})")
        print(f"    -> assets/music-src/{dest.name}   [chuyển, không chép]")
        print(f"    -> public/audio/music/{p.stem}-lyria.wav   "
              f"{' '.join(['--shift auto'] + once)}", flush=True)
        if not dry:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(p), str(dest))
            subprocess.run(PY + [str(ROOT / "tools" / "import-music.py"), str(dest),
                                 "--name", f"{p.stem}-lyria", "--shift", "auto"] + once, check=True)
        done += 1
    if not done:
        print("  không có file nhạc nào khớp tên bối cảnh.")
        print("  Tải về thì đặt đúng tên ở cột cuối docs/MUSIC-PROMPTS.md, vd field-bed-stalk.mp3")
    return done


def take_sfx(spec, src_dir, dry):
    """Một file -> đúng một lớp của một cue, rồi dựng lại riêng cue ấy."""
    if "/" not in spec:
        raise SystemExit("cần dạng <cue>/<lớp>, vd: call-k7-soft/frog_uong\n"
                         "Danh sách đang thiếu: python tools/build-sfx.py <slug>")
    cue, layer = spec.split("/", 1)
    src = newest_audio(src_dir)
    dest = ROOT / "assets" / "sfx-src" / cue / f"{layer}.wav"
    print(f"  {src.name}  ({mb(src.stat().st_size)}, {sniff(src)})")
    print(f"    -> assets/sfx-src/{cue}/{layer}.wav   [chuyển, đổi sang wav 48 kHz mono]",
          flush=True)
    if dry:
        return 1
    dest.parent.mkdir(parents=True, exist_ok=True)
    npx = shutil.which("npx") or shutil.which("npx.cmd")
    if sniff(src) == "wav" and not npx:
        shutil.move(str(src), str(dest))
    else:
        subprocess.run([npx, "remotion", "ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                        "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(dest)], check=True)
        src.unlink()                      # bản gốc đã nằm trong dest, đừng giữ hai bản
    slug = next((d.name for d in (ROOT / "videos").iterdir() if (d / "sfx.json").exists()), None)
    if slug:
        subprocess.run(PY + [str(ROOT / "tools" / "build-sfx.py"), slug, "--only", cue], check=True)
    return 1


def status():
    print("Bản gốc — thứ duy nhất không dựng lại được:\n")
    total = 0
    for d in (ROOT / "assets" / "music-src", ROOT / "assets" / "sfx-src"):
        n = sum(1 for _ in d.rglob("*")) if d.exists() else 0
        sz = sum(p.stat().st_size for p in d.rglob("*") if p.is_file()) if d.exists() else 0
        total += sz
        print(f"  {str(d.relative_to(ROOT)):24} {n:3} file  {mb(sz):>8}")
    print(f"\nBản dựng ra — xoá lúc nào cũng được:\n")
    for d in (ROOT / "public" / "audio" / "music", ROOT / "public" / "audio" / "sfx"):
        n = sum(1 for _ in d.rglob("*.wav")) if d.exists() else 0
        sz = sum(p.stat().st_size for p in d.rglob("*") if p.is_file()) if d.exists() else 0
        print(f"  {str(d.relative_to(ROOT)):24} {n:3} file  {mb(sz):>8}")

    # Bản gốc nằm hai nơi thì báo — đây là kiểu lãng phí hay xảy ra nhất.
    dl = Path.home() / "Downloads"
    if dl.exists():
        dup = [p for p in dl.iterdir()
               if p.is_file() and (ROOT / "assets" / "music-src" / p.name).exists()]
        if dup:
            print(f"\n⚠ {len(dup)} file còn sót bản sao trong Downloads "
                  f"({mb(sum(p.stat().st_size for p in dup))}) — nạp rồi thì xoá đi:")
            for p in dup[:8]:
                print(f"    {p.name}")
    print(f"\nTổng bản gốc: {mb(total)}. Đây là phần phải sao lưu; phần còn lại thì không.")


def main():
    argv = sys.argv[1:]
    dry = "--dry-run" in argv
    src_dir = Path(argv[argv.index("--from") + 1]) if "--from" in argv else Path.home() / "Downloads"

    if "--status" in argv:
        return status()
    if not src_dir.exists():
        raise SystemExit(f"không thấy thư mục {src_dir} — chỉ chỗ khác bằng --from <thư mục>")

    print(f"Quét {src_dir}{'  (--dry-run: không đụng file nào)' if dry else ''}\n")
    if "--sfx" in argv:
        n = take_sfx(argv[argv.index("--sfx") + 1], src_dir, dry)
    else:
        n = take_music(src_dir, dry)
    print(f"\n{n} file đã nạp." if n and not dry else "")
    if n and not dry:
        print("Bản gốc nằm trong assets/ (ngoài git, phải sao lưu).")
        print("Bản dựng nằm trong public/audio/ (xoá được, dựng lại bằng một lệnh).")


if __name__ == "__main__":
    main()
