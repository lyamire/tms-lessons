"""
 Напишите функцию get_most_frequent_word, которая на вход принимает текст (только английские слова и пробелы),
 и возвращает самое часто встречающееся слово. Если таких слов несколько - верните любое.
"""

def get_most_frequent_word(text: str) -> str:
    words_counter = {}
    words = text.split()
    for element in words:
        counter = words_counter.get(element, 0)
        counter += 1
        words_counter[element] = counter
    most_frequent_word = ""
    most_frequent_count = 0
    for element in words_counter:
        if words_counter.get(element) > most_frequent_count:
            most_frequent_word = element
            most_frequent_count = words_counter.get(element)
    return most_frequent_word


assert (get_most_frequent_word("hello this is a string with words and spaces and big big woooooooooord and and and")
        == "and")
assert (get_most_frequent_word("hello this is a string with words and spaces and big big woooooooooord and and and")
        != "woooooooooord")
assert get_most_frequent_word("All the world is made of faith and trust and pixie dust") == "and"
assert get_most_frequent_word("All the world is made of faith and trust and pixie dust") != "is"

