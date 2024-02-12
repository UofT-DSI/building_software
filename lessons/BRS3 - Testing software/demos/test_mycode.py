import math
from pytest import approx, raises

def calc_area_square(side_length: float) -> float:
    area = side_length ** 2
    return area

def test_calc_area_square():
    assert calc_area_square(1) == 1
    assert calc_area_square(0) == 0
    assert calc_area_square(2) == 4
    assert calc_area_square(3) == 9


def calc_area_circle(radii):
    if not isinstance(radii, float):
        raise TypeError("The radius must be a number")
    if radii < 0:
        raise ValueError("The radius cannot be negative")
    areas = math.pi * radii**2
    return areas


def test_calc_area_circle_raises():
    with raises(TypeError):
        calc_area_circle("a")
    with raises(ValueError):
        calc_area_circle(-1)


def test_calc_area_circle():
    inputs = [2, 4, 10]
    exp_output = [12.5664, 50.2655, 314.159]

    for i, e in zip(inputs, exp_output):
        actual_output = calc_area_circle(i)
        assert actual_output == approx(e, rel=1e-3, abs=1e-3)
