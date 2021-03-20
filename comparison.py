# demonstrating the comparison operators overloading


class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # TODO: implement greater than or equal function
    def __ge__(self, other):
        return self.grade >= other.grade

    # TODO: implement less than or equal function
    def __le__(self, other):
        return self.grade <= other.grade

    # TODO: implement less than function
    def __lt__(self, other):
        return self.grade < other.grade

    # TODO: implement greater than function
    def __gt__(self, other):
        return self.grade > other.grade

    # TODO: implement equals function
    def __equal__(self, other):
        return self.grade == other.grade


def main():
    # create student objects
    S1 = Student('Atul', 12)
    S2 = Student('Vicky', 11)
    S3 = Student('Nitin', 10)

    # TODO: Check for seniority
    print(S1 <= S2)
    print(S2 >= S3)
    print(S1 > S3)


if __name__ == '__main__':
    main()
