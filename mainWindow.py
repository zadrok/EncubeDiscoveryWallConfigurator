import tkinter as tk
from menuBar import MBMain
from screen import Screen
from keyHandeler import KeyHandeler
from selectionController import selcon


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
    self.split_h = tk.IntVar()
    self.split_v = tk.IntVar()
    self.splitAmount = tk.StringVar()
    self.canvas_w = 1000
    self.canvas_h = 700

    self.keyHandeler = KeyHandeler(self.root,self)

    self.createWidgets()
    self.focus_set()

    selcon.setWindow(self)

  def createWidgets(self):
    ''' sets up companents for user to interact with '''
    # menu bar
    self.menuBar = MBMain(self)

    self.canvas = tk.Canvas(self, width=self.canvas_w, height=self.canvas_h, bg="gray74")
    self.canvas.bind('<Button-1>', self.canvas_clicked)
    self.canvas.pack(side="left")

    self.menuBar.eventLock = True

  def canvas_clicked(self, event):
    for s in self.screens:
      sx = s.get_x()
      sw = sx + s.get_width()

      sy = s.get_y()
      sh = sy + s.get_height()

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
  #   width = self.canvas_w / cScreens
  #   for i, s in enumerate(self.screens):
  #     x = width * i
  #     y = 0
  #     w = width
  #     h = 720
  #
  #     s.set_position( x,y,w,h )
  #     # s.rePackPanels( x,y,w,h )
  #
  #   self.draw()

  def draw(self):
    self.canvas.delete("all")
    for s in self.screens:
      s.draw()

    self.gui.model.set_screens(self.screens, width=self.canvas_w, height=self.canvas_h)

  def create_screen(self):
    self.screens.append( Screen(self, self.canvas, "Screen", 0, 0, 0, 0, "#3d3d3d") )
    self.rePackScreens()

  def createScreens(self,numScreenRows,numScreenColumns):
    self.numScreenRows = numScreenRows
    self.numScreenColumns = numScreenColumns

    x = 0
    y = 0
    w = int( self.canvas_w / self.numScreenColumns )
    h = int( self.canvas_h / self.numScreenRows )

    for row in range(numScreenRows):
      for col in range(numScreenColumns):
        self.screens.append( Screen(self, self.canvas, "Screen", x, y, w, h, "#3d3d3d") )
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
