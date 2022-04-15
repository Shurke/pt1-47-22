"""
Вводится число найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4)
"""


def get_max_divisor(number):
    """Вычисляет максимальный делитель, являющийся степенью двойки к введенному числу.

    :param number: Введенное число
    :return: Максимальный делитель, являющийся степенью двойки

    """
    if number <= 0:
        return "Введенное число меньше или равно 0"
    number_bin = format(number, "b")
    n = len(number_bin)
    while number % int("0b" + "1" + "0" * (n - 1), base=2) != 0:
        n -= 1
    return int("0b" + "1" + "0" * (n - 1), base=2)


number_input = int(input("Введите число больше 0: "))
print(get_max_divisor(number_input))
