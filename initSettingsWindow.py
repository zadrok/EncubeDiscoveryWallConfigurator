import tkinter as tk

class InitSettingsWindow(tk.Toplevel):
  def __init__(self,root,gui):
    ''' creates options window, all model options are displayed here '''
    super().__init__(root)
    self.root = root
    self.protocol('WM_DELETE_WINDOW', self.withdraw)
    self.attributes('-topmost', 'true')
    self.gui = gui
    self.grid()

    self.createWidgets()

  def createWidgets(self):
    ''' sets up companents for user to interact with '''

    self.titleInformationLabel = tk.Label(self, text="Once this information is set it can't be changed")

    self.numScreensRowsVar = tk.StringVar(self, value='2')
    self.numScreensRowsLabel = tk.Label(self, text='Number of screen rows:')
    self.numScreensRowsEntry = tk.Entry(self, textvariable=self.numScreensRowsVar, width=30)

    self.numScreensColumnsVar = tk.StringVar(self, value='6')
    self.numScreensColumnsLabel = tk.Label(self, text='Number of screen columns:')
    self.numScreensColumnsEntry = tk.Entry(self, textvariable=self.numScreensColumnsVar, width=30)

    self.aspectRatioScreensVar = tk.StringVar(self, value='16x9')  # read AxB, 16x9
    self.aspectRatioScreensLabel = tk.Label(self, text='Aspect ratio of screens:')
    self.aspectRatioScreensEntry = tk.Entry(self, textvariable=self.aspectRatioScreensVar, width=30)

    self.loadBttn = tk.Button(self,text='Load Settings',command=self.loadSettings)
    self.commitBttn = tk.Button(self,text='Commit',command=self.commitSettings)


    self.titleInformationLabel.grid(row=0, column=0, columnspan=50, sticky=tk.W)
    self.numScreensRowsLabel.grid(row=2, column=0, sticky=tk.W)
    self.numScreensRowsEntry.grid(row=2, column=1, sticky=tk.W)
    self.numScreensColumnsLabel.grid(row=3, column=0, sticky=tk.W)
    self.numScreensColumnsEntry.grid(row=3, column=1, sticky=tk.W)
    self.aspectRatioScreensLabel.grid(row=4, column=0, sticky=tk.W)
    self.aspectRatioScreensEntry.grid(row=4, column=1, sticky=tk.W)
    self.loadBttn.grid(row=10,column=1)
    self.commitBttn.grid(row=11,column=1)


  def loadSettings(self):
    self.attributes('-topmost', 'false')
    self.gui.model.load()
    self.withdraw()
    # self.attributes('-topmost', 'true')



  def commitSettings(self):
    numScreenRows = 0
    numScreenColumns = 0
    aspectRatioScreensA = 16  # read AxB, 16x9
    aspectRatioScreensB = 9
    try:
      numScreenRows = int(self.numScreensRowsVar.get())
      numScreenColumns = int(self.numScreensColumnsVar.get())

      if numScreenRows < 1 or numScreenColumns < 1:
        print("Number of screens needs to be higher then 1")
        return

    except ValueError:
      print("Number of screens needs to be a number")
      return

    try:
      parts = self.aspectRatioScreensVar.get().split('x')
      aspectRatioScreensA = int( parts[0] )  # read AxB, 16x9
      aspectRatioScreensB = int( parts[1] )

    except ValueError:
      print("Aspect ratio needs to follow the format 16x9")
      return

    self.withdraw()
    self.gui.mainWindow.createScreens(numScreenRows,numScreenColumns,aspectRatioScreensA,aspectRatioScreensB)
    # self.gui.model.printOptions()
    self.gui.model.updateOption( "n_rows", numScreenRows )
    self.gui.model.updateOption( "n_cols", numScreenColumns )
    self.gui.optionsWindow.refreshValues()
    # self.gui.model.printOptions()
