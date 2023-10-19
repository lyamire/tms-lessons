"""
Дан список чисел. Если среди них есть ноль - вывести yes, иначе no.
"""

lst = list(map(int, input("Введите числа через пробел: ").split()))
answer = None

for i in lst:
    if i == 0:
        answer = "Yes"
        break
    else:
        answer = "No"
print(answer)

