from panel import Panel
from selectionController import selcon

class Screen:
  def __init__(self, master, canvas, ident, x, y, width, height, color, panel_color):
    self.master = master
    self.canvas = canvas
    self.id = ident
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.panel_color = panel_color
    self.panels = []
    self.createPanel("C", x, y, width, height)


  def draw(self):
    color = self.color
    if selcon.screenSelected(self):
      color = '#6d6d6d'

    bbox = ( self.x, self.y, self.x+self.width, self.y+self.height )
    self.canvas.create_rectangle( bbox, width=7, fill=color, outline='red' )
    for panel in self.panels:
      panel.draw(self.panel_color)

  def setPosition(self, x, y, w, h):
    self.x = x
    self.y = y
    self.width = w
    self.height = h

  def getId(self):
    return self.id

  def setId(self, ident):
    self.id = ident

  def getX(self):
    return self.x

  def setX(self, x):
    self.x = x

  def getY(self):
    return self.y

  def setY(self, y):
    self.y = y

  def getWidth(self):
    return self.width

  def setWidth(self, width):
    self.width = width

  def getHeight(self):
    return self.height

  def setHeight(self, height):
    self.height = height

  def get_canvas(self):
    return self.canvas

  def set_canvas(self, canvas):
    self.canvas = canvas

  def getRectangle(self):
    return self.x, self.y, self.width, self.height

  def countPanels(self):
    count = 0
    for panel in self.panels:
      count += panel.countPanels()
    return count

  def createPanel(self, method, x, y, width, height):
    self.panels.append( Panel(
      screen=self,
      canvas=self.canvas,
      ident="0",
      method=method,
      x=x,
      y=y,
      width=width,
      height=height
      )
    )

  def divideHorizontally(self,num=2):
    ''' create new panels '''
    x = self.getX()
    y = self.getY()
    w = self.getWidth()
    h = (self.getHeight() / num)

    for n in range(num):
      p = Panel(
        screen=self,
        canvas=self.canvas,
        ident="0",
        method='h',
        x=x,
        y=y + (h*n),
        width=w,
        height=h
      )
      self.panels.append( p )

  def divideVertically(self,num=2):
    ''' create new panels '''
    x = self.getX()
    y = self.getY()
    w = (self.getWidth() / num)
    h = self.getHeight()

    for n in range(num):
      p = Panel(
        screen=self,
        canvas=self.canvas,
        ident="0",
        method='v',
        x=x + (w*n),
        y=y,
        width=w,
        height=h
      )
      self.panels.append( p )

  def getPanelAtXY(self, x, y):
    for p in self.panels:
      px = p.getX()
      py = p.getY()
      pw = px + p.getWidth()
      ph = py + p.getHeight()
      if (x >= px and x <= pw) and (y >= py and y <= ph):
        return p
    return None

  def removePanel(self, panel):
    # try and remove this panel from self.panels list
    try:
      self.panels.remove(panel)
    except ValueError:
      # if error pass down panel chain
      for p in self.panels:
        p.removePanel(panel)

  def toDimensionArray(self):
    panels = dict()
    for (index, p) in enumerate(self.panels, start=1):
        panels['p'+str(index)] = {"type": p.get_mode(), "dimensions": p.toS2plotDimensions()}
    return panels

  # def rePackPanels(self,pX,pY,pW,pH):
  #   ''' pack panels within the screen, passing in the change in position '''
  #   # make sure this instance has panels to replace
  #   if len(self.panels) <= 0: return
  #
  #   # check method of how panels were divided
  #   m = self.panels[0].method # will be 'h' or 'v'
  #
  #   # apply position and pass down panel chain
  #   for i,p in enumerate(self.panels):
  #     # work out the new position for each panel
  #     x = pX
  #     y = pY
  #     w = pW
  #     h = pH
  #     l = len(self.panels)
  #
  #     # adjust for method
  #     if m == 'v':
  #       x = pX + int( i*(pW/l) )
  #       w = int( (pW/l) )
  #     elif m == 'h':
  #       y = pY + int( i*(pH/l) )
  #       h = int( pH/l )
  #
  #     # adjust panel to new position
  #     p.setPosition(x,y,w,h)
  #     # if this panel has panels, pass them the change in position
  #     if len(p.panels) > 0:
  #       p.rePackPanels(x,y,w,h)
