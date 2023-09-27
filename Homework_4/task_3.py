import random

answered = False

while not answered:
    number = random.randint(0, 100)
    print(number)

    while True:
        answer = input("Should we break? ")
        if answer == "yes":
            answered = True
            break
        elif answer == "no":
            break

        print("Don't understand you")
