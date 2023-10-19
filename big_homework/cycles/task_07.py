"""
Дан словарь "слово" -> число. Вывести ключ, соответствующий максимальному значению.
Пример: {'a': 1, 'b': 2} -> 'b'.
"""

dict_elem = {"one": 1, "two": 2, "three": 3}
max_key = None
max_value = None

for key, value in dict_elem.items():
    if max_value is None or value > max_value:
        max_key = key
        max_value = value

print(max_key)