import tkinter as tk
from jsonHandler import JsonHandler

from tkinter import filedialog

class MBMain():
  def __init__(self,master):
    ''' creates the menu bar for a window '''
    self.eventLock = False
    self.master = master
    self.menuBar = tk.Menu(master.root)
# ------------------------------------------------------------------------------
    self.fileMenu = tk.Menu(self.menuBar,tearoff=0)
    # self.fileMenu.add_command(label = "New", command = self.doNothing)
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
    self.optionMenu.add_command(label = "Split horizontally   - Key: 1", command=self.doKeyEvent1)
    self.optionMenu.add_command(label = "Split vertically        - Key: 2", command=self.doKeyEvent2)
    self.optionMenu.add_command(label = "Join                         - Key: 3", command=self.doKeyEvent3)
    self.optionMenu.add_command(label = "Remove                  - Key: 4", command=self.doKeyEvent4)
    self.optionMenu.add_command(label = "Deselect                  - Key: 5", command=self.doKeyEvent5)
    self.optionMenu.add_command(label = "Select all                 - Key: 6", command=self.doKeyEvent6)
    self.optionMenu.add_command(label = "Force redraw          - Key: 7", command=self.doKeyEvent7)
    self.optionMenu.add_separator()
    self.optionMenu.add_command(label = "Options", command = self.master.gui.toggleOptionWindow)
    self.optionMenu.add_separator()
    self.optionMenu.add_command(label = "Print Options", command = self.master.gui.model.printOptions)
    self.menuBar.add_cascade(label = "Options", menu = self.optionMenu)
# ------------------------------------------------------------------------------
    # self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
    # self.helpMenu.add_command(label = "Help Index", command = self.doNothing)
    # self.helpMenu.add_command(label = "About...", command = self.doNothing)
    # self.menuBar.add_cascade(label = "Help", menu = self.helpMenu)
# ------------------------------------------------------------------------------
    self.splitNumIndex = 3 # if adding something before this +1 to index !!!!!!!
    self.menuBar.add_cascade(label=self.master.keyHandeler.getScrollCountText())

    master.root.config(menu=self.menuBar)

  def open(self):
    ''' opens a file dialog and passes the file to the model '''
    fname = tk.filedialog.askopenfilename()
    self.master.gui.model.open(fname)
    self.master.gui.optionsWindow.refreshValues()

  def save(self):
    ''' opens a file dialog and passes the file to the model '''
    fname = tk.filedialog.asksaveasfilename()
    self.master.gui.model.save(fname)

  def doKeyEvent1(self): self.passKeyEvent('1')
  def doKeyEvent2(self): self.passKeyEvent('2')
  def doKeyEvent3(self): self.passKeyEvent('3')
  def doKeyEvent4(self): self.passKeyEvent('4')
  def doKeyEvent5(self): self.passKeyEvent('5')
  def doKeyEvent6(self): self.passKeyEvent('6')
  def doKeyEvent7(self): self.passKeyEvent('7')
  def doKeyEvent8(self): self.passKeyEvent('8')
  def doKeyEvent9(self): self.passKeyEvent('9')
  def doKeyEvent0(self): self.passKeyEvent('0')

  def passKeyEvent(self,event):
    if self.eventLock:
      self.master.keyHandeler.doEventDown(event)

  def doNothing(self):
    ''' used for menu items that are not implemented yet '''
    print( ' This button does nothing ' )



class MBOptions():
  def __init__(self,master):
    ''' creates the menu bar for a window '''
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
    ''' used for menu items that are not implemented yet '''
    print( ' This button does nothing ' )
