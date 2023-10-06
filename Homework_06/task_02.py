"""
Пользователь вводит произвольное количество маленьких латинских букв через пробел.
Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
Выведите результат работы на экран.
Пример:
Ввод пользователя: a b c d e f
Результат программы: ['b', 'c', 'd', 'f']
Используйте функцию filter.
Список всех гласных английского языка: a, e, i, o, u
"""

def remove_vowels(source_list: list[str]) -> list:
    vowels = ["a", "e", "i", "o", "u"]
    return list(filter(lambda x: x not in vowels, source_list))


assert remove_vowels(["a", "b", "c", "d", "e", "f"]) == ["b", "c", "d", "f"]
assert remove_vowels(["a", "a", "c", "d", "e", "f"]) == ["c", "d", "f"]

lst = input("Enter small letters with a space: ").split()
print(remove_vowels(lst))
