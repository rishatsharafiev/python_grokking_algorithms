def max_number(items):
    """Max number"""
    if not items:
        return None
    temp = items[0]
    for item in items:
        if temp < item:
            temp = item
    return temp


assert max_number([1, 2, 3, 4]) == 4
assert max_number([20]) == 20
assert max_number([]) is None
