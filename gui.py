import tkinter as tk

from screen import Screen


class GUI(tk.Frame):
    def __init__(self, model, jsonHandler, root):
        super().__init__(root)
        self.model = model
        self.jsonHandler = jsonHandler
        self.root = root
        self.screens = []
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.add_screen = tk.Button(self)
        self.add_screen["text"] = "Add Screen"
        self.add_screen["command"] = self.create_screen
        self.add_screen.grid(row=0, column=0)

        self.set_up_screen_area()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.grid(row=0, column=1)

    def create_screen(self):

        # Creating a new screen.
        s = Screen("id", 0, 0)
        self.screens.append(s)

        # Calculate new size of screens.
        count_screens = len(self.screens)
        height = self.root.winfo_height()
        width = (self.root.winfo_width() / count_screens) if (count_screens > 0) else self.root.winfo_width()

        for sc in self.screens:
            sc.set_width(width)
            sc.set_height(height)
            sc.set_id(sc.get_name())
            sc.update_pane()

        for sc in self.screens:
            self.paned.remove(sc.get_pane())

        for sc in self.screens:
            self.paned.add(sc.get_pane(), stretch="always")

    def set_up_screen_area(self):
        self.paned = tk.PanedWindow(orient="horizontal", width=1280, height=720)
        self.paned.grid(row=2, column=0)
