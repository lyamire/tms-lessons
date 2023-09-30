"""
Напишите функцию is_year_leap, которая принимает число (год) и возвращает True если год високосный, False если нет.
"""


def is_year_leap(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    else:
        return False


assert is_year_leap(2004)
assert is_year_leap(2020)
assert is_year_leap(2000)
assert is_year_leap(1600)
assert not is_year_leap(2003)
assert not is_year_leap(1700)

