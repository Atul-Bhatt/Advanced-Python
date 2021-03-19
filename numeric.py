# demonstrate objects number like behavior (operator overloading)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: define repr function
    def __repr__(self):
        return f"<Point {self.x}, {self.y}>"

    # TODO: define add function
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # TODO: define sub function
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # TODO: define in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return Point(self.x, self.y)


def main():
    # Initial Point Object
    P1 = Point(10, 20)
    P2 = Point(20, 30)

    # TODO: use + operator to add two points
    P1 = P1 + P2
    print(P1, P2)

    # TODO: use - operator to subtract one point from another
    P1 = P1 - P2
    print(P1, P2)

    # TODO: use += to add two points
    P1 += P2
    print(P1, P2)


if __name__ == '__main__':
    main()
