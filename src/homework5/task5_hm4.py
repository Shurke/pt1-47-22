"""
Вводится число найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4)
"""


def get_max_divisor(number):
    """Calculates the maximum divisor that is a power of two to the given number.

    :param number: Entered number
    :return: Maximum divisor that is a power of two

    """
    if number <= 0:
        return "The entered number is less than or equal to 0"
    number_bin = format(number, "b")
    n = len(number_bin)
    while number % int("0b1" + "0" * (n - 1), base=2) != 0:
        n -= 1
    res = int("0b1" + "0" * (n - 1), base=2)
    return f"{number}({res})"


if __name__ == '__main__':
    number_input = int(input("Please enter a number greater than 0: "))
    print(get_max_divisor(number_input))
