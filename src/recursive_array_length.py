def recursive_array_length(items):
    """Recursive array length"""
    if not items:
        return 0
    else:
        items.pop()
        return 1 + recursive_array_length(items)


assert recursive_array_length([1, 2, 3, 4]) == 4
assert recursive_array_length([20]) == 1
assert recursive_array_length([]) == 0
