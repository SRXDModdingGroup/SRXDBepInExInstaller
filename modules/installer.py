import zipfile
import urllib.request
import tempfile
import os
import shutil
import time
import pathlib
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

    def install(self, bepinUrl): 
        # Downloads BepInEx and extracts to Steam Library
        print("\nDownloading and Installing BepInEx")
        self.utils.downloadFileAndUnzip(bepinUrl, self.gameDirectory)

        bepinPath = os.path.join(self.gameDirectory, "BepInEx")

        # Downloads Unity-Libs and extracts to Steam Library
        print("\nDownloading and Extracting Unity Libraries")
        self.utils.downloadFileAndUnzip(self.unitylibsutils.githubRawUrl, os.path.join(bepinPath, "unity-libs"))

        try:
            DirectoryFiller(self.gameDirectory).fillWithBepinExFolders()
            ConfigUtils(os.path.join(bepinPath, "config", "BepInEx.cfg")).setAttr("Logging.Console", "Enabled", "true")
        except Exception as e:
            print(f'Post-Installation Scripts have Failed to Run. "Logging.Console" will not Enabled by Default. Exception: {e}')
        
        print('Done!\n You can put your Mods in "{}"'.format(os.path.join(bepinPath, "plugins")))

    def uninstall(self):
        print("Uninstalling...")
        if (os.path.exists(os.path.join(self.gameDirectory, "MelonLoader"))):
            print("MelonLoader was detected in your game folder. If you'd like for this to be deleted, this will be done in 10 seconds. If not, PLEASE CLOSE THIS APPLICATION NOW!")
            time.sleep(10)
            self.deleteFiles(["MelonLoader", "Plugins", "Mods", "Logs", "version.dll"])
        else:
            self.deleteFiles(["BepInEx", "mono", "changelog.txt", "doorstop_config.ini", "winhttp.dll"])        
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

