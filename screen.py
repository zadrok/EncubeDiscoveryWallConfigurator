import tkinter as tk
from panel import Panel


class Screen:
    def __init__(self, gui, id="id", width=100, height=100):
        self.name = id
        self.width = width
        self.height = height
        self.gui = gui
        self.id = self.name + " : " + str(self.width) + " x " + str(self.height)
        self.pane = tk.LabelFrame(text=self.id, padx=self.height, pady=self.width)

        self.panels = []

        self.add_panel = tk.Button(self.pane, text="+", command=self.create_panel)
        self.add_panel.pack(fill="y")

        # Set up delete button
        self.delete = tk.Button(self.pane, text="Delete", fg="red",border=2, command=self.delete_screen)
        self.delete.pack(fill="y")

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

    def delete_screen(self):
        print("Screen@Delete Screen: " + str(self.id))
        self.gui.delete_screen(self.id)

    def create_panel(self):
        # Creating a new panel
        p = Panel(self.pane, "id", 0, 0, 100, 100)
        self.panels.append(p)

        count_panels = len(self.panels)
        width = self.width / count_panels if(count_panels > 0) else self.width
        height = self.height / count_panels if (count_panels > 0) else self.height

        for pan in self.panels:
            pan.set_width(width)
            pan.set_height(height)
            pan.set_id(pan.get_id())
            pan.update_frame()

        for pan in self.panels:
            pan.get_frame().pack_forget()

        for pan in self.panels:
            pan.get_frame().pack()
