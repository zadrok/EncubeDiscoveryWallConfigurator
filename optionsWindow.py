import tkinter as tk
from menuBar import MBOptions

class OptionsWindow(tk.Frame):
    def __init__(self,gui,root):
        super().__init__(root)
        self.root = root
        self.gui = gui

        self.frame = tk.Frame(master=self.root)
        self.frame.grid()

        self.createWidgets()

    def createWidgets(self):
        # menu bar
        self.menuBar = MBOptions(self.root)
        # options
        self.items = []
        i = 0
        j = 0
        for key,value in self.gui.model.options.items():
            # print( str(key) + ' ' + str(value) )

            if i > 35:
                i = 0
                j += 11

            label = tk.Label(self.root, text=str(key))
            entryVar = tk.StringVar()
            entry = tk.Entry(self.root, textvariable=entryVar)
            label.grid(row=i,column=j)
            entry.grid(row=i,column=j+1)
            entryVar.set( str(value) )
            self.items.append( [label,entry,entryVar] )
            i += 1

        # for x in self.items:
        #     print( x[2].get() )
