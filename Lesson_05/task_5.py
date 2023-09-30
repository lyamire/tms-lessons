"""
Напишите функцию is_palindrome, которая принимает на вход строку, и возвращает True если это палиндром, иначе False.
"""

def is_palindrome(stroke):
    if stroke == stroke[::-1]:
        return True
    else:
        return False


assert is_palindrome(stroke="поп")
assert not is_palindrome(stroke="dsgsdy")
