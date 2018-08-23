import tkinter as tk

class InitSettingsWindow(tk.Toplevel):
  def __init__(self,master,gui):
    ''' creates options window, all model options are displayed here '''
    super().__init__(master)
    self.master = master
    self.protocol('WM_DELETE_WINDOW', self.withdraw)
    self.attributes('-topmost', 'true')
    self.gui = gui
    self.grid()

    self.createWidgets()

  def createWidgets(self):
    ''' sets up companents for user to interact with '''

    self.titleInformationLabel = tk.Label(self, text="Once this information is set it can't be changed")

    self.numScreensRowsVar = tk.StringVar()
    self.numScreensRowsLabel = tk.Label(self, text='Number of screen rows:')
    self.numScreensRowsEntry = tk.Entry(self, textvariable=self.numScreensRowsVar, width=30)

    self.numScreensColumnsVar = tk.StringVar()
    self.numScreensColumnsLabel = tk.Label(self, text='Number of screen columns:')
    self.numScreensColumnsEntry = tk.Entry(self, textvariable=self.numScreensColumnsVar, width=30)

    self.commitBttn = tk.Button(self,text='Commit',command=self.commitSettings)


    self.titleInformationLabel.grid(row=0, column=0, columnspan=50, sticky=tk.W)
    self.numScreensRowsLabel.grid(row=2, column=0, sticky=tk.W)
    self.numScreensRowsEntry.grid(row=2, column=1, sticky=tk.W)
    self.numScreensColumnsLabel.grid(row=3, column=0, sticky=tk.W)
    self.numScreensColumnsEntry.grid(row=3, column=1, sticky=tk.W)
    self.commitBttn.grid(row=10,column=1)


  def commitSettings(self):
    numScreenRows = 0
    numScreenColumns = 0
    try:
      numScreenRows = int(self.numScreensRowsVar.get())
      numScreenColumns = int(self.numScreensColumnsVar.get())

      if numScreenRows < 1 or numScreenColumns < 1:
        print("Number of screens needs to be higher then 1")
        return

    except ValueError:
      print("Number of screens needs to be a number")
      return

    self.withdraw()
    self.gui.mainWindow.createScreens(numScreenRows,numScreenColumns)
