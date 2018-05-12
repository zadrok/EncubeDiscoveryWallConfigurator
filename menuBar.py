import tkinter as tk
from jsonHandler import JsonHandler

from tkinter import filedialog

class MBMain():
    def __init__(self,master):
        self.master = master
        self.menuBar = tk.Menu(master.root)
# ------------------------------------------------------------------------------
        self.fileMenu = tk.Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label = "New", command = self.doNothing)
        self.fileMenu.add_command(label = "Open", command = self.open)
        self.fileMenu.add_command(label = "Save", command = self.save)
        # self.fileMenu.add_command(label = "Save as...", command = self.doNothing)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label = "Exit", command = master.quit)
        self.menuBar.add_cascade(label = "File", menu = self.fileMenu)
# ------------------------------------------------------------------------------
        # self.editMenu = tk.Menu(self.menuBar, tearoff=0)
        # self.editMenu.add_command(label = "Undo", command = self.doNothing)
        # self.editMenu.add_separator()
        # self.editMenu.add_command(label = "Cut", command = self.doNothing)
        # self.editMenu.add_command(label = "Copy", command = self.doNothing)
        # self.editMenu.add_command(label = "Paste", command = self.doNothing)
        # self.editMenu.add_command(label = "Delete", command = self.doNothing)
        # self.editMenu.add_command(label = "Select All", command = self.doNothing)
        # self.menuBar.add_cascade(label = "Edit", menu = self.editMenu)
# ------------------------------------------------------------------------------
        self.optionMenu = tk.Menu(self.menuBar,tearoff=0)
        self.optionMenu.add_command(label = "Options", command = self.toggleOptionWindow)
        self.menuBar.add_cascade(label = "Options", menu = self.optionMenu)
# ------------------------------------------------------------------------------
        # self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        # self.helpMenu.add_command(label = "Help Index", command = self.doNothing)
        # self.helpMenu.add_command(label = "About...", command = self.doNothing)
        # self.menuBar.add_cascade(label = "Help", menu = self.helpMenu)
# ------------------------------------------------------------------------------
        master.root.config(menu=self.menuBar)


    def toggleOptionWindow(self):
        if self.master.gui.optionsWindow.state() == 'normal':
            self.master.gui.optionsWindow.withdraw()
        elif self.master.gui.optionsWindow.state() == 'withdrawn':
            self.master.gui.optionsWindow.deiconify()

    def open(self):
        fname = tk.filedialog.askopenfilename()
        self.master.gui.model.options = JsonHandler().importFile( fname )
        self.master.gui.optionsWindow.refreshValues()

    def save(self):
        fname = tk.filedialog.asksaveasfilename()
        JsonHandler().exportFile( self.master.gui.model, fname )

    def doNothing(self):
        print( ' This button does nothing ' )



class MBOptions():
    def __init__(self,master):
        self.master = master
        self.menuBar = tk.Menu(master)
# ------------------------------------------------------------------------------
        self.fileMenu = tk.Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label = "Add Option", command = self.master.toggleAddOptionWindow)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label = "Close", command = master.withdraw)
        self.menuBar.add_cascade(label = "File", menu = self.fileMenu)
# ------------------------------------------------------------------------------
        # self.editMenu = tk.Menu(self.menuBar, tearoff=0)
        # self.editMenu.add_command(label = "None", command = self.doNothing)
        # self.menuBar.add_cascade(label = "Edit", menu = self.editMenu)
# ------------------------------------------------------------------------------
        # self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        # self.helpMenu.add_command(label = "None", command = self.doNothing)
        # self.menuBar.add_cascade(label = "Help", menu = self.helpMenu)
# ------------------------------------------------------------------------------
        master.config(menu=self.menuBar)

    def doNothing(self):
        print( ' This button does nothing ' )
