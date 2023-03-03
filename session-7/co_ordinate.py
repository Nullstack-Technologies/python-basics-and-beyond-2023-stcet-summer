import math

class Coordinate:

    def distance(self, other):
        return math.sqrt(
            (other.y - self.y)**2 + (other.x - self.x)**2
        )

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def add(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def midpoint(self, other):
        return Coordinate(
            (self.x + other.x)/2, (self.y + other.y)/2
        )

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

c = Coordinate(1, 2)
c1 = Coordinate(3, 4)
c2 = Coordinate(0, 0)
c3 = Coordinate(1, 1)

# print(c)
# print(c1)
# print(c == c1)
# print(c2.distance(c3))
# print(c3.distance(c2))

c5 = c1.add(c3)
print(c5)
print(c.midpoint(c1))

c6 = c1 - c
print(c6)