import test_utils

def merge_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    middle: int = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    sorted_lst = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1

    if i < len(left):
        sorted_lst += left[i:]
    if j < len(right):
        sorted_lst += right[j:]
    return sorted_lst


if __name__ == '__main__':
    test_utils.test_sort(merge_sort)
