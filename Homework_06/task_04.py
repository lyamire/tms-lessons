"""
Пользователь вводит произвольное количество слов через пробел. Затем (на следующей строке) вводит один символ (разделитель).
Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить, и возвращает строку,
в которой все слова из списка соединены через символ разделитель.
Пример ввода пользователя:
hello this is my string
@
Вывод программы: hello@this@is@my@string
"""
from functools import reduce

def my_join(source_list: list[str], separator: str):
    return reduce(lambda x, y: x + separator + y, source_list)


assert my_join("hello this is my string".split(), "@") == "hello@this@is@my@string"
assert my_join("test test".split(), "*") == "test*test"


lst = input("Enter words with a space: ").split()
sep = input("Enter a symbol to separate: ")

print(my_join(lst, sep))
