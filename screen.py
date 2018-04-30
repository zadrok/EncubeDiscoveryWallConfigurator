import tkinter as tk


class Screen:
    def __init__(self, id="id", width=100, height=100):
        self.name = id
        self.width = width
        self.height = height
        self.id = self.name + " : " + str(self.width) + " x " + str(self.height)
        self.pane = tk.LabelFrame(text=self.id, padx=self.height, pady=self.width)

        self.panels = []
        
        self.add_panel = tk.Button(self.pane, text="+", command=self.create_panel)
        self.add_panel.pack(fill="y")

        # Set up delete button
        self.delete = tk.Button(self.pane, text="Delete", command=self.delete)
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

    def delete(self):
        print("Delete Screen: " + str(self.id))
        # ToDo: emit event from here, listen for it in gui.class.

    def create_panel(self): 
        print("Creating Panel");