# demonstrate the usage of filter and map functions


def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def squareFunc(x):
    return x**2


def toGrade(x):
    if x > 90:
        return "A"
    elif x > 80:
        return "B"
    elif x > 70:
        return "C"
    elif x > 60:
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 23, 2, 34, 44, 32, 74)
    chars = "aXyILiAWbscIL"
    grades = (89, 76, 85, 44, 56, 90, 34)

    # TODO: use filter to remove items from a list
    odds = list(filter(filterFunc, nums))
    print(odds)

    # TODO: use filter on non-numeric sequence
    lower = list(filter(filterFunc2, chars))
    print(lower)

    # TODO: use map to create a new sequence of values
    square = list(map(squareFunc, nums))
    print(square)

    # TODO: use sorted and map to change numbers to grades
    grade_letter = list(map(toGrade, sorted(grades)))
    print(grade_letter)


if __name__ == '__main__':
    main()
