"""
Дан номер месяца (число от 1 до 12). Выведите пору года, которой этот месяц принадлежит: зима, весна, лето или осень.
"""

month = int(input())

if month == 3 or month == 4 or month == 5:
    print("весна")
elif month == 6 or month == 7 or month == 8:
    print("лето")
elif month == 9 or month == 10 or month == 11:
    print("осень")
else:
    print("зима")



#match month:
#   case 3 | 4 | 5:
#        print("весна")
#    case 6 | 7 | 8:
#        print("лето")
#    case 9 | 10 | 11:
#        print("осень")
#    case 12 | 1 | 2:
#        print("зима")

