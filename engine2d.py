class Engine2D:
    def __init__(self, pen_color="black"):
        self.canvas = []
        self.__pen_color = pen_color

    def add_figure(self, BaseFigure):
        BaseFigure.set_color(self.__pen_color)
        self.canvas.append(BaseFigure)

    def switch_color_in_use_to(self, color):
        self.__pen_color = color

    def draw(self):
        for figure in self.canvas:
            figure.draw()
        self.canvas.clear()
