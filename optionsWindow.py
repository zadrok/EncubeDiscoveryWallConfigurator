import tkinter as tk
from menuBar import MBOptions

class OptionsWindow(tk.Toplevel):
  def __init__(self,root,gui):
    ''' creates options window, all model options are displayed here '''
    super().__init__(root)
    self.root = root
    self.protocol('WM_DELETE_WINDOW', self.withdraw)
    self.gui = gui
    self.grid()

    self.createWidgets()

  def createWidgets(self):
    ''' sets up components for user to interact with '''
    # menu bar
    self.menuBar = MBOptions(self)
    # options
    self.items = []
    self.i = 0
    self.j = 0
    self.max = 30
    self.side = 11
    for key,value in self.gui.model.options.items():
      if self.i > self.max:
        self.i = 0
        self.j += self.side
      self.items.append( Item( self, self.i, self.j, str(key), str(value) ) )
      self.i += 1

    self.refreshValues()

    # window used to create options
    self.addOptionsWindow = AddOptionsWindow(self)
    self.addOptionsWindow.withdraw()

  def toggleAddOptionWindow(self,state=None):
    ''' shows and hides the add options window.
        state=<hide/show> '''
    # check if state specified
    if state != None:
      if state == 'hide':
        self.addOptionsWindow.withdraw()
      elif state == 'show':
        self.addOptionsWindow.deiconify()
    # if None state then toggle
    if self.addOptionsWindow.state() == 'normal':
      self.addOptionsWindow.withdraw()
    elif self.addOptionsWindow.state() == 'withdrawn':
      self.addOptionsWindow.deiconify()

  def commitOption(self):
      ''' takes values in add options window and adds item '''
      key = self.addOptionsWindow.KEYentryVar.get()
      value = self.addOptionsWindow.VALUEentryVar.get()
      # add option to model.options
      self.gui.model.addOption(key,value)
      # create item
      self.items.append( Item( self, self.i+1, self.j, str(key), str(value) ) )
      # hide window
      self.toggleAddOptionWindow()
      # reGrid Items
      self.reGridItems()

  def refreshValues(self):
    ''' checks all options and makes sure items displayed match '''
    # change options or add new ones
    for key,value in self.gui.model.options.items():
      # find option
      if self.getItem(key) != None:
        self.getItem(key).entryVar.set(value)
      else:
        # add this as a new option
        if self.i > self.max:
          self.i = 0
          self.j += self.side
        self.items.append( Item( self, self.i, self.j, str(key), str(value) ) )
        self.i += 1
    # remove old item if not needed
    for itm in self.items:
      if not self.gui.model.inOptions(itm.key):
        itm.destroy()
        self.items.remove(itm)
    # make sure there are no gapes between items
    self.reGridItems()

  def reGridItems(self):
    ''' all items are placed in the grid '''
    self.i = 0
    self.j = 0
    self.max = 30
    self.side = 11
    for item in self.items:
      if self.i > self.max:
        self.i = 0
        self.j += self.side
      item.reGrid(self.i,self.j)
      self.i += 1

  def getItem(self,item):
    ''' returns item with same key '''
    for i in self.items:
      if i.key == item: return i
    return None

  def removeItem(self,item):
    ''' removes item with same key '''
    self.gui.model.removeOption(item.key)
    self.refreshValues()

class Item:
  def __init__(self,optionsWindow,i,j,key,value):
    ''' item repersenting options '''
    self.optionsWindow = optionsWindow
    self.i = i
    self.j = j
    self.key = key
    self.value = value

    self.entryVar = tk.StringVar()
    self.entryVar.set( str(self.value) )
    self.entryVar.trace('w', self.callback)
    self.label = tk.Label(self.optionsWindow, text=str(self.key))
    self.entry = tk.Entry(self.optionsWindow, textvariable=self.entryVar, width=30)

    self.removeBttn = tk.Button(self.optionsWindow,text='X',command=self.delete,bg="indianRed1")

    self.label.grid(row=i,column=j)
    self.entry.grid(row=i,column=j+1)
    self.removeBttn.grid(row=i,column=j+2)

  def delete(self):
    ''' delets this item '''
    self.optionsWindow.removeItem(self)

  def callback(self,*args):
    ''' updates this options in the model '''
    self.optionsWindow.gui.model.updateOption( self.key, self.entryVar.get() )

  def reGrid(self,i,j):
    ''' places this items at given position '''
    self.label.grid(row=i,column=j)
    self.entry.grid(row=i,column=j+1)
    self.removeBttn.grid(row=i,column=j+2)

  def destroy(self):
    ''' removes this items companents '''
    self.label.destroy()
    self.entry.destroy()
    self.removeBttn.destroy()


class AddOptionsWindow(tk.Toplevel):
  def __init__(self,optionsWindow):
    ''' creates add options window, allows new options to be created here '''
    super().__init__(optionsWindow.root)
    self.optionsWindow = optionsWindow
    self.title("Add Option")
    self.protocol('WM_DELETE_WINDOW', self.withdraw)
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    ''' sets up companents for user to interact with '''
    # key
    self.KEYentryVar = tk.StringVar()
    self.KEYentryVar.set( '' )
    self.KEYlabel = tk.Label(self, text='Key')
    self.KEYentry = tk.Entry(self, textvariable=self.KEYentryVar, width=30)

    self.KEYlabel.grid()
    self.KEYentry.grid()

    # value
    self.VALUEentryVar = tk.StringVar()
    self.VALUEentryVar.set( '' )
    self.VALUElabel = tk.Label(self, text='Value')
    self.VALUEentry = tk.Entry(self, textvariable=self.VALUEentryVar, width=30)

    self.VALUElabel.grid()
    self.VALUEentry.grid()

    # done button
    self.doneBttn = tk.Button(self,text='Commit',command=self.optionsWindow.commitOption)
    self.doneBttn.grid()
