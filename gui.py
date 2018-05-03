import tkinter as tk
import random
from screen import Screen


class GUI(tk.Frame):
    def __init__(self,model,jsonHandler,root):
        super().__init__(root)
        self.model = model
        self.jsonHandler = jsonHandler
        self.root = root
        self.grid()
        self.screens = []
        self.quit = None
        self.add_screen = None
        self.canvas = None
        # self.canvas_w = self.root.winfo_windowwidth()
        # self.canvas_h = self.root.winfo_windowheight()
        self.canvas_w = 1280
        self.canvas_h = 720
        self.create_widgets()

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.pack()

        self.add_screen = tk.Button(self, text="Add Screen", command=self.create_screen)
        self.add_screen.pack()

        self.canvas = tk.Canvas(self, width=self.canvas_w, height=self.canvas_h, bg="blue")
        self.canvas.pack()

    def create_screen(self):
        s = Screen(str(len(self.screens)), self.root.winfo_width(), self.root.winfo_height())
        self.screens.append(s)
        count_screens = len(self.screens)
        print(str(count_screens) + " screens")
        self.canvas.delete("all")


        for i, s in enumerate(self.screens):
            x = (self.canvas_w / count_screens) * i if (i > 0) else 0
            y = 0
            w = x * 2 if ( x > 0) else self.canvas_w
            h = 720
            color = self.random_color()
            self.canvas.create_rectangle(x, y, w, h, width=3, fill=color)

    def random_color(self):
        return '#%02X%02X%02X' % (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))