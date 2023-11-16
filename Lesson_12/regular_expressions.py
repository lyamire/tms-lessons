import re
def is_car_number(stroke: str) -> bool:
    result = re.fullmatch(r'\d{4}[A-Z]{2}-\d', stroke)
    return result is not None

def is_phone_number(stroke: str) -> bool:
    result = re.fullmatch(r'\+375 ?\(?(29|25|33|44)\)? ?\d{3}-?\d{2}-?\d{2}', stroke)
    return result is not None


if __name__ == '__main__':

    assert is_car_number("1234AB-5")
    assert is_car_number("4576MO-2")
    assert not is_car_number("AX2323-Z")
    assert not is_car_number("ZZZZ98-Z")
    assert not is_car_number("!!!!23-@")
    assert not is_car_number("апке34-@")
    
    assert is_phone_number("+375 (29) 123-45-67")
    assert is_phone_number("+375 (25) 126-43-67")
    assert is_phone_number("+375 (33) 126-43-67")
    assert is_phone_number("+37544126-43-67")
    assert is_phone_number("+375441264367")
    assert not is_phone_number("+375 (45) 126-43-67")
    assert not is_phone_number("+375 [45] 126-43-67")
