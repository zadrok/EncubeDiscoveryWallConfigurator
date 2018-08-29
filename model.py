from jsonHandler import JsonHandler
import sys
import pprint
import json
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

  def setScreens(self, screens, width, height):
    self.screens = screens
    self.max_height = height
    self.max_width = width

  def screensToArray(self):
    screens = dict()
    for (index, screen) in enumerate(self.screens, start=1):
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
    out_screens = self.screensToArray()
    for key,value in self.options.items():
        d = self.processVar( str(value) )
        data += '  "' + str(key) + '": ' + d + ',\n'
    try:
      data += '  "screens":' + json.dumps(out_screens, sort_keys=False, indent=2)
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

    if self.checkInt(d): return str(d)

    return '"' + str(d) + '"'

  def checkInt(self,s):
    ''' returns true if given string is a digit '''
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
