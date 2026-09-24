"""Ảnh này là ảnh thật hay ảnh giữ chỗ?

tools/placeholders.py vẽ ảnh giữ chỗ 2400×1350 gần như một màu, ghi "PLACEHOLDER — thay bằng ảnh
Flow cùng tên" — để dựng thử khi chưa sinh ảnh. Chúng nằm cùng thư mục, cùng tên với ảnh thật, nên
chỉ nhìn tên file thì tưởng đã có ảnh. Tập 001 từng có mười tấm như vậy bị coi là "có sẵn".
"""
from functools import lru_cache
from pathlib import Path

PLACEHOLDER_SIZE = (2400, 1350)
FLAT = 25          # độ lệch chuẩn độ sáng; ảnh thật của Flow đo được 34–88, ảnh giữ chỗ 18–21


@lru_cache(maxsize=None)
def is_placeholder(path):
    p = Path(path)
    if not p.exists():
        return False
    from PIL import Image, ImageStat
    with Image.open(p) as im:
        if im.size != PLACEHOLDER_SIZE:
            return False
        return ImageStat.Stat(im.convert("L").resize((240, 135))).stddev[0] < FLAT


def real_image(folder, stem):
    """Đường dẫn ảnh THẬT của một id (jpg/png/webp), hoặc None nếu chưa có hay chỉ là ảnh giữ chỗ."""
    for ext in ("jpg", "png", "webp"):
        f = Path(folder) / f"{stem}.{ext}"
        if f.exists() and not is_placeholder(f):
            return f
    return None
