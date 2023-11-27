import copy
from test_utils import test_sort
def insertion_sort(lst: list) -> list:
    lst = copy.deepcopy(lst)
    for i in range(1, len(lst)):
        key = lst[i]
        while (i - 1 >= 0) and (lst[i - 1] > key):
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1

        lst[i] = key

    return lst


if __name__ == '__main__':
    test_sort(insertion_sort)


