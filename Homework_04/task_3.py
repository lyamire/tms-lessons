"""
Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
Если он ответил “yes” - завершите программу.
Если он ответил “no” - продолжайте - продолжайте вывод чисел.
Если что-то другое - напечатайте "Don't understand you" и продолжайте спрашивать до тех пор, пока ответ не будет корректным.
"""

for number in range(0, 101):
    print(number)

    answer = ""
    while True:
        answer = input("Should we break? ")
        if answer == "yes" or answer == "no":
            break
        else:
            print("Don't understand you")

    if answer == "yes":
        break


