"""
Напишите функцию simple_compare, которая принимает два числа и возвращает True,
если первое число меньше второго. Иначе возвращает False.
"""

def simple_compare(x, y) -> bool:
    return True if x < y else False


assert simple_compare(1, 2) is True
assert simple_compare(2, 1) is False


