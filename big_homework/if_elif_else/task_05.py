"""
Даны три числа. Если они все больше 0 - вывести yes, иначе - no.
"""

a, b, c = map(int, input("Введите три числа через пробел: ").split())
print("Yes" if a > 0 and b > 0 and c > 0 else "No")

