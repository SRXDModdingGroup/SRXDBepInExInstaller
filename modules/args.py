import sys

class ArgsUtils:
    def __init__(self):
        return
    def getArgs(self):
        tempArgs = sys.argv
        tempArgs.pop(0)
        return tempArgs            
    