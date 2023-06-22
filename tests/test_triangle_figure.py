from main_figures import Triangle
from point import Point


def test_triangle_has_attributes():
    triang = Triangle(1, 2, 4, 5, 8, 2)
    assert hasattr(triang, "first_point")
    assert hasattr(triang, "second_point")
    assert hasattr(triang, "third_point")
    assert hasattr(triang, "color")


def test_triangle_draw(capfd):
    point1 = Point(1, 1)
    point2 = Point(4, 5)
    point3 = Point(1, 9)
    test_color = "green"
    expected_result = f"Drawing Triangle with using three points in coordinates: ({point1.x}, {point1.y}), " \
                      f"({point2.x}, {point2.y}), ({point3.x}, {point3.y}). Color is {test_color}."

    triang = Triangle(point1.x, point1.y, point2.x, point2.y, point3.x, point3.y)
    triang.set_color(test_color)
    triang.draw()

    captured = capfd.readouterr()
    assert captured.out.strip() == expected_result

# in future add tests to validate figure was created correctly
# (e.g. all points are not in one line, points do not have same coordinates, etc.)
