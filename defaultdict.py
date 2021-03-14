# demonstrate the usage of defaultdict module

from collections import defaultdict


def main():
    # a list of fruits
    fruits = [
        "apple", "pear", "orange", "banana",
        "apple", "grape", "banana", "banana"
    ]

    # TODO: use a dictionary to count the fruits
    # requires a factory method to initialize all the keys
    # fruitCounter = defaultdict(int)
    fruitCounter = defaultdict(lambda: 100)

    # TODO: count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # TODO: print the result
    for fruit, count in fruitCounter.items():
        print(fruit, count)


if __name__ == "__main__":
    main()
