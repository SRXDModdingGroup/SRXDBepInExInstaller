import sys
import os
from os import path
import re
import json

class SteamUtils:
    def __init__(self):
        self.platform = sys.platform
        try:
            SRXDInCurrentPath = path.join(".", "SpinRhythm.exe")
            if (path.exists(SRXDInCurrentPath)):
                self.gameDirectory = SRXDInCurrentPath
            else:
                self.baseSteamPath = self.getSteamBasePath()
                self.gameDirectory = path.join(self.baseSteamPath, "common", "Spin Rhythm")
                if (not os.path.exists(self.gameDirectory)):
                    self.gameDirectory = self.getGameDirFromVDF()
                # self.gameDirectory = "./test"
        except:
            self.gameDirectory = ""
                    

    def getbepinDirectory(self):
        return os.path.join(self.gameDirectory, "BepInEx")

    def getunityLibsDirectory(self):
        return os.path.join(self.getbepinDirectory(), "unity-libs")

    def getSteamBasePath(self):
        baseSteamAppsPath = None
        if (self.platform == "win32"):
            baseSteamAppsPath = path.join("C:\\","Program Files (x86)", "Steam", "steamapps")
        else:
            baseSteamAppsPath = path.join(path.expanduser("~"),".local", "share", "Steam", "steamapps")
        
        if (not path.exists(baseSteamAppsPath)):
            baseSteamAppsPath = None
        return baseSteamAppsPath
        
    def getGameDirFromVDF(self):
        returnVal = ""

        vdfDirectory = path.join(self.baseSteamPath, "libraryfolders.vdf")
        
        for key, value in self.vdfToDict(open(vdfDirectory).read()).items():
            if (key.isdigit() and "1058830" in value["apps"]):
                returnVal = os.path.join(value["path"], "steamapps", "common", "Spin Rhythm")
        # for value in vdfDictionary:
        #     tempCommonPath = path.join(vdfDictionary[value], "steamapps", "common")
        #     if (value.isdigit() and path.exists(tempCommonPath)):
        #         arrayOfPaths.append(tempCommonPath)
        return returnVal
        
        
    def vdfToDict(self, vdfText) -> dict:
        dictionary = {}
        newVdfText = ""
        vdfText = re.sub(r'"\n[\s+]*"', '", "', vdfText.split("\n",1)[1]).strip()
        vdfText = re.sub(r"\s+", ' ', vdfText).replace('" "', '" : "').replace('" {', '" : {')
        # for idx, line in enumerate(vdfText):
        #     line = line.strip()
        #     if (idx != 0):
        #         re.sub(r"\s+", " ", line)
                
        #         newVdfText = newVdfText + line
        return json.loads(vdfText)

    def inputPathIfEmpty(self):
        inputPath = None
        pathIsValid = False
        while (not pathIsValid):
            inputPath = input('Game Directory Could not be Found! This is Usually Something Like: "{usualPath}". \nPlease Enter (or Drag and Drop) your Spin Rhythm Game Folder Here: '.format(usualPath = path.join('C:\\','Program Files (x86)', 'Steam', 'steamapps\\')))
            if (not inputPath.__len__() == 0 and path.exists(inputPath)):
                pathIsValid = True
            else:
                print("Input Path was Invalid. Please Try Again...")   

        inputPath = path.abspath(inputPath)              
        return inputPath
            