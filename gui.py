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
        self.split_mode = None
        self.split_h = tk.IntVar()
        self.split_v = tk.IntVar()
        self.canvas_w = 1080
        self.canvas_h = 720
        self.create_widgets()

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.pack()

        self.add_screen = tk.Button(self, text="Add Screen", command=self.create_screen)
        self.add_screen.pack()

        self.canvas = tk.Canvas(self, width=self.canvas_w, height=self.canvas_h, bg="blue")
        self.canvas.bind('<Button-1>', self.canvas_clicked)
        self.canvas.pack(side="left")

        self.split_mode = tk.LabelFrame(self, text="Split Mode", width=200)
        vert = tk.Checkbutton(self.split_mode, text="Vertical", variable=self.split_v)
        hori = tk.Checkbutton(self.split_mode, text="Horizontal", variable=self.split_h)
        vert.pack(fill="x")
        hori.pack(fill="x")
        self.split_mode.pack(side="left")

        for i in range(0, 6):
            self.create_screen()

    def canvas_clicked(self, event):
        print("clicked at: ", event.x, "x", event.y)
        split_v = self.split_v.get()
        split_h = self.split_h.get()
        for s in self.screens:
            sx = s.get_x()
            sw = s.get_width()

            ex = event.x
            ey = event.y
            if ex >= sx and ex <=  sw:
                s.clicked(ex, ey, split_h, split_v)

    def create_screen(self):
        s = Screen(self.canvas, "Screen", 0, 0, 0, 0, "#3d3d3d")
        self.screens.append(s)
        count_screens = len(self.screens)

        self.canvas.delete("all")

        for i, s in enumerate(self.screens):
            x = (self.canvas_w / count_screens) * i
            w = (self.canvas_w / count_screens) + x
            y = 0
            h = 720

            ident = "#" + str(i) + ": " + str(x) + "," + str(y)
            s.set_id(ident)
            s.set_position(x, y, w, h)
            s.draw()

    def random_color(self):
        return '#%02X%02X%02X' % (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))