import math

def calc_circle_area(radius:float) -> float:
    ''' Calculates the area of a circle given a radius. '''
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


radius = 2
area = calc_circle_area(radius)
assert area > 0, f"Area is {area} but should be positive"


