import tkinter as tk

class Panel:
    def __init__(self, screen, id, x=10, y=10, width=100, height=100):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.frame = tk.LabelFrame(screen, text=self.id, padx=self.height, pady=self.width)
        self.frame.pack()

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_id(self,id):
        self.id = str(self.height) + " x " + str(self.width)

    def get_frame(self):
        return self.frame

    def get_id(self):
        return self.id

    def update_frame(self):
        self.frame.config(height=self.height, width=self.width, text=self.id)
