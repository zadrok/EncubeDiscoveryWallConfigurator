import tkinter as tk
from menuBar import MBMain

class MainWindow(tk.Frame):
    def __init__(self,gui,root):
        super().__init__(root)
        self.root = root
        self.gui = gui

        self.frame = tk.Frame(master=self.root)
        self.frame.grid()

        self.createWidgets()

    def createWidgets(self):
        # menu bar
        self.menuBar = MBMain(self.root)
        # other stuff
