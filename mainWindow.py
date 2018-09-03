import tkinter as tk
from menuBar import MBMain
from screen import Screen
from keyHandeler import KeyHandeler
from selectionController import selcon
from controlPanel import controlPanel


class MainWindow(tk.Frame):
  def __init__(self, gui, root):
    ''' creates main window, screens and panels are displayed here '''
    super().__init__(root)
    self.root = root
    self.gui = gui
    self.pack()
    self.add_screen = None
    self.canvas = None
    self.split_mode = None
    self.splitH = tk.IntVar()
    self.splitV = tk.IntVar()
    self.splitAmount = tk.StringVar()

    self.update()
    self.canvasW = self.root.winfo_width()
    self.canvasH = self.root.winfo_height()

    self.keyHandeler = KeyHandeler(self.root,self)

    self.createWidgets()
    self.focus_set()

    selcon.setMainWindow(self)
    self.draw()


  def createWidgets(self):
    ''' sets up companents for user to interact with '''
    self.menuBar = MBMain(self)
    self.controlPanel = controlPanel(self)
    self.canvas = tk.Canvas(self, width=self.canvasW, height=self.canvasH, bg="gray74")
    self.canvas.bind('<Button-1>', self.canvaslCicked)
    self.canvas.pack(side="left")
    self.menuBar.eventLock = True

  def canvaslCicked(self, event):
    for s in self.gui.model.screens:
      sx = s.getX()
      sw = sx + s.getWidth()

      sy = s.getY()
      sh = sy + s.getHeight()

      ex = event.x
      ey = event.y
      if ex >= sx and ex <= sw:
        if ey >= sy and ey <= sh:
          # found clicked screen
          selcon.screenClick(ex,ey,s)

    self.draw()


  def draw(self):
    self.canvas.delete("all")
    for s in self.gui.model.screens:
      s.draw()


  def createScreen(self, color):
    self.gui.model.screens.append(Screen(self, self.canvas, "Screen", 0, 0, 0, 0, "#3d3d3d", color))


  def createScreens(self,numScreenRows,numScreenColumns,aspectRatioScreensA=16,aspectRatioScreensB=9):  # read AxB, 16x9
    self.gui.model.screens = []
    self.numScreenRows = numScreenRows
    self.numScreenColumns = numScreenColumns
    self.aspectRatioScreensA = aspectRatioScreensA # read AxB, 16x9
    self.aspectRatioScreensB = aspectRatioScreensB

    x = 0
    y = 0
    w = int( self.canvasW / self.numScreenColumns )
    h = int( w / ( self.aspectRatioScreensA / self.aspectRatioScreensB ) )

    if h*self.numScreenRows > self.canvasH:
      overflow = (h*self.numScreenRows) - self.canvasH
      h -= int( overflow/self.numScreenRows )
      w = h*( ( self.aspectRatioScreensA / self.aspectRatioScreensB ) )

    for row in range(numScreenRows):
      for col in range(numScreenColumns):
        self.gui.model.screens.append( Screen(self, self.canvas, "Screen", x, y, w, h, "#3d3d3d", "#3366FF") )
        x += w
      x = 0
      y += h

    self.draw()

  def countScreensPanels(self):
    cS = 0
    cP = 0

    for screen in self.gui.model.screens:
      cS += 1
      cP += screen.countPanels()

    print('Screens: ' + str(cS))
    print('Panels: ' + str(cP))
