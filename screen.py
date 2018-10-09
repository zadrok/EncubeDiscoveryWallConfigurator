from panel import Panel
from selectionController import selcon
from jsonHandler import NoIndent

# this should probably be changed to 'Node'

class Screen:
  def __init__(self, model, canvas, ident, x, y, width, height, color, panel_color):
    '''initialize screen objects'''
    self.model = model
    self.canvas = canvas
    self.id = ident
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.panel_color = panel_color
    self.panels = []


  def removePanel(self,aPanel):
    # remove and share panels
    for scr in self.model.screens:
      for pan in scr.panels:
        try:
          pan.sharePanels.remove(aPanel)
        except:
          pass
    # remove panel
    try:
      self.panels.remove(aPanel)
    except:
      pass


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
    p = Panel(
      screen=self,
      canvas=self.canvas,
      ident="0",
      method=method,
      x=x,
      y=y,
      width=width,
      height=height
      )
    self.panels.append( p )
    return p

  def divideHorizontally(self,num=2):
    ''' create new panels '''
    x = 0
    y = 0
    w = 1
    h = (self.getHeight() / num) / self.getHeight()

    if len(self.panels) < 1:
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
    x = 0
    y = 0
    w = (self.getWidth() / num) / self.getWidth()
    h = 1

    if len(self.panels) < 1:
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
      px,py,pw,ph = p.getRect()
      pw += px
      ph += py
      if (x >= px and x <= pw) and (y >= py and y <= ph):
        return p
    return None

  def toDimensionArray(self):
    panels = dict()
    for (index, p) in enumerate(self.panels):
        dim = p.toS2plotDimensions()
        if len( p.sharePanels ) > 0:
          panels['p'+str(index)] = {"type": p.get_mode(), "shareID": p.getShareID(),"dimensions": NoIndent(dim)}
        else:
          panels['p'+str(index)] = {"type": p.get_mode(),"dimensions": NoIndent(dim)}
    return panels
