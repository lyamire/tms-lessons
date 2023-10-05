from task_01 import input_list
from functools import reduce

l = input_list()

print(f"Сумма чисел списка {reduce(lambda x, y: x + y, l, 0)}")
print(f"Минимальное число из списка {reduce(lambda x, y: min(x, y), l)}")
print(f"Произведение всех элементов {reduce(lambda x, y: x * y, l)}")
print(f"Факториал числа 5 {reduce(lambda x, y: x * y, range(1, 6))}")


# Напишите свою реализацию функции my_reduce. Для простоты можно сделать третий параметр обязательным.
def my_reduce(func, iterable, initializer=None):
    if initializer is None:
        result = next(iterable)
    else:
        result = initializer
    for el in iterable:
        result = func(result, el)
    return result


print(f"Сумма чисел списка {my_reduce(lambda x, y: x + y, l, 0)}")
print(f"Минимальное число из списка {my_reduce(lambda x, y: min(x, y), l, initializer= 1)}")
print(f"Произведение всех элементов {my_reduce(lambda x, y: x * y, l, 1)}")
print(f"Факториал числа 5 {my_reduce(lambda x, y: x * y, range(1, 6), 1)}")

