# demonstrate the usage of variable length arguments


def add_values(*args):
    """ add_values(*args) --> add all the values provided

    Parameters
    *args: variable length argument, values you want to add.
    """
    sum = 0
    for arg in args:
        sum += arg
    return sum


def main():
    """ main() --> main function will run only if the module is executed directly.
    """
    print(add_values(1, 2, 3, 4, 5))


if __name__ == "__main__":
    main()
