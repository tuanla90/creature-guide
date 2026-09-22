"""Nhập ảnh từ file ZIP của Batch Studio Pro (Flow) vào public/img/<ep>/.

    python tools/import-flow.py <file.zip> [kanto-001]

ZIP đặt tên "<id>_<n>.jpg" (n = số thứ tự trong batch) -> đổi thành "<id>.jpg" đúng như
prompts/<ep>.jsonl hẹn. Id lạ (không có trong jsonl) thì bỏ qua và báo ra.
"""
import json, re, sys, zipfile
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
zpath, ep = Path(sys.argv[1]), (sys.argv[2] if len(sys.argv) > 2 else "kanto-001")
want = {json.loads(l)["id"]: ROOT / json.loads(l)["file"]
        for l in (ROOT / "prompts" / f"{ep}.jsonl").read_text(encoding="utf-8").splitlines()}

with zipfile.ZipFile(zpath) as z:
    for name in z.namelist():
        stem = re.sub(r"_\d+$", "", Path(name).stem)
        if stem not in want:
            print(f"bỏ qua {name}: id không có trong prompts/{ep}.jsonl"); continue
        out = want[stem]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(z.read(name))
        print(f"{name} -> {out.relative_to(ROOT)}")
missing = [i for i, p in want.items() if not p.exists()]
print(f"còn thiếu {len(missing)}: {', '.join(missing)}" if missing else "đủ ảnh")
