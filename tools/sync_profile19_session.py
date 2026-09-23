"""Script sao chép session/cookies từ Profile 19 sang .chrome_flow
Giúp mở Chrome Flow độc lập đã đăng nhập sẵn mà KHÔNG CẦN TẮT Chrome công ty.

Chạy:
    python tools/sync_profile19_session.py
"""
import shutil
import sys
from pathlib import Path

SRC_USER_DATA = Path(r"D:\Users\tuanla2\AppData\Local\Google\Chrome\User Data")
SRC_PROFILE = SRC_USER_DATA / "Profile 19"

DEST_USER_DATA = Path(r"D:\Users\tuanla2\.chrome_flow")
DEST_PROFILE = DEST_USER_DATA / "Default"


def sync_session():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 60)
    print("Đang sao chép phiên đăng nhập từ Profile 19 sang Chrome Flow...")
    print("=" * 60)

    if not SRC_PROFILE.exists():
        print(f"[!] Không tìm thấy thư mục nguồn: {SRC_PROFILE}")
        return False

    DEST_PROFILE.mkdir(parents=True, exist_ok=True)

    # 1. Sao chép Local State (chứa khóa giải mã DPAPI của Chrome)
    src_local_state = SRC_USER_DATA / "Local State"
    if src_local_state.exists():
        shutil.copy2(src_local_state, DEST_USER_DATA / "Local State")
        print("[✓] Đã sao chép khóa bảo mật (Local State)")

    # 2. Danh sách các thư mục và file chứa phiên đăng nhập & cookies
    items_to_copy = [
        "Network",
        "Local Storage",
        "Sessions",
        "Session Storage",
        "IndexedDB",
        "Login Data",
        "Preferences",
        "Secure Preferences",
    ]

    for item in items_to_copy:
        src_path = SRC_PROFILE / item
        dest_path = DEST_PROFILE / item
        if not src_path.exists():
            continue

        try:
            if src_path.is_dir():
                if dest_path.exists():
                    shutil.rmtree(dest_path, ignore_errors=True)
                shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
            else:
                shutil.copy2(src_path, dest_path)
            print(f"[✓] Đã sao chép: {item}")
        except Exception as e:
            print(f"[-] Bỏ qua {item} (file có thể đang bị Chrome khóa): {e}")

    print("-" * 60)
    print("[✓] ĐÃ SAO CHÉP XONG PHIÊN ĐĂNG NHẬP!")
    print("Bây giờ bạn có thể chạy: tools/open_chrome_debug.bat")
    print("Cửa sổ Chrome mới mở lên sẽ có sẵn tài khoản từ Profile 19!")
    return True


if __name__ == "__main__":
    sync_session()
