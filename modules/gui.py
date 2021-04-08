import tkinter as tk

class GuiUtils:
    def run(self):
        window = tk.Tk()
        # to rename the title of the window
        window.title("Installer")
        # pack is used to show the object in the window
        label = tk.Label(window, text = "Installer").pack()
        window.mainloop()
