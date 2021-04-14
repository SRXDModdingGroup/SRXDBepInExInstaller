from modules.steamutils import SteamUtils
from modules.bepinex import BepInExUtils
# from modules.gui import GuiUtils
from modules.utils import Utils
from modules.unitylibs import UnityLibsUtils

# Init Modules
unitylibsutils = UnityLibsUtils()
utils = Utils()

print("Getting Steam Info...")
steamutils = SteamUtils()

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
