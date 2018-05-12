import tkinter as tk

from mainWindow import MainWindow
from optionsWindow import OptionsWindow

class GUI():
    def __init__(self,model,jsonHandler):
        self.model = model
        self.jsonHandler = jsonHandler

        self.widthMain = 1280
        self.heightMain = 720
        self.root = tk.Tk()
        self.root.title("Encube Discovery Wall Configurator")
        self.root.minsize(width=self.widthMain,height=self.heightMain)
        self.mainWindow = MainWindow(self,self.root)

        self.widthOptions = 600
        self.heightOptions = 800
        self.optionsWindow = OptionsWindow(self,self.root)
        self.optionsWindow.title("Options")
        self.optionsWindow.minsize(width=self.widthOptions,height=self.heightOptions)

    def mainloop(self):
        self.mainWindow.mainloop()
