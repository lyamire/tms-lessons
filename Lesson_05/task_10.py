"""
Напишите функцию filter_odd_numbers, которая принимает на вход список целых чисел и возвращает новый список,
состоящий из элементов первоначального, но без нечётных чисел.
"""

def filter_odd_numbers(*args):
    new_arr = [i for i in args if i % 2 == 0]
    return new_arr


assert filter_odd_numbers(1, 2, 3, 4, 5) == [2, 4]