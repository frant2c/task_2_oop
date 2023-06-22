from engine2d import Engine2D
from main_figures import Circle, Triangle, Rectangle

if __name__ == '__main__':
    circ1 = Circle(2,3,5)
    triang1 = Triangle(1,1,3,4,1,6)
    rect1 = Rectangle(4,5,6,7)

    engine = Engine2D()
    engine.add_figure(circ1)
    engine.switch_color_in_use_to("red")
    engine.add_figure(triang1)
    engine.switch_color_in_use_to("white")
    engine.add_figure(rect1)
    engine.draw()