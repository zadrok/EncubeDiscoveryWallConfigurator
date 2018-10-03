import tkinter as tk
from gui import GUI

class Application:
  def __init__(self):
    ''' creates the GUI '''
    self.gui = GUI()

  def run(self):
    ''' starts the GUI '''
    self.gui.mainloop()

if __name__ == '__main__':
  app = Application()
  app.run()
