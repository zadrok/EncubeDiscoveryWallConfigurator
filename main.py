import tkinter as tk

from model import Model
from gui import GUI
from screen import Screen
from panel import Panel
from jsonHandler import JsonHandler

class Application:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.title = "Encube Discovery Wall Configurator"

        self.model = Model()
        self.jsonHandler = JsonHandler()

        self.root = tk.Tk()
        self.rootPrep()

        self.gui = GUI(self.model,self.jsonHandler,self.root)

    def rootPrep(self):
        self.root.minsize(width=self.width,height=self.height)
        self.root.wm_title(self.title)

    def run(self):
        self.gui.mainloop()


if __name__ == '__main__':
    app = Application()
    app.run()
