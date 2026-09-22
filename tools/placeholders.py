"""Ảnh giữ chỗ cho một tập: đúng tên file mà prompts/<ep>.jsonl hẹn, để dựng video trước khi có ảnh.

    python tools/placeholders.py kanto-001

Chỉ tạo file CHƯA có — ảnh thật tải về từ Flow đặt đè cùng tên là xong, chạy lại không ghi đè.
Ảnh có lưới 10% để đọc toạ độ callout (x, y trên ảnh) khi soạn scenes.json.
"""
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ep = sys.argv[1] if len(sys.argv) > 1 else "kanto-001"
W, H = 2400, 1350

def font(size):
    for f in ("arial.ttf", "DejaVuSans.ttf"):
        try: return ImageFont.truetype(f, size)
        except OSError: pass
    return ImageFont.load_default()

made = 0
for line in (ROOT / "prompts" / f"{ep}.jsonl").read_text(encoding="utf-8").splitlines():
    s = json.loads(line)
    out = ROOT / s["file"]
    if out.exists(): continue
    out.parent.mkdir(parents=True, exist_ok=True)
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    for y in range(H):                      # gradient dọc cho có cảm giác chuyển động khi camera lia
        c = int(38 + 40 * y / H); d.line([(0, y), (W, y)], fill=(c, c + 8, c - 6))
    for i in range(1, 10):
        d.line([(W * i / 10, 0), (W * i / 10, H)], fill=(90, 96, 84), width=2)
        d.line([(0, H * i / 10), (W, H * i / 10)], fill=(90, 96, 84), width=2)
        d.text((W * i / 10 + 8, 8), f".{i}", fill=(150, 156, 140), font=font(30))
        d.text((8, H * i / 10 + 6), f".{i}", fill=(150, 156, 140), font=font(30))
    d.text((W / 2, H / 2 - 40), s["id"], fill=(235, 240, 225), font=font(110), anchor="mm")
    d.text((W / 2, H / 2 + 70), "PLACEHOLDER — thay bằng ảnh Flow cùng tên", fill=(170, 176, 160), font=font(44), anchor="mm")
    im.save(out, quality=88)
    made += 1
print(f"{made} ảnh giữ chỗ mới trong {ROOT / 'public' / 'img'}")
