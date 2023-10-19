"""
Дан список чисел. Найти их сумму.
"""

lst = list(map(int, input("Введите числа через пробел: ").split()))
count_numbers = 0

for i in lst:
    count_numbers += i

print(count_numbers)

