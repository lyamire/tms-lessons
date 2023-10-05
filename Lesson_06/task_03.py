from task_01 import input_list

l = input_list("Enter numbers: ")

positive_numbers_removed = list(filter(lambda x: x > 0, l))
print(f"Отфильтрованный список без отрицательных чисел  {positive_numbers_removed}")
even_numbers_removed = list(filter(lambda x: x % 2 == 0, l))
print(f"Отфильтрованный список без нечетных чисел {even_numbers_removed}")


positive_counter = len(list(filter(lambda x: x < 0, l)))
zero_counter = len(list(filter(lambda x: x == 0, l)))
negative_counter = len(list(filter(lambda x: x > 0, l)))
print(f"Количество положительных чисел: {positive_counter}, количество нулей в списке: {zero_counter}, количество "
      f"отрицательных чисел: {negative_counter}")


# Напишите свою реализацию функций my_filter, возвращающую список
def my_filter_v1(function, iterable):
    return (i for i in iterable if function(i))

print(list(my_filter_v1(lambda x: x > 0, l)))
print(list(my_filter_v1(lambda x: x % 2 == 0, l)))


#Напишите свою реализацию функций my_filter, которая вместо возвращения списка использует ключевое слово yield
# при генерации очередного элемента.

def my_filter_v2(function, iterable):
    for i in iterable:
        if function(i):
            yield i

print(list(my_filter_v2(lambda x: x > 0, l)))
print(list(my_filter_v2(lambda x: x % 2 == 0, l)))
