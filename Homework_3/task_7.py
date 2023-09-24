"""
Определить является ли число простым
"""

number = int(input("Введите число: "))

result = True

if number > 1:
    for i in range(2, number):
        remainder = number % i == 0  # проверка, что число является делитель
        if remainder:
            result = False
            break
else:
    result = False

print(result)
