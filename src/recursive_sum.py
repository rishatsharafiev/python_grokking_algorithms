def recursive_sum(items):
    """Recursive sum of list items"""
    if not len(items):
        return 0
    else:
        return items[0] + recursive_sum(items[1:])


assert recursive_sum([1, 2, 3, 4]) == 10
assert recursive_sum([20]) == 20
