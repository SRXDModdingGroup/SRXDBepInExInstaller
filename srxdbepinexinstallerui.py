from tkinter import * 
from tkinter import ttk
from modules.steamutils import SteamUtils
from modules.bepinex import BepInExUtils

class GUIWindow:
    def __init__(self, win):
        # Init Modules
        self.steamutils = SteamUtils()
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

        # Logo Canvas
        self.LogoCanvas = Canvas(win, bg="blue")
        self.LogoCanvas.pack(expand=1, fill=BOTH)
        self.LogoCanvas.grid(row=0, column=0, columnspan=3)

        paddingInt = 2
        # Directory
        self.DirectoryInput = ttk.Entry(win)
        self.DirectoryInput.grid(row=1, column=1, sticky=S+E+W, ipady=5, pady=paddingInt, padx=paddingInt)
        self.DirectoryInput.insert(END, self.steamutils.gameDirectory)
        # Selector
        self.DirectoryInputButton = ttk.Button(win, text=f'Select')
        self.DirectoryInputButton.grid(row=1, column=0, sticky=S+E+W, ipady=4, pady=paddingInt, padx=paddingInt)
        # DropDown
        self.VersionDropDown = ttk.Combobox(win, textvariable=self.selectedVersion, width=5)
        self.VersionDropDown.grid(row=1, column=2, sticky=S+E+W, pady=paddingInt, padx=paddingInt, ipady=5)
        self.VersionDropDown['values'] = self.bepinutils.downloadVersions
        self.VersionDropDown.set(self.bepinutils.downloadVersions[0])
        
        # Install Button
        self.installButton = ttk.Button(win, text=f'Install')
        self.installButton.grid(row=2, column=0, sticky=E+W, columnspan = 3, pady=paddingInt, padx=paddingInt)
        self.installButton.bind('<Button-1>', self.install)

    def install(self, args):
        print(self.bepinutils.downloadURLs[self.bepinutils.downloadVersions.index(self.selectedVersion.get())])
        
        

        

window=Tk()
mywin=GUIWindow(window)
window.title('SRXDBepInEXInstaller')
window.geometry("400x300+10+10")
window.mainloop()