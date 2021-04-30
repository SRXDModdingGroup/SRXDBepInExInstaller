from tkinter import *
import tkinter 
from tkinter.filedialog import askdirectory
from tkinter import ttk

import threading
import sys
from os import path

from modules.gui import GuiUtils, PrintLogger
from modules.steamutils import SteamUtils
from modules.bepinex import BepInExUtils
from modules.installer import Installer

class GUIWindow:
    def __init__(self, win : Tk):
        self.win = win

        # Define UI Variables
        self.paddingInt = 3
        self.canInstall = False
    
        self.initConsole()

        # Init Modules and VersionVar
        print(f"Initialising...")
        self.steamutils = SteamUtils()
        print(f"Found Game Path: {self.steamutils.gameDirectory}")
        threading.Thread(target=self.initLongModules, daemon=True).start()

        self.initTheme()
        self.initUI()

    def initConsole(self):
        self.consoleOutputText = Text(self.win, bg="black", fg="white", border=0, state=DISABLED)
        self.consoleOutputText.pack(expand=1, fill=BOTH)
        self.consoleOutputText.grid(row=0, column=0, columnspan=4, sticky=NSEW,)
        pl = PrintLogger(self.consoleOutputText)
        sys.stdout = pl
        print(GuiUtils().asciiArt)

    def initLongModules(self):
        self.bepinutils = BepInExUtils()
        if (len(self.bepinutils.downloadURLs) != 0):
            print(f"Got BepInEx Metadata from: {self.bepinutils.baseBepinexUrl}")
            self.canInstall = True
        self.initDropDown()
        print(f"Initialisation Finished.")

    def initTheme(self):
        # Theme
        style = ttk.Style(self.win)
        style.theme_names()

        if(hasattr(sys, "_MEIPASS")):
            baseStylePath = sys._MEIPASS            
        else:
            baseStylePath = path.dirname(__file__)
        
        try:
            self.win.tk.call('source', path.join(baseStylePath, "assets", "themes", "azure-dark.tcl"))
            style.theme_use('azure-dark')
        except:
            self

    def initUI(self):
        self.selectedVersion = StringVar()
        # Softening Grid:
        n_rows =1
        for i in range(n_rows):
            self.win.grid_rowconfigure(i,  weight =1)
        self.win.grid_columnconfigure(1,  weight =1)
        self.win.grid_columnconfigure(2,  weight =1)

        self.initDirectorySelector()
        self.initDropDown()
        self.initButtons()
    def initDirectorySelector(self):
        # Directory
        self.DirectoryInput = ttk.Entry(self.win)
        self.DirectoryInput.grid(row=1, column=1, sticky=S+E+W, columnspan=2, pady=self.paddingInt, padx=self.paddingInt)
        self.DirectoryInput.insert(END, self.steamutils.gameDirectory)
        # Selector
        self.DirectoryInputButton = ttk.Button(self.win, text=f'Select')
        self.DirectoryInputButton.grid(row=1, column=0, sticky=S+E+W, pady=self.paddingInt, padx=self.paddingInt)
        self.DirectoryInputButton.bind("<Button>", self.choose)
    def choose(self, args):
        selectorGameDirectory = askdirectory()
        if(len(selectorGameDirectory) != 0):
            self.DirectoryInput.delete(0, END)
            self.DirectoryInput.insert(0, selectorGameDirectory)
    def initDropDown(self):
        self.VersionDropDown = ttk.Combobox(self.win, textvariable=self.selectedVersion, width=5)
        self.VersionDropDown.grid(row=1, column=3, sticky=S+E+W, pady=self.paddingInt, padx=self.paddingInt)
        try:
            self.VersionDropDown['values'] = self.bepinutils.downloadVersions
            self.VersionDropDown.set("362")
        except:
            self.VersionDropDown.set("Loading...")
    def initButtons(self):
        # Install Button
        self.installButton = ttk.Button(self.win, text=f'Install', command=lambda isUninstall=False, : self.install(isUninstall))
        self.installButton.grid(row=2, column=0, sticky=E+W, columnspan = 3, pady=self.paddingInt, padx=self.paddingInt)

        # Uninstall Button
        self.uninstallButton = ttk.Button(self.win, text=f'Uninstall', command=lambda isUninstall=True, : self.install(isUninstall))
        self.uninstallButton.grid(row=2, column=3, sticky=E+W, columnspan = 1, pady=self.paddingInt, padx=self.paddingInt)
    def install(self, isUninstall):

            self.steamutils.gameDirectory = self.DirectoryInput.get()
            if(path.exists(self.steamutils.gameDirectory) or self.steamutils.gameDirectory != "" ):
                installerInstance = Installer(self.steamutils.gameDirectory)
                installthread = None
                if (not isUninstall and self.canInstall):
                    downloadUrl = self.bepinutils.downloadURLs[self.bepinutils.downloadVersions.index(self.selectedVersion.get())]
                    installthread = threading.Thread(target=installerInstance.install, args=(downloadUrl,), daemon=True).start()
                elif (isUninstall):
                    installthread = threading.Thread(target=installerInstance.uninstall, daemon=True).start()
                else:
                    print("Installer may not have initialised properly yet.")
                
            else:
                print("Please Enter a Valid Path.")
        
window=Tk()
mywin=GUIWindow(window)
window.title('SRXDBepInExInstaller')
window.geometry("520x405")
window.mainloop()