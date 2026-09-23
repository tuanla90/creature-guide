@echo off
setlocal
echo ========================================================
echo KHOI DONG CHROME CHO GOOGLE FLOW (PORT 9222)
echo ========================================================

set FLOW_DATA_DIR=D:\Users\tuanla2\.chrome_flow

echo [*] Khoi dong Chrome doc lap voi session da dong bo tu Profile 19...
echo [*] Mo cong Remote Debugging 9222...

start "" "chrome.exe" --remote-debugging-port=9222 --user-data-dir="%FLOW_DATA_DIR%" "https://flow.google"

echo [✓] Da mo Chrome thanh cong!
echo.
echo Hay kiem tra ket noi bang lenh:
echo python tools/test_flow_connect.py
pause
