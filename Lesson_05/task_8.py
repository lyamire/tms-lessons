"""
Напишите функцию my_round, аналог встроенной round.
Использование самой функции round запрещено.
"""

def my_round(number: float, digits: int = 0):
    multiplier = 10 ** digits
    diff = 0.5
    if number < 0:
        diff = -0.5
    round_number = int(number * multiplier + diff) / multiplier
    return round_number


assert my_round(number=3.443534, digits=3) == 3.444
assert my_round(123.456, 3) == 123.456
assert my_round(123.456, 2) == 123.46
assert my_round(123.456, 1) == 123.5
assert my_round(123.456) == 123.0
assert my_round(123.456, -1) == 120.0
assert my_round(123.456, -2) == 100.0
assert my_round(123.456, -3) == 0.0
assert my_round(3.443534, 1) == 3.4
assert my_round(123.567, 2) == 123.57
assert my_round(123.890, 2) == 123.89
assert my_round(-123.456, 2) == -123.46
assert my_round(1.5) == 2
assert my_round(2.5) == 3
