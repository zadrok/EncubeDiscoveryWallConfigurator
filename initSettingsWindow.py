import tkinter as tk

class InitSettingsWindow(tk.Toplevel):
  def __init__(self,master,gui):
    ''' creates options window, all model options are displayed here '''
    super().__init__(master)
    self.master = master
    self.protocol('WM_DELETE_WINDOW', self.withdraw)
    self.gui = gui
    self.grid()

    self.createWidgets()

  def createWidgets(self):
    ''' sets up companents for user to interact with '''

    self.titleInformationLabel = tk.Label(self, text="Once this information is set it can't be changed")

    self.numScreensVar = tk.StringVar()
    self.numScreensLabel = tk.Label(self, text='Number of screens:')
    self.numScreensEntry = tk.Entry(self, textvariable=self.numScreensVar, width=30)

    self.commitBttn = tk.Button(self,text='Commit',command=self.commitSettings)


    self.titleInformationLabel.grid(row=0, column=0, columnspan=50, sticky=tk.W)
    self.numScreensLabel.grid(row=2, column=0, sticky=tk.W)
    self.numScreensEntry.grid(row=2, column=1, sticky=tk.W)
    self.commitBttn.grid(row=10,column=1)


  def commitSettings(self):
    numScreens = 0
    try:
      numScreens = int(self.numScreensVar.get())
    except ValueError:
      print("Number of screens needs to be a number")
      return

    self.withdraw()
    for i in range( numScreens ):
      self.gui.mainWindow.create_screen()
