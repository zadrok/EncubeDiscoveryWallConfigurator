import tkinter as tk
from menuBar import MBMain
from screen import Screen


class MainWindow(tk.Frame):
    def __init__(self, gui, root):
        super().__init__(root)
        self.root = root
        self.gui = gui
        self.screens = []
        self.grid()
        self.add_screen = None
        self.canvas = None
        self.split_mode = None
        self.split_h = tk.IntVar()
        self.split_v = tk.IntVar()
        self.canvas_w = 1080
        self.canvas_h = 720

        self.createWidgets()

    def createWidgets(self):
        # menu bar
        self.menuBar = MBMain(self)
        # other stuff
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
        split_v = self.split_v.get()
        split_h = self.split_h.get()
        canvas_changed = False
        for s in self.screens:
            sx = s.get_x()
            sw = s.get_width()

            ex = event.x
            ey = event.y
            if ex >= sx and ex <=  sw:
                s.clicked(ex, ey, split_h, split_v)
                canvas_changed = True

        if canvas_changed:
            self.canvas.delete("all")
            for i, s in enumerate(self.screens):
                s.draw()

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
