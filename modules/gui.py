from tkinter import *
import sys


class GuiUtils:
    def __init__(self):
        self.asciiArt = """                                        
                  %(((                  
                  #(((                  
           (((#   #(((    (((#          
           ((((   #(((   %(((#          
   (***/   ((((   #(((   %(((#   /**/   
   (***/   ((((   #(((   %(((#   /**/   
   (***/   ((((   #(((   %(((#   /**/   
   (***/   ((((   #(((   %(((#   /**/   
   (***/   ((((   #(((   %(((#   /**/   
   (***/   ((((   #(((   %(((#   /**/   
   (***/   ((((   #(((   %(((#   /**/   
           ((((   #(((   %(((#          
           (((#   #(((    (((#          
                  #(((                  
                  %(((                  \n"""
        return

class PrintLogger(): # create file like object
    def __init__(self, textbox : Text): # pass reference to text widget
        self.textbox = textbox # keep ref
        self.textbox

    def write(self, text):
        self.textbox.config(state=NORMAL)
        self.textbox.insert(END, text) # write text to textbox
        self.textbox.config(state=DISABLED)
        self.textbox.see(END)
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass
