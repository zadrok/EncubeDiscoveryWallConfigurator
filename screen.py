
import tkinter as tk

class Screen:
    def __init__(self,id,width=100,height=100):
        self.id = id
        self.width = width
        self.height = height

    def getTkObject(self, window_height, window_width):

        paned = tk.PanedWindow(orient="vertical", bg="blue", height=window_height, width=window_width)
        text = self.id + ": " + str(self.width) + " x " + str(self.height)
        label = tk.Label(text=text)
        paned.add(label)
        return paned
