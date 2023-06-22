class BaseFigure:
    def __init__(self):
        self.color = None

    def draw(self):
        raise NotImplementedError("Cannot draw BaseFigure.")

    def set_color(self, pen_color):
        self.color = pen_color
