import tkinter as tk
from menuBar import MBMain
from screen import Screen
from keyHandeler import KeyHandeler
from selectionController import selcon
from bttwidget import Wbuttons


class MainWindow(tk.Frame):
  def __init__(self, gui, root):
    ''' creates main window, screens and panels are displayed here '''
    super().__init__(root)
    self.root = root
    self.gui = gui
    self.screens = []
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
    self.buttonWidget = Wbuttons(self)
    self.canvas = tk.Canvas(self, width=self.canvasW, height=self.canvasH, bg="gray74")
    self.canvas.bind('<Button-1>', self.canvaslCicked)
    self.canvas.pack(side="left")

    # menu bar
    # TODO - base this off of what is read in from options
    # TODO - update options when screens and/or panels are updated
    # for i in range(6):
    #   if(i % 2 == 0):
    #     color = "#4d94ff"
    #   else:
    #     color = "#3366FF"
    #
    #   self.createScreen(color)

    self.menuBar.eventLock = True

  def canvaslCicked(self, event):
    for s in self.screens:
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


  # def rePackScreens(self):
  #   self.canvas.delete("all")
  #   cScreens = len(self.screens)
  #   if cScreens == 0: return
  #   width = self.canvasW / cScreens
  #   for i, s in enumerate(self.screens):
  #     x = width * i
  #     y = 0
  #     w = width
  #     h = 720
  #
  #     s.setPosition( x,y,w,h )
  #     # s.rePackPanels( x,y,w,h )
  #
  #   self.draw()

  def draw(self):
    self.canvas.delete("all")
    for s in self.screens:
      s.draw()

    self.gui.model.setScreens(self.screens, width=self.canvasW, height=self.canvasH)

  def createScreen(self, color):
    self.screens.append(Screen(self, self.canvas, "Screen", 0, 0, 0, 0, "#3d3d3d", color))

  def createScreens(self,numScreenRows,numScreenColumns,aspectRatioScreensA=16,aspectRatioScreensB=9):  # read AxB, 16x9
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
        self.screens.append( Screen(self, self.canvas, "Screen", x, y, w, h, "#3d3d3d", "#3366FF") )
        x += w
      x = 0
      y += h

    self.draw()

  def countScreensPanels(self):
    cS = 0
    cP = 0

    for screen in self.screens:
      cS += 1
      cP += screen.countPanels()

    print('Screens: ' + str(cS))
    print('Panels: ' + str(cP))
