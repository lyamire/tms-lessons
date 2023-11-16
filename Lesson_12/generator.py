def generate_squares(count):
    x = 1
    while x <= count:
        yield x ** 2
        x += 1


if __name__ == '__main__':

    for i in generate_squares(10):
        print(i)

    assert [i for i in generate_squares(10)] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert [i for i in generate_squares(5)] == [1, 4, 9, 16, 25]
    assert [i for i in generate_squares(5)] != [1, 4, 9, 16, 25, 36, 49, 64]
    assert [i for i in generate_squares(5)] != ["1", "4", "9", "16", "25"]