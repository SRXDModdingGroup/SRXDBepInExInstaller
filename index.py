from modules.steamutils import SteamUtils
from modules.bepinex import BepInExUtils
from modules.gui import GuiUtils
from modules.utils import Utils

# Init Modules
steamutils = SteamUtils()
bepinutils = BepInExUtils()
utils = Utils()

# Get Download URL
url = bepinutils.downloadURLs[0]
print(f"Found BepInExURL: {url}")

# Get and Save File
downloadedFile = utils.download(url)
fileObject, bepinZipFilePath = utils.saveResponseAsTempFile(downloadedFile)
print(f"Saved Temp BepinEx Zip: {bepinZipFilePath}")

# Unzip File to 
utils.unzipTo(bepinZipFilePath, f"{steamutils.bepinDirectory}")
print(f"Unzipped: {bepinZipFilePath} => {steamutils.bepinDirectory}")
utils.deleteFile(bepinZipFilePath)
