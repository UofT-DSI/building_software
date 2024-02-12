import math

def calc_area_square(side_length: float) -> float:
    area = side_length ** 2
    return area

def calc_area_circle(radii):
    if not isinstance(radii, float):
        raise TypeError("The radius must be a number")
    if radii < 0:
        raise ValueError("The radius cannot be negative")
    areas = math.pi * radii**2
    return areas
