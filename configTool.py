import tkinter as tk
from gui import GUI

class Application:
  ''' Application
  The Application class is the main entry point into this configuration tool,
  it creates the gui.
  '''
  def __init__(self):
    ''' creates the GUI '''
    self.gui = GUI()


  def run(self):
    ''' starts the GUI '''
    self.gui.mainloop()


if __name__ == '__main__':
  ''' main entry point into the tool '''
  app = Application()
  app.run()
