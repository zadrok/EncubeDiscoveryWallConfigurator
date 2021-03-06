import tkinter as tk
import platform
from selectionController import selcon

# all keysyms that need to be tracked
keysyms = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8',
        '9','0', 'space', 'Control_L', 'Shift_L' ]


class KeyHandeler:
  def __init__(self,root,mainWindow):
    '''key handeler for user interface configuration tool'''
    self.root = root
    self.mainWindow = mainWindow
    self.root.bind("<KeyRelease>", self.keyUp)
    self.root.bind("<KeyPress>", self.keyDown)

    #if platform.system() == "Linux":
    #   self.root.bind("<Button-4>", self.onMouseWheelLinux)
    #    self.root.bind("<Button-5>", self.onMouseWheelLinux)
    #else:
    #    self.root.bind('<MouseWheel>', self.onMouseWheel)

    # needed to make sure key events only happen once
    self.keyMemory = {}
    for k in keysyms:
      self.keyMemory.update( {k:False} )

    # tell selcon about this
    selcon.setKeyHandeler(self)


  def onMouseWheelLinux(self, event):
    ''' what sould happen when mouse wheel is used on linux '''
    if event.num == 4:
      self.mainWindow.controlPanel.IncreaseSplitNum()
    elif event.num == 5:
      self.mainWindow.controlPanel.DecreaseSplitNum()


  def onMouseWheel(self, event):
    ''' what sould happen when mouse wheel is used '''
    if event.delta > 0:
      self.mainWindow.controlPanel.IncreaseSplitNum()
    elif event.delta < 0:
      self.mainWindow.controlPanel.DecreaseSplitNum()


  def doEventUp(self,keySym):
    ''' do this when a key is released '''
    # print('Doing up event ' + keySym)
    self.mainWindow.draw()


  def doEventDown(self,keySym):
    ''' do this when a key is pressed '''
    # print('Doing down event ' + keySym)
    # pick and action
    if keySym == '1':
      selcon.splitHorizontally()
      selcon.deselectAll()
    if keySym == '2':
      selcon.splitVertically()
      selcon.deselectAll()
    if keySym == '3':
      selcon.join()
      selcon.deselectAll()
    if keySym == '4':
      selcon.remove()
      selcon.deselectAll()
    if keySym == '5':
      selcon.deselectAll()
    if keySym == '6':
      selcon.allselect()
    if keySym == '7':
      pass # just redraw
    if keySym == '8':
      selcon.fillGap()
    if keySym == 'c':
      self.mainWindow.countScreensPanels()

    self.mainWindow.draw()


  def keySafe(self,key):
    ''' return true if key in key memory
    @return boolean true if the key is in memory
    '''
    for k,v in self.keyMemory.items():
      if k == key: return True
    return False


  def keyUp(self,e):
    ''' do this when a key is released '''
    # print('up ' + str(e.keysym))
    # exit if key not in memory
    if not self.keySafe(str(e.keysym)): return

    # do key action and remove from memory
    if self.keyMemory[ str(e.keysym) ]:
      # key let go
      # do event
      self.doEventUp(str(e.keysym))
      self.keyMemory[ str(e.keysym) ] = False
    else:
      # not sure how this would happen
      pass


  def keyDown(self,e):
    ''' do this when a key is pressed '''
    # print('down ' + str(e.keysym))
    # exit if key not in memory
    if not self.keySafe(str(e.keysym)): return

    # do key action and add to memory
    if self.keyMemory[ str(e.keysym) ]:
      # key is alreay down
      pass
    else:
      # key just pressed
      # do event
      self.doEventDown(str(e.keysym))
      self.keyMemory[ str(e.keysym) ] = True
