months = {"January": 31,
          "February": 28,
          "March": 31,
          "April": 30,
          "May": 31,
          "June": 30,
          "July": 31,
          "August": 31,
          "September": 30,
          "October": 31,
          "November": 30,
          "December": 31}

month = input("Введите месяц: ").capitalize()
day = int(input("Введите день: "))

days_in_month = months[month]
result = day <= days_in_month

print(result)