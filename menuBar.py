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
    self.fileMenu.add_command(label = "Init Settings", command = self.initWindow)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label = "Exit", command = self.mainWindow.gui.closeEvent)
    self.menuBar.add_cascade(label = "File", menu = self.fileMenu)
# ------------------------------------------------------------------------------
    self.editMenu = tk.Menu(self.menuBar,tearoff=0)
    self.editMenu.add_command(label = "Split horizontally   - Key: 1", command=self.doKeyEvent1)
    self.editMenu.add_command(label = "Split vertically        - Key: 2", command=self.doKeyEvent2)
    self.editMenu.add_command(label = "Join                         - Key: 3", command=self.doKeyEvent3)
    self.editMenu.add_command(label = "Remove                  - Key: 4", command=self.doKeyEvent4)
    self.editMenu.add_command(label = "Deselect                  - Key: 5", command=self.doKeyEvent5)
    self.editMenu.add_command(label = "Select all                 - Key: 6", command=self.doKeyEvent6)
    self.editMenu.add_command(label = "Fill Gap                   - Key: 8", command=self.doKeyEvent8)
    self.editMenu.add_separator()
    self.editMenu.add_command(label = "Set Panels as image", command = self.setPanelsImage)
    self.editMenu.add_command(label = "Set Panels as cube", command = self.setPanelsCube)
    self.editMenu.add_command(label = "Set Panels as graph", command = self.setPanelsGraph)
    self.editMenu.add_separator()
    self.editMenu.add_command(label = "Join panels between nodes", command = self.joinBetweenNodes)
    self.editMenu.add_command(label = "Remove links between panels", command = self.removeLinks)
    self.menuBar.add_cascade(label = "Edit", menu = self.editMenu)
# ------------------------------------------------------------------------------
    self.optionMenu = tk.Menu(self.menuBar,tearoff=0)
    self.optionMenu.add_command(label = "Other Options", command = self.mainWindow.gui.toggleOptionWindow)
    self.menuBar.add_cascade(label = "Options", menu = self.optionMenu)
# ------------------------------------------------------------------------------
    mainWindow.root.config(menu=self.menuBar)


  def save(self):
    ''' calls model.save() '''
    self.mainWindow.gui.model.save()


  def load(self):
    ''' calls model.load() '''
    self.mainWindow.gui.model.load()


  def initWindow(self):
    ''' calls gui.setupInitSettingsWindow() '''
    self.mainWindow.gui.setupInitSettingsWindow()


  def setPanelsImage(self):
    ''' sets selected panels mode to image '''
    selcon.setPanelsMode('image')


  def setPanelsCube(self):
    ''' sets selected panels mode to cube '''
    selcon.setPanelsMode('cube')


  def setPanelsGraph(self):
    ''' sets selected panels mode to graph '''
    selcon.setPanelsMode('graph')


  def removeLinks(self):
    ''' removes any links panels have between nodes '''
    selcon.removelinksbetweenPanelsInDifferentNodes()


  def joinBetweenNodes(self):
    ''' creates links between selected panels in different nodes '''
    selcon.joinWithOtherScreens()


  # short hand to call passKeyEvent function
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
    ''' pass the key event to the key handeler '''
    if self.eventLock:
      self.mainWindow.keyHandeler.doEventDown(event)


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
