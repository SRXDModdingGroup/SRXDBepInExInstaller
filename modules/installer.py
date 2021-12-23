import zipfile
import urllib.request
import tempfile
import os
from os import path
import shutil
import time
import pathlib
import glob
from modules.unitylibs import UnityLibsUtils
from modules.downloadutils import DownloadUtils
from modules.config import ConfigUtils
from modules.directoryfiller import DirectoryFiller
import hashlib

# Instantiate with game directory.
class Installer:
    def __init__(self, gameDirectory):
        self.unitylibsutils = UnityLibsUtils()
        self.utils = DownloadUtils()
        self.gameDirectory = gameDirectory
        self.unityplayerwrapper = {
            "norm": path.join(self.gameDirectory, "UnityPlayer.dll"),
            "mono": path.join(self.gameDirectory, "UnityPlayer_Mono.dll"),
            "norm_bak": path.join(self.gameDirectory, "UnityPlayer.bak.dll")
        }
        self.unityplayermovemsg = "UnityPlayer.dll could not be moved! It is advisable to delete any files starting with \"UnityPlayer\" in your directory, and click on Steam > SRXD Properties > Local Files > Verify Integrity."
        return

    def getUnityPlayerWrapperHashes(self):
        dict = self.unityplayerwrapper.copy()
        for key in dict:
            if path.exists(dict[key]):
                hash_md5 = hashlib.md5()
                with open(dict[key], "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)
                dict[key] = hash_md5.hexdigest()
            else:
                dict[key] = ""
        return dict

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

        hashdict = self.getUnityPlayerWrapperHashes()
        if hashdict["mono"] == hashdict["norm"]:
            ""
        else:
            shutil.move(self.unityplayerwrapper["norm"], self.unityplayerwrapper["norm_bak"])
            shutil.copy(self.unityplayerwrapper["mono"], self.unityplayerwrapper["norm"])

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

        hashdict = self.getUnityPlayerWrapperHashes()
        if hashdict["norm_bak"] != hashdict["norm"] and hashdict["mono"] == hashdict["norm"]:
            shutil.move(self.unityplayerwrapper["norm_bak"], self.unityplayerwrapper["norm"])
        elif hashdict["norm_bak"].__len__() == 0 and hashdict["mono"] != hashdict["norm"]:
            ""
        elif hashdict["norm_bak"] != hashdict["norm"] and hashdict["mono"] != hashdict["norm"]:
            os.remove(self.unityplayerwrapper["norm_bak"])

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

