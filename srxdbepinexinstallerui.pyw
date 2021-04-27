from tkinter import * 
from tkinter.filedialog import askdirectory
from tkinter import ttk

import threading
import sys
from os import path

from modules.gui import PrintLogger
from modules.steamutils import SteamUtils
from modules.bepinex import BepInExUtils
from modules.installer import Installer

class GUIWindow:
    def __init__(self, win):
        # Print to Frame
        # self.UpperCanvas = Frame(win)
        # self.UpperCanvas.pack(expand=1, fill=BOTH)
        # self.UpperCanvas.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        self.consoleOutputText = Text(win, bg="black", border=0, state=DISABLED)
        self.consoleOutputText.pack(expand=1, fill=BOTH)
        self.consoleOutputText.grid(row=0, column=0, columnspan=4, sticky=NSEW,)
        pl = PrintLogger(self.consoleOutputText)
        sys.stdout = pl

        # Init Modules and VersionVar
        self.steamutils = SteamUtils()
        print(f"Found Game Path: {self.steamutils.gameDirectory}")

        self.bepinutils = BepInExUtils()
        self.selectedVersion = StringVar()

        # Theme
        style = ttk.Style(win)
        style.theme_names()
        win.tk.call('source', """./themes/azure-dark.tcl""")
        style.theme_use('azure-dark')

        # Softening Grid:
        n_rows =1
        for i in range(n_rows):
            win.grid_rowconfigure(i,  weight =1)
        win.grid_columnconfigure(1,  weight =1)
        win.grid_columnconfigure(2,  weight =1)

        paddingInt = 3
        # Directory
        self.DirectoryInput = ttk.Entry(win)
        self.DirectoryInput.grid(row=1, column=1, sticky=S+E+W, columnspan=2, pady=paddingInt, padx=paddingInt)
        self.DirectoryInput.insert(END, self.steamutils.gameDirectory)
        # Selector
        self.DirectoryInputButton = ttk.Button(win, text=f'Select')
        self.DirectoryInputButton.grid(row=1, column=0, sticky=S+E+W, pady=paddingInt, padx=paddingInt)
        self.DirectoryInputButton.bind("<Button>", self.choose)
        # DropDown
        self.VersionDropDown = ttk.Combobox(win, textvariable=self.selectedVersion, width=5)
        self.VersionDropDown.grid(row=1, column=3, sticky=S+E+W, pady=paddingInt, padx=paddingInt)
        self.VersionDropDown['values'] = self.bepinutils.downloadVersions
        self.VersionDropDown.set(self.bepinutils.downloadVersions[0])
        
        # Install Button
        self.installButton = ttk.Button(win, text=f'Install', command=lambda isUninstall=False, : self.install(isUninstall))
        self.installButton.grid(row=2, column=0, sticky=E+W, columnspan = 3, pady=paddingInt, padx=paddingInt)

        # Uninstall Button
        self.uninstallButton = ttk.Button(win, text=f'Uninstall', command=lambda isUninstall=True, : self.install(isUninstall))
        self.uninstallButton.grid(row=2, column=3, sticky=E+W, columnspan = 1, pady=paddingInt, padx=paddingInt)

    def install(self, isUninstall):
        self.steamutils.gameDirectory = self.DirectoryInput.get()
        if(path.exists(self.steamutils.gameDirectory) or self.steamutils.gameDirectory != "" ):
            downloadUrl = self.bepinutils.downloadURLs[self.bepinutils.downloadVersions.index(self.selectedVersion.get())]
            installerInstance = Installer(self.steamutils.gameDirectory)
            installthread = None
            if (not isUninstall):
                installthread = threading.Thread(target=installerInstance.install, args=(downloadUrl,), daemon=True)
            else:
                installthread = threading.Thread(target=installerInstance.uninstall, daemon=True)
            installthread.start()
        else:
            print("Please Enter a Valid Path.")

    def choose(self, args):
        Tk().withdraw()
        self.DirectoryInput.delete(0, END)
        self.DirectoryInput.insert(0, askdirectory())
        
window=Tk()
mywin=GUIWindow(window)
window.title('SRXDBepInEXInstaller')
window.geometry("400x300+10+10")
window.mainloop()