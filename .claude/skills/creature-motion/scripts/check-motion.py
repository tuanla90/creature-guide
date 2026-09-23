"""Đo xem cái gì trong vòng lặp thật sự động, và động bao nhiêu.

    PYTHONUTF8=1 python .claude/skills/creature-motion/scripts/check-motion.py <file.gif> \
        --still SỌ=0.46,0.42,0.68,0.62 --still CHÂN=0.44,0.80,0.90,0.88 \
        --move SƯỜN=0.72,0.60,0.88,0.85

Cổng của skill là "sọ, chân chạm đất và vật cứng phải đứng yên; chuyển động phải đọc ra là thở".
Nhìn contact sheet không kết luận được chuyện đó — chênh lệch vài pixel mắt không thấy, nhưng
xem ở tốc độ thật thì thành cả con vật phồng lên. Đo thì thấy ngay.

Dấu hiệu ĐÚNG: vùng phải-động lệch gấp vài lần vùng phải-đứng-yên.
Sọ mà lệch ngang hoặc hơn sườn thì gần như chắc chắn đặt sai `face_side` trong anchors.

Vùng ghi theo toạ độ CHUẨN HOÁ trên ảnh: tên=x0,y0,x1,y1 (0..1, gốc trên-trái).
"""
import argparse, sys
import numpy as np
from PIL import Image, ImageSequence

STILL_MAX, MOVE_MIN = 1.0, 0.8


def region(spec):
    name, nums = spec.split("=", 1)
    x0, y0, x1, y1 = (float(v) for v in nums.split(","))
    return name, (x0, y0, x1, y1)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("gif")
    ap.add_argument("--still", action="append", default=[], help="tên=x0,y0,x1,y1 — phải đứng yên")
    ap.add_argument("--move", action="append", default=[], help="tên=x0,y0,x1,y1 — phải động")
    a = ap.parse_args()

    frames = [np.asarray(f.convert("RGB"), dtype=np.int16)
              for f in ImageSequence.Iterator(Image.open(a.gif))]
    H, W = frames[0].shape[:2]
    print(f"  {len(frames)} khung · {W}x{H}")

    bad = 0
    for kind, specs in (("yên", a.still), ("động", a.move)):
        for name, (x0, y0, x1, y1) in (region(s) for s in specs):
            sl = (slice(int(y0 * H), int(y1 * H)), slice(int(x0 * W), int(x1 * W)))
            d = max(float(np.abs(f[sl] - frames[0][sl]).mean()) for f in frames[1:])
            flag = ""
            if kind == "yên" and d > STILL_MAX:
                flag, bad = "  ← ĐỘNG QUÁ, phải đứng yên", bad + 1
            if kind == "động" and d < MOVE_MIN:
                flag, bad = "  ← gần như không động", bad + 1
            print(f"  [{kind}] {name:14} lệch trung bình {d:6.2f}{flag}")

    print("\n  ĐẠT" if not bad else f"\n  {bad} vùng chưa đạt")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
