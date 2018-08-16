import tkinter as tk
from jsonHandler import JsonHandler
from selectionController import selcon
from tkinter import filedialog
from keyHandeler import *



class Wbuttons():
    def __init__(self, secondaryWindow):

        self.secondaryWindow = secondaryWindow

        self.scroll = tk.Label(secondaryWindow, text=self.secondaryWindow.keyHandeler.getScrollCountText())
        self.scroll.pack(side="top")

        self.secondaryWindow.HorizonSplitButton = tk.Button(self.secondaryWindow, text ="H-split", command=self.HSplit)
        self.secondaryWindow.HorizonSplitButton.pack(side="top")

        self.secondaryWindow.VerticalSplitButton = tk.Button(self.secondaryWindow, text="V-split", command=self.VSplit)
        self.secondaryWindow.VerticalSplitButton.pack(side="top")
        self.splitNumIndex = 3  # if adding something before this +1 to index !!!!!!!

    def HSplit(self):
        selcon.splitHorizontally()
        self.secondaryWindow.draw()

    def VSplit(self):
        selcon.splitVertically()
        self.secondaryWindow.draw()