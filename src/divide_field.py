import math


def divide_field(x, y):
    """Divide field to squares"""
    if x == 0:
        return y
    elif y == 0:
        return x
    elif x < y:
        c = math.floor(y / x)
        y2 = y - x * c
        return divide_field(x, y2)
    else:
        c = math.floor(x / y)
        x2 = x - y * c
        return divide_field(x2, y)


assert divide_field(640, 400) == 80
assert divide_field(800, 400) == 400
