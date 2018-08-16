from jsonHandler import JsonHandler
import sys
import pprint
import tkinter.messagebox

class Model:
  def __init__(self):
    self.screens = []
    self.panels = []
    self.max_width = 0
    self.max_height = 0
    self.n_panels   = 0
    # options
    self.defaultConfigFile = 'defaultConfig.json'
    self.options = JsonHandler().importFile(self.defaultConfigFile)

  def set_screens(self, screens, width, height):
    self.screens = screens
    self.max_height = height
    self.max_width = width

  def panel_to_array(self, panel):
    ret = []

    if len(panel.panels) > 0:
      for sub_panel in panel.panels:
        ret.append(self.panel_to_array(sub_panel))
    else:
      ret = self.calculate_area(panel)

    return ret

  def screens_to_array(self):
    screens = []
    for screen in self.screens:
        screens.append(screen.to_dimension_array())

    return screens

  def calculate_area(self, panel):
    px1 = panel.get_x()
    py1 = panel.get_y()
    px2 = panel.get_width()
    py2 = panel.get_height()

    nx1 = px1 / self.max_width
    nx2 = nx1 + (px2 / self.max_width)
    # Because S2PLOT uses a reversed coordinate system, we need to transform our coords
    # eg. 0.25 in a tkInter Canvas becomes 0.75 on a S2PLOT XY system.
    ny1 = py1 / self.max_height
    ny2 = ny1 + (py2 / self.max_height)

    return [nx1, ny1, nx2, ny2]

  def addOption(self,key,value):
    ''' adds key and value to options '''
    self.options.update( {key:value} )

  def updateOption(self,uKey,uValue):
    ''' finds matching key and sets new value in options '''
    # print('update called')
    for key,value in self.options.items():
      if key == uKey:
        # print( str(key) + ' == ' + str(uKey) )
        self.options[key] = uValue
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


  def open(self,fname):
    ''' calls jsonHandler.importFile and sets options to returned value '''
    self.options = JsonHandler().importFile( fname )

  def save(self,fname):
    ''' calls jsonHandler.exportFile and passes it options to save '''
    JsonHandler().exportFile( self, fname )

  def toJson(self):
    ''' creates a json sting to save to file '''
    data = '{\n'
    out_screens = self.screens_to_array()
    for key,value in self.options.items():
        d = self.processVar( str(value) )
        data += '  "' + str(key) + '": ' + d + ',\n'
    try:
      data += '  "screens":' + pprint.pformat(out_screens)
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

    if self.check_int(d): return str(d)

    return '"' + str(d) + '"'

  def check_int(self,s):
    ''' returns true if given string is a digit '''
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
