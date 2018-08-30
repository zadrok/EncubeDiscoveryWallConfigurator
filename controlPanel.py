import tkinter as tk
from jsonHandler import JsonHandler
from selectionController import selcon
from tkinter import filedialog
from keyHandeler import *



class controlPanel():
    def __init__(self, secondaryWindow):

        self.secondaryWindow = secondaryWindow

        #Create root frame to store all children frames
        self.frame = tk.Frame(self.secondaryWindow)
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
        self.secondaryWindow.saveButton = tk.Button(self.saveAndLoadFrame, text="Save", command=self.saveWithButton, activebackground="white")
        self.secondaryWindow.saveButton.pack(side="left", padx=20)
        self.secondaryWindow.loadButton = tk.Button(self.saveAndLoadFrame, text="Load", command=self.loadWithButton, activebackground="white")
        self.secondaryWindow.loadButton.pack(side="left", padx=20)

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
        self.secondaryWindow.DecreaseSplitNumberButton = tk.Button(self.splitButtonFrame, text=u"\u21e6", command=self.DecreaseSplitNum, activebackground="white")
        self.secondaryWindow.DecreaseSplitNumberButton.pack(side="left")
        # Display split number
        self.splitNumberString = tk.StringVar()
        self.splitNumber = 2
        self.splitNumberLabel = tk.Label(self.splitButtonFrame, textvariable=self.splitNumberString, background="white")
        self.splitNumberLabel.pack(side="left")
        self.splitNumberString.set("Split Number : " + str(self.splitNumber))
        # Increase button
        self.secondaryWindow.IncreaseSplitNumberButton = tk.Button(self.splitButtonFrame, text=u"\u21e8", command=self.IncreaseSplitNum, activebackground="white")
        self.secondaryWindow.IncreaseSplitNumberButton.pack(side="left")
        # Horizon Split button
        self.secondaryWindow.HorizonSplitButton = tk.Button(self.splitButtonFrame, text="H-split", command=self.HSplit, activebackground="white")
        self.secondaryWindow.HorizonSplitButton.pack(side="left", padx=10)
        # Vertical Split button
        self.secondaryWindow.VerticalSplitButton = tk.Button(self.splitButtonFrame, text="V-split", command=self.VSplit)
        self.secondaryWindow.VerticalSplitButton.pack(side="left", padx=10)
        # Join panel Button
        self.secondaryWindow.JoinPannelButton = tk.Button(self.splitButtonFrame, text="Join", command=self.JoinPannel)
        self.secondaryWindow.JoinPannelButton.pack(side="left", padx=10)
        # Remove panel Button
        self.secondaryWindow.RemovePannelButton = tk.Button(self.splitButtonFrame, text="Remove", command=self.RemovePannel)
        self.secondaryWindow.RemovePannelButton.pack(side="left", padx=10)
        # Filling gap panel Button
        self.secondaryWindow.FillingGapPannelButton = tk.Button(self.splitButtonFrame, text="Filling Gap", command=self.FillingGap)
        self.secondaryWindow.FillingGapPannelButton.pack(side="left", padx=10)
        # Deselect panel button
        self.secondaryWindow.DeselectPannelButton = tk.Button(self.splitButtonFrame, text="Deselect", command=self.DeselectPannel)
        self.secondaryWindow.DeselectPannelButton.pack(side="left", padx=10)
        # Select All panel button
        self.secondaryWindow.SelectAllPannelButton = tk.Button(self.splitButtonFrame, text="Select All", command=self.SelectAllPannel)
        self.secondaryWindow.SelectAllPannelButton.pack(side="left", padx=10)
        # Reset panel button
        self.secondaryWindow.ResetPannelButton = tk.Button(self.splitButtonFrame, text="Reset", command=self.Reset)
        self.secondaryWindow.ResetPannelButton.pack(side="left", padx=10)


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
        self.secondaryWindow.ChangePannelModeCubeLabel = tk.Label(self.ChangePannelModeFrame, text = "", width= 5, background="#00FFFF")
        self.secondaryWindow.ChangePannelModeCubeLabel.pack(side="left",padx=(20,0))
        self.secondaryWindow.ChangePannelModeCube = tk.Button(self.ChangePannelModeFrame, text="Cube", command=self.setPanelsCubeButton)
        self.secondaryWindow.ChangePannelModeCube.pack(side="left", padx=(0,20))
        # Change panel mode to Image button
        self.secondaryWindow.ChangePannelModeImageLabel = tk.Label(self.ChangePannelModeFrame, text="", width=5, background="#e500ff")
        self.secondaryWindow.ChangePannelModeImageLabel.pack(side="left")
        self.secondaryWindow.ChangePannelModeImage = tk.Button(self.ChangePannelModeFrame, text="Image", command=self.setPanelsImageButton)
        self.secondaryWindow.ChangePannelModeImage.pack(side="left",padx=(0,20))
        # Change panel mode to Graph button
        self.secondaryWindow.ChangePannelModeGraphLabel = tk.Label(self.ChangePannelModeFrame, text="", width=5, background="#f8ff47")
        self.secondaryWindow.ChangePannelModeGraphLabel.pack(side="left")
        self.secondaryWindow.ChangePannelModeGraph = tk.Button(self.ChangePannelModeFrame, text="Graph", command=self.setPanelsGraphButton)
        self.secondaryWindow.ChangePannelModeGraph.pack(side="left",padx=(0,20))

    def saveWithButton(self):
        self.secondaryWindow.gui.model.save()

    def loadWithButton(self):
        self.secondaryWindow.gui.model.load()

    def setPanelsImageButton(self):
        selcon.setPanelsMode('image')

    def setPanelsCubeButton(self):
        selcon.setPanelsMode('cube')

    def setPanelsGraphButton(self):
        selcon.setPanelsMode('graph')

    def DecreaseSplitNum(self):
        if self.splitNumber > 2:
            self.splitNumber -= 1
            self.splitNumberString.set("Split Number : "+ str(self.splitNumber))


    def IncreaseSplitNum(self):
        if self.splitNumber < 8:
            self.splitNumber += 1
            self.splitNumberString.set("Split Number : "+ str(self.splitNumber))

    def HSplit(self):
        selcon.splitHorizontally()
        self.secondaryWindow.draw()

    def VSplit(self):
        selcon.splitVertically()
        self.secondaryWindow.draw()

    def JoinPannel(self):
        selcon.join()
        self.secondaryWindow.draw()

    def RemovePannel(self):
        selcon.remove()
        self.secondaryWindow.draw()

    def FillingGap(self):
        selcon.fillGap()
        self.secondaryWindow.draw()

    def DeselectPannel(self):
        selcon.deselectAll()
        self.secondaryWindow.draw()

    def SelectAllPannel(self):
        selcon.allselect()
        self.secondaryWindow.draw()

    def Reset(self):
        selcon.reset()
        self.secondaryWindow.draw()