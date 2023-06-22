import point
from base_figure import BaseFigure


class Circle(BaseFigure):
    def __init__(self, radius, x, y):
        super().__init__()
        self.r = radius
        self.center = point.Point(x, y)

    def draw(self):
        print(f"Drawing Circle with radius: {self.r} and center in ({self.center.x}, {self.center.y}). "
              f"Color is {self.color}.")


class Triangle(BaseFigure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__()
        self.first_point = point.Point(x1, y1)
        self.second_point = point.Point(x2, y2)
        self.third_point = point.Point(x3, y3)


    def draw(self):
        print(f"Drawing Triangle with using three points in coordinates: "
                     f"({self.first_point.x}, {self.first_point.y}), "
                     f"({self.second_point.x}, {self.second_point.y}), "
                     f"({self.third_point.x}, {self.third_point.y}). "
                     f"Color is {self.color}.")


class Rectangle(BaseFigure):
    def __init__(self, x1, y1, length, width):
        super().__init__()
        self.starting_point = point.Point(x1, y1)
        self.len = length
        self.wid = width

    def draw(self):
        print(f"Drawing Rectangle from ({self.starting_point.x}, {self.starting_point.y}) coordinates with length: "
              f"{self.len} and width: {self.wid}. Color is {self.color}.")
