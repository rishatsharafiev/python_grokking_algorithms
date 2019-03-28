import math


def recursive_binary_search(items, search_item):
    low = 0
    high = len(items) - 1

    mid = math.ceil((low + high) / 2)

    guess = items[mid]

    if guess == search_item:
        return mid
    elif guess > search_item:
        return low + recursive_binary_search(items[:mid], search_item)
    elif guess < search_item:
        return high - 1 + recursive_binary_search(items[mid + 1:], search_item)
    else:
        return None


# testing part
search_list = [1, 3, 5, 7, 9]

print(recursive_binary_search(search_list, 1))
print(recursive_binary_search(search_list, 7))

for index, item in enumerate(search_list):
    assert recursive_binary_search(search_list, item) == index

# assert recursive_binary_search(search_list, -1) is None
