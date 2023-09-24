from math import sqrt

side = int(input("Введите сторону квадрата: "))
p = side * 4
s = side ** 2
d = side * sqrt(2)
result = (p, s, d)

print(result)
