"""Sao lưu một chiều những thứ không tái tạo được của một tập.

    PYTHONUTF8=1 python tools/backup-episode.py <slug> --to "<thư mục đích>"
    PYTHONUTF8=1 python tools/backup-episode.py <slug>            # xem sẽ chép gì, không chép

Đích thường là một thư mục Google Drive dưới máy, ví dụ:
    --to "G:/My Drive/creature-field-guide"
Đặt sẵn vào biến môi trường CFG_BACKUP_DIR thì khỏi gõ mỗi lần.

MỘT CHIỀU, VÀ KHÔNG BAO GIỜ XOÁ. Script này chỉ chép thêm và ghi đè file đã đổi. Nó không xoá gì ở
đích, kể cả khi bên máy đã xoá — đó là điểm khác giữa sao lưu và đồng bộ. Đồng bộ hai chiều thì xoá
nhầm dưới máy là mất luôn bản sao.

Chép cái gì: chỉ nhóm **không tái tạo được** (xem docs/BUSINESS-FLOW.md mục E3).

  public/img/<ep>/          ảnh đã chốt — sinh lại ra ảnh khác là hỏng toạ độ callout
  public/video/<ep>/        clip đã trả token
  public/audio/sfx/<ep>/    tiếng đã ghép
  public/audio/music/       thư viện nhạc của kênh (dùng chung, chép một lần)
  videos/<slug>/            content.py, scenes.json, timings.json, review-notes.json…

Không chép: out/ (render lại được), node_modules, prompts/ và bible/ (đã nằm trong git).
"""
import os, shutil, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
if not args:
    sys.exit(__doc__)
SLUG = args[0]
EP = "-".join(SLUG.split("-")[:2])

dest = None
if "--to" in sys.argv:
    dest = Path(sys.argv[sys.argv.index("--to") + 1])
elif os.environ.get("CFG_BACKUP_DIR"):
    dest = Path(os.environ["CFG_BACKUP_DIR"])

if not (ROOT / "videos" / SLUG).is_dir():
    sys.exit(f"không có videos/{SLUG}/")

SOURCES = [
    Path("videos") / SLUG,
    Path("public/img") / EP,
    Path("public/video") / EP,
    Path("public/audio/sfx") / EP,
    Path("public/audio/music"),
]


def files_under(rel: Path):
    src = ROOT / rel
    if not src.is_dir():
        return []
    return [p for p in sorted(src.rglob("*")) if p.is_file()]


def human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


plan, total = [], 0
for rel in SOURCES:
    hits = files_under(rel)
    size = sum(p.stat().st_size for p in hits)
    total += size
    plan.append((rel, hits, size))
    mark = "—" if not hits else f"{len(hits):>4} file  {human(size):>9}"
    print(f"  {mark}  {rel.as_posix()}/")

print(f"\n  tổng {human(total)}")

if dest is None:
    print("\nChưa có đích. Thêm --to \"<thư mục>\" hoặc đặt CFG_BACKUP_DIR. Chưa chép gì cả.")
    sys.exit(0)

if not dest.is_dir():
    sys.exit(f"\nđích không tồn tại: {dest}\n"
             "Tạo thư mục đó trước (và chắc chắn Drive đã đồng bộ xong thư mục ấy).")

print(f"\nchép sang {dest}\n")
copied = skipped = 0
for rel, hits, _ in plan:
    for src in hits:
        out = dest / rel / src.relative_to(ROOT / rel)
        # bỏ qua nếu đích đã có bản cùng cỡ và mới bằng hoặc mới hơn
        if out.exists() and out.stat().st_size == src.stat().st_size \
                and out.stat().st_mtime >= src.stat().st_mtime:
            skipped += 1
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, out)
        copied += 1
        print(f"  + {rel.as_posix()}/{src.relative_to(ROOT / rel).as_posix()}")

print(f"\n  chép {copied} · bỏ qua {skipped} (đã có bản giống)")
print("  không xoá gì ở đích — đây là sao lưu, không phải đồng bộ.")
