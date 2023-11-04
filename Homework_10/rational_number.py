def nod(x: int, y: int) -> int:
    """Получение наибольшего общего делителя"""
    for i in range(min(abs(x), abs(y)), 0, -1):
        if x % i == 0 and y % i == 0:
            return i

class Rational:
    __numerator: int
    __denominator: int

    def __init__(self, numerator: int, denominator: int):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__normalise()

    @property
    def numerator(self) -> int:
        return self.__numerator

    @property
    def denominator(self) -> int:
        return self.__denominator

    def __normalise(self):
        n = nod(self.__numerator, self.__denominator)
        self.__numerator //= n
        self.__denominator //= n
        if self.__denominator < 0:
            self.__denominator *= -1
            self.__numerator *= -1

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other: 'Rational') -> 'Rational':
        new_num = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        new_den = self.__denominator * other.__denominator
        return Rational(new_num, new_den)

    def __sub__(self, other: 'Rational') -> 'Rational':
        new_num = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        new_den = self.__denominator * other.__denominator
        return Rational(new_num, new_den)

    def __eq__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num == second_num

    def __ne__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num != second_num

    def __lt__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num < second_num

    def __gt__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num > second_num

    def __le__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num <= second_num

    def __ge__(self, other: 'Rational') -> bool:
        first_num = self.__numerator * other.__denominator
        second_num = self.__denominator * other.__numerator
        return first_num >= second_num


if __name__ == '__main__':
    first_rational = Rational(2, 5)
    second_rational = Rational(3, 4)

    assert first_rational.numerator == 2
    assert second_rational.denominator == 4
    assert str(first_rational) == "2 / 5"
    assert str(second_rational) == "3 / 4"
    assert first_rational * second_rational == Rational(6, 20)
    assert first_rational / second_rational == Rational(8, 15)
    assert first_rational + second_rational == Rational(23, 20)
    assert first_rational - second_rational == Rational(-7, 20)

    assert Rational(2, 8) != Rational(2, 4)
    assert first_rational < second_rational
    assert Rational(6, 9) > Rational(2, 5)
    assert Rational(1, 5) <= Rational(2, 1)
    assert Rational(3, 4) >= Rational(3, 4)

    assert Rational(2, 4) == Rational(1, 2)
    assert Rational(-1, -2) == Rational(1, 2)

    a = Rational(1, 4)
    b = Rational(3, 2)
    c = Rational(1, 8)
    d = Rational(156, 100)
    assert a * (b + c) + d == Rational(1573, 800)
