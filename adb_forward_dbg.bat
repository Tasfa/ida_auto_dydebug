@echo off
adb forward tcp:23946 tcp:23946
echo 转发成功
choice /t 1 /d y /n >nul
exit

