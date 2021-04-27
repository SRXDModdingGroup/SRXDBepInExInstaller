from tkinter import * 
from tkinter import filedialog
from modules.steamutils import SteamUtils

class GUIWindow:
    def __init__(self, win):
        self.steamutils = SteamUtils()

        n_rows =2
        n_columns =3
        for i in range(n_rows):
            win.grid_rowconfigure(i,  weight =1)
        for i in range(n_columns):
            win.grid_columnconfigure(i,  weight =1)

        # Directory
        self.DirectoryInput = Entry(win)
        self.DirectoryInput.grid(row=1, column=1, sticky=S+E+W, ipady=4)
        self.DirectoryInput.insert(END, self.steamutils.gameDirectory)

        self.DirectoryInputButton = Button(win, text=f'...', height = 1)
        self.DirectoryInputButton.grid(row=1, column=2, sticky=S+W)

        # Install Button
        self.installButton = Button(win, text=f'Install')
        self.installButton.grid(row=2, column=1, sticky=E+W)

        
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

window=Tk()
mywin=GUIWindow(window)
window.title('SRXDBepInEXInstaller')
window.geometry("400x300+10+10")
window.mainloop()