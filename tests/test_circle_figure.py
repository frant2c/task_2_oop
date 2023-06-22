from main_figures import Circle


def test_circle_has_attributes():
    test_circle = Circle(3, 3, 4)
    assert hasattr(test_circle, 'r')
    assert hasattr(test_circle, 'center')
    assert hasattr(test_circle, 'color')


def test_circle_draw(capfd):
    radius = 5
    x, y = 3, 4
    test_color = "pink"
    expected_result = f"Drawing Circle with radius: {str(radius)} and center in ({str(x)}, {str(y)}). " \
                      f"Color is {test_color}."

    test_circle = Circle(radius, x, y)
    test_circle.set_color(test_color)
    test_circle.draw()

    captured = capfd.readouterr()
    assert captured.out.strip() == expected_result

# in future add tests to validate figure was created correctly
# (e.g. radius < 0, coordinates are in acceptable range, etc.)
