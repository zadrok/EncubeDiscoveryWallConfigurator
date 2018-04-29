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
        self.screens = []
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

        self.set_up_screen_area()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.grid(row=1, column=0)

    def say_hi(self):
        print("hi there, everyone!")

    def create_screen(self):
        # Creating a new screen.
        screen = Screen("id",120,400)
        self.screens.append(screen)
        count_screens = len(self.screens)
        # Calculate new size of screens.
        width = self.root.winfo_width() / count_screens
        self.paned.add(screen.getTkObject(
            window_height=self.root.winfo_height(),
            window_width=width)
        )
        children = self.paned.winfo_children()
        for screen in children:
            screen.configure(width=width)
        # self.paned.add(screen.getTkObject(
        #     window_height=self.root.winfo_height(),
        #     window_width=self.root.winfo_width()))

    def set_up_screen_area(self):
        self.paned = tk.PanedWindow(orient="horizontal",width=1280,height=720)
        self.paned.grid(row=2,column=0)