@echo off
rem Android��̬�����Զ����ű�
rem 
rem __author__ : Tasfa
rem __info__ : www.tasfa.cn
rem __e-mail__: root#tasfa.cn
rem 
rem 



rem ��������server
start cmd /k "android_server_listen.py"

rem ����ʱ���ӳ�
choice /t 2 /d y /n >nul             

rem ����ת��
start cmd /c "adb_forward_dbg.bat"
start cmd /c "adb_forward_dbg.bat"

echo Do you want to attach the target ?
choice /c:yn

if errorlevel 2 goto debug
if errorlevel 1 goto attach

goto :eof
:debug
rem ����activity
start cmd /k "am-start.py"

choice /t 8 /d y /n >nul

rem ����ida
start E:\IDA\IDA_Pro_v6.8_and_Hex-Rays_Decompiler_(ARM,x64,x86)_Green\idaq.exe

rem ����ddms
choice /t 30 /d y /n >nul
start cmd /k "ddms"

rem ����jdb-connect
choice /t 8 /d y /n >nul
start cmd /k "jdb-connect.bat"

goto :eof
:attach
echo Do you want to start IDA ?
choice /c:yn
if errorlevel 2 exit
if errorlevel 1 start E:\IDA\IDA_Pro_v6.8_and_Hex-Rays_Decompiler_(ARM,x64,x86)_Green\idaq.exe



