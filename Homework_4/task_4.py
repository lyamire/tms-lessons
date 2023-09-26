import random
number = random.randint(1, 100)

while True:
    entered_number = int(input("Введите число от 1 до 100: "))
    if entered_number == number:
        print("Поздравляю, Вы угадали число")
        break
    elif entered_number > number:
        print("не угадал, число больше загаданного")
    elif entered_number < number:
        print("не угадал, число меньше загаданного")

