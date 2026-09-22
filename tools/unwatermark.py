"""Gỡ logo ngôi sao (watermark hiển thị của Gemini) khỏi ảnh Flow của một tập.

    python tools/unwatermark.py kanto-001            # xử lý public/img/kanto-001/*.jpg
    python tools/unwatermark.py kanto-001 --check    # chỉ xuất ảnh so sánh trước/sau

Logo là một ngôi sao trắng trộn alpha CỐ ĐỊNH ở cùng một chỗ trên mọi ảnh cùng kích thước
(ý tưởng của allenk/GeminiWatermarkTool: tính ngược phép trộn alpha). Ở đây bản đồ alpha
được ƯỚC LƯỢNG ngay từ ảnh của tập, không cần file mẫu:
  1. mặt nạ = chỗ sáng lên nhất quán ở góc dưới-phải trên mọi ảnh
  2. alpha(x,y) = trung vị qua các ảnh của (W - B) / (255 - B), với B = nền vá bằng inpaint
  3. nền thật = (W - a*255) / (1 - a); chỗ alpha quá cao thì inpaint nhẹ
Ảnh gốc được giữ trong out/flow/raw/<ep>/ (chạy lại luôn đọc từ bản gốc, không gỡ chồng lên nhau).
Chỉ gỡ lớp logo hiển thị; watermark ẩn SynthID vẫn còn nguyên trong ảnh.
"""
import shutil, sys
from pathlib import Path
import cv2, numpy as np
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
ep = sys.argv[1] if len(sys.argv) > 1 else "kanto-001"
check = "--check" in sys.argv
src_dir, raw_dir = ROOT / "public" / "img" / ep, ROOT / "out" / "flow" / "raw" / ep
raw_dir.mkdir(parents=True, exist_ok=True)
for f in sorted(src_dir.glob("*.jpg")):           # lần đầu: cất bản gốc
    if not (raw_dir / f.name).exists(): shutil.copy2(f, raw_dir / f.name)

files = sorted(raw_dir.glob("*.jpg"))
imgs = [cv2.imread(str(f)).astype(np.float32) for f in files]
by_size = {}
for f, im in zip(files, imgs): by_size.setdefault(im.shape[:2], []).append((f, im))

for (H, W), group in by_size.items():
    if len(group) < 3:
        print(f"bỏ qua {H}x{W}: cần >= 3 ảnh cùng cỡ để ước lượng alpha"); continue
    R = 200                                          # vùng tìm ở góc dưới-phải
    y0, x0 = H - R, W - R
    crops = np.stack([im[y0:, x0:].mean(axis=2) for _, im in group])
    # 1) mặt nạ: phần "sáng hơn nền lân cận" lặp lại ở mọi ảnh
    hp = np.stack([c - cv2.GaussianBlur(c, (0, 0), 9) for c in crops])
    score = np.median(hp, axis=0)
    mask = (score > 4).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(mask)
    if n < 2:
        print(f"{H}x{W}: không thấy logo"); continue
    k = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    mask = (lab == k).astype(np.uint8)
    x, y, w, h = stats[k, :4]
    print(f"{H}x{W}: logo {w}x{h}px tại ({x0 + x}, {y0 + y}) — {len(group)} ảnh")
    grow = cv2.dilate(mask, np.ones((7, 7), np.uint8))
    # 2) ước lượng alpha
    alphas = []
    for c in crops:
        c8 = np.clip(c, 0, 255).astype(np.uint8)
        B = cv2.inpaint(c8, grow, 6, cv2.INPAINT_TELEA).astype(np.float32)
        a = (c - B) / np.maximum(255 - B, 25)
        alphas.append(np.where(grow > 0, a, 0))
    alpha = np.clip(np.median(np.stack(alphas), axis=0), 0, 0.85)
    alpha = cv2.GaussianBlur(alpha, (0, 0), 0.6) * (grow > 0)
    # 3) tính ngược + vá chỗ alpha cao
    for f, im in group:
        out = im.copy()
        reg = im[y0:, x0:]
        a3 = alpha[..., None]
        rec = (reg - a3 * 255) / np.maximum(1 - a3, 0.15)
        reg2 = np.where(grow[..., None] > 0, rec, reg)
        reg2 = np.clip(reg2, 0, 255).astype(np.uint8)
        # viền logo: alpha ước lượng kém nhất ở mép (nhoè JPEG) -> vá luôn dải viền mỏng
        edge = cv2.dilate(mask, np.ones((5, 5), np.uint8)) - cv2.erode(mask, np.ones((3, 3), np.uint8))
        hard = ((alpha > 0.6) | (edge > 0) | ((grow > 0) & (np.abs(rec.mean(axis=2) - reg.mean(axis=2)) > 120))).astype(np.uint8)
        if hard.any(): reg2 = cv2.inpaint(reg2, cv2.dilate(hard, np.ones((3, 3), np.uint8)), 3, cv2.INPAINT_TELEA)
        out[y0:, x0:] = reg2
        if check:
            pair = np.hstack([im[y0:, x0:], out[y0:, x0:]]).astype(np.uint8)
            cv2.imwrite(str(ROOT / "out" / "flow" / f"wm-check-{f.stem}.png"), cv2.resize(pair, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST))
        else:
            cv2.imwrite(str(src_dir / f.name), out.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 95])
print("xong (chế độ kiểm tra)" if check else f"đã ghi đè {src_dir.relative_to(ROOT)} — bản gốc ở {raw_dir.relative_to(ROOT)}")
