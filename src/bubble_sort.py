def find_smallest(items):
    """Find smallest value in list"""
    if not len(items):
        return None

    smallest_index = 0

    for index, item in enumerate(items):
        if items[smallest_index] > item:
            smallest_index = index

    return smallest_index


assert find_smallest([3, 5, 7, 1, 9]) == 3
assert find_smallest([]) is None


def selection_sort(items):
    """Sort list items by selection sort"""
    sorted_list = []
    for i in range(len(items)):
        smallest = find_smallest(items)
        sorted_list.append(items.pop(smallest))

    return sorted_list


assert selection_sort([3, 5, 7, 1, 9]) == [1, 3, 5, 7, 9]
