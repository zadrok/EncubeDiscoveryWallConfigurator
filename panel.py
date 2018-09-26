from selectionController import selcon
import random

class Panel:
  def __init__(self, screen, canvas, ident, method, x=1, y=1, width=1, height=1, mode='cube'):
    '''initialize panel objjects'''
    self.id = ident
    self.screen = screen
    self.canvas = canvas
    self.method = method
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    # panels in other screens
    self.sharePanels = []
    self.shareID = None

    # modes: cube, image, graph
    self.mode = mode

    self.colorCubeNormal = "#00FFFF"
    self.colorCubeSelected = '#008080'

    self.colorImageNormal = "#e500ff"
    self.colorImageSelected = '#730080'

    self.colorGraphNormal = "#f8ff47"
    self.colorGraphSelected = '#7b8000'

    self.colorOther = None

  def getShareID(self):
    if self.shareID == None and len(self.sharePanels) > 0:
      # see if any of the shared panels have an id
      for sp in self.sharePanels:
        self.shareID = sp.shareID
        if self.shareID != None:
          break
      if self.shareID == None:
        # if still none generate an id
        self.shareID = self.screen.model.getNextPanelShareID()
    return self.shareID

  def addSharePanel(self, aPanel):
    if self != aPanel and not self.sharePanelsContains(aPanel):
      self.sharePanels.append(aPanel)


  def sharePanelsContains(self, aPanel):
    for p in self.sharePanels:
      if aPanel == p:
        return True
    return False


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

  def getRectangle(self):
    return self.x, self.y, self.width, self.height

  def get_mode(self):
    return self.mode

  def set_mode(self, mode):
    self.mode = mode

  def draw(self, color):
    color = self.colorCubeNormal
    if self.mode == 'cube':
      color = self.colorCubeNormal
      if selcon.panelSelected(self):
        color = self.colorCubeSelected
    elif self.mode == 'image':
      color = self.colorImageNormal
      if selcon.panelSelected(self):
        color = self.colorImageSelected
    elif self.mode == 'graph':
      color = self.colorGraphNormal
      if selcon.panelSelected(self):
        color = self.colorGraphSelected

    if self.colorOther != None:
      color = self.colorOther

    x,y,w,h = self.getRect()
    bbox = ( x, y, x+w, y+h )
    self.canvas.create_rectangle( bbox, width=2, fill=color, tags="panel" )

    for p in self.sharePanels:
      # other panel
      xP,yP,wP,hP = p.getRect()
      x1 = x + ( w / 2 )
      y1 = y + ( h / 2 )
      x2 = xP + ( wP / 2 )
      y2 = yP + ( hP / 2 )
      self.canvas.create_line(x1,y1,x2,y2,fill="white",width=4)


  def getRect(self):
    ''' returns pixel location for panel '''
    x = ( self.screen.getWidth() * self.getX() ) + self.screen.getX()
    y = ( self.screen.getHeight() * self.getY() ) + self.screen.getY()
    w = self.screen.getWidth() * self.getWidth()
    h = self.screen.getHeight() * self.getHeight()
    return x,y,w,h


  def toS2plotDimensions(self):
    x,y,w,h = self.getRect()
    x1 = x - self.screen.getX()
    y1 = y - self.screen.getY()
    x2 = x1 + w
    y2 = y1 + h
    # screen_width = self.screen.getX() + self.screen.getWidth()
    # screen_height = self.screen.getY() + self.screen.getHeight()
    nx1 = x1 / self.screen.getWidth()
    nx2 = x2 / self.screen.getWidth()
    # calculate then invert the Y coordinates (inversion for S2PLOT's xy system)
    ny1 = y1 / self.screen.getHeight()
    ny1 = abs((ny1 - 1) * 1)
    ny2 = y2 / self.screen.getHeight()
    ny2 = abs((ny2 - 1) * 1)
    return [nx1, ny2, nx2, ny1]



  def divideHorizontally(self,num=2):
    ''' create new panels '''
    x = self.getX()
    y = self.getY()
    w = self.getWidth()
    h = (self.getHeight() / num)

    for n in range(num):
      p = Panel(
        screen=self.screen,
        canvas=self.canvas,
        ident="0",
        method='h',
        x=x,
        y=y + (h*n),
        width=w,
        height=h,
        mode=self.mode
      )
      self.screen.panels.append( p )

    self.screen.removePanel(self)

  def divideVertically(self,num=2):
    ''' create new panels '''
    x = self.getX()
    y = self.getY()
    w = (self.getWidth() / num)
    h = self.getHeight()

    for n in range(num):
      p = Panel(
        screen=self.screen,
        canvas=self.canvas,
        ident="0",
        method='v',
        x=x + (w*n),
        y=y,
        width=w,
        height=h,
        mode=self.mode
      )
      self.screen.panels.append( p )

    self.screen.removePanel(self)
