from panel import Panel
from selectionController import selcon

class Screen:
  def __init__(self, master, canvas, ident, x, y, width, height, color):
    self.master = master
    self.canvas = canvas
    self.id = ident
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.panels = []

  def draw(self):
    color = self.color
    if selcon.screenSelected(self):
      color = '#6d6d6d'

    bbox = ( self.x, self.y, self.x+self.width, self.y+self.height )
    self.canvas.create_rectangle( bbox, width=3, fill=color )
    for panel in self.panels:
      panel.draw()

  def set_position(self, x, y, w, h):
    self.x = x
    self.y = y
    self.width = w
    self.height = h

  def get_id(self):
    return self.id

  def set_id(self, ident):
    self.id = ident

  def get_x(self):
    return self.x

  def set_x(self, x):
    self.x = x

  def get_y(self):
    return self.y

  def set_y(self, y):
    self.y = y

  def get_width(self):
    return self.width

  def set_width(self, width):
    self.width = width

  def get_height(self):
    return self.height

  def set_height(self, height):
    self.height = height

  def get_canvas(self):
    return self.canvas

  def set_canvas(self, canvas):
    self.canvas = canvas

  def get_rectangle(self):
    return self.x, self.y, self.width, self.height

  def countPanels(self):
    count = 0
    for panel in self.panels:
      count += panel.countPanels()
    return count

  def divideHorizontally(self,num=2):
    ''' create two new panels '''
    x = self.get_x()
    y = self.get_y()
    w = self.get_width()
    h = (self.get_height() / num)

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
    ''' create two new panels '''
    x = self.get_x()
    y = self.get_y()
    w = (self.get_width() / num)
    h = self.get_height()

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

  def get_panel_at_xy(self, x, y):
    for p in self.panels:
      if len(p.panels) > 0:
        pN = p.get_panel_at_xy(x,y)
        if pN != None: return pN
      else:
        px = p.get_x()
        py = p.get_y()
        pw = px + p.get_width()
        ph = py + p.get_height()
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

  def to_dimension_array(self):
    print("Screen----------------")
    screen = []
    dimensionArray = []
    for panel in self.panels:
        panel.to_dimension_array(screen)

    for panel in screen:
        dimensionArray.append(panel.s2plotDimensions())

    return dimensionArray

  def rePackPanels(self,pX,pY,pW,pH):
    ''' pack panels within the screen, passing in the change in position '''
    # make sure this instance has panels to replace
    if len(self.panels) <= 0: return

    # check method of how panels were divided
    m = self.panels[0].method # will be 'h' or 'v'

    # apply position and pass down panel chain
    for i,p in enumerate(self.panels):
      # work out the new position for each panel
      x = pX
      y = pY
      w = pW
      h = pH
      l = len(self.panels)

      # adjust for method
      if m == 'v':
        x = pX + int( i*(pW/l) )
        w = int( (pW/l) )
      elif m == 'h':
        y = pY + int( i*(pH/l) )
        h = int( pH/l )

      # adjust panel to new position
      p.set_position(x,y,w,h)
      # if this panel has panels, pass them the change in position
      if len(p.panels) > 0:
        p.rePackPanels(x,y,w,h)
