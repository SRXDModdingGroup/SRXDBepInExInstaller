import os

class TuiUtils:
    def __init__(self):
        return
    def clear(self): 
        # for windows
        if os.name == 'nt':
            os.system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            os.system('clear')
    def printBepinUrlList(self, urlList):
        self.clear()
        for index, url in enumerate(urlList):
            print(index, url)
        return urlList[0]