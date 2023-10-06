"""
Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
Вам по прежнему нужно удалить все гласные. При этом вывести результат нужно вывести сохранив изначальный регистр.
Пример:
Ввод пользователя: a B c d E F
Результат программы: ['B', 'c', 'd', 'F']
Используйте функцию filter.
"""

def remove_vowels(source_list: list[str]) -> list:
    vowels = ["a", "e", "i", "o", "u"]
    return list(filter(lambda x: x.lower() not in vowels, source_list))


assert remove_vowels(["a", "B", "c", "d", "e", "f"]) == ["B", "c", "d", "f"]
assert remove_vowels(["A", "a", "c", "d", "E", "F"]) == ["c", "d", "F"]

lst = input("Enter letters with a space: ").split()
print(remove_vowels(lst))
