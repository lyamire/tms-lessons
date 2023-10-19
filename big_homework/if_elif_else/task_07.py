"""
Дано три числа. Вывести количество положительных чисел среди них.
"""

a, b, c = list(map(int, input("Введите три числа через пробел: ").split()))

count = 0

if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1

print(count)

