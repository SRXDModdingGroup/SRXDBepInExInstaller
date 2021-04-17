import tkinter as tk

class GuiUtils:
    def __init__(self):
        self.window = tk.Tk()

    def run(self, urls):

        variable = tk.StringVar()

        # to rename the title of the window
        self.window.title("Installer")
        # pack is used to show the object in the window
        option = tk.OptionMenu(self.window, variable, urls).pack()
        label = tk.Label(self.window, text = "Installer").pack()
        self.window.mainloop()
        
