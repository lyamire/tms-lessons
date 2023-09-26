sum_numbers_100 = 0
for i in range(0, 101):
    sum_numbers_100 += i
print(f"{1} : {sum_numbers_100}")

sum_numbers_1000 = 0
for i in range(100, 1001):
    sum_numbers_1000 += i
print(f"{2} : {sum_numbers_1000}")

sum_numbers_1000_even = 0
for i in range(100, 1001, 2):
    sum_numbers_1000_even += i
print(f"{3} : {sum_numbers_1000_even}")

exponentiation = 1
for i in range(10):
    exponentiation *= 2
print(f"{4} : {exponentiation}")

sum_num = 0
i = 0
while sum_num < 1000:
    i += 1
    sum_num += i

print(f"{5} : {sum_num},  {i}")
