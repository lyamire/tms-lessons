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


