"""
Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def get_degree_two(number):
    """Calculates the nearest power of two to the given number.

    :param number: Entered number
    :return: Nearest power of two

    """
    if number <= 0:
        return "The entered number is less than or equal to 0"
    number_bin = format(number, "b")
    more = int("0b1" + "0" * len(number_bin), base=2)
    less = int("0b1" + "0" * (len(number_bin) - 1), base=2)
    if number - less <= more - number:
        return f"{number}({less})"
    else:
        return f"{number}({more})"


if __name__ == '__main__':
    number_input = int(input("Please enter a number greater than 0: "))
    print(get_degree_two(number_input))
