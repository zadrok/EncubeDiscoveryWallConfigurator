import tkinter as tk
from jsonHandler import JsonHandler
from selectionController import selcon
from tkinter import filedialog
from keyHandeler import *



class Wbuttons():
    def __init__(self, secondaryWindow):

        self.secondaryWindow = secondaryWindow

        #Create Frame to store all buttons
        self.frame = tk.Frame(self.secondaryWindow)
        self.frame.pack(side="top")

        #Decrease Split number button, using Unicode to create Arrow
        self.secondaryWindow.DecreaseSplitNumberButton = tk.Button(self.frame, text=u"\u2B9C", command=self.DecreaseSplitNum, activebackground="white")
        self.secondaryWindow.DecreaseSplitNumberButton.pack(side="left", padx=20)

        # Display split number
        self.splitNumberString = tk.StringVar()
        self.splitNumber = 2
        self.splitNumberLabel = tk.Label(self.frame, textvariable= self.splitNumberString)
        self.splitNumberLabel.pack(side="left")
        self.splitNumberString.set("Split Number : "+str(self.splitNumber))

        # Increase Split number button, using Unicode to create Arrow
        self.secondaryWindow.IncreaseSplitNumberButton = tk.Button(self.frame,  text=u"\u2B9E", command=self.IncreaseSplitNum, activebackground="white")
        self.secondaryWindow.IncreaseSplitNumberButton.pack(side="left", padx=20)

        self.secondaryWindow.HorizonSplitButton = tk.Button(self.frame, text ="H-split", command=self.HSplit, activebackground = "white")
        self.secondaryWindow.HorizonSplitButton.pack(side="left",padx= 20 )
        self.secondaryWindow.VerticalSplitButton = tk.Button(self.frame, text="V-split", command=self.VSplit)
        self.secondaryWindow.VerticalSplitButton.pack(side="left",padx=20)
        self.secondaryWindow.HorizonSplitButton = tk.Button(self.frame, text="Join", command=self.JoinPannel)
        self.secondaryWindow.HorizonSplitButton.pack(side="left",padx=20)
        self.secondaryWindow.VerticalSplitButton = tk.Button(self.frame, text="Remove", command=self.RemovePannel)
        self.secondaryWindow.VerticalSplitButton.pack(side="left",padx=20)
        self.secondaryWindow.HorizonSplitButton = tk.Button(self.frame, text="Deselect", command=self.DeselectPannel)
        self.secondaryWindow.HorizonSplitButton.pack(side="left",padx=20)
        self.secondaryWindow.VerticalSplitButton = tk.Button(self.frame, text="Select All", command=self.SelectAllPannel)
        self.secondaryWindow.VerticalSplitButton.pack(side="left",padx=20)

        self.secondaryWindow.VerticalSplitButton = tk.Button(self.frame, text="Reset", command=self.Reset)
        self.secondaryWindow.VerticalSplitButton.pack(side="left", padx=20)

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