"""Sao lưu cả dự án sang chỗ khác — đủ để dựng lại trên một máy mới.

    PYTHONUTF8=1 python tools/backup-all.py                     # ra <CFG_BACKUP_DIR hoặc ../cfg-backup>
    PYTHONUTF8=1 python tools/backup-all.py --to "G:/My Drive/creature-field-guide-backup"
    PYTHONUTF8=1 python tools/backup-all.py --zip               # gói thêm một file .zip để tải lên tay

Chép MỘT CHIỀU (không bao giờ xoá gì ở đích), gồm:
  git/creature-field-guide.bundle   mọi nhánh của repo kênh (git clone <bundle> là có lại lịch sử)
  git/blog2video.bundle             mọi nhánh của engine — nhánh feat/specimen-freeze-media chưa lên GitHub
  files/…                           mọi thứ git KHÔNG giữ: public/, assets/, bible/refs/, out/, inbox/,
                                    experiments/ — chỉ chép file mới hoặc đã đổi

Không chép .env (khoá bí mật) và node_modules (npm install là có lại).
Chạy định kỳ: xem docs/BACKUP.md (Task Scheduler + Google Drive for Desktop).
"""
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
ENGINE = Path(os.environ.get("CFG_ENGINE_DIR", r"D:\Users\tuanla2\blog2video"))
KEEP = ["public", "assets", "bible/refs", "out", "inbox", "experiments"]
SKIP_DIRS = {"node_modules", ".git", "__pycache__", "worktrees"}


def arg(flag, default=None):
    a = sys.argv[1:]
    return a[a.index(flag) + 1] if flag in a and a.index(flag) + 1 < len(a) else default


def bundle(repo, out):
    out.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["git", "-C", str(repo), "bundle", "create", str(out), "--all"],
                       capture_output=True, text=True)
    print(f"  {'✓' if r.returncode == 0 else '✗'} {out.name}" + ("" if r.returncode == 0 else f": {r.stderr.strip()}"))


def mirror(dst):
    n = size = 0
    for top in KEEP:
        src = ROOT / top
        if not src.exists():
            continue
        for p in src.rglob("*"):
            if p.is_dir() or SKIP_DIRS & set(p.parts):
                continue
            q = dst / p.relative_to(ROOT)
            st = p.stat()
            if q.exists() and q.stat().st_size == st.st_size and q.stat().st_mtime >= st.st_mtime:
                continue
            q.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, q)
            n, size = n + 1, size + st.st_size
    print(f"  ✓ files/: {n} file mới hoặc đã đổi ({size / 1e6:.0f} MB)")


def main():
    dst = Path(arg("--to") or os.environ.get("CFG_BACKUP_DIR") or ROOT.parent / "cfg-backup")
    print(f"Sao lưu → {dst}")
    bundle(ROOT, dst / "git" / "creature-field-guide.bundle")
    if ENGINE.exists():
        bundle(ENGINE, dst / "git" / "blog2video.bundle")
    mirror(dst / "files")
    (dst / "RESTORE.txt").write_text(
        "Dựng lại trên máy mới:\n"
        "  git clone git/creature-field-guide.bundle creature-field-guide\n"
        "  git clone git/blog2video.bundle blog2video && cd blog2video && git checkout feat/specimen-freeze-media\n"
        "  chép files/* đè vào thư mục creature-field-guide\n"
        "  sửa đường dẫn blog2video trong package.json nếu khác D:/Users/tuanla2/blog2video, rồi npm install\n"
        "  tạo lại .env từ .env.example\n", encoding="utf-8")
    if "--zip" in sys.argv:
        z = dst.parent / f"{dst.name}-{date.today().isoformat()}.zip"
        with zipfile.ZipFile(z, "w", zipfile.ZIP_STORED) as zf:
            for p in dst.rglob("*"):
                if p.is_file():
                    zf.write(p, p.relative_to(dst))
        print(f"  ✓ {z}  ({z.stat().st_size / 1e6:.0f} MB) — tải file này lên Drive")


if __name__ == "__main__":
    main()
