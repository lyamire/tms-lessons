import random
number = random.randint(1, 5)

while True:
    entered_number = int(input("Введите число от 1 до 5: "))
    if entered_number == number:
        print("Поздравляю, Вы угадали число")
        break
    else:
        print("Вы не угадали, попробуйте еще раз ")

