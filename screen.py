
class Screen:
    def __init__(self, canvas, ident, x, y, width, height, color):
        self.canvas = canvas
        self.id = ident
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canvas.create_rectangle(
            self.x,
            self.y,
            self.width,
            self.height,
            width=3,
            fill=self.color
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
        if v:
            print("vertically")
