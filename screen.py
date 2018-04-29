import tkinter as tk


class Screen:
    def __init__(self, id="id", width=100, height=100):
        self.name = id
        self.width = width
        self.height = height
        self.id = self.name + " : " + str(self.width) + " x " + str(self.height)
        self.pane = tk.LabelFrame(text=self.id, padx=self.height, pady=self.width)

    def get_pane(self):
        return self.pane

    def get_name(self):
        return self.name

    def update_pane(self):
        self.pane.config(height=self.height)
        self.pane.config(width=self.width)
        self.pane.config(text=self.id)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_id(self, id):
        self.id = id + ": " + str(self.width) + " x " + str(self.height)
