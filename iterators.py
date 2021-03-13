# use iterator functions like enumerate, iter, zip and next


def main():
    # define a list of days in english and french
    days_english = ["Sunday", "Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday"]
    days_french = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi",
                   "Vendredi", "Samedi"]

    # TODO: use iter to create an iterator over a collection
    days_iterator = iter(days_english)
    print(next(days_iterator))
    print(next(days_iterator))

    # TODO: iterate using a function and a sentinel
    with open('testfile.txt', mode='r') as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # TODO: use regular iteration over the days
    for i in range(len(days_english)):
        print(i+1, days_english[i])

    # TODO: using enumerate reduces code and provides a counter
    for i, m in enumerate(days_english, start=1):
        print(i, m)

    # TODO: use zip to combine sequences
    for i, m in enumerate(zip(days_english, days_french), start=1):
        print("{} {} in french is {}".format(i, m[0], m[1]))


if __name__ == '__main__':
    main()
