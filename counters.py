# demonstrating the use of counters collection

from collections import Counter


def main():
    # list of students in two classes
    class1 = [
        "Bob", "Cecily", "Bill", "Ryan", "Kelly", "Dwight",
        "Abraham", "Reese", "Robert", "Greg", "Ryan", "Bob"
    ]
    class2 = [
        "Frank", "John", "Reese", "Kelly", "Ryan", "Jim",
        "Adolf", "Michael", "Creed", "Robert", "John"
    ]

    # TODO: create a counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)

    # TODO: how many students in class1 named Ryan?
    print(c1["Ryan"])

    # TODO: how many students are in class1?
    print(sum(c1.values()))

    # TODO: combine the classes
    c1.update(class2)

    # TODO: what's the most common name in the two classes?
    print(c1.most_common(3))

    # TODO: seperate the two classes
    c1.subtract(class2)
    print(c1.most_common(3))

    # TODO: what's common between the two classes?
    print(c1 & c2)


if __name__ == "__main__":
    main()
