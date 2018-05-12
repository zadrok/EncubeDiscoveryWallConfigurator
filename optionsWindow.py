import tkinter as tk
from menuBar import MBOptions

class OptionsWindow(tk.Toplevel):
    def __init__(self,gui,master):
        super().__init__(master)
        self.master = master
        self.protocol('WM_DELETE_WINDOW', self.withdraw)
        self.gui = gui
        self.grid()

        self.createWidgets()

    def createWidgets(self):
        # menu bar
        self.menuBar = MBOptions(self)
        # options
        self.items = []
        i = 0
        j = 0
        for key,value in self.gui.model.options.items():
            # print( str(key) + ' ' + str(value) )

            if i > 30:
                i = 0
                j += 11

            self.items.append( Item( self, i, j, str(key), str(value) ) )
            i += 1

        # self.button = tk.Button(self, text='Check Print', command=self.printCallback)
        # self.button.grid()


    def printCallback(self):
        for x in self.items:
            print( x.entryVar.get() )
            print( x.entry.get() )


class Item:
    def __init__(self,master,i,j,key,value):
        self.master = master
        self.i = i
        self.j = j
        self.key = key
        self.value = value

        self.entryVar = tk.StringVar()
        self.entryVar.set( str(self.value) )
        self.label = tk.Label(self.master, text=str(self.key))
        self.entry = tk.Entry(self.master, textvariable=self.entryVar, width=30)

        self.label.grid(row=i,column=j)
        self.entry.grid(row=i,column=j+1)
