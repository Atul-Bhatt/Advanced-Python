# Demonstrate the usage of ordered dict objects

from collections import OrderedDict


def main():
    # TODO: list of sports teams with wins and loses
    teams = [
        ("Lions", (21, 33)),
        ("Non-Lions", (33, 21)),
        ("Fockers", (22, 11)),
        ("Non-Fockers", (11, 22))
    ]

    # TODO: sort the teams by the number of wins
    sorted_teams = sorted(teams, key=lambda x: x[1][0], reverse=True)
    print(sorted_teams)

    # TODO: create an ordered dictionary of the teams
    ordered_teams = OrderedDict(sorted_teams)

    # TODO: use pop item to remove the top item
    # tm, wl = ordered_teams.popitem(False)
    # print(f"{tm} won {wl[0]} matches and loss {wl[1]} matches.")

    # TODO: what are the next top 4 items?
    for teams in ordered_teams:
        print(teams)

    # TODO: test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = {"a": 1, "c": 3, "b": 2}
    print(f"Equality Test: {a == b}")


if __name__ == "__main__":
    main()
