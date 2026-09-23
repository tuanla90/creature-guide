"""Script kiểm tra kết nối với Chrome đang mở (cổng 9222).

Chạy thử:
    python tools/test_flow_connect.py
"""
import json
import sys
import urllib.error
import urllib.request

DEBUG_URL = "http://127.0.0.1:9222/json/list"


def check_chrome_tabs():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 60)
    print("Đang quét các tab trên Chrome (cổng 9222)...")
    print("=" * 60)

    try:
        req = urllib.request.Request(DEBUG_URL)
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError:
        print("[!] Không kết nối được với Chrome trên cổng 9222.")
        print("    -> Bạn hãy đảm bảo đã chạy file: tools/open_chrome_debug.bat")
        print("    -> Sau đó mở lại script này để kiểm tra.")
        return False

    pages = [t for t in data if t.get("type") == "page"]
    print(f"[✓] Kết nối thành công! Đang có {len(pages)} tab mở trong Chrome:")

    flow_tab = None
    for idx, p in enumerate(pages, 1):
        title = p.get("title", "Không có tiêu đề")
        url = p.get("url", "")
        print(f"  {idx}. [{title}] -> {url}")
        if "flow.google" in url:
            flow_tab = p

    print("-" * 60)
    if flow_tab:
        print(f"[✓] TÌM THẤY TAB GOOGLE FLOW:")
        print(f"    Tiêu đề: {flow_tab.get('title')}")
        print(f"    URL:     {flow_tab.get('url')}")
        print("    -> Script hoàn toàn có thể điều khiển trực tiếp tab này!")
    else:
        print("[-] Chưa thấy tab nào mở https://flow.google.")
        print("    -> Bạn chỉ cần mở một tab mới trên Chrome đó và vào flow.google")

    return True


if __name__ == "__main__":
    check_chrome_tabs()
