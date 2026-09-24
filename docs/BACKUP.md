# Sao lưu và dựng lại trên máy khác

`PYTHONUTF8=1 python tools/backup-all.py [--to <thư mục>] [--zip]` chép **một chiều**, không bao giờ xoá gì ở đích:

- `git/creature-field-guide.bundle` và `git/blog2video.bundle`: mọi nhánh của hai repo. Repo kênh đã
  có remote (`github.com/tuanla90/creature-guide`); nhánh engine `feat/specimen-freeze-media` thì chưa lên
  GitHub, nên bundle engine là bản duy nhất ngoài máy.
- `files/`: mọi thứ git không giữ (`public/`, `assets/`, `bible/refs/`, `out/`, `inbox/`,
  `experiments/`). Chỉ chép file mới hoặc đã đổi.
- `RESTORE.txt`: các lệnh dựng lại.

Không chép `.env` (khoá bí mật), cũng không chép `node_modules`.

Drive: thư mục `creature-guide` (drive.google.com/drive/folders/17FJ0H4Wl5esRz1uIiR7_rPRs7Ce4QrMx).

## Tự động

1. Cài **Google Drive for Desktop**, bật chế độ *Mirror* hoặc *Stream*, rồi tạo thư mục
   `G:/My Drive/creature-field-guide-backup`.
2. `setx CFG_BACKUP_DIR "G:\My Drive\creature-field-guide-backup"`
3. Tạo lịch chạy mỗi tối (Task Scheduler):
   `schtasks /create /tn cfg-backup /sc daily /st 21:00 /tr "cmd /c set PYTHONUTF8=1 && python D:\Users\tuanla2\creature-field-guide\tools\backup-all.py"`

Chưa có Drive for Desktop thì dùng `--zip`, rồi kéo file `.zip` vào Drive trên web.

## Dựng lại trên máy mới

```
git clone https://github.com/tuanla90/creature-guide.git creature-field-guide   # hoặc: git clone git/creature-field-guide.bundle
git clone git/blog2video.bundle blog2video && git -C blog2video checkout feat/specimen-freeze-media
```

Chép `files/*` đè vào `creature-field-guide/`. Nếu engine không nằm ở `D:/Users/tuanla2/blog2video`
thì sửa đường dẫn `file:` trong `package.json`, rồi chạy `npm install`, và bên engine chạy
`node scripts/build-lib.mjs`. Tạo lại `.env` từ `.env.example`.
