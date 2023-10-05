def check_types(func):
    def inner_func(x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            print('Expected int type')
            return None
        return func(x, y)

    return inner_func

@check_types
def plus(x, y):
    return x + y


@check_types
def minus(x, y):
    return x - y


@check_types
def mult(x, y):
    return x * y


@check_types
def div(x, y):
    return x / y


assert plus(1, 2) == 3
assert not plus(x='1', y=2)
assert minus(x=5, y=3) == 2
assert not minus(x='2', y=4)




