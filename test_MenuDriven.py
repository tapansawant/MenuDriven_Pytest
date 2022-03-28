import MenuDriven
import pytest


@pytest.mark.skip(reason="currently no need to execute")  # inbuilt
def test_Area_Rectangle():
    x = 10
    y = 20
    result = MenuDriven.Area_Rectangle(x, y)
    assert x * y == result


@pytest.mark.myproject
def test_Perimeter_Rect():
    x = 20
    y = 10
    result = MenuDriven.Perimeter_Rect(x, y)
    assert x + x + y + y == result


@pytest.mark.myproject
def test_Area_Square():
    x = 5
    result = MenuDriven.Area_Square(x)
    assert x * x == result
