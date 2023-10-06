"""
Напишите функцию-декоратор my_decorator, в которую можно обернуть функцию, которая принимает один входной параметр.
Ваш декоратор должен будет выводить в консоль входной параметр оборачиваемой функции, запускать функцию,
а затем выводить результат этой функции.

Ожидаемый вывод программы:
Функция получила на вход значение 3
Результат функции: 9
y = 9
"""

def my_decorator(original_func):
    def wrapper(x):
        print(f"Функция получила на вход значение {x}")
        y = original_func(x)
        print(f"Результат функции {y}")
        return y

    return wrapper


@my_decorator
def my_func(x):
    return x ** 2


y = my_func(3)
print(f'y = {y}')
