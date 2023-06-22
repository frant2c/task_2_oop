from main_figures import Rectangle
from point import Point


def test_rectangle_has_attributes():
    rectang = Rectangle(4, 2, 8, 2)
    assert hasattr(rectang, "starting_point")
    assert hasattr(rectang, "len")
    assert hasattr(rectang, "wid")
    assert hasattr(rectang, "color")


def test_rectangle_draw(capfd):
    start_point = Point(4, 5)
    length = 9
    width = 6
    test_color = "blue"
    expected_result = f"Drawing Rectangle from ({start_point.x}, {start_point.y}) coordinates with length: {length} " \
                      f"and width: {width}. Color is {test_color}."

    rectang = Rectangle(start_point.x, start_point.y, length, width)
    rectang.set_color(test_color)
    rectang.draw()

    captured = capfd.readouterr()
    assert captured.out.strip() == expected_result

# in future add tests to validate figure was created correctly
# (e.g. length and width > 0)
