"""
Напишите функцию my_round, аналог встроенной round.
Использование самой функции round запрещено.
"""

def my_round(number: float, digits: int):
    delimiter = 0.1 ** digits
    result_int = number // delimiter
    result_int = result_int * delimiter
    return float(f"{result_int:.10f}")


assert my_round(number=3.443534, digits=3) == 3.443
assert my_round(number=3.443534, digits=3) != 2.44
