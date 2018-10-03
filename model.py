from jsonHandler import JsonHandler, MyEncoder
import sys
import pprint
import json
import tkinter.messagebox
import tkinter as tk
from screen import Screen
from panel import Panel

class Model:
  def __init__(self,gui):
    self.screens = []
    self.max_width = 0
    self.max_height = 0
    self.n_panels   = 0
    self.gui = gui
    self.currentPanelShareID = 0;
    # options
    self.defaultConfigFile = 'defaultConfig.json'
    self.options = JsonHandler().importFile( self.defaultConfigFile )
    self.convertOptionsToStrings()


  def load(self):
    ''' opens a file dialog and loads it into the model '''
    fname = tk.filedialog.askopenfile( filetypes = (("json files","*.json"),("all files","*.*")) )
    if fname != None:
      self.options = JsonHandler().importFile(fname.name)
      self.gui.toggleOptionWindow(state='hide') # hide the window
      self.setupScreensFromFile()
      self.convertOptionsToStrings()
      self.gui.setupOptionsWindow() # remake the window, easiest thing to do
      self.gui.mainWindow.draw()
    else:
      print( 'file name was found to be null' )


  def save(self):
    ''' opens a file dialog and saves the model to a file '''
    fname = tk.filedialog.asksaveasfilename( filetypes = (("json files","*.json"),("all files","*.*")) )
    if fname != '':
      JsonHandler().exportFile( self, fname )
    else:
      print( 'file needs a name to save' )


  def getNextPanelShareID(self):
    ''' if panels are shared between nodes they need an id so they know who to share with,
    call this to get a new share id if the panel doesn't have one and the shared panels also don't have one '''
    self.currentPanelShareID += 1
    return self.currentPanelShareID


  def updateScreenSize(self,width,height):
    ''' sets all of the screens in the model to have a new size '''
    if len(self.screens) < 1:
      return

    x = 0
    y = 0
    # w = int( self.gui.mainWindow.canvasW / ( self.numNodes*self.numScreenColumns ) )
    w = int( width / len(self.screens) )
    h = int( w / ( self.aspectRatioScreensA / self.aspectRatioScreensB ) )

    if h*self.numScreenRows > height:
      overflow = (h*self.numScreenRows) - height
      h -= int( overflow/self.numScreenRows )
      w = h*( ( self.aspectRatioScreensA / self.aspectRatioScreensB ) )

    for screen in self.screens:
      screen.x = x
      screen.y = y
      screen.width = w
      screen.height = h
      x += w


  def setupScreensFromFile(self):
    try:
      if self.options['screens'] != None:
        data = self.options['screens']
        n_per_slave = int( self.options['n_per_slave'] )
        n_rows = int( self.options['n_rows'] )
        n_cols = int( self.options['n_cols'] )
        numNodes = len( data )
        self.createScreens(numNodes,n_rows,n_cols)
        i = 0 # current screen index
        for nKey,nValue in data.items():
          # print( 'nKey: ' + str(nKey) + ', nValue: ' + str(nValue) ) # for each screen in the file
          screen = self.screens[i] # current screen
          for pKey,pValue in nValue.items():
            # print('x ' + str( pValue['dimensions'][0] ) + ' y ' + str( pValue['dimensions'][1] ) + ' w ' + str( pValue['dimensions'][2] ) + ' h ' + str( pValue['dimensions'][3] ))
            dim = pValue['dimensions']
            x1 = dim[0]
            y1 = dim[3]
            x2 = dim[2]
            y2 = dim[1]

            x = x1
            y = y1
            w = x2 - x1
            h = y2 - y1

            # print('x ' + str(x) + ' y ' + str(y) + ' w ' + str(w) + ' h ' + str(h))

            p = Panel(
              screen=screen,
              canvas=screen.canvas,
              ident="0",
              method='c',
              x=x,
              y=y,
              width=w,
              height=h,
              mode=pValue['type']
            )
            screen.panels.append( p )
          i += 1

    except Exception as e:
      print(e)
      # pass


  def convertOptionsToStrings(self):
    ''' convert all options to a string (clean) so they can be put into a text area for user to edit '''
    for key,value in self.options.items():
      if isinstance(value,str):
        pass
      elif isinstance(value,list):
        self.options[key] = str(value)
      elif isinstance(value,dict):
        pass
      elif isinstance(value,bool):
        if value:
          self.options[key] = 'true'
        else:
          self.options[key] = 'false'
      elif isinstance(value,int):
        pass
        # self.options[key] = '"' + str(value) + '"'
      elif isinstance(value,float):
        pass
        # self.options[key] = '"' + str(value) + '"'
      elif isinstance(value,complex):
        pass
        # self.options[key] = '"' + str(value) + '"'


  def screensToArray(self):
    ''' returns screen data as a dictionary '''
    screens = dict()
    for (index, screen) in enumerate(self.screens):
        screens['n'+str(index)] = screen.toDimensionArray()
    return screens

  def addOption(self,key,value):
    ''' adds key and value to options '''
    self.options.update( {key:value} )

  def updateOption(self,uKey,uValue):
    ''' finds matching key and sets new value in options '''
    # print('update called')
    for key,value in self.options.items():
      if key == uKey:
        self.options[key] = uValue
        # print( str(key) + ' == ' + str(uKey) )
        # print( 'updating to ' + str(uValue) )
        # value = uValue


  def removeOption(self,key):
    ''' finds matching key and removes it from options '''
    r = dict( self.options )
    del r[key]
    self.options = r

  def inOptions(self,item):
    ''' finds if given key is contained in options '''
    for key,value in self.options.items():
      if key == item:
        return True
    return False

  def printOptions(self):
    ''' prints all options to console '''
    print('---------------------')
    print('All Options:')
    for k,v in self.options.items():
      print( 'K: ' + str(k) + ', v: ' + str(v) )
    print('---------------------')

  def toJson(self):
    ''' creates a json sting to save to file '''
    data = '{\n'
    out_screens = self.screensToArray()
    for key,value in self.options.items():
      if key != 'screens':
        d = self.processVar( str(value) )
        data += '  "' + str(key) + '": ' + d + ',\n'
    try:
      data += '  "screens":' + json.dumps(out_screens, cls=MyEncoder, sort_keys=False, indent=2)
    except TypeError:
      tkinter.messagebox.showerror(title='Configuration Error', message='No screens were added to this configuration')
    data += '\n}'
    data = data.replace("'", '"')
    return data

  def processVar(self,d):
    ''' creates if value has to be modified when converted to string '''
    if d == '': return '""'
    if d.startswith('['): return d
    if d.startswith('{'): return d
    if d.startswith('('): return d
    if d.lower() == 'false': return str(False).lower()
    if d.lower() == 'true': return str(True).lower()
    if self.checkInt(d): return str(d)
    return '"' + str(d) + '"'

  def checkInt(self,s):
    ''' returns true if given string is a digit '''
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


  def createScreen(self, color):
    self.screens.append( Screen(self, self.gui.mainWindow.canvas, "Screen", 0, 0, 0, 0, "#3d3d3d", color) )


  def createScreens(self,numNodes,numScreenRows,numScreenColumns,aspectRatioScreensA=16,aspectRatioScreensB=9):  # read AxB, 16x9
    self.screens = []
    self.numNodes = numNodes
    self.numScreenRows = numScreenRows
    self.numScreenColumns = numScreenColumns

    # read AxB, 16x9
    self.aspectRatioScreensA = aspectRatioScreensA * numScreenColumns
    self.aspectRatioScreensB = aspectRatioScreensB * numScreenRows

    x = 0
    y = 0
    # w = int( self.gui.mainWindow.canvasW / ( self.numNodes*self.numScreenColumns ) )
    w = int( self.gui.mainWindow.canvasW / self.numNodes )
    h = int( w / ( self.aspectRatioScreensA / self.aspectRatioScreensB ) )

    if h*self.numScreenRows > self.gui.mainWindow.canvasH:
      overflow = (h*self.numScreenRows) - self.gui.mainWindow.canvasH
      h -= int( overflow/self.numScreenRows )
      w = h*( ( self.aspectRatioScreensA / self.aspectRatioScreensB ) )

    for node in range( self.numNodes ):
      # make screen for each node
      screen = Screen(self, self.gui.mainWindow.canvas, "Screen", x, y, w, h, "#3d3d3d", "#3366FF")
      # make panel for each self.numScreenRows
      screen.divideHorizontally(self.numScreenRows)

      # make panel for each self.numScreenColumns
      # panel removes itself from screen when dividing so can't loop through that
      pans = []
      for col in screen.panels:
        pans.append(col)

      for col in pans:
        col.divideVertically( self.numScreenColumns )


      self.screens.append( screen )
      x += w

    self.gui.mainWindow.draw()

  def countScreensPanels(self):
    cS = 0
    cP = 0

    for screen in self.screens:
      cS += 1
      cP += screen.countPanels()

    print('Screens: ' + str(cS))
    print('Panels: ' + str(cP))
