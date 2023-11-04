from my_time import MyTime


class MyTimeInterval:
    start: MyTime
    finish: MyTime

    def __init__(self, start_second, finish_second):
        self.start = MyTime(start_second)
        self.finish = MyTime(finish_second)

    def is_inside(self, time: MyTime) -> bool:
        return self.start <= time <= self.finish

    def intersects(self, other: "MyTimeInterval") -> bool:
        return self.start <= other.finish and self.finish >= other.start


if __name__ == '__main__':
    interval = MyTimeInterval(10, 20)

    assert interval.is_inside(MyTime(15))
    assert interval.is_inside(MyTime(10))
    assert interval.is_inside(MyTime(20))
    assert not interval.is_inside(MyTime(5))
    assert not interval.is_inside(MyTime(25))

    assert interval.intersects(MyTimeInterval(5, 15))
    assert interval.intersects(MyTimeInterval(5, 25))
    assert interval.intersects(MyTimeInterval(10, 25))
    assert interval.intersects(MyTimeInterval(11, 19))
    assert not interval.intersects(MyTimeInterval(0, 5))
    assert not interval.intersects(MyTimeInterval(25, 30))
