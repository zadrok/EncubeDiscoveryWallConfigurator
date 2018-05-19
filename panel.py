
class Panel:
    def __init__(self, canvas, ident, x=10, y=10, width=100, height=100):
        self.id = ident
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
        self.rectangle = self.canvas.create_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            width=2,
            fill="#00FFFF",
            tags="panel"
        )
        self.draw_id()

    def split_horizontally(self):
        v_size = self.get_height() - self.get_y()
        v_size = v_size / 2
        self.set_height(self.get_y()+v_size)

    def split_vertically(self):
        h_size = self.get_width() - self.get_x()
        h_size = h_size / 2
        self.set_width(self.get_x() + h_size)

    def draw_id(self):
        self.canvas.create_rectangle(
            self.x, 
            self.y, 
            self.x + 20, 
            self.y + 20, 
            fill="#8144A9"
        )
        self.canvas.create_text(
            self.x + 10, 
            self.y + 10, 
            text=self.id[:2],
            font="Arial 8 bold"
        )