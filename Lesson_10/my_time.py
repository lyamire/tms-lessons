class MyTime:
    def __init__(self, seconds: float):
        self.seconds = seconds

    @property
    def hours(self) -> int:
        return int(self.seconds) // 3600

    @property
    def minutes(self) -> int:
        return int(self.seconds) // 60 % 60

    def __mul__(self, other: float) -> "MyTime":
        return MyTime(self.seconds * other)

    def __truediv__(self, other: float) -> "MyTime":
        return MyTime(self.seconds / other)

    def __add__(self, other: "MyTime") -> "MyTime":
        return MyTime(self.seconds + other.seconds)

    def __sub__(self, other: "MyTime") -> "MyTime":
        return MyTime(self.seconds - other.seconds)

    def get_formatted_str(self) -> str:
        """Возвращает строку в формате 'HH:MM:SS.S'"""
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds % 60:04.1f}"

    def __str__(self) -> str:
        return f"{self.seconds}s"

    def __eq__(self, other: "MyTime") -> bool:
        return self.seconds == other.seconds

    def __ne__(self, other: "MyTime") -> bool:
        return self.seconds != other.seconds

    def __lt__(self, other: "MyTime") -> bool:
        return self.seconds < other.seconds

    def __gt__(self, other: "MyTime") -> bool:
        return self.seconds > other.seconds

    def __le__(self, other: "MyTime") -> bool:
        return self.seconds <= other.seconds

    def __ge__(self, other: "MyTime") -> bool:
        return self.seconds >= other.seconds


if __name__ == '__main__':
    time = MyTime(3724.5)
    assert time.hours == 1
    assert time.minutes == 2
    assert time.get_formatted_str() == '01:02:04.5'
    assert str(time) == '3724.5s'
    assert MyTime(10) * 2 == MyTime(20)
    assert MyTime(10) / 2 != MyTime(6)
    assert MyTime(20) + MyTime(30) > MyTime(10)
    assert MyTime(4) - MyTime(2) < MyTime(10)
    assert MyTime(360) >= MyTime(360)
    assert MyTime(360) <= MyTime(360)
