"""
Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.
"""

def get_longest_word(text: str) -> str:
    words = text.split()
    the_longest_word = ""
    for element in words:
        if len(element) > len(the_longest_word):
            the_longest_word = element
    return the_longest_word


assert get_longest_word("The only thing in life achieved without effort is failure") == "achieved"
assert get_longest_word("The only thing in life achieved without effort is failure") != "failure"
assert get_longest_word("Too many of us are not living our dreams because we are living our fears") == "because"
assert get_longest_word("Too many of us are not living our dreams because we are living our fears") != "living"
assert get_longest_word("") == ""

