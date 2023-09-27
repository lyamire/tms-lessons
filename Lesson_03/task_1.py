number_seconds = int(input("Введите число секунд: "))
number_minutes = number_seconds // 60
remainders_of_seconds = number_seconds % 60
print(str(number_minutes) + ":" + str(remainders_of_seconds))

