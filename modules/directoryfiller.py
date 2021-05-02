from pathlib import Path
import os

class DirectoryFiller:
    def __init__(self, gameDirectory):
        self.gameDirectory = gameDirectory
        

    def fillWithBepinExFolders(self):
        insideBePinExFolders = ["config", "patchers", "plugins", "cache"]
        for folderName in insideBePinExFolders:
            Path(os.path.join(self.gameDirectory, "BepInEx", folderName)).mkdir(parents=True, exist_ok=True)

          
    