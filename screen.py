from panel import Panel


class Screen:
    def __init__(self, canvas, ident, x, y, width, height, color):
        self.canvas = canvas
        self.id = ident
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.panels = []

    def draw(self):
        self.canvas.create_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            width=3,
            fill=self.color
        )
        for panel in self.panels:
            panel.draw()

    def draw_id(self, visible):
        if visible is True:
            self.canvas.create_rectangle(
                self.x, 
                self.y, 
                self.x + 20, 
                self.y + 20, 
                fill="#81AAA9"
            )
            self.canvas.create_text(
                self.x + 10, 
                self.y + 10, 
                text=self.id[:2],
                font="Arial 8 bold"
            )

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

    def clicked(self, x, y, h, v):
        print("I, ", self.get_id(), " have been clicked at ", x, ",", y)
        print("I have been asked to split: ")

        if h:
            print("horizontally")
            self.split_horizontally(x, y)
        elif v:
            print("vertically")
            self.split_vertically(x, y)

    def split_horizontally(self, x, y):
        panel_at_xy = self.get_panel_at_xy(x, y)
        if panel_at_xy is not None:
            orig_h = panel_at_xy.get_height()
            panel_at_xy.split_horizontally()
            p = Panel(
                canvas=self.canvas,
                ident=str(len(self.panels)),
                x=panel_at_xy.get_x(),
                y=panel_at_xy.get_height(),
                width=panel_at_xy.get_width(),
                height=orig_h
            )
            self.panels.append(p)
        else:
            panel_one = Panel(
                canvas=self.canvas,
                ident="0",
                x=self.get_x() + 2,
                y=self.get_y() + 2,
                width=self.get_width(),
                height=self.get_height() / 2
            )
            panel_two = Panel(
                canvas=self.canvas,
                ident="1",
                x=self.get_x() + 2,
                y=self.get_y() + self.get_height() / 2,
                width=self.get_width(),
                height=self.get_height()
            )
            self.panels.append(panel_one)
            self.panels.append(panel_two)

    def split_vertically(self, x, y):
        panel_at_xy = self.get_panel_at_xy(x, y)
        if panel_at_xy is not None:
            orig_w = panel_at_xy.get_width()
            panel_at_xy.split_vertically()
            p = Panel(
                canvas=self.canvas,
                ident=str(len(self.panels)),
                x=panel_at_xy.get_width(),
                y=panel_at_xy.get_y(),
                width=orig_w,
                height=panel_at_xy.get_height()
            )
            self.panels.append(p)
        else:
            panel_one = Panel(
                canvas=self.canvas,
                ident="0",
                x=self.get_x() + 2,
                y=self.get_y() + 2,
                width=((self.get_width() - self.get_x()) / 2 ) + self.get_x(),
                height=self.get_height()
            )
            panel_two = Panel(
                canvas=self.canvas,
                ident="1",
                x=panel_one.get_width(),
                y=self.get_y() + 2,
                width=self.get_width(),
                height=self.get_height()
            )
            self.panels.append(panel_one)
            self.panels.append(panel_two)

    def get_panel_at_xy(self, x, y):
        panel = None
        for i, p in enumerate(self.panels):
            px = p.get_x()
            py = p.get_y()
            pw = p.get_width()
            ph = p.get_height()
            if (x >= px and x <= pw) and (y >= py and y <= ph):
                panel = p
        return panel
