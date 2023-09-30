"""
Вывести на экран числа кратные 5 от 0 до 100 включительно.
"""

# variant 1 Сделать это с помощью функции range с шагом 5


sum_numbers_1 = 0
for i in range(0, 101, 5):
    sum_numbers_1 += i


assert sum_numbers_1 == 1050
assert sum_numbers_1 != 1055


# variant 2 Сделать это с помощью функции range c шагом 1 и вложенным if


sum_numbers_2 = 0
for i in range(0, 101):
    if i % 5 == 0:
        sum_numbers_2 += i


assert sum_numbers_2 == 1050
assert sum_numbers_2 != 1150
