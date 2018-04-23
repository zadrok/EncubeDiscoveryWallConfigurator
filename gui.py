import tkinter as tk

from screen import Screen
from panel import Panel

class GUI(tk.Frame):
    def __init__(self,model,jsonHandler,root):
        super().__init__(root)
        self.model = model
        self.jsonHandler = jsonHandler
        self.root = root
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=0, column=0)

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.grid(row=1, column=0)

    def say_hi(self):
        print("hi there, everyone!")
