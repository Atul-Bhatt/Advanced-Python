# customize string representations of objects


class Person():
    def __init__(self):
        self.name = "Atul Bhatt"
        self.age = 22

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person - name:{self.name} age:{self.age}"

    # TODO: use str for a more human readable string
    def __str__(self):
        return f"Person name:{self.name} age:{self.age}"

    # TODO: override the bytes method
    def __bytes__(self):
        return bytes(f"Person name:{self.name} age:{self.age}".encode('utf-8'))


def main():
    # create a new person
    person1 = Person()

    # use different Python functions to convert it to a string
    print(repr(person1))
    print(str(person1))
    print({"Formatted: {0}".format(person1)})
    print(bytes(person1))


if __name__ == "__main__":
    main()
