# demonstrate the working of namedtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)

    # TODO: use _replace to create a new instance
    p1 = p1._replace(x=50)
    print(p1, p2)


if __name__ == "__main__":
    main()
