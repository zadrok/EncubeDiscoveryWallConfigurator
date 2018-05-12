import tkinter as tk

from mainWindow import MainWindow
from optionsWindow import OptionsWindow

class GUI():
    def __init__(self,model,jsonHandler):
        self.model = model
        self.jsonHandler = jsonHandler

        # setup main window
        self.widthMain = 1280
        self.heightMain = 720
        self.root = tk.Tk()
        self.root.title("Encube Discovery Wall Configurator")
        self.root.minsize(width=self.widthMain,height=self.heightMain)
        self.mainWindow = MainWindow(self,self.root)

        # setup options window
        # child of main window, will close when main does
        # can be hidden/closed without affecting main window
        self.widthOptions = 650
        self.heightOptions = 800
        self.optionsWindow = OptionsWindow(self,self.root)
        self.optionsWindow.title("Options")
        self.optionsWindow.minsize(width=self.widthOptions,height=self.heightOptions)
        # start with the options window closed
        self.optionsWindow.withdraw()

    def mainloop(self):
        self.mainWindow.mainloop()
