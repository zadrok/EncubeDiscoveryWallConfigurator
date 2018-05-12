import tkinter as tk

from model import Model
from jsonHandler import JsonHandler
from gui import GUI

class Application:
    def __init__(self):
        self.model = Model()
        self.jsonHandler = JsonHandler()
        self.gui = GUI(self.model,self.jsonHandler)

    def run(self):
        self.gui.mainloop()

if __name__ == '__main__':
    app = Application()
    app.run()
