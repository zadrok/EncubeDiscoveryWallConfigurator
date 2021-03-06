import tkinter as tk
from jsonHandler import JsonHandler
from selectionController import selcon
from tkinter import filedialog
from keyHandeler import *

class controlPanel():
  def __init__(self, mainWindow):
    ''' creates buttons to manage configuration tool'''
    self.mainWindow = mainWindow

    #Create root frame to store all children frames
    self.frame = tk.Frame(self.mainWindow)
    self.frame.pack(side="top")

    # Frame for Save and Load
    self.saveAndLoadFrame = tk.Frame(self.frame, highlightbackground="black", highlightthickness=1, width=200)
    self.saveAndLoadFrame.pack(side="left")
    # Frame for Save and Load Label
    self.saveAndLoadLabelFrame = tk.Frame(self.saveAndLoadFrame, background = "#8583D7" )
    self.saveAndLoadLabelFrame.pack(side="top", fill="both")
    # Save and Load Label
    self.saveAndLoadLabel = tk.Label(self.saveAndLoadLabelFrame, text="File", font =2, background = "#8583D7" )
    self.saveAndLoadLabel.pack(side="left", padx = (4,6))
    # Save and Load buttons
    self.mainWindow.saveButton = tk.Button(self.saveAndLoadFrame, text="Save", command=self.saveWithButton, activebackground="white")
    self.mainWindow.saveButton.pack(side="left", padx=20)
    self.mainWindow.loadButton = tk.Button(self.saveAndLoadFrame, text="Load", command=self.loadWithButton, activebackground="white")
    self.mainWindow.loadButton.pack(side="left", padx=20)

    # Frame for Split buttons
    self.splitButtonFrame = tk.Frame(self.frame, highlightbackground="black", highlightthickness=1, width=1250)
    self.splitButtonFrame.pack(side="left")
    # Frame for Split buttons Label
    self.splitButtonLabelFrame = tk.Frame(self.splitButtonFrame, background = "#8583D7")
    self.splitButtonLabelFrame.pack(side="top", fill="both")
    # Label for split buttons frame
    self.splitNumberLabel = tk.Label(self.splitButtonLabelFrame, text="Split Panel", font =2, background = "#8583D7")
    self.splitNumberLabel.pack(side="left", fill="both", padx = (4,6))
    # Decrease button
    self.mainWindow.DecreaseSplitNumberButton = tk.Button(self.splitButtonFrame, text=u"\u21e6", command=self.decreaseSplitNum, activebackground="white")
    self.mainWindow.DecreaseSplitNumberButton.pack(side="left")
    # Display split number
    self.splitNumberString = tk.StringVar()
    self.splitNumber = 2
    self.splitNumberLabel = tk.Label(self.splitButtonFrame, textvariable=self.splitNumberString, background="white")
    self.splitNumberLabel.pack(side="left")
    self.splitNumberString.set("Split Number : " + str(self.splitNumber))
    # Increase button
    self.mainWindow.IncreaseSplitNumberButton = tk.Button(self.splitButtonFrame, text=u"\u21e8", command=self.increaseSplitNum, activebackground="white")
    self.mainWindow.IncreaseSplitNumberButton.pack(side="left")
    # Horizon Split button
    self.mainWindow.HorizonSplitButton = tk.Button(self.splitButtonFrame, text="H-split", command=self.HSplit, activebackground="white")
    self.mainWindow.HorizonSplitButton.pack(side="left", padx=10)
    # Vertical Split button
    self.mainWindow.VerticalSplitButton = tk.Button(self.splitButtonFrame, text="V-split", command=self.VSplit)
    self.mainWindow.VerticalSplitButton.pack(side="left", padx=10)
    # Join panel Button
    self.mainWindow.JoinPannelButton = tk.Button(self.splitButtonFrame, text="Join", command=self.joinPanel)
    self.mainWindow.JoinPannelButton.pack(side="left", padx=10)
    # Remove panel Button
    self.mainWindow.RemovePannelButton = tk.Button(self.splitButtonFrame, text="Remove", command=self.removePanel)
    self.mainWindow.RemovePannelButton.pack(side="left", padx=10)
    # Filling gap panel Button
    self.mainWindow.FillingGapPannelButton = tk.Button(self.splitButtonFrame, text="Filling Gap", command=self.fillingGap)
    self.mainWindow.FillingGapPannelButton.pack(side="left", padx=10)
    # Deselect panel button
    self.mainWindow.DeselectPannelButton = tk.Button(self.splitButtonFrame, text="Deselect", command=self.deselectPanel)
    self.mainWindow.DeselectPannelButton.pack(side="left", padx=10)
    # Select All panel button
    self.mainWindow.SelectAllPannelButton = tk.Button(self.splitButtonFrame, text="Select All", command=self.selectAllPanel)
    self.mainWindow.SelectAllPannelButton.pack(side="left", padx=10)
    # Reset panel button
    self.mainWindow.ResetPannelButton = tk.Button(self.splitButtonFrame, text="Reset", command=self.resetPanel)
    self.mainWindow.ResetPannelButton.pack(side="left", padx=10)


    #the other frame to store change pannel mode buttons
    self.ChangePannelModeFrame = tk.Frame(self.frame, highlightbackground="black", highlightthickness=1, width=800)
    self.ChangePannelModeFrame.pack(side="left")
    # the other frame to store change pannel mode buttons
    self.ChangePannelModeLabelFrame = tk.Frame(self.ChangePannelModeFrame, width=800, background = "#8583D7")
    self.ChangePannelModeLabelFrame.pack(side="top", fill="both")
    # Label for change panel mode buttons frame
    self.ChangePanelModeLabel = tk.Label(self.ChangePannelModeLabelFrame, text="Panel mode", font =2, background = "#8583D7")
    self.ChangePanelModeLabel.pack(side="left", padx = (4,6))
    # Change panel mode to Encube button
    self.mainWindow.ChangePannelModeCubeLabel = tk.Label(self.ChangePannelModeFrame, text = "", width= 5, background="#2FA1D6")
    self.mainWindow.ChangePannelModeCubeLabel.pack(side="left",padx=(20,0))
    self.mainWindow.ChangePannelModeCube = tk.Button(self.ChangePannelModeFrame, text="Cube", command=self.setPanelsCubeButton)
    self.mainWindow.ChangePannelModeCube.pack(side="left", padx=(0,20))
    # Change panel mode to Image button
    self.mainWindow.ChangePannelModeImageLabel = tk.Label(self.ChangePannelModeFrame, text="", width=5, background="#e500ff")
    self.mainWindow.ChangePannelModeImageLabel.pack(side="left")
    self.mainWindow.ChangePannelModeImage = tk.Button(self.ChangePannelModeFrame, text="Image", command=self.setPanelsImageButton)
    self.mainWindow.ChangePannelModeImage.pack(side="left",padx=(0,20))
    # Change panel mode to Graph button
    self.mainWindow.ChangePannelModeGraphLabel = tk.Label(self.ChangePannelModeFrame, text="", width=5, background="#f8ff47")
    self.mainWindow.ChangePannelModeGraphLabel.pack(side="left")
    self.mainWindow.ChangePannelModeGraph = tk.Button(self.ChangePannelModeFrame, text="Graph", command=self.setPanelsGraphButton)
    self.mainWindow.ChangePannelModeGraph.pack(side="left",padx=(0,20))


  def saveWithButton(self):
    '''Save configuration'''
    self.mainWindow.gui.model.save()


  def loadWithButton(self):
    '''Load configuration'''
    self.mainWindow.gui.model.load()


  def setPanelsImageButton(self):
    '''Set panel as image'''
    selcon.setPanelsMode('image')


  def setPanelsCubeButton(self):
    '''Set panel as cube'''
    selcon.setPanelsMode('cube')


  def setPanelsGraphButton(self):
    '''Set panel as graph'''
    selcon.setPanelsMode('graph')


  def decreaseSplitNum(self):
    '''Decrease number of splitting panel'''
    if self.splitNumber > 2:
      self.splitNumber -= 1
      self.splitNumberString.set("Split Number : "+ str(self.splitNumber))


  def increaseSplitNum(self):
    '''Increase number of splitting panel'''
    if self.splitNumber < 8:
      self.splitNumber += 1
      self.splitNumberString.set("Split Number : "+ str(self.splitNumber))


  def HSplit(self):
    '''Horizontal Split'''
    selcon.splitHorizontally()
    self.mainWindow.draw()


  def VSplit(self):
    '''Vertical Split'''
    selcon.splitVertically()
    self.mainWindow.draw()


  def joinPanel(self):
    '''Join multiple panels'''
    selcon.join()
    self.mainWindow.draw()


  def removePanel(self):
    '''Remove selected panels'''
    selcon.remove()
    self.mainWindow.draw()


  def fillingGap(self):
    '''Filling empty panel '''
    selcon.fillGap()
    self.mainWindow.draw()


  def deselectPanel(self):
    '''Deselect panels'''
    selcon.deselectAll()
    self.mainWindow.draw()


  def selectAllPanel(self):
    '''Select all panels'''
    selcon.allselect()
    self.mainWindow.draw()


  def resetPanel(self):
    '''Reset configuration'''
    selcon.reset()
    self.mainWindow.draw()
