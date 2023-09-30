'''
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования (целое
число), которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
Написать также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
Подсказка: см. функции ord и chr.
'''

def xor_cipher(stroke: str, n: int) -> str:
    encoded_str = ''
    for element in stroke:
        code = ord(element)
        code = code ^ n
        encoded_str += chr(code)
    return encoded_str

assert xor_cipher('test', 42) != '1111'

assert xor_cipher('test', 42) == '^OY^'
assert xor_cipher('^OY^', 42) == 'test'

assert xor_cipher(xor_cipher('test', 42), 42) == 'test'


