number = int(input("Введите число: "))

result = True

if number > 1:
    for i in range(2, number):
        divisor = number % i == 0
        if divisor:
            result = False

print(result)
