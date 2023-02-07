v4\2\3\UnrealPak.exe %1 -list -cryptokeys="..\..\..\crypto.json" > lista.txt
pause
v4\2\3\UnrealPak.exe %1 -extract ..\..\..\ -cryptokeys="..\..\..\crypto.json"
pause