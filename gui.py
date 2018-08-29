import tkinter as tk

from mainWindow import MainWindow
from optionsWindow import OptionsWindow
from initSettingsWindow import InitSettingsWindow


class GUI():
  def __init__(self,model,jsonHandler):
    ''' creates a window handler for Tkinter windows '''
    self.model = model
    self.model.gui = self
    self.jsonHandler = jsonHandler

    # setup main window
    self.setupMainWindow()

    # setup options window
    # child of main window, will close when main does
    # can be hidden/closed without affecting main window
    self.setupOptionsWindow()

    # setup initilization settings window
    # child of main window, will close when main does
    # can be hidden/closed without affecting main window
    self.setupInitSettingsWindow()


  def setupMainWindow(self):
    self.widthMain = 1280
    self.heightMain = 720
    self.root = tk.Tk()
    self.root.title("Encube Discovery Wall Configurator")
    self.root.minsize(width=self.widthMain,height=self.heightMain)
    self.mainWindow = MainWindow(self,self.root)


  def setupOptionsWindow(self):
    self.widthOptions = 650
    self.heightOptions = 800
    self.optionsWindow = OptionsWindow(self.root,self)
    self.optionsWindow.title("Options")
    self.optionsWindow.minsize(width=self.widthOptions,height=self.heightOptions)
    # start with the options window hidden
    self.toggleOptionWindow(state='hide')


  def setupInitSettingsWindow(self):
    self.widthInitSettings = 400
    self.heightInitSettings = 600
    self.initSettingsWindow = InitSettingsWindow(self.root,self)
    self.initSettingsWindow.title("Init Settings")
    self.initSettingsWindow.minsize(width=self.widthInitSettings,height=self.heightInitSettings)
    # start with the options window hidden
    self.toggleinitSettingsWindow(state='show')


  def mainloop(self):
    ''' starts the main loop for the main window, where all other windows use as a root.
        run this to start the GUI '''
    self.mainWindow.mainloop()

  def toggleOptionWindow(self,state=None):
    ''' shows and hides the options window.
        state=<hide/show> '''
    # check if state specified
    if state != None:
      if state == 'hide':
        self.optionsWindow.withdraw()
      elif state == 'show':
        self.optionsWindow.deiconify()
    # if None state then toggle
    elif self.optionsWindow.state() == 'normal':
      self.optionsWindow.withdraw()
    elif self.optionsWindow.state() == 'withdrawn':
      self.optionsWindow.deiconify()


  def toggleinitSettingsWindow(self,state=None):
    ''' shows and hides the options window.
        state=<hide/show> '''
    # check if state specified
    if state != None:
      if state == 'hide':
        self.initSettingsWindow.withdraw()
      elif state == 'show':
        self.initSettingsWindow.deiconify()
    # if None state then toggle
    elif self.initSettingsWindow.state() == 'normal':
      self.initSettingsWindow.withdraw()
    elif self.initSettingsWindow.state() == 'withdrawn':
      self.initSettingsWindow.deiconify()
