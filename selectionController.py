

class SelectionController:
  def __init__(self):
    self.screens = []
    self.panels = []

    self.keyHandeler = None
    self.window = None

  def setKeyHandeler(self,kh):
    self.keyHandeler = kh

  def setWindow(self,w):
    self.window = w

  def screenClick(self,x,y,screen):
    panel = screen.get_panel_at_xy(x,y)
    if self.keyHandeler.keyMemory['Control_L'] or self.keyHandeler.keyMemory['Shift_L']:
      if panel != None:
        self.panels.append( panel )
      else:
        self.screens.append( screen )
    else:
      if panel != None:
        self.panels = []
        self.panels.append( panel )
      else:
        self.screens = []
        self.screens.append( screen )


  def splitHorizontally(self):
    # print('Split Horizontally')
    for s in self.screens:
      s.split_horizontally(s.x,s.y)
    for p in self.panels:
      p.screen.split_horizontally(p.x,p.y)

  def splitVertically(self):
    # print('Split Vertically')
    for s in self.screens:
      s.split_vertically(s.x,s.y)
    for p in self.panels:
      p.screen.split_vertically(p.x,p.y)

  def join(self):
    print('TODO Join')

  def remove(self):
    # print('Remove')
    if self.window != None:
      for p in self.panels:
        p.screen.panels.remove(p)

      for s in self.screens:
        self.window.screens.remove(s)

  def deselect(self):
    # print('Deselect')
    self.clearAll()

  def panelSelected(self,panel):
    for p in self.panels:
      if p == panel:
        return True
    return False

  def screenSelected(self,screen):
    for s in self.screens:
      if s == screen:
        return True
    return False

  def clearAll(self):
    self.clearPanels()
    self.clearScreens()

  def clearPanels(self):
    self.panels = []

  def clearScreens(self):
    self.screens = []

selcon = SelectionController()
