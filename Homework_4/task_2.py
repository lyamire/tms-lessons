import random

while True:
    number = random.randint(0,100)
    print(number)
    answer = input("Should we break? ")
    if answer == "yes":
        break
