import copy
from test_utils import test_sort


def bubble_sort(lst: list) -> list:
    lst = copy.deepcopy(lst)
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    test_sort(bubble_sort)

