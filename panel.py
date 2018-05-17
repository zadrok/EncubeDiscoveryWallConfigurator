from selectionController import selcon

class Panel:
    def __init__(self, screen, canvas, ident, x=10, y=10, width=100, height=100, ):
        self.id = ident
        self.screen = screen
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rectangle = None

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

    def get_rectangle(self):
        return self.rectangle

    def draw(self):
        color = "#00FFFF"
        if selcon.panelSelected(self):
          color = '#00ff90'

        bbox = ( self.x, self.y, self.x+self.width, self.y+self.height )
        self.canvas.create_rectangle( bbox, width=2, fill=color, tags="panel" )

    def divideHorizontally(self):
        ''' return two new panels '''
        p1 = None
        p2 = None

        x = self.get_x()
        y = self.get_y()
        w = self.get_width()
        h = (self.get_height() / 2)

        p1 = Panel(
            screen=self.screen,
            canvas=self.canvas,
            ident="0",
            x=x,
            y=y,
            width=w,
            height=h
        )
        p2 = Panel(
            screen=self.screen,
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

        x = self.get_x()
        y = self.get_y()
        w = (self.get_width() / 2)
        h = self.get_height()

        p1 = Panel(
            screen=self.screen,
            canvas=self.canvas,
            ident="1",
            x=x,
            y=y,
            width=w,
            height=h
        )
        p2 = Panel(
            screen=self.screen,
            canvas=self.canvas,
            ident="1",
            x=x + w,
            y=y,
            width=w,
            height=h
        )

        return p1,p2
