number = int(input("Введите число: "))
answer = 0

while number != 0:
    answer += number % 10
    number = number // 10

print(answer)
