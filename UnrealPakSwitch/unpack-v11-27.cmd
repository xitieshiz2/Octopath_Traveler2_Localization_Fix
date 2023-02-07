@echo off
xcopy /i /e /q /c /y v11.27\OodleData\ Engine\Plugins\Compression\OodleData > NUL 2> NUL
@echo on
v11.27\2\3\UnrealPak.exe %1 -list > lista.txt
pause
v11.27\2\3\UnrealPak.exe %1 -extract ..\..\..\
pause