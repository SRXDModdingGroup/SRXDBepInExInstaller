# Instantiate with game directory.
class ConfigUtils:
    def __init__(self, path): 
        
        self.path = path
        
        self.fileOpen = open(self.path, "w+", encoding="utf-8")

    def enableLog(self): 
        
        if(self.fileOpen.read() == ""):
            print()
        return

