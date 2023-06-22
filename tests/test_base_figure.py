import pytest

import base_figure


def test_draw():
    figure = base_figure.BaseFigure()
    with pytest.raises(NotImplementedError):
        figure.draw()


def test_new_object_has_no_color():
    figure = base_figure.BaseFigure()
    assert figure.color is None


def test_set_color():
    figure = base_figure.BaseFigure()
    figure.set_color("red")
    assert figure.color == "red"
