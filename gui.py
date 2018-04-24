import tkinter as tk
import random

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

        self.add_screen = tk.Button(self)
        self.add_screen["text"] = "Add Screen"
        self.add_screen["command"] = self.create_screen
        self.add_screen.grid(row=0,column=1)

        self.set_up_canvas()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.grid(row=1, column=0)

    def say_hi(self):
        print("hi there, everyone!")

    def create_screen(self):
        print("Creating a screen")
        screen = Screen("id",120,400)
        self.paned.add(screen.getTkObject())

    def set_up_canvas(self):
        # self.canvas = tk.PanedWindow(self,fill=BOTH,expand=1,bg="white")
        self.paned = tk.PanedWindow(orient="horizontal",width=1280,height=720)
        self.paned.grid(row=2,column=0)