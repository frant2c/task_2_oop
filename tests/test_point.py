import point


def test_point():
    a, b = 4, 5
    point_test = point.Point(a, b)
    assert point_test.x == a
    assert point_test.y == b