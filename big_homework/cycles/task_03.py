"""
Дан список чисел. Найти их максимальное среди них.
"""

lst = list(map(int, input("Введите числа через пробел: ").split()))
max_number = lst[0]

for i in lst:
    if i > max_number:
        max_number = i

print(max_number)
