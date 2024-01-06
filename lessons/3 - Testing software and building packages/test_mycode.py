import pytest
import mycode


def test_calc_area_square():
    inputs = [2, 4, 10]
    exp_output = [4, 16, 100]

    for i, e in zip(inputs, exp_output):
        actual_output = mycode.calc_area_square(i)
        assert actual_output == e


def test_calc_area_square_negative():
    with pytest.raises(ValueError):
        mycode.calc_area_square(-10)


def test_calc_area_circle():
    inputs = [2, 4, 10]
    exp_output = [12.5664, 50.2655, 314.159]

    for i, e in zip(inputs, exp_output):
        actual_output = mycode.calc_area_circle(i)
        assert actual_output == pytest.approx(e, rel=1e-3, abs=1e-3)
