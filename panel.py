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

  def draw(self):
    if len(self.panels) > 0:
      for p in self.panels:
        p.draw()
    else:
      color = "#00FFFF"
      if selcon.panelSelected(self):
        color = '#00ff90'

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
        method='h',
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

  def rePackPanels(self,cX,cY,cW,cH):
    ''' pack panels within the screen, passing in the change in position '''
    # make sure this instance has panels to replace
    if len(self.panels) <= 0: return
    # check method of how panels were divided
    m = self.panels[0].method # will be 'h' or 'v'
    # apply position change and pass down panel chain
    for i,p in enumerate(self.panels):
      # work out the new position for each panel
      x = cX
      y = cY
      w = cW
      h = cH

      # adjust for method
      if m == 'v':
        w = cW / len(self.panels)
        x += w*i
      elif m == 'h':
        h = cH / len(self.panels)

      # adjust panel to new position
      p.adjustPosition(x,y,w,h)
      # if this panel has panels, pass them the change in position
      if len(p.panels) > 0:
        p.rePackPanels(x,y,w,h)
