from engine2d import Engine2D
from main_figures import Circle, Triangle


def test_engine2d_add_figure():
    engine = Engine2D()
    circle = Circle(1, 1, 2)
    engine.add_figure(circle)
    assert engine.canvas == [circle]


def test_engine2d_switch_color_in_use():
    engine = Engine2D()
    engine.switch_color_in_use_to("red")
    assert engine._Engine2D__pen_color == "red"


def test_engine_apply_color():
    default_color = "black"
    color = "blue"

    engine = Engine2D()
    figure1 = Circle(1, 2, 3)
    figure2 = Triangle(2, 3, 5, 6, 1, 7)
    engine.add_figure(figure1)
    engine.switch_color_in_use_to(color)
    engine.add_figure(figure2)
    assert engine.canvas[0].color == default_color
    assert engine.canvas[1].color == color


def test_engine2d_draw(capfd):
    engine = Engine2D()
    figure1 = Circle(1, 2, 3)
    figure2 = Triangle(2, 3, 5, 6, 1, 7)
    engine.add_figure(figure1)
    engine.add_figure(figure2)
    engine.draw()
    captured = capfd.readouterr()
    assert captured.out == "Drawing Circle with radius: 1 and center in (2, 3). Color is black.\nDrawing " \
                           "Triangle with using three points in coordinates: (2, 3), (5, 6), (1, 7). Color is black.\n"
    assert engine.canvas == []
