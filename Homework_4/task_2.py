import random

number = random.randint(0,100)

while True:
    print(number)
    answer = input("Should we break? ")
    if answer == "yes":
        break