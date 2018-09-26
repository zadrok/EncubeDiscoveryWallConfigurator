import tkinter as tk
from menuBar import MBMain
from keyHandeler import KeyHandeler
from selectionController import selcon
from controlPanel import controlPanel
from panel import Panel

class MainWindow(tk.Frame):
  def __init__(self, gui, root):
    ''' creates main window, screens and panels are displayed here '''
    super().__init__(root)
    self.root = root
    self.gui = gui
    self.pack()

    self.canvas = None

    self.splitH = tk.IntVar()
    self.splitV = tk.IntVar()
    self.splitAmount = tk.StringVar()

    self.rect = None
    self.startX = None
    self.startY = None
    self.endX = None
    self.endY = None

    self.update()
    self.canvasW = max( self.root.winfo_width(), self.gui.widthMain )
    self.canvasH = max( self.root.winfo_height(), self.gui.heightMain )

    self.keyHandeler = KeyHandeler(self.root,self)

    self.createWidgets()
    self.focus_set()

    selcon.setMainWindow(self)

    # window changes size
    self.updateLock = True
    self.root.bind("<Configure>", self.configure)

    self.draw()


  def createWidgets(self):
    ''' sets up companents for user to interact with '''
    self.menuBar = MBMain(self)
    self.controlPanel = controlPanel(self)
    self.canvas = tk.Canvas(self, width=self.canvasW, height=self.canvasH, bd=0, bg='gray74', highlightthickness=0)
    self.canvas.pack(fill=tk.BOTH, expand=1)
    self.canvas.bind('<Button-1>', self.canvaslCicked)
    self.canvas.bind('<B1-Motion>', self.drawRectangle)
    self.canvas.bind('<ButtonRelease-1>', self.onMouseRelease)
    self.menuBar.eventLock = True


  def configure(self,event):
    if event.widget != self or self.updateLock: return
    self.update()
    if self.canvasW != self.root.winfo_width() or self.canvasH != self.root.winfo_height():
      self.canvasW = self.root.winfo_width()
      self.canvasH = self.root.winfo_height()
      self.canvas.config(width=self.canvasW, height=self.canvasH)
      self.gui.model.updateScreenSize(self.canvasW,self.canvasH)
      self.draw()


  def drawRectangle(self, event):
    '''Draws a rectangle on screen to highlight the user's selection box'''
    #ensure there are screens on the canvas
    if self.gui.model.screens:
      self.endX = event.x
      self.endY = event.y
      #refresh the canvas
      self.draw()
      self.rect = self.canvas.create_rectangle(self.startX, self.startY, self.endX, self.endY, dash=(6, 4))


  def onMouseRelease(self, event):
    '''confirmation of screens selected'''
    #don't run if you come into this with a 'half' click or a selection box hasn't been drawn
    if (self.endX or self.endY is not None) and self.rect is not None:
      #create the selection area
      width = self.endX - self.startX
      height = self.endY - self.startY

      #check the direction of the selection box, update starting position (allows hightlighting box in any drag direction)
      if width < 0:
        x = self.endX
      else:
        x = self.startX
      if height < 0:
        y = self.endY
      else:
        y = self.startY

      selectionArea = Panel(screen=None, canvas=None, ident="0", method=None, x=x, y=y, width=abs(width), height=abs(height))
      selectedPanels = []
      for s in self.gui.model.screens:
        for p in s.panels:
          #find if panel is within the selection area
          withinArea = selcon.rectOverlap(selectionArea,p)
          if withinArea:
            # add to selected group
            selectedPanels.append(p)

      #check if selected
      for p in selectedPanels:
        if not selcon.panelSelected(p):
          selcon.appendPanel(p)

      #refresh screen with new selected panels
      self.draw()
      self.rect = None

  def canvaslCicked(self, event):
    for s in self.gui.model.screens:
      sx = s.getX()
      sw = sx + s.getWidth()

      sy = s.getY()
      sh = sy + s.getHeight()

      ex = event.x
      ey = event.y

      self.startX = ex
      self.startY = ey
      if ex >= sx and ex <= sw:
        if ey >= sy and ey <= sh:
          # found clicked screen
          selcon.screenClick(ex,ey,s)

    self.draw()


  def draw(self):
    self.canvas.delete("all")
    for s in self.gui.model.screens:
      s.draw()
