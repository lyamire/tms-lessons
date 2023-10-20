"""
Скопируйте функции прошлых 5 заданий в один файл.
Напишите программу, спрашивает у пользователя номер задачи, решение которой он хочет проверить,
пользователь вводит число от 1 до 5, в зависимости от выбранного номера запросите у пользователя входные данные
для задачи (если это нужно) и выведите ответ.
"""
from task_01 import hello_world
from task_02 import my_sum
from task_03 import simple_compare
from task_04 import compare
from task_05 import filter_negative_numbers


def input_two_numbers():
    x, y = map(int, input('Введите 2 числа через пробел: ').split())
    return x, y

def input_numbers_list():
    user_input = input('Введите числа, разделённые пробелом: ')
    return [int(num) for num in user_input.split()]


n = int(input("Введите номер задачи(1-5): "))
match n:
    case 1:
        hello_world()
    case 2:
        x, y = input_two_numbers()
        print(f"Сумма чисел: {my_sum(x, y)}")
    case 3:
        x, y = input_two_numbers()
        print(f"Первое число меньше второго? Ответ: {simple_compare(x, y)}")
    case 4:
        x, y = input_two_numbers()
        print(f"Результат сравнения: {compare(x, y)}")
    case 5:
        numbers = input_numbers_list()
        print(f"Удалили отрицательные числа из вашего списка: {filter_negative_numbers(numbers)}")
