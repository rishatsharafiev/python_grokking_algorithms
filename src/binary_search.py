import math


def binary_search(items, item):
    """Find item position in given list"""
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = math.ceil((low + high) / 2)
        guess = items[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


# testing part
search_list = [1, 3, 5, 7, 9]

for index, item in enumerate(search_list):
    assert binary_search(search_list, item) == index

assert binary_search(search_list, -1) is None
