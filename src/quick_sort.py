import random


def quick_sort(items):
    """Quick sort of items"""
    if len(items) < 2:
        return items
    else:
        pivot = random.choice(items)
        index = items.index(pivot)
        items.pop(index)

        less = [item for item in items if item <= pivot]
        greater = [item for item in items if item > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


assert quick_sort([3, 5, 7, 1, 9]) == [1, 3, 5, 7, 9]
