from selectionController import selcon

class Panel:
  def __init__(self, screen, canvas, ident, method, x=10, y=10, width=100, height=100, ):
    self.id = ident
    self.screen = screen
    self.canvas = canvas
    self.method = method
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.panels = []

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

  def get_rectangle(self):
    return self.x, self.y, self.width, self.height

  def countPanels(self):
    count = 0
    for panel in self.panels:
      count += panel.countPanels()
    return count + 1

  def draw(self, color):
    if len(self.panels) > 0:
      for p in self.panels:
        p.draw(color)
    else:
      if selcon.panelSelected(self):
        if color == "#4d94ff":
          color = "#70db70"
        else:
          color = "#2EB82E"

      bbox = ( self.x, self.y, self.x+self.width, self.y+self.height )
      self.canvas.create_rectangle( bbox, width=2, fill=color, tags="panel" )

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

  def adjustPosition(self,cX,cY,cW,cH):
    self.x += cX
    self.y += cY
    self.width += cW
    self.height += cH

  def s2_plot_dimensions(self):
    x1 = self.get_x()
    y1 = self.get_y()
    x2 = self.get_x() + self.get_width()
    y2 = self.get_y() + self.get_height()
    screen_width  = self.screen.get_x() + self.screen.get_width()
    screen_height = self.screen.get_y() + self.screen.get_height()
    nx1 = x1 / screen_width
    nx2 = x2 / screen_width

    # calculate then invert the Y coordinates (inversion for S2PLOT's xy system)
    ny1 = y1 / screen_height
    ny1 = abs((ny1-1)*1)

    ny2 = y2 / screen_height
    ny2 = abs((ny2-1)*1)

    return [nx1, ny1, nx2, ny2]

  def flatten(self,l):
    return self.flatten(l[0]) + (self.flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]

  def to_dimension_array(self, appendTo):
    if len(self.panels) > 0:
        for panel in self.panels:
            panel.to_dimension_array(appendTo)
    else:
        appendTo.append(self)

  def rePackPanels(self,pX,pY,pW,pH):
    ''' pack panels within the screen, passing in the change in position '''
    # make sure this instance has panels to replace
    if len(self.panels) <= 0: return

    # if this panel only has one panel in it, take any panels it has, move them to this panel and remove the panel
    if len(self.panels) == 1:
      self.panels = self.panels[0].panels
      if len(self.panels) <= 0: return

    # check method of how panels were divided
    m = self.panels[0].method # will be 'h' or 'v'

    # apply position change and pass down panel chain
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

      # set panel to new position
      p.set_position(x,y,w,h)
      # if this panel has panels, pass them the change in position
      if len(p.panels) > 0:
        p.rePackPanels(x,y,w,h)
