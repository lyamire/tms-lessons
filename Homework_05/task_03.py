"""
Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список,
состоящий из их квадратов.
То есть generate_squares(1, 2, 3) -> [1, 4, 9]
"""

def generate_squares(*args) -> list:
    return [i ** 2 for i in args]


assert generate_squares(1, 2, 3) == [1, 4, 9]
assert generate_squares(1, 2, 3) != [2, 6, 7]
assert generate_squares(1, 3, 5, 9, 22) == [1, 9, 25, 81, 484]
assert generate_squares(1, 3, 5, 9, 22) != [0, 10, 25, 81, 424]
assert generate_squares(1, 0, -1, 1.5) == [1, 0, 1, 2.25]
assert generate_squares(1, 0, -1, 1.5) != [1, 0.9, -1, 2]
