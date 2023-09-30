"""
Создать функцию sum_and_max, которая принимает на вход неопределенное количество аргументов и возвращает их сумму
и максимальное из них. Использовать встроенные sum и max разрешено.
"""

def sum_and_max(*args):
    sum_element = 0
    max_element = args[0]
    for element in args:
        sum_element += element
        if element > max_element:
           max_element = args[element]
    return sum_element, max_element


assert sum_and_max(1, 2, 3, 4, 5) == (15, 5)
assert sum_and_max(1, 2, 3, 4, 5) != (16, 1)