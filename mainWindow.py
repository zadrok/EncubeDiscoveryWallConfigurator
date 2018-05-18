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
    self.canvas_w = 1080
    self.canvas_h = 720

    self.keyHandeler = KeyHandeler(self.root,self)

    self.createWidgets()
    self.focus_set()

    selcon.setWindow(self)

  def createWidgets(self):
    ''' sets up companents for user to interact with '''
    # menu bar
    self.menuBar = MBMain(self)
    # other stuff
    # self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
    # self.quit.pack()
    #
    # self.add_screen = tk.Button(self, text="Add Screen", command=self.create_screen)
    # self.add_screen.pack()

    self.canvas = tk.Canvas(self, width=self.canvas_w, height=self.canvas_h, bg="blue")
    self.canvas.bind('<Button-1>', self.canvas_clicked)
    self.canvas.pack(side="left")

    # self.split_mode = tk.LabelFrame(self, text="Split Mode", width=200)
    # vert = tk.Checkbutton(self.split_mode, text="Vertical", variable=self.split_v)
    # hori = tk.Checkbutton(self.split_mode, text="Horizontal", variable=self.split_h)
    # vert.pack(fill="x")
    # hori.pack(fill="x")
    # self.split_mode.pack(side="left")

    # TODO - base this off of what is read in from options
    # TODO - update options when screens and/or panels are updated
    for i in range(6):
      self.create_screen()

    self.menuBar.eventLock = True

  def canvas_clicked(self, event):
    # print('x ' + str(event.x) + ', y ' + str(event.y))
    for s in self.screens:
      sx = s.get_x()
      sw = sx + s.get_width()

      ex = event.x
      ey = event.y
      if ex >= sx and ex <=  sw:
        # found clicked screen
        selcon.screenClick(ex,ey,s)

    self.draw()

  def rePackScreens(self):
    self.canvas.delete("all")
    cScreens = len(self.screens)
    if cScreens == 0: return
    width = self.canvas_w / cScreens
    for i, s in enumerate(self.screens):
      sX,sY,sW,sH = s.get_rectangle()
      x = width * i
      y = 0
      w = width
      h = 720

      s.set_position(x,y,w,h)
      # pass change in position
      cX = x - sX
      cY = y - sY
      cW = w - sW
      cH = h - sH
      s.rePackPanels( cX,cY,cW,cH )

    self.draw()

  def draw(self):
    self.canvas.delete("all")
    for s in self.screens:
      s.draw()

  def create_screen(self):
    self.screens.append( Screen(self, self.canvas, "Screen", 0, 0, 0, 0, "#3d3d3d") )
    self.rePackScreens()
