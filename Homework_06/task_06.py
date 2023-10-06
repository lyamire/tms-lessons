"""
Решите прошлую задачу так, чтобы ваш декоратор работал для любой функции, с любым количеством параметров.
А также чтобы работало с именованными параметрами.
Подсказка: используйте *args и **kwargs.

Ожидаемый вывод программы:
Функция получила на вход значение (1, 2) {'d': 3, 'c': 4}
Результат функции: 10
y = 10
"""
def my_decorator(original_func):
    def wrapper(*args, **kwargs):
        print(f"Функция получила на вход значение {args} {kwargs} ")
        y = original_func(*args, **kwargs)
        print(f"Результат функции: {y}")
        return y
    return wrapper


@my_decorator
def my_func(a, b, c, d):
    return a + b + c + d


y = my_func(1, 2, c=3, d=4)
print(f'y = {y}')
