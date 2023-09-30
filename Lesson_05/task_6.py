"""
Напишите функцию list_sum, которая принимает на вход список и возвращает сумму элементов списка.
Использование встроенной функции sum запрещено.
"""

def list_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result


assert list_sum([1, 2, 3, 4, 5]) == 15
assert list_sum([1, 2, 3, 4, 5]) != 20
