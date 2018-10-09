import random
import math

class SelectionController:
  def __init__(self):
    # selected screens and panels
    self.screens = []
    self.panels = []

    self.keyHandeler = None
    self.mainWindow = None

  def setKeyHandeler(self,kh):
    '''give the SelectionController a reference to a keyHandeler'''
    self.keyHandeler = kh

  def setMainWindow(self,w):
    '''give the SelectionController a reference to a mainWindow'''
    self.mainWindow = w
    self.reset()

  def setPanelsMode(self, mode):
    '''for all of the selected panels set their mode to "mode"'''
    for p in self.panels:
      p.mode = mode
    self.deselectAll()
    self.mainWindow.draw()

  def deselect(self,screen,panel):
    '''remove the "screen" and/or "panel" from the selected list'''
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
    '''
      decides on actions to take when a screen is clicked, if a panel is clicked
      and to select the screen or panel or to deselect
      - x : click event x locatoin
      - y : click event y locatoin
      - screen : the screen that was clicked on
    '''
    panel = screen.getPanelAtXY(x,y)
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
          # print( "x " + str(panel.getX()) + ", y " + str(panel.getY()) + ", w " + str(panel.getWidth()) + ", h " + str(panel.getHeight()) )
        else:
          self.clearAll()
          self.screens.append( screen )

  def screenHighlighted(self,x,y,screen):
    '''
      decides on actions to take when a screen is clicked, if a panel is clicked
      and to select the screen or panel or to deselect
      - x : click event x locatoin
      - y : click event y locatoin
      - screen : the screen that was clicked on
    '''
    panel = screen.getPanelAtXY(x,y)
    # check if this is a deselect
    if not self.deselect(screen,panel):
      # select it
        if panel != None:
          self.panels.append( panel )
        else:
          self.screens.append( screen )


  def splitHorizontally(self):
    '''splits selected screen/panels a number of times horizontally set by the split amount'''
    for s in self.screens:
      s.divideHorizontally(num=self.mainWindow.controlPanel.splitNumber)
    for p in self.panels:
      p.divideHorizontally(num=self.mainWindow.controlPanel.splitNumber)
    self.clearAll()


  def splitVertically(self):
    '''splits selected screen/panels a number of times vertically set by the split amount'''
    for s in self.screens:
      s.divideVertically(num=self.mainWindow.controlPanel.splitNumber)
    for p in self.panels:
      p.divideVertically(num=self.mainWindow.controlPanel.splitNumber)
    self.clearAll()



  def removelinksbetweenPanelsInDifferentNodes(self):
    for panel in self.panels:
      for p in panel.sharePanels:
        p.sharePanels.remove( panel )
      panel.sharePanels = []

    self.clearAll()
    self.mainWindow.draw()



  def joinWithOtherScreens(self):
    maxLoop = 100
    loop = 0
    while len(self.panels) > 1 and loop < maxLoop:
      loop += 1
      # primary panel
      for pPanel in self.panels:
        # secondary panel
        for sPanel in self.panels:
          # skip if same panel
          if pPanel == sPanel: continue
          # share edge?
          if self.panelShareEdge(pPanel,sPanel):
            if pPanel.screen != sPanel.screen:
              pPanel.addSharePanel( sPanel )
              sPanel.addSharePanel( pPanel )

    self.clearAll()
    self.mainWindow.draw()



  def join(self):
    '''for the selected panels, join ones that make a rectangle/square'''
    # go through all screens
    for aScreen in self.mainWindow.gui.model.screens:
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
      # only join panels that are next together and make a rectangle/square
      # jPanels <- all panels in this screen that want to join
      panelGroups = []
      while len(jPanels) > 1:
        curPanel = jPanels.pop()
        curGroup = []
        curGroup.append(curPanel)
        for pan in jPanels:
          if curPanel == jPanels:
            jPanels.remove(curPanel)
            # print('same panel, removing')
            continue
          if self.panelShareEdge(curPanel,pan):
            curGroup.append(pan)
            jPanels.remove(pan)
            break

        panelGroups.append(curGroup)

      join = True
      maxLoop = 100
      loop = 0
      while join and loop < maxLoop:
        join = False
        loop += 1
        for group in panelGroups:
          for otherGroup in panelGroups:
            if group == otherGroup: continue
            if self.groupShareEdge(group,otherGroup):
              newGroup = []
              newGroup.extend(group)
              newGroup.extend(otherGroup)
              panelGroups.remove(group)
              panelGroups.remove(otherGroup)
              panelGroups.append(newGroup)
              join = True
              break

      if loop >= maxLoop:
        print('exit due to loop max')

      for group in panelGroups:
        # find the bounding box for join panels
        xMin = min( group, key=lambda p: p.x )
        yMin = min( group, key=lambda p: p.y )
        wMax = max( group, key=lambda p: p.x + p.width )
        hMax = max( group, key=lambda p: p.y + p.height )

        xMin =  xMin.x
        yMin =  yMin.y
        wMax =  wMax.x + wMax.width - xMin
        hMax =  hMax.y + hMax.height - yMin

        # go through all panels marked as join (in the join list)
        for panel in group:
          # remove the panel
          aScreen.removePanel(panel)

        # create the new panel
        aScreen.createPanel(method='n', x=xMin, y=yMin, width=wMax, height=hMax)


  def panelShareEdge(self,panelA,panelB):
    '''return true if panelA and panelB share a edge'''
    # create vertices
    verticesA = self.getPanelVertices(panelA)
    verticesB = self.getPanelVertices(panelB)

    sameCount = 0
    for verA in verticesA:
      for verB in verticesB:
        if verA[0] == verB[0] and verA[1] == verB[1]:
          # print('match ' + str(sameCount))
          sameCount += 1
        if sameCount >= 2:
          return True

    return False

  def panelShareVertex(self,panelA,panelB):
    '''return true if panelA and panelB share a corner(vertex)'''
    # create vertices
    verticesA = self.getPanelVertices(panelA)
    verticesB = self.getPanelVertices(panelB)
    # go through all vertices and check if they match
    for verA in verticesA:
      for verB in verticesB:
        if verA[0] == verB[0] and verA[1] == verB[1]:
          return True

    return False


  def getPanelVertices(self,panel):
    '''returns an array/list of x,y points from each corner'''
    vertices = []
    vertices.append( [panel.x, panel.y] )
    vertices.append( [panel.x + panel.width, panel.y] )
    vertices.append( [panel.x, panel.y + panel.height] )
    vertices.append( [panel.x + panel.width, panel.y + panel.height] )
    return vertices


  def getGroupVertices(self,group):
    '''returns an array/list of x,y points for a group of panels'''
    vertices = []
    # find the bounding box for join panels
    xMin = min( group, key=lambda p: p.x )
    yMin = min( group, key=lambda p: p.y )
    wMax = max( group, key=lambda p: p.x + p.width )
    hMax = max( group, key=lambda p: p.y + p.height )

    xMin =  xMin.x
    yMin =  yMin.y
    wMax =  wMax.x + wMax.width - xMin
    hMax =  hMax.y + hMax.height - yMin

    vertices.append( [xMin, yMin] )
    vertices.append( [xMin + wMax, yMin] )
    vertices.append( [xMin, yMin + hMax] )
    vertices.append( [xMin + wMax, yMin + hMax] )
    return vertices


  def groupShareEdge(self,groupA,groupB):
    '''returns true if a group of panels share an edge with another group'''
    # create vertices
    verticesA = self.getGroupVertices(groupA)
    verticesB = self.getGroupVertices(groupB)

    sameCount = 0
    for verA in verticesA:
      for verB in verticesB:
        if verA[0] == verB[0] and verA[1] == verB[1]:
          # print('match ' + str(sameCount))
          sameCount += 1
        if sameCount >= 2:
          return True

    return False


  def fillGap(self):
    '''for each selected panel, checks to see if it can expand in any direction to fill a gap'''
    # for each selected panel
    keepLooping = True
    loop = 0
    maxLoop = 10
    while loop < maxLoop:
      loop += 1
      for p in self.panels:
        # expand the panel in each direction until it collides with another panel or the side of the screen
        self.panelExpandUp(p)
        self.panelExpandDown(p)
        self.panelExpandLeft(p)
        self.panelExpandRight(p)


  def valueInRange(self, value, min, max):
    '''returns true if value is >= min and value is <= max'''
    return (value >= min) and (value <= max)


  def rectOverlap(self, A, B):
    ''' returns true if the rectangle of A and B overlap 
        A, B panels'''
    x1, y1, w1, h1 = A.getRect()
    x2, y2, w2, h2 = B.getRect()
    xOverlap = self.valueInRange(x1, x2, x2 + w2) or self.valueInRange(x2, x1, x1 + w1)
    yOverlap = self.valueInRange(y1, y2, y2 + h2) or self.valueInRange(y2, y1, y1 + h1)
    return xOverlap and yOverlap

  def selectionOverlap(self, A, B):
    ''' returns true if the rectangle of A and B overlap.
        A, B tuples'''
    x1, y1, w1, h1 = A
    x2, y2, w2, h2 = B
    xOverlap = self.valueInRange(x1, x2, x2 + w2) or self.valueInRange(x2, x1, x1 + w1)
    yOverlap = self.valueInRange(y1, y2, y2 + h2) or self.valueInRange(y2, y1, y1 + h1)
    return xOverlap and yOverlap

  def panelIntersectionOtherPanels(self, pan, panels):
    '''returns true 'pan' overlaps and panel in 'panels'''
    for p in panels:
      if p != pan and self.rectOverlap(pan, p):
        return True
    return False


  def panelInScreen(self,panel,screen):
    '''returns true if 'panel' is in 'screen'''
    x,y,w,h = panel.getRect()
    if x >= screen.getX():
      if y >= screen.getY():
        if x+w <= screen.getX()+screen.getWidth():
          if y+h <= screen.getY()+screen.getHeight():
            return True
    return False


  def panelExpandUp(self, panel):
    '''trys to expand a panel up'''
    # expaned by one pixel per loop, workout what one pixel equals to in this screen
    pixel = 1 / panel.screen.getHeight()
    # while panel doesn't go out of th screen and, while the panel doesn't overlap another panel
    while self.panelInScreen( panel, panel.screen ) and not self.panelIntersectionOtherPanels(panel,panel.screen.panels):
      panel.y -= pixel
      panel.height += pixel
    # back off one pixel so panels arn't on top of each other
    panel.y += pixel
    panel.height -= pixel


  def panelExpandDown(self, panel):
    '''trys to expand a panel down'''
    # expaned by one pixel per loop, workout what one pixel equals to in this screen
    pixel = 1 / panel.screen.getHeight()
    # while panel doesn't go out of th screen and, while the panel doesn't overlap another panel
    while self.panelInScreen( panel, panel.screen ) and not self.panelIntersectionOtherPanels(panel,panel.screen.panels):
      panel.height += pixel
    # back off one pixel so panels arn't on top of each other
    panel.height -= pixel


  def panelExpandLeft(self, panel):
    '''trys to expand a panel left'''
    # expaned by one pixel per loop, workout what one pixel equals to in this screen
    pixel = 1 / panel.screen.getWidth()
    # while panel doesn't go out of th screen and, while the panel doesn't overlap another panel
    while self.panelInScreen( panel, panel.screen ) and not self.panelIntersectionOtherPanels(panel,panel.screen.panels):
      panel.x -= pixel
      panel.width += pixel
    # back off one pixel so panels arn't on top of each other
    panel.x += pixel
    panel.width -= pixel


  def panelExpandRight(self, panel):
    '''trys to expand a panel right'''
    # expaned by one pixel per loop, workout what one pixel equals to in this screen
    pixel = 1 / panel.screen.getWidth()
    # while panel doesn't go out of th screen and, while the panel doesn't overlap another panel
    while self.panelInScreen( panel, panel.screen ) and not self.panelIntersectionOtherPanels(panel,panel.screen.panels):
      panel.width += pixel
    # back off one pixel so panels arn't on top of each other
    panel.width -= pixel


  def initialPanel(self):
    '''creates a single panel in each screen'''
    for s in self.screens:
      # s.createPanel("C", s.getX(), s.getY(), s.width, s.height)
      s.divideHorizontally(num=2)


  def reset(self):
    '''removes all panels from all screens and gives each screen one panel'''
    self.allselect()
    self.remove()
    self.deselectAll()
    self.allselect()
    self.initialPanel()

  def remove(self):
    '''remove all selected panels'''
    if self.mainWindow != None:
      for p in self.panels:
        p.screen.removePanel(p)

  def deselectAll(self):
    '''clear selected screens and panels lists'''
    self.clearAll()

  def allselect(self):
    '''add all screens and panels to selected lists'''
    self.clearAll()
    if self.mainWindow != None:
      for s in self.mainWindow.gui.model.screens:
        if len(s.panels) <= 0:
          self.screens.append( s )
        else:
          for p in s.panels:
            self.panels.append( p )

  def selectedArea(self, selectedRect):
    for p in self.panels:
      print('Height:'+ str(p.getHeight()) + ' Width:'+str(p.getWidth()))
      #self.rectOverlap(selectedRect, p)


  def panelSelected(self,panel):
    '''returns true if panel is in selected list'''
    for p in self.panels:
      if p == panel:
        return True
    return False

  def screenSelected(self,screen):
    '''returns true if screen is in selected list'''
    for s in self.screens:
      if s == screen:
        return True
    return False

  def clearAll(self):
    '''clear selected screens and panels lists'''
    self.clearPanels()
    self.clearScreens()

  def clearPanels(self):
    '''clear selected panels list'''
    self.panels = []

  def clearScreens(self):
    '''clear selected screens list'''
    self.screens = []

  def appendPanel(self, p):
    '''add a passed in panel, p to the panels list'''
    self.panels.append(p)

selcon = SelectionController()
