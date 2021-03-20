# demonstrate the use of list comrehension


def main():
    # TODO: create a list of numbers
    num_list = [i for i in range(10)]

    # TODO: use list and map functions to square numbers
    # squared = list(
    #     map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, num_list)))
    # print(squared)

    # TODO: use list comprehension to square only even nubers
    squared = [i ** 2 for i in num_list if i % 2 == 0]
    print(squared)


if __name__ == '__main__':
    main()
