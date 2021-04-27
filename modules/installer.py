import zipfile
import urllib.request
import tempfile
import os
import shutil
import pathlib
from modules.unitylibs import UnityLibsUtils
from modules.utils import Utils

# Instantiate with game directory.
class Installer:
    def __init__(self, gameDirectory):
        self.unitylibsutils = UnityLibsUtils()
        self.utils = Utils()
        self.gameDirectory = gameDirectory
        return

    def install(self, bepinUrl): 
        # Downloads BepInEx and extracts to Steam Library
        print("\nDownloading and Installing BepInEx")
        self.utils.downloadFileAndUnzip(bepinUrl, self.gameDirectory)

        # Downloads Unity-Libs and extracts to Steam Library
        print("\nDownloading and Extracting Unity Libraries")
        self.utils.downloadFileAndUnzip(self.unitylibsutils.githubRawUrl, os.path.join(self.gameDirectory, "BepInEx", "unity-libs"))

    def uninstall(self):
        deleteFiles = ["BepInEx", "mono", "changelog.txt", "doorstop_config.ini", "winhttp.dll"]
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
        return

