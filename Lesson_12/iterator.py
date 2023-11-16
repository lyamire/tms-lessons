class SquaresIterable:
    def __init__(self, count):
        self.count = count
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_number += 1
        if self.current_number > self.count:
            raise StopIteration()
        return self.current_number ** 2


if __name__ == '__main__':

    for i in SquaresIterable(10):
        print(i)

    assert [x for x in SquaresIterable(3)] == [1, 4, 9]
    assert [x for x in SquaresIterable(5)] == [1, 4, 9, 16, 25]
    assert [x for x in SquaresIterable(10)] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert [x for x in SquaresIterable(3)] != [1, 4, 9, 16, 25]
    assert [x for x in SquaresIterable(3)] != ["1", "4", 9, 16, 25]
    assert [x for x in SquaresIterable(3)] != ["f", "r", 9, 16, 25]
