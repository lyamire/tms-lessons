x = int(input("Сумма рублей: "))
y = int(input("Количество лет: "))

result = x * ((1 + 0.1) ** y)
print(round(result))

# r2 = x
# for i in range(y):
#     r2 = r2 + r2 * 0.1
#     print(f"Год {i + 1} = {r2}")
