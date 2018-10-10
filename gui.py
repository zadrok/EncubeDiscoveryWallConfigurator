import tkinter as tk
from tkinter import messagebox
from model import Model
from jsonHandler import JsonHandler
from mainWindow import MainWindow
from optionsWindow import OptionsWindow
from initSettingsWindow import InitSettingsWindow


class GUI():
  def __init__(self):
    ''' creates a window handler for Tkinter windows '''
    self.model = Model(self)
    self.jsonHandler = JsonHandler()

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
    ''' create the main window with title'''
    self.widthMain = 1280
    self.heightMain = 720
    self.root = tk.Tk()
    self.root.title("Encube Discovery Wall Configurator")
    # self.root.minsize(width=self.widthMain,height=self.heightMain)
    self.mainWindow = MainWindow(self,self.root)
    # create listener event, delete window to call closeEvent
    self.root.protocol("WM_DELETE_WINDOW", self.closeEvent)


  def setupOptionsWindow(self):
    ''' sets up the options GUI for editting the configuration file JSON option fields '''
    self.widthOptions = 650
    self.heightOptions = 400
    self.optionsWindow = OptionsWindow(self.root,self)
    self.optionsWindow.title("Options")
    self.optionsWindow.minsize(width=self.widthOptions,height=self.heightOptions)
    # start with the options window hidden
    self.toggleOptionWindow(state='hide')


  def setupInitSettingsWindow(self):
    ''' sets up the initial settings GUI for the number rows and columns per nodes '''
    self.widthInitSettings = 400
    self.heightInitSettings = 200
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


  def closeEvent(self):
    ''' query user if they trully do wish to close the window '''
    exitMsg = "Are you sure you wish to exit?"
    mExit = messagebox.askyesno(title="Quit", message=exitMsg)
    if mExit is True:
      # print('Exiting')
      self.root.destroy()
