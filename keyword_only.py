# demonstrating the use of keyword-only arguments


def dummyFunction(arg1, arg2, *, key_only_arg=False):
    """ dummyFunction(arg1, arg2, *, key_only_arg=False) --> This function doesn't do anything

    Parameters
    arg1: nothing
    arg2: nothing
    *: used to seperate positional argument from keyword-only arguments
    key_only_arg: can only be passed with keyword
    """
    pass


def main():
    # Cannot run the function without keyword
    #dummyFunction(1, 2, True)

    # TODO: run the function using keyword
    dummyFunction(1, 2, key_only_arg=True)


if __name__ == "__main__":
    main()
