

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
    self.reset()

  def setPanelsMode(self, mode):
    for p in self.panels:
      p.mode = mode
    self.deselectAll()
    self.window.draw()

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
    panel = screen.getPanelAtXY(x,y)

    # if panel != None: print( 'x ' + str(panel.x) + ', y ' + str(panel.y) + ', w ' + str(panel.width) + ', h ' + str(panel.height) )

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
      s.divideHorizontally(num=self.window.buttonWidget.splitNumber)
    for p in self.panels:
      p.divideHorizontally(num=self.window.buttonWidget.splitNumber)


  def splitVertically(self):
    for s in self.screens:
      s.divideVertically(num=self.window.buttonWidget.splitNumber)
    for p in self.panels:
      p.divideVertically(num=self.window.buttonWidget.splitNumber)






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

      # TODO - Split panels into 'zones'/'groups' within each screen
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

      # cI = 0
      # for group in panelGroups:
      #   colors = ['gold', 'hot pink', 'khaki1', 'tomato2', 'magenta3', 'SeaGreen1', 'slate blue', 'ivory2', 'OrangeRed2', 'plum2', 'DarkOliveGreen2', 'purple', 'pink1', 'forest green', 'navy']
      #   color = colors[cI]
      #   cI += 1
      #   if cI >= len(colors): cI = 0
      #   for panel in group:
      #     panel.colorOther = color


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

        # print('xMin ' + str(int(xMin)) + ', yMin ' + str(int(yMin)) + ', wMax ' + str(int(wMax)) + ', hMax ' + str(int(hMax)))
        # print('xMin ' + str(xMin) + ', yMin ' + str(yMin) + ', wMax ' + str(wMax) + ', hMax ' + str(hMax))

        # go through all panels marked as join (in the join list)
        for panel in group:
          # remove the panel
          aScreen.panels.remove(panel)

        # create the new panel
        aScreen.createPanel(method='n', x=xMin, y=yMin, width=wMax, height=hMax)




  def panelShareEdge(self,panelA,panelB):
    # create vertices
    verticesA = self.getPanelVertices(panelA)
    verticesB = self.getPanelVertices(panelB)

    # print( 'verticesA: 0 ' + str(verticesA[0][0]) + ', ' + str(verticesA[0][1]) +
    #        '     1 ' + str(verticesA[1][0]) + ', ' + str(verticesA[1][1]) +
    #        '     2 ' + str(verticesA[2][0]) + ', ' + str(verticesA[2][1]) +
    #        '     3 ' + str(verticesA[3][0]) + ', ' + str(verticesA[3][1]) )
    #
    # print( 'verticesB: 0 ' + str(verticesB[0][0]) + ', ' + str(verticesB[0][1]) +
    #        '     1 ' + str(verticesB[1][0]) + ', ' + str(verticesB[1][1]) +
    #        '     2 ' + str(verticesB[2][0]) + ', ' + str(verticesB[2][1]) +
    #        '     3 ' + str(verticesB[3][0]) + ', ' + str(verticesB[3][1]) )

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
    vertices = []
    vertices.append( [panel.x, panel.y] )
    vertices.append( [panel.x + panel.width, panel.y] )
    vertices.append( [panel.x, panel.y + panel.height] )
    vertices.append( [panel.x + panel.width, panel.y + panel.height] )
    return vertices


  def getGroupVertices(self,group):
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

    # print('xMin ' + str(xMin) + ', yMin ' + str(yMin) + ', wMax ' + str(wMax) + ', hMax ' + str(hMax))

    vertices.append( [xMin, yMin] )
    vertices.append( [xMin + wMax, yMin] )
    vertices.append( [xMin, yMin + hMax] )
    vertices.append( [xMin + wMax, yMin + hMax] )
    return vertices



  def groupShareEdge(self,groupA,groupB):
    # create vertices
    verticesA = self.getGroupVertices(groupA)
    verticesB = self.getGroupVertices(groupB)

    # print( 'verticesA: 0 ' + str(verticesA[0][0]) + ', ' + str(verticesA[0][1]) +
    #        '     1 ' + str(verticesA[1][0]) + ', ' + str(verticesA[1][1]) +
    #        '     2 ' + str(verticesA[2][0]) + ', ' + str(verticesA[2][1]) +
    #        '     3 ' + str(verticesA[3][0]) + ', ' + str(verticesA[3][1]) )
    #
    # print( 'verticesB: 0 ' + str(verticesB[0][0]) + ', ' + str(verticesB[0][1]) +
    #        '     1 ' + str(verticesB[1][0]) + ', ' + str(verticesB[1][1]) +
    #        '     2 ' + str(verticesB[2][0]) + ', ' + str(verticesB[2][1]) +
    #        '     3 ' + str(verticesB[3][0]) + ', ' + str(verticesB[3][1]) )

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
    # for each selected panel
    keepLooping = True
    loop = 0
    maxLoop = 10
    while loop < maxLoop:
      loop += 1
      for p in self.panels:
        # print( 'x ' + str(p.getX()) + ' y ' + str(p.getY()) + ' w ' + str(p.getWidth()) + ' h ' + str(p.getHeight()) )
        # expand the panel in each direction until it collides with another panel or the side of the screen
        self.panelExpandUp(p)
        self.panelExpandDown(p)
        self.panelExpandLeft(p)
        self.panelExpandRight(p)


  def valueInRange(self, value, min, max):
    return (value >= min) and (value <= max)


  def rectOverlap(self, A, B):
    xOverlap = self.valueInRange(A.x, B.x, B.x + B.width) or self.valueInRange(B.x, A.x, A.x + A.width);
    yOverlap = self.valueInRange(A.y, B.y, B.y + B.height) or self.valueInRange(B.y, A.y, A.y + A.height);
    # print(xOverlap and yOverlap)
    return xOverlap and yOverlap;


  def panelIntersectionOtherPanels(self, pan, panels):
    for p in panels:
      if p != pan and self.rectOverlap(pan, p):
        # p.colorOther = "#333300"
        # print('panel Intersection')
        return True
    # print('no panel Intersection')
    return False


  def panelInScreen(self,panel,screen):
    if panel.getX() >= screen.getX():
      if panel.getY() >= screen.getY():
        if panel.getX()+panel.getWidth() <= screen.getX()+screen.getWidth():
          if panel.getY()+panel.getHeight() <= screen.getY()+screen.getHeight():
            # print('panel in screen')
            return True
    # print('panel not in screen')
    return False


  def panelExpandUp(self, panel):
    # while panel doesn't go out of th screen and, while the panel doesn't overlap another panel
    # print('Up')
    while self.panelInScreen( panel, panel.screen ) and not self.panelIntersectionOtherPanels(panel,panel.screen.panels):
      panel.y -= 1
      panel.height += 1
    # back off one pixel so panels arn't on top of each other
    panel.y += 1
    panel.height -= 1


  def panelExpandDown(self, panel):
    # while panel doesn't go out of th screen and, while the panel doesn't overlap another panel
    # print('Down')
    while self.panelInScreen( panel, panel.screen ) and not self.panelIntersectionOtherPanels(panel,panel.screen.panels):
      panel.height += 1
    # back off one pixel so panels arn't on top of each other
    panel.height -= 1


  def panelExpandLeft(self, panel):
    # while panel doesn't go out of th screen and, while the panel doesn't overlap another panel
    # print('Left')
    while self.panelInScreen( panel, panel.screen ) and not self.panelIntersectionOtherPanels(panel,panel.screen.panels):
      panel.x -= 1
      panel.width += 1
    # back off one pixel so panels arn't on top of each other
    panel.x += 1
    panel.width -= 1


  def panelExpandRight(self, panel):
    # while panel doesn't go out of th screen and, while the panel doesn't overlap another panel
    # print('Right')
    while self.panelInScreen( panel, panel.screen ) and not self.panelIntersectionOtherPanels(panel,panel.screen.panels):
      panel.width += 1
    # back off one pixel so panels arn't on top of each other
    panel.width -= 1







  def initialPanel(self):
    for s in self.screens:
      s.createPanel("C", s.getX(), s.getY(), s.width, s.height)


  def reset(self):
    self.allselect()
    self.remove()
    self.deselectAll()
    self.allselect()
    self.initialPanel()

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
