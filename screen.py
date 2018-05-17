from panel import Panel
from selectionController import selcon

class Screen:
    def __init__(self, master, canvas, ident, x, y, width, height, color):
        self.master = master
        self.canvas = canvas
        self.id = ident
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.panels = []

    def draw(self):
        color = self.color
        if selcon.screenSelected(self):
          color = '#6d6d6d'

        bbox = ( self.x, self.y, self.x+self.width, self.y+self.height )
        self.canvas.create_rectangle( bbox, width=3, fill=color )
        for panel in self.panels:
            panel.draw()

    def set_position(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def get_id(self):
        return self.id

    def set_id(self, ident):
        self.id = ident

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_canvas(self):
        return self.canvas

    def set_canvas(self, canvas):
        self.canvas = canvas

    def divideHorizontally(self):
        ''' return two new panels '''
        p1 = None
        p2 = None

        x = self.get_x() + 2
        y = self.get_y() + 2
        w = self.get_width() - 4
        h = (self.get_height() / 2) - 2

        p1 = Panel(
            screen=self,
            canvas=self.canvas,
            ident="0",
            x=x,
            y=y,
            width=w,
            height=h
        )
        p2 = Panel(
            screen=self,
            canvas=self.canvas,
            ident="0",
            x=x,
            y=y + h,
            width=w,
            height=h
        )

        return p1,p2

    def divideVertically(self):
        ''' return two new panels '''
        p1 = None
        p2 = None

        x = self.get_x() + 2
        y = self.get_y() + 2
        w = (self.get_width() / 2) - 2
        h = self.get_height() - 4

        p1 = Panel(
            screen=self,
            canvas=self.canvas,
            ident="1",
            x=x,
            y=y,
            width=w,
            height=h
        )
        p2 = Panel(
            screen=self,
            canvas=self.canvas,
            ident="1",
            x=x + w,
            y=y,
            width=w,
            height=h
        )

        return p1,p2

    def get_panel_at_xy(self, x, y):
        for i, p in enumerate(self.panels):
            px = p.get_x()
            py = p.get_y()
            pw = px + p.get_width()
            ph = py + p.get_height()
            if (x >= px and x <= pw) and (y >= py and y <= ph):
                return p
        return None
