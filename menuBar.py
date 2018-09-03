import tkinter as tk
from jsonHandler import JsonHandler
from selectionController import selcon
from tkinter import filedialog

class MBMain():
  def __init__(self,mainWindow):
    ''' creates the menu bar for a window '''
    self.eventLock = False
    self.mainWindow = mainWindow
    self.menuBar = tk.Menu(mainWindow.root)
# ------------------------------------------------------------------------------
    self.fileMenu = tk.Menu(self.menuBar,tearoff=0)
    self.fileMenu.add_command(label = "Save", command = self.save)
    self.fileMenu.add_command(label = "Load", command = self.load)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label = "Exit", command = self.mainWindow.gui.closeEvent)
    self.menuBar.add_cascade(label = "File", menu = self.fileMenu)
# ------------------------------------------------------------------------------
    self.optionMenu = tk.Menu(self.menuBar,tearoff=0)
    self.optionMenu.add_command(label = "Split horizontally   - Key: 1", command=self.doKeyEvent1)
    self.optionMenu.add_command(label = "Split vertically        - Key: 2", command=self.doKeyEvent2)
    self.optionMenu.add_command(label = "Join                         - Key: 3", command=self.doKeyEvent3)
    self.optionMenu.add_command(label = "Remove                  - Key: 4", command=self.doKeyEvent4)
    self.optionMenu.add_command(label = "Deselect                  - Key: 5", command=self.doKeyEvent5)
    self.optionMenu.add_command(label = "Select all                 - Key: 6", command=self.doKeyEvent6)
    self.optionMenu.add_command(label = "Force redraw          - Key: 7", command=self.doKeyEvent7)
    self.optionMenu.add_command(label = "Fill Gap                    - Key: 8", command=self.doKeyEvent8)
    self.optionMenu.add_separator()
    self.optionMenu.add_command(label = "Set Panels as image", command = self.setPanelsImage)
    self.optionMenu.add_command(label = "Set Panels as cube", command = self.setPanelsCube)
    self.optionMenu.add_command(label = "Set Panels as graph", command = self.setPanelsGraph)
    self.optionMenu.add_separator()
    self.optionMenu.add_command(label = "Options", command = self.mainWindow.gui.toggleOptionWindow)
    self.optionMenu.add_separator()
    self.optionMenu.add_command(label = "Print Options", command = self.mainWindow.gui.model.printOptions)
    self.menuBar.add_cascade(label = "Options", menu = self.optionMenu)
# ------------------------------------------------------------------------------
    mainWindow.root.config(menu=self.menuBar)

  def save(self):
    self.mainWindow.gui.model.save()

  def load(self):
    self.mainWindow.gui.model.load()

  def setPanelsImage(self):
    selcon.setPanelsMode('image')

  def setPanelsCube(self):
    selcon.setPanelsMode('cube')

  def setPanelsGraph(self):
    selcon.setPanelsMode('graph')


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
      self.mainWindow.keyHandeler.doEventDown(event)

  def doNothing(self):
    ''' used for menu items that are not implemented yet '''
    print( ' This button does nothing ' )


class MBOptions():
  def __init__(self,optionsWindow):
    ''' creates the menu bar for a window '''
    self.optionsWindow = optionsWindow
    self.menuBar = tk.Menu(optionsWindow)
# ------------------------------------------------------------------------------
    self.fileMenu = tk.Menu(self.menuBar,tearoff=0)
    self.fileMenu.add_command(label = "Add Option", command = self.optionsWindow.toggleAddOptionWindow)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label = "Close", command = optionsWindow.withdraw)
    self.menuBar.add_cascade(label = "File", menu = self.fileMenu)
# ------------------------------------------------------------------------------
    optionsWindow.config(menu=self.menuBar)

  def doNothing(self):
    ''' used for menu items that are not implemented yet '''
    print( ' This button does nothing ' )
