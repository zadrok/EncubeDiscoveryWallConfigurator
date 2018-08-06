

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

  def deselect(self,screen,panel):
    try:
      if panel != None:
        # this is a panel and try to deselect it
        self.panels.remove(panel)
        return True
      else:
        # this is a screen and try to deselect it
        self.screens.remove(screen)
        return True

    except ValueError:
      return False

    return False

  def screenClick(self,x,y,screen):
    panel = screen.get_panel_at_xy(x,y)
    # check if this is a deselect
    if not self.deselect(screen,panel):
      # select it
      if self.keyHandeler.keyMemory['Control_L'] or self.keyHandeler.keyMemory['Shift_L']:
        if panel != None:
          self.panels.append( panel )
        else:
          self.screens.append( screen )
      else:
        if panel != None:
          self.clearAll()
          self.panels.append( panel )
        else:
          self.clearAll()
          self.screens.append( screen )

  def splitHorizontally(self):
    for s in self.screens:
      s.divideHorizontally(num=self.keyHandeler.getScrollCount())
    for p in self.panels:
      p.divideHorizontally(num=self.keyHandeler.getScrollCount())


  def splitVertically(self):
    for s in self.screens:
      s.divideVertically(num=self.keyHandeler.getScrollCount())
    for p in self.panels:
      p.divideVertically(num=self.keyHandeler.getScrollCount())

  def join(self):
    # TODO - make this work
    # print('TODO - Join')

    # go through all screens
    for aScreen in self.window.screens:
      # make a list of panels in the same screen to join together
      jPanels = []
      # go through each panel in the screen
      for asPanel in aScreen.panels:
        # go through all selected panels
        for sPanel in self.panels:
          # if these panels are the same add them to the list to join
          if asPanel == sPanel:
            jPanels.append(asPanel)
            # remove panel form selected list so it isn't checked again
            self.panels.remove(asPanel)

      # if there are no panels to join continue
      if len(jPanels) < 1: continue

      # find the bounding box for join panels
      xMin = min( jPanels, key=lambda p: p.x )
      yMin = min( jPanels, key=lambda p: p.y )
      wMax = max( jPanels, key=lambda p: p.x + p.width )
      hMax = max( jPanels, key=lambda p: p.y + p.height )

      xMin =  xMin.x
      yMin =  yMin.y
      wMax =  wMax.x + wMax.width - xMin
      hMax =  hMax.y + hMax.height - yMin

      # print('xMin ' + str(int(xMin)) + ', yMin ' + str(int(yMin)) + ', wMax ' + str(int(wMax)) + ', hMax ' + str(int(hMax)))
      # print('xMin ' + str(xMin) + ', yMin ' + str(yMin) + ', wMax ' + str(wMax) + ', hMax ' + str(hMax))

      # go through all panels marked as join (in the join list)
      for jPanel in jPanels:
        # remove the panel
        aScreen.panels.remove(jPanel)

      # create the new panel
      aScreen.createPanel(method='n', x=xMin, y=yMin, width=wMax, height=hMax)




  def remove(self):
    if self.window != None:
      for p in self.panels:
        p.screen.removePanel(p)

  def deselectAll(self):
    self.clearAll()

  def allselect(self):
    if self.window != None:
      for s in self.window.screens:
        if len(s.panels) <= 0:
          self.screens.append( s )
        else:
          for p in s.panels:
            self.panels.append( p )

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
