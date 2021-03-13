# demonstrate built in functions of Python


def main():
    # create a list with numeric values
    list_1 = [1, 2, 3, 0, 4]

    # TODO: any() and all() functions
    print(any(list_1))
    print(all(list_1))

    # TODO: min() and max() functions
    print("Min: ", min(list_1))
    print("Max: ", max(list_1))

    # TODO: sum() function
    print("Sum: ", sum(list_1))


if __name__ == '__main__':
    main()
