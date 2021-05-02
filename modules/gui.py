from tkinter import *

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
        try:
            self.textbox = textbox # keep ref
            self.textbox
        except:
            self.errormessage()

    def write(self, text):
        try:
            self.textbox.config(state=NORMAL)
            self.textbox.insert(END, text) # write text to textbox
            self.textbox.config(state=DISABLED)
            self.textbox.see(END)
        except:
            self.errormessage()
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass

    def errormessage(self):
        raise Exception("Console could not be attatched.")
