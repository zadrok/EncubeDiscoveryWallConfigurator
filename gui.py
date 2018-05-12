import tkinter as tk

from mainWindow import MainWindow
from optionsWindow import OptionsWindow

class GUI():
    def __init__(self,model,jsonHandler):
        self.model = model
        self.jsonHandler = jsonHandler

        self.widthMain = 1280
        self.heightMain = 720
        self.titleMain = "Encube Discovery Wall Configurator"
        self.rootMain = tk.Tk()
        self.rootMain.minsize(width=self.widthMain,height=self.heightMain)
        self.rootMain.wm_title(self.titleMain)
        self.mainWindow = MainWindow(self,self.rootMain)

        self.widthOptions = 600
        self.heightOptions = 800
        self.titleOptions = "Options"
        self.rootOptions = tk.Tk()
        self.rootOptions.minsize(width=self.widthOptions,height=self.heightOptions)
        self.rootOptions.wm_title(self.titleOptions)
        self.optionsWindow = OptionsWindow(self,self.rootOptions)

    def mainloop(self):
        self.mainWindow.mainloop()
        self.optionsWindow.mainloop()
