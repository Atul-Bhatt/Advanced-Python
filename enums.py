# Demnonstrate the working of enums

from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    GRAPE = 3
    TOMATO = 4
    # ORANGE = 1    cannot have repetitive elements with a @unique decorator
    PEAR = auto()


def main():
    # TODO: enums have human readable values and types
    print(Fruit.APPLE)

    # TODO: enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # TODO: print the auto generated value
    print(Fruit.PEAR.name, Fruit.PEAR.value)

    # TODO: enums are hashable - can be used as keys\
    my_fruits = {}
    my_fruits[Fruit.APPLE] = "I am an Apple."
    print(my_fruits)


if __name__ == "__main__":
    main()
