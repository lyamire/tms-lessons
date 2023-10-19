"""
Дан словарь "слово" -> число. Вывести максимальное число среди значений словаря.
Пример: {'a': 1, 'b': 2} -> 2.
"""

dict_elem = {"one": 1, "two": 2, "three": 3}
max_value = None

for key, value in dict_elem.items():
    if max_value is None or value > max_value:
        max_value = value

print(max_value)
