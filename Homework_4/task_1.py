sum_numbers_1 = 0
for i in range(0, 101, 5):
    sum_numbers_1 += i

print(sum_numbers_1)

sum_numbers_2 = 0
for i in range(0, 101):
    if i % 5 == 0:
        sum_numbers_2 += i
print(sum_numbers_2)

