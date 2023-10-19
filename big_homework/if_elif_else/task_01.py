"""
Даны два числа, если они равны выведите yes, иначе - no.
"""

a, b = map(int, input("Введите два числа через пробел: ").split())
print("Yes" if a == b else "No")
