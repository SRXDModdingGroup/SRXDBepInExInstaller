from modules.args import ArgsUtils
from modules.steamutils import SteamUtils
from modules.bepinex import BepInExUtils
# from modules.gui import GuiUtils
from modules.utils import Utils
from modules.unitylibs import UnityLibsUtils
from modules.args import ArgsUtils

# Init Modules
unitylibsutils = UnityLibsUtils()
utils = Utils()

# Init Arg Vars
uninstall = False
# Parse Args
argsutils = ArgsUtils()
for index, arg in enumerate(argsutils.getArgs()):
    if arg == "uninstall":
        uninstall = True

# Init Steam Module
print("Getting Steam Info...")
steamutils = SteamUtils()

if (uninstall):
    utils.uninstall(steamutils.gameDirectory)

# Do rest of work:
else:
    # Init BepInEx Webpage
    print("\nGetting Info from BepInEx Bleeding Edge Website...")
    bepinutils = BepInExUtils()

    # Get Download URL
    url = bepinutils.downloadURLs[0]
    print(f"Found BepInExURL: {url}")

    # Downloads BepInEx and extracts to Steam Library
    print("\nDownloading and Installing BepInEx")
    utils.downloadFileAndUnzip(url, steamutils.gameDirectory)

    # Downloads Unity-Libs and extracts to Steam Library
    print("\nDownloading and Extracting Unity Libraries")
    utils.downloadFileAndUnzip(unitylibsutils.githubRawUrl, steamutils.unityLibsDirectory)
