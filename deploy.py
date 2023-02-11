import os
import shutil
import sys



TARGET_PATH = r'F:\Octopath_Traveler2_Localization_Fix\UnrealPakSwitch'
OCTO_PATH = r'F:\SteamLibrary\steamapps\common\Octopath_Traveler2_DEMO\Octopath_Traveler2\Content\Paks'

def main():
    scriptFolder = os.path.split(__file__)[0]
    sourceFolder = os.path.join(scriptFolder, 'Output')
    with os.scandir(sourceFolder) as it:
        for entry in it:
            if entry.is_file():
                fileName, filePath = entry.name, entry.path
                if fileName.startswith('TalkData_ZH_CN'):
                    outputFolder = os.path.join(TARGET_PATH, r'Octopath_Traveler2\Content\Talk\Database')
                    if not os.path.exists(outputFolder):
                        os.makedirs(outputFolder)
                    shutil.copy2(filePath, outputFolder)
                elif fileName.startswith('GameTextZH_CN'):
                    outputFolder = os.path.join(TARGET_PATH, r'Octopath_Traveler2\Content\GameText\Database')
                    if not os.path.exists(outputFolder):
                        os.makedirs(outputFolder)
                    shutil.copy2(filePath, outputFolder)
                elif fileName.startswith('NarrationTable_zh_cn'):
                    outputFolder = os.path.join(TARGET_PATH, r'Octopath_Traveler2\Content\UserInterface\Narration\Database')
                    if not os.path.exists(outputFolder):
                        os.makedirs(outputFolder)
                    shutil.copy2(filePath, outputFolder)
                elif fileName.startswith('GameTextCharacterInfo_ZH_CN'):
                    outputFolder = os.path.join(TARGET_PATH, r'Octopath_Traveler2\Content\Text\Database')
                    if not os.path.exists(outputFolder):
                        os.makedirs(outputFolder)
                    shutil.copy2(filePath, outputFolder)
                elif fileName.startswith('GameTextItemInfo_ZH_CN'):
                    outputFolder = os.path.join(TARGET_PATH, r'Octopath_Traveler2\Content\Text\Database')
                    if not os.path.exists(outputFolder):
                        os.makedirs(outputFolder)
                    shutil.copy2(filePath, outputFolder)
                elif fileName.endswith('.ttf'):
                    outputFolder = os.path.join(TARGET_PATH, r'Octopath_Traveler2\Content\UserInterface\Common\Font')
                    if not os.path.exists(outputFolder):
                        os.makedirs(outputFolder)
                    shutil.copyfile(filePath, os.path.join(outputFolder, os.path.splitext(fileName)[0]) + '.ufont')
    os.chdir(os.path.join(TARGET_PATH, r'v11.27\2\3'))
    executeResult = os.popen(r'UnrealPak.exe ..\..\..\Octopath_Traveler2-WindowsNoEditor_cnfix.pak -Create=..\..\..\lista.txt -compress')
    for line in executeResult.read().splitlines():
        print(line)
    shutil.copy2(os.path.join(TARGET_PATH, 'Octopath_Traveler2-WindowsNoEditor_cnfix.pak'), OCTO_PATH)

if __name__ == '__main__':
    main()