"""
Напишите функцию filter_negative_numbers, которая принимает список чисел,
и возвращает новый список, составленный из элементов первого без отрицательных чисел,
"""

def filter_negative_numbers(list_n: list) -> list:
    return [i for i in list_n if i >= 0]


assert filter_negative_numbers([6, -5, 0, -1, 100]) == [6, 0, 100]
assert filter_negative_numbers([-6, -5, 0, -1, -100]) == [0]
