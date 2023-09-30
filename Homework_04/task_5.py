"""
* Пользователь вводит произвольное число. Посчитайте сумму цифр этого числа используя операторы % и //
Пример для числа 12.
Ответ должен быть получен примерно так:
answer = 12 % 10  # 2
answer += 12 // 10  # 1
print(answer)  # 3
"""

number = int(input("Введите число: "))
answer = 0

while number != 0:
    answer += number % 10
    number = number // 10

print(answer)
