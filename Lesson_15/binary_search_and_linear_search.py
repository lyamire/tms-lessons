import datetime
import random
def binary_search(lst: list, target: int):
    low = 0
    high = len(lst) - 1
    while low <= high:
        middle = (low + high) // 2
        if target == lst[middle]:
            return middle
        elif target > lst[middle]:
            low = middle + 1
        else:
            high = middle

def linear_search(lst: list[int], target: int) -> int:
    for index, num in enumerate(lst):
        if num == target:
            return index


if __name__ == '__main__':
    nums: list[int] = sorted([random.randint(-1000000, 1000000) for _ in range(1000000)])
    elem = nums[891920]

    before_1 = datetime.datetime.now()
    print(binary_search(nums, elem))
    total_1 = datetime.datetime.now() - before_1
    print(f"Затраченное время бинарного поиска {total_1.microseconds}")

    before_2 = datetime.datetime.now()
    print(linear_search(nums, elem))
    total_2 = datetime.datetime.now() - before_2
    print(f"Затраченное время линейного поиска {total_2.microseconds}")

    assert total_1.microseconds < total_2.microseconds
