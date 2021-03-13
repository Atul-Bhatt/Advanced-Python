# demonstrate template string functions
from string import Template


def main():
    # Usual string formatting with format
    string_1 = 'You should not {} while {}.'.format('watch movies', 'studying')
    print(string_1)

    # TODO: Create a placeholder with template
    templ = Template("You should not ${entertain} while ${work}.")

    # TODO: Use the substitue method with keyword arguments
    string_2 = templ.substitute(entertain='watch movies', work='studying')
    print(string_2)

    # TODO: Use the substitue method with keyword dictinary
    data = {
        "entertain": "watch movies",
        "work": "studying"
    }
    string_3 = templ.substitute(data)
    print(string_3)


if __name__ == '__main__':
    main()
