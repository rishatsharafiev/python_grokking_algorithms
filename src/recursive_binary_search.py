def recursive_binary_search(items, search_item, low=0, high=None):
    """Recursive binary search"""
    if high is None:
        high = len(items) - 1
    if low > high:
        return None

    mid = (low + high) // 2

    guess = items[mid]

    if guess == search_item:
        return mid
    elif guess > search_item:
        return recursive_binary_search(items, search_item, low, mid - 1)
    else:
        return recursive_binary_search(items, search_item, mid + 1, high)


# testing part
search_list = [1, 3, 5, 7, 9]

for index, item in enumerate(search_list):
    assert recursive_binary_search(search_list, item) == index

assert recursive_binary_search(search_list, -1) is None
