from selectionController import selcon

class Panel:
  def __init__(self, screen, canvas, ident, method, x=10, y=10, width=100, height=100, mode='cube'):
    self.id = ident
    self.screen = screen
    self.canvas = canvas
    self.method = method
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    # modes: cube, image, graph
    self.mode = mode

    self.colorCubeNormal = "#00FFFF"
    self.colorCubeSelected = '#008080'

    self.colorImageNormal = "#e500ff"
    self.colorImageSelected = '#730080'

    self.colorGraphNormal = "#f8ff47"
    self.colorGraphSelected = '#7b8000'

    self.colorOther = None


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

  def countPanels(self):
    count = 0
    for panel in self.panels:
      count += panel.countPanels()
    return count + 1

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

      bbox = ( self.x, self.y, self.x+self.width, self.y+self.height )
      self.canvas.create_rectangle( bbox, width=2, fill=color, tags="panel" )

  def toS2plotDimensions(self):
    x1 = self.getX()
    y1 = self.getY()
    x2 = self.getX() + self.getWidth()
    y2 = self.getY() + self.getHeight()
    screen_width = self.screen.getX() + self.screen.getWidth()
    screen_height = self.screen.getY() + self.screen.getHeight()
    nx1 = x1 / screen_width
    nx2 = x2 / screen_width
    # calculate then invert the Y coordinates (inversion for S2PLOT's xy system)
    ny1 = y1 / screen_height
    ny1 = abs((ny1 - 1) * 1)
    ny2 = y2 / screen_height
    ny2 = abs((ny2 - 1) * 1)
    return [nx1, ny1, nx2, ny2]

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

    self.screen.panels.remove(self)

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

    self.screen.panels.remove(self)


  def getPanelAtXY(self, x, y):
    for p in self.panels:
      if len(p.panels) > 0:
        pN = p.getPanelAtXY(x,y)
        if pN != None: return pN
      else:
        px = p.getX()
        py = p.getY()
        pw = px + p.getWidth()
        ph = py + p.getHeight()
        if (x >= px and x <= pw) and (y >= py and y <= ph):
          return p
    return None

  def removePanel(self,panel):
    # try and remove this panel from self.panels list
    try:
      self.panels.remove(panel)
    except ValueError:
      # if error pass down panel chain
      for p in self.panels:
        p.removePanel(panel)

  # def rePackPanels(self,pX,pY,pW,pH):
  #   ''' pack panels within the screen, passing in the change in position '''
  #   # make sure this instance has panels to replace
  #   if len(self.panels) <= 0: return
  #
  #   # if this panel only has one panel in it, take any panels it has, move them to this panel and remove the panel
  #   if len(self.panels) == 1:
  #     self.panels = self.panels[0].panels
  #     if len(self.panels) <= 0: return
  #
  #   # check method of how panels were divided
  #   m = self.panels[0].method # will be 'h' or 'v'
  #
  #   # apply position change and pass down panel chain
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
  #     # set panel to new position
  #     p.setPosition(x,y,w,h)
  #     # if this panel has panels, pass them the change in position
  #     if len(p.panels) > 0:
  #       p.rePackPanels(x,y,w,h)
