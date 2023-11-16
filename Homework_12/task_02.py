import re
def is_date(stroke: str) -> bool:
    regex = r'(0[1-9]|[1-2]\d|30|31)-(0[1-9]|1[0-2])-\d{4}'
    return re.fullmatch(regex, stroke) is not None


if __name__ == '__main__':
    assert is_date('26-10-2023')
    assert is_date('01-01-1500')
    assert is_date('31-12-2022')
    assert is_date('01-01-8989')
    assert not is_date('32-12-2022')
    assert not is_date('01-13-2022')
    assert not is_date('00-12-2022')
    assert not is_date('as-as-asdf')
    assert not is_date('@#-@#-#@#$')
    assert not is_date('234-234-23')
    assert not is_date('ᓚᘏᗢ')
