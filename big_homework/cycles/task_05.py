"""
Дана строка. Посчитайте сколько раз в ней встречается символ "a".
"""

stroke = input()
count = 0

for i in stroke:
    if i == "a":
        count += 1

print(count)

