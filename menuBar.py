import tkinter as tk

class MBMain():
    def __init__(self,root):
        self.menuBar = tk.Menu(root)
        self.fileMenu = tk.Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label="New", command = self.doNothing)
        self.fileMenu.add_command(label = "Open", command = self.doNothing)
        self.fileMenu.add_command(label = "Save", command = self.doNothing)
        self.fileMenu.add_command(label = "Save as...", command = self.doNothing)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label = "Exit", command = root.quit)

        self.menuBar.add_cascade(label = "File", menu = self.fileMenu)

        self.editMenu = tk.Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label = "Undo", command = self.doNothing)

        self.editMenu.add_separator()

        self.editMenu.add_command(label = "Cut", command = self.doNothing)
        self.editMenu.add_command(label = "Copy", command = self.doNothing)
        self.editMenu.add_command(label = "Paste", command = self.doNothing)
        self.editMenu.add_command(label = "Delete", command = self.doNothing)
        self.editMenu.add_command(label = "Select All", command = self.doNothing)

        self.menuBar.add_cascade(label = "Edit", menu = self.editMenu)

        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label = "Help Index", command = self.doNothing)
        self.helpMenu.add_command(label = "About...", command = self.doNothing)

        self.menuBar.add_cascade(label = "Help", menu = self.helpMenu)

        root.config(menu=self.menuBar)

    def doNothing(self):
        print( ' This button does nothing ' )

class MBOptions():
    def __init__(self,root):
        self.menuBar = tk.Menu(root)
        self.fileMenu = tk.Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label="None", command = self.doNothing)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label = "Close", command = root.withdraw)
        self.menuBar.add_cascade(label = "File", menu = self.fileMenu)

        self.editMenu = tk.Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label = "None", command = self.doNothing)
        self.menuBar.add_cascade(label = "Edit", menu = self.editMenu)

        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label = "None", command = self.doNothing)
        self.menuBar.add_cascade(label = "Help", menu = self.helpMenu)

        root.config(menu=self.menuBar)

    def doNothing(self):
        print( ' This button does nothing ' )
