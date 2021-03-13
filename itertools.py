# advanced iterator functions in ther itertools package
import itertools


def testFunction(x):
    if x > 40:
        return False
    return True


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    names = ["John", "Casey", "Nile"]
    cycle_names = itertools.cycle(names)
    print(next(cycle_names))
    print(next(cycle_names))
    print(next(cycle_names))
    print(next(cycle_names))

    # TODO: use count to create a simple counter
    count = itertools.count(100, 10)
    print(next(count))
    print(next(count))
    print(next(count))

    # TODO: accumulate creates an iterator that accumulate values
    values = [10, 70, 34, 23, 50, 12, 11]
    print(list(itertools.accumulate(values)))

    print(list(itertools.accumulate(values, max)))

    # TODO: use chain to connect sequences together
    letters = "ABCDEF"
    byte_values = [0x24, 0x25, 0x26, 0x27, 0x28,
                   0x29, 0x30, 0x31, 0x33, 0x34, 0x12, 0x55]
    print(list(itertools.chain(values, letters, byte_values)))

    # TODO: dropwhile and takewhile will return values until a certain
    # condition is met that stops them
    print(list(itertools.dropwhile(testFunction, values)))
    print(list(itertools.takewhile(testFunction, values)))


if __name__ == '__main__':
    main()
