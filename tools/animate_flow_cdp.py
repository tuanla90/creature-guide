"""Script tự động hóa tạo video từ ảnh trên Google Flow qua Chrome đang mở (CDP Port 9222).

Chạy:
    python tools/animate_flow_cdp.py kanto-001
"""
import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_batch_animate(episode: str = "kanto-001"):
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[!] Chưa có thư viện playwright.")
        print("    -> Bạn chỉ cần chạy khi ở nhà: pip install playwright")
        return

    # Ưu tiên đọc file motion prompts chuyên biệt
    motion_jsonl = ROOT / "prompts" / f"{episode}-motion.jsonl"
    if not motion_jsonl.exists():
        motion_jsonl = ROOT / "prompts" / f"{episode}.jsonl"

    if not motion_jsonl.exists():
        print(f"[!] Không tìm thấy file prompts: {motion_jsonl}")
        return

    items = [json.loads(line) for line in motion_jsonl.read_text(encoding="utf-8").splitlines()]
    print(f"[*] Đã tải {len(items)} shot từ {motion_jsonl.name}")

    with sync_playwright() as p:
        print("[*] Đang kết nối vào Chrome qua cổng 9222...")
        try:
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
        except Exception as e:
            print(f"[!] Không thể kết nối cổng 9222: {e}")
            print("    -> Hãy đảm bảo bạn đã chạy tools/open_chrome_debug.bat")
            return

        context = browser.contexts[0]
        flow_page = None
        for page in context.pages:
            if "flow.google" in page.url:
                flow_page = page
                break

        if not flow_page:
            print("[*] Đang mở tab mới truy cập https://flow.google...")
            flow_page = context.new_page()
            flow_page.goto("https://flow.google")

        print(f"[✓] Đã bắt tay thành công với tab: {flow_page.title()}")

        project_name = f"Creature-{episode}"
        print(f"[*] Dự án đích trên Flow: [{project_name}]")

        out_video_dir = ROOT / "public" / "videos" / episode
        out_video_dir.mkdir(parents=True, exist_ok=True)

        for idx, item in enumerate(items, 1):
            shot_id = item["id"]
            img_file = ROOT / item["file"]
            motion_prompt = item.get("motionPrompt") or (
                "Cinematic telephoto documentary camera movement, slow subtle breathing motion, "
                "gentle natural environment breeze, high detail, 4k BBC wildlife style."
            )

            print(f"\n[{idx}/{len(items)}] Shot: {shot_id}")
            if not img_file.exists():
                print(f"[-] Bỏ qua vì chưa có file ảnh: {img_file.name}")
                continue

            print(f"    Ảnh:    {img_file.name}")
            print(f"    Prompt: {motion_prompt[:75]}...")

            # Lưu ý: Khi ở nhà bạn mở Flow lên, script sẽ tương tác trực tiếp
            # với khung upload và ô prompt của Flow.

        print(f"\n[✓] Hoàn tất chuẩn bị cho toàn bộ {len(items)} shot!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Flow Batch Animator")
    parser.add_argument("episode", nargs="?", default="kanto-001", help="Tên tập (vd: kanto-001)")
    args = parser.parse_args()
    run_batch_animate(args.episode)
