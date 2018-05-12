import tkinter as tk
from menuBar import MBOptions

class OptionsWindow(tk.Toplevel):
    def __init__(self,master,gui):
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
        self.i = 0
        self.j = 0
        self.max = 30
        self.side = 11
        for key,value in self.gui.model.options.items():
            if self.i > self.max:
                self.i = 0
                self.j += self.side
            self.items.append( Item( self, self.i, self.j, str(key), str(value) ) )
            self.i += 1

        # window used to create options
        self.addOptionsWindow = AddOptionsWindow(self)
        self.addOptionsWindow.withdraw()

    def toggleAddOptionWindow(self):
        if self.addOptionsWindow.state() == 'normal':
            self.addOptionsWindow.withdraw()
        elif self.addOptionsWindow.state() == 'withdrawn':
            self.addOptionsWindow.deiconify()

    def commitOption(self):
        key = self.addOptionsWindow.KEYentryVar.get()
        value = self.addOptionsWindow.VALUEentryVar.get()
        # add option to model.options
        self.gui.model.addOption(key,value)
        # create item
        self.items.append( Item( self, self.i+1, self.j, str(key), str(value) ) )
        # hide window
        self.toggleAddOptionWindow()
        # reGrid Items
        self.reGridItems()

    def refreshValues(self):
        # change options or add new ones
        for key,value in self.gui.model.options.items():
            # find option
            if self.getItem(key) != None:
                self.getItem(key).entryVar.set(value)
            else:
                # add this as a new option
                if self.i > self.max:
                    self.i = 0
                    self.j += self.side
                self.items.append( Item( self, self.i, self.j, str(key), str(value) ) )
                self.i += 1
        # remove old item if not needed
        for itm in self.items:
            if not self.gui.model.inOptions(itm.key):
                itm.destroy()
                self.items.remove(itm)
        # make sure there are no gapes between items
        self.reGridItems()

    def reGridItems(self):
        self.i = 0
        self.j = 0
        self.max = 30
        self.side = 11
        for item in self.items:
            if self.i > self.max:
                self.i = 0
                self.j += self.side
            item.reGrid(self.i,self.j)
            self.i += 1

    def getItem(self,item):
        for i in self.items:
            if i.key == item: return i
        return None

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

    def reGrid(self,i,j):
        self.label.grid(row=i,column=j)
        self.entry.grid(row=i,column=j+1)

    def destroy(self):
        self.label.destroy()
        self.entry.destroy()


class AddOptionsWindow(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master.master)
        self.master = master
        self.protocol('WM_DELETE_WINDOW', self.withdraw)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # key
        self.KEYentryVar = tk.StringVar()
        self.KEYentryVar.set( '' )
        self.KEYlabel = tk.Label(self, text='Key')
        self.KEYentry = tk.Entry(self, textvariable=self.KEYentryVar, width=30)

        self.KEYlabel.grid()
        self.KEYentry.grid()

        # value
        self.VALUEentryVar = tk.StringVar()
        self.VALUEentryVar.set( '' )
        self.VALUElabel = tk.Label(self, text='Value')
        self.VALUEentry = tk.Entry(self, textvariable=self.VALUEentryVar, width=30)

        self.VALUElabel.grid()
        self.VALUEentry.grid()

        # done button
        self.doneBttn = tk.Button(self,text='Commit',command=self.master.commitOption)
        self.doneBttn.grid()
