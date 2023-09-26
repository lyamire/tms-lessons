import random
number = random.randint(1, 5)

solved = False
while not solved:
    entered_number = int(input("Введите число от 1 до 5: "))
    if entered_number == number:
        print("Поздравляю, Вы угадали число")
    else:
        print("Вы не угадали, попробуйте еще раз ")

