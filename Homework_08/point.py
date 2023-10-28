class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to_point(self, second_point) -> float:
        tx = self.x - second_point.x
        ty = self.y - second_point.y
        return (tx ** 2 + ty ** 2) ** 0.5


p1 = Point(3, 4)
p2 = Point(3, 10)
p3 = Point(10, 10)

print('Distance between p1 and zero point:', p1.distance_to_zero())
print('Distance between p2 and zero point:', p2.distance_to_zero())
print('Distance between p3 and zero point:', p3.distance_to_zero())
print('Distance between p1 and p1:', p1.distance_to_point(p1))
print('Distance between p1 and p2:', p1.distance_to_point(p2))
print('Distance between p2 and p1:', p2.distance_to_point(p1))
print('Distance between p1 and p3:', p1.distance_to_point(p3))
print('Distance between p2 and p3:', p2.distance_to_point(p3))
