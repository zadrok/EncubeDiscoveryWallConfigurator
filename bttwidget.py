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

        # Display split number
        self.splitNumIndex = 3  # if adding something before this +1 to index !!!!!!!
        self.scrollNum = tk.StringVar()
        self.scrolLabel = tk.Label(self.frame, textvariable=self.scrollNum)
        self.scrolLabel.pack(side="left")
        self.scrollNum.set(self.secondaryWindow.keyHandeler.getScrollCountText())

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


    def HSplit(self):
        selcon.splitHorizontally()
        self.secondaryWindow.draw()

    def VSplit(self):
        selcon.splitVertically()
        self.secondaryWindow.draw()

    def JoinPannel(self):
        #selcon.splitHorizontally()
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