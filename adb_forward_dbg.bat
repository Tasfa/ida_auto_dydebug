@echo off
adb forward tcp:23946 tcp:23946
echo [+]adb forward successfully...
echo [+]Listening on #23333...
choice /t 1 /d y /n >nul
exit

