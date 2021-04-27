import sys
import os
from os import path
import re
import ast

class SteamUtils:
    def __init__(self):
        self.platform = sys.platform

        try:
            self.baseSteamPath = self.getSteamBasePath()
            self.steamCommonPathArray = self.getAllSteamAppsPath()

            self.gameDirectory = self.getGameDirectory()
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
        
    def getAllSteamAppsPath(self):
        arrayOfPaths = []

        basicSteamCommonPath = path.join(self.baseSteamPath, "common")

        vdfDirectory = path.join(self.baseSteamPath, "libraryfolders.vdf")
        
        if (path.exists(basicSteamCommonPath)):
            arrayOfPaths.append(basicSteamCommonPath)
        vdfDictionary = self.vdfToDict(open(vdfDirectory))
        for value in vdfDictionary:
            tempCommonPath = path.join(vdfDictionary[value], "steamapps", "common")
            if (value.isdigit() and path.exists(tempCommonPath)):
                arrayOfPaths.append(tempCommonPath)
        return arrayOfPaths
        
        
    def vdfToDict(self, vdfText):
        dictionary = {}
        newVdfText = ""
        for idx, line in enumerate(vdfText):
            if (idx != 0):
                regexSearch = re.search('\s"[\s\S]*"\t', line)
                if (regexSearch != None):
                    line = line[:regexSearch.end()] + ":" + line[regexSearch.end():]
                    line = line[:-1]
                    line = f"{line},\n"
                newVdfText = newVdfText + line
        return ast.literal_eval(newVdfText)

    def getGameDirectory(self):
        gameDirectory = None
        allGameDirectories = []
        for commonPath in self.steamCommonPathArray:
            onlyDirectories = [path.join(commonPath, f) for f in os.listdir(commonPath) if not path.isfile(path.join(commonPath, f))]
            allGameDirectories.extend(onlyDirectories)
        for directory in allGameDirectories:            
            # Easier Way:
            execPath = path.join(directory, "SpinRhythm.exe")
            if (path.exists(execPath)):
                gameDirectory = directory

            if (gameDirectory == None):
                # Old Appid Way:
                appIDFile = path.join(directory, "steam_appid.txt")
                if (path.exists(appIDFile)):
                    appid = open(appIDFile).readline().replace("\n", "")
                    if (appid == "1058830"):
                        gameDirectory = directory
        return gameDirectory

    def inputPathIfEmpty(self):
        inputPath = None

        currentPathwithExec = path.join(".", "SpinRhythm.exe")
        if (path.exists(currentPathwithExec)):
            inputPath = currentPathwithExec

        else:
            pathIsValid = False
            while (not pathIsValid):
                inputPath = input('Game Directory Could not be Found! This is Usually Something Like: "{usualPath}". \nPlease Enter (or Drag and Drop) your Spin Rhythm Game Folder Here: '.format(usualPath = path.join('C:\\','Program Files (x86)', 'Steam', 'steamapps\\')))
                if (not inputPath.__len__() == 0 and path.exists(inputPath)):
                    pathIsValid = True
                else:
                    print("Input Path was Invalid. Please Try Again...")   

        inputPath = path.abspath(inputPath)              
        return inputPath
            