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

    # number of nodes
    self.numNodesVar = tk.StringVar(self, value='6')
    self.numNodesLabel = tk.Label(self, text='Number of Nodes:')
    self.numNodesEntry = tk.Entry(self, textvariable=self.numNodesVar, width=30)

    # number of columns per node
    self.numScreensColumnsVar = tk.StringVar(self, value='1')
    self.numScreensColumnsLabel = tk.Label(self, text='Number of columns in Node:')
    self.numScreensColumnsEntry = tk.Entry(self, textvariable=self.numScreensColumnsVar, width=30)

    # number of rows per node
    self.numScreensRowsVar = tk.StringVar(self, value='2')
    self.numScreensRowsLabel = tk.Label(self, text='Number of rows in Node:')
    self.numScreensRowsEntry = tk.Entry(self, textvariable=self.numScreensRowsVar, width=30)

    # aspect ratio of each screen
    self.aspectRatioScreensVar = tk.StringVar(self, value='16x9')  # read AxB, 16x9
    self.aspectRatioScreensLabel = tk.Label(self, text='Aspect ratio of screens:')
    self.aspectRatioScreensEntry = tk.Entry(self, textvariable=self.aspectRatioScreensVar, width=30)

    self.loadBttn = tk.Button(self,text='Load from file',command=self.loadSettings)
    self.commitBttn = tk.Button(self,text='Commit',command=self.commitSettings)


    self.titleInformationLabel.grid(row=1, column=0, columnspan=50, sticky=tk.W, padx=10)
    self.numNodesLabel.grid(row=3, column=0, sticky=tk.W, padx=10)
    self.numNodesEntry.grid(row=3, column=1, sticky=tk.W)
    self.numScreensRowsLabel.grid(row=4, column=0, sticky=tk.W, padx=10)
    self.numScreensRowsEntry.grid(row=4, column=1, sticky=tk.W)
    self.numScreensColumnsLabel.grid(row=5, column=0, sticky=tk.W, padx=10)
    self.numScreensColumnsEntry.grid(row=5, column=1, sticky=tk.W)
    self.aspectRatioScreensLabel.grid(row=6, column=0, sticky=tk.W, padx=10)
    self.aspectRatioScreensEntry.grid(row=6, column=1, sticky=tk.W)
    self.loadBttn.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
    self.commitBttn.grid(row=11,column=1, sticky=tk.E)


  def loadSettings(self):
    ''' calles the load function in the model, opening a open file dialog '''
    self.attributes('-topmost', 'false')
    self.gui.model.load()
    self.withdraw()


  def commitSettings(self):
    ''' takes all settings the user could give in the init window and sets up the model with the number of nodes and panels specified '''
    # basic variables
    numNodes = 0
    numScreenRows = 0
    numScreenColumns = 0
    aspectRatioScreensA = 16  # read AxB, 16x9
    aspectRatioScreensB = 9

    # try and grab variables from GUI elements
    try:
      numNodes = int( self.numNodesVar.get() )
      numScreenRows = int( self.numScreensRowsVar.get() )
      numScreenColumns = int( self.numScreensColumnsVar.get() )

      if numScreenRows < 1 or numScreenColumns < 1 or numNodes < 1:
        print("Number of Nodes, Rows and columns needs to be an int greater then or equal to 1")
        return

    except ValueError:
      print("Number of Nodes, Rows and columns needs to be an int greater then or equal to 1")
      return

    # try and convert string to int
    try:
      parts = self.aspectRatioScreensVar.get().split('x')
      aspectRatioScreensA = int( parts[0] )  # read AxB, 16x9
      aspectRatioScreensB = int( parts[1] )

    except ValueError:
      print("Aspect ratio needs to follow the format 16x9")
      return

    # hide window
    self.withdraw()
    # create number of screens (nodes) at size, with number of panels
    self.gui.model.createScreens(numNodes,numScreenRows,numScreenColumns,aspectRatioScreensA,aspectRatioScreensB)
    # self.gui.model.printOptions()
    # update some options (although these might not be used?)
    self.gui.model.updateOption( "n_rows", numScreenRows )
    self.gui.model.updateOption( "n_cols", numScreenColumns )
    self.gui.optionsWindow.refreshValues()
    # self.gui.model.printOptions()
    # allow menuaber to do things, command functions in menubar options call function when made (really annoying)
    self.gui.mainWindow.updateLock = False
