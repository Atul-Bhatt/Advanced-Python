# demonstrating the use of lambda functions


def celciusToFahrenheit(temp):
    """ celciusToFahrenheit(arg) --> convert celcius to fahrenheit

    Parameter
    arg: temperature in celcius
    """
    return (temp * 9/5) + 32


def fahrenheitToCelcius(temp):
    """ fahrenheitToCelcius(arg) --> convert fahrenheit to celcius

    Parameter
    temp: temperature in fahrenheit
    """
    return (temp - 32) * 5/9


def main():
    """ main() --> main function will run only if the module is run directly
    """
    # list of temperatures in Fahrenheit and celcius
    t_cel = [20, 24, 23, 25, 43, 32]
    t_fah = [78, 98, 67, 88, 77, 68]

    # TODO: use regular functions to convert temperature
    print(list(map(celciusToFahrenheit, t_cel)))
    print(list(map(fahrenheitToCelcius, t_fah)))

    # TODO: use lambda functions to run convert temperature
    print(list(map(lambda t: (t * 9/5) + 32, t_cel)))
    print(list(map(lambda t: (t - 32) * 5/9, t_fah)))


if __name__ == "__main__":
    main()
