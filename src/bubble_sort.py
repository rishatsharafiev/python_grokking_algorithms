def bubble_sort(items):
    """Sort list items by bubble sort"""
    length = len(items)
    if len(items) < 2:
        return items

    for i in range(length):
        for j in range(0, length - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


assert bubble_sort([3, 5, 7, 1, 9]) == [1, 3, 5, 7, 9]
