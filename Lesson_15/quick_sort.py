import test_utils
def quick_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = [i for i in lst if i < pivot]
    center = [i for i in lst if i == pivot]
    right: list[int | float] = [i for i in lst if i > pivot]
    return quick_sort(left) + center + quick_sort(right)


if __name__ == '__main__':
    test_utils.test_sort(quick_sort)