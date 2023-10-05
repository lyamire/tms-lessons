from task_01 import input_list

l = input_list("Enter numbers: ")

print(f"Каждый элемент увеличен на 100: {list(map(lambda x: x * 100, l))}")
print(f"Каждый элемент преобразован в строку {list(map(lambda x: str(x), l))}")
print(f"Каждый элемент разделен на 100 и округлен до целого цисла {list(map(lambda x: round(x / 100), l))}")

# Напишите свою реализацию функций my_map, возвращающую список.

def my_map_v1(func, iterables) -> list:
    return [func(i) for i in iterables]


print(my_map_v1(lambda x: x * 100, l))
print(my_map_v1(lambda x: str(x), l))
print(my_map_v1(lambda x: round(x / 100), l))


# Напишите свою реализацию функций my_map, которая вместо возвращения списка использует
# ключевое слово yield при генерации очередного элемента.

def my_map_v2(func, iterables) -> list:
    for i in iterables:
        yield func(i)

print(list((my_map_v2(lambda x: x * 100, l))))
print(list((my_map_v2(lambda x: str(x), l))))
print(list((my_map_v2(lambda x: round(x / 100), l))))

