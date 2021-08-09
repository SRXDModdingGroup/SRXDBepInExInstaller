import zipfile
import urllib.request
import tempfile
import os
import shutil
import time
import pathlib
import glob
from modules.unitylibs import UnityLibsUtils
from modules.downloadutils import DownloadUtils
from modules.config import ConfigUtils
from modules.directoryfiller import DirectoryFiller


# Instantiate with game directory.
class Installer:
    def __init__(self, gameDirectory):
        self.unitylibsutils = UnityLibsUtils()
        self.utils = DownloadUtils()
        self.gameDirectory = gameDirectory
        return

    def install(self, bepinUrl:str, installUnityLibs:bool): 
        # Downloads BepInEx and extracts to Steam Library
        print("\nDownloading and Installing BepInEx")
        self.utils.downloadFileAndUnzip(bepinUrl, self.gameDirectory)

        bepinPath = os.path.join(self.gameDirectory, "BepInEx")

        unityLibsFolder = os.path.join(bepinPath, "unity-libs")
        # Downloads Unity-Libs and extracts to Steam Library
        if (installUnityLibs):
            print("\nDownloading and Extracting Unity Libraries")
            self.utils.downloadFileAndUnzip(self.unitylibsutils.githubRawUrl, unityLibsFolder)
        elif(os.path.exists(unityLibsFolder)):
            self.utils.recursiveDeleteFolder(unityLibsFolder)

        try:
            DirectoryFiller(self.gameDirectory).fillWithBepinExFolders()
            ConfigUtils(os.path.join(bepinPath, "config", "BepInEx.cfg")).setAttr("Logging.Console", "Enabled", "true")
        except Exception as e:
            print(f'Post-Installation Scripts have Failed to Run. "Logging.Console" will not Enabled by Default. Exception: {e}')
        
        print('Done!\nYou Can Now Put Your Mods in "{}"'.format(os.path.join(bepinPath, "plugins")))

    def uninstall(self, preservePlugins:bool = True):
        print("Uninstalling...")
        
        if (os.path.exists(os.path.join(self.gameDirectory, "MelonLoader"))):
            print("MelonLoader was detected in your game folder. If you'd like for this to be deleted, this will be done in 10 seconds. If not, PLEASE CLOSE THIS APPLICATION NOW!")
            time.sleep(10)
            self.deleteFiles(["MelonLoader", "Plugins", "Mods", "Logs", "version.dll"])
        elif (not preservePlugins):
            self.deleteFiles(["BepInEx", "mono", "changelog.txt", "doorstop_config.ini", "winhttp.dll"])
        elif (preservePlugins):
            willDelList = ["mono", "changelog.txt", "doorstop_config.ini", "winhttp.dll"]
            for fileOrFolder in glob.glob(os.path.join(self.gameDirectory, "BepInEx", "*")):
                fileBName = os.path.basename(fileOrFolder)
                if fileBName != "plugins" and fileBName != "config":
                    willDelList.append(os.path.join("BepInEx", fileBName))
            self.deleteFiles(willDelList)
                
        print("Done!\n")
        return

    def deleteFiles(self, deleteFiles):
        for file in deleteFiles:
            pathOfFile = os.path.join(self.gameDirectory, file)
            if (os.path.exists(pathOfFile)):
                suffixOfFile = pathlib.Path(pathOfFile).suffix
                try:
                    if (suffixOfFile == ""):
                        self.utils.recursiveDeleteFolder(pathOfFile)
                    else:
                        self.utils.deleteFile(pathOfFile)
                    print(f"Deleted: {pathOfFile}")
                except:
                    print(f"Error with deleting: {pathOfFile}")

