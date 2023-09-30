"""
Напишите функцию hello, которая принимает на вход строку (имя) и возвращает строку "Hello {имя}".
Вызовите написанную функцию и выведите результат на экран.
"""

def hello_2(name):
    return f"Hello {name}"


assert hello_2(name="Tatsiana") == "Hello Tatsiana"
