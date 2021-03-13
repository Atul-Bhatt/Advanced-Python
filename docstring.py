# demonstrating the use of a function docstring


def dummyFunction(arg1, arg2):
    """ dummyFunction(arg1, arg2) --> Doesn't do anything

    Parameters
    arg1: First argument
    arg2: Second argument
    """


def main():
    """ main() --> runs if the module is running directly
    """
    print(dummyFunction.__doc__)


if __name__ == "__main__":
    main()
