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

        # One of children frame to store save and load buttons
        self.saveAndLoadFrame = tk.Frame(self.frame, highlightbackground="black", highlightthickness=1, width=200, height=55)
        self.saveAndLoadFrame.pack(side="left")

        #One of children frame to store split buttons
        self.splitButtonFrame = tk.Frame(self.frame, highlightbackground="black", highlightthickness=1, width=1250, height=55, bd=0)
        self.splitButtonFrame.pack(side="left")
        #nested frame in splitButtonFrame in order to gives different rows
        self.splitButtonFrame2 = tk.Frame(self.splitButtonFrame)
        self.splitButtonFrame2.pack(side="top")

        self.splitNumberLabel = tk.Label(self.splitButtonFrame2, text="Split Panel")
        self.splitNumberLabel.pack(side="left")


        #the other frame to store change pannel mode buttons
        self.ChangePannelModeFrame = tk.Frame(self.frame, highlightbackground="black", highlightthickness=1, width=800, height=55)
        self.ChangePannelModeFrame.pack(side="right")

        #Decrease Split number button, using Unicode to create Arrow
        self.secondaryWindow.DecreaseSplitNumberButton = tk.Button(self.splitButtonFrame2, text=u"\u2B9C", command=self.DecreaseSplitNum, activebackground="white")
        self.secondaryWindow.DecreaseSplitNumberButton.pack(side="left", padx=20)
        # Display split number
        self.splitNumberString = tk.StringVar()
        self.splitNumber = 2
        self.splitNumberLabel = tk.Label(self.splitButtonFrame2, textvariable= self.splitNumberString)
        self.splitNumberLabel.pack(side="left")
        self.splitNumberString.set("Split Number : "+str(self.splitNumber))
        # Increase Split number button, using Unicode to create Arrow
        self.secondaryWindow.IncreaseSplitNumberButton = tk.Button(self.splitButtonFrame2,  text=u"\u2B9E", command=self.IncreaseSplitNum, activebackground="white")
        self.secondaryWindow.IncreaseSplitNumberButton.pack(side="left", padx=20)

        self.secondaryWindow.HorizonSplitButton = tk.Button(self.splitButtonFrame, text ="H-split", command=self.HSplit, activebackground = "white")
        self.secondaryWindow.HorizonSplitButton.pack(side="left",padx= 20 )
        self.secondaryWindow.VerticalSplitButton = tk.Button(self.splitButtonFrame, text="V-split", command=self.VSplit)
        self.secondaryWindow.VerticalSplitButton.pack(side="left",padx=20)
        self.secondaryWindow.JoinPannelButton = tk.Button(self.splitButtonFrame, text="Join", command=self.JoinPannel)
        self.secondaryWindow.JoinPannelButton.pack(side="left",padx=20)
        self.secondaryWindow.RemovePannelButton = tk.Button(self.splitButtonFrame, text="Remove", command=self.RemovePannel)
        self.secondaryWindow.RemovePannelButton.pack(side="left",padx=20)
        self.secondaryWindow.DeselectPannelButton = tk.Button(self.splitButtonFrame, text="Deselect", command=self.DeselectPannel)
        self.secondaryWindow.DeselectPannelButton.pack(side="left",padx=20)
        self.secondaryWindow.SelectAllPannelButton = tk.Button(self.splitButtonFrame, text="Select All", command=self.SelectAllPannel)
        self.secondaryWindow.SelectAllPannelButton.pack(side="left",padx=20)
        self.secondaryWindow.ResetPannelButton = tk.Button(self.splitButtonFrame, text="Reset", command=self.Reset)
        self.secondaryWindow.ResetPannelButton.pack(side="left", padx=20)

        self.secondaryWindow.ChangePannelModeCube = tk.Button(self.ChangePannelModeFrame, text="Cube", command=self.DeselectPannel)
        self.secondaryWindow.ChangePannelModeCube.pack(side="left", padx=20)
        self.secondaryWindow.ChangePannelModeImage = tk.Button(self.ChangePannelModeFrame, text="Image", command=self.SelectAllPannel)
        self.secondaryWindow.ChangePannelModeImage.pack(side="left", padx=20)
        self.secondaryWindow.ChangePannelModeGraph = tk.Button(self.ChangePannelModeFrame, text="Graph", command=self.Reset)
        self.secondaryWindow.ChangePannelModeGraph.pack(side="left", padx=20)

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

    def DeselectPannel(self):
        selcon.deselectAll()
        self.secondaryWindow.draw()

    def SelectAllPannel(self):
        selcon.allselect()
        self.secondaryWindow.draw()

    def Reset(self):
        selcon.reset()
        self.secondaryWindow.draw()