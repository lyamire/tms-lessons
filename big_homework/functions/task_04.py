"""
Напишите функцию compare, которая принимает два числа и возвращает -1 если первое число меньше второго,
1 если первое больше второго, и 0 если они равны.
Примеры:
compare(100, 200) -> -1
compare(200, 100) -> 1
compare(10, 10) -> 0
"""

def compare(x, y) -> int:
    return -1 if x < y else 1 if x > y else 0


assert compare(1, 2) == -1
assert compare(2, 1) == 1
assert compare(2, 2) == 0

