import re

def is_float_number(stroke: str) -> bool:
    regex = r'\d+\.\d+'
    return re.fullmatch(regex, stroke) is not None


if __name__ == '__main__':
    assert is_float_number('1.0')
    assert is_float_number('3.14')
    assert is_float_number('2345436456457754745754574.23423423423423424')
    assert not is_float_number('1111')
    assert not is_float_number('1122.')
    assert not is_float_number('232423,34234')
    assert not is_float_number('wewetwe.werwrw')
    assert not is_float_number('!@#$.!@#$')
    assert not is_float_number('ʕ ᵔᴥᵔ ʔ')

