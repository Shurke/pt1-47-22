"""
Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def get_degree_two(number):
    """Вычисляет ближайшую степень двойки к введенному числу.

    :param number: Введенное число
    :return: Ближайшая степень двойки

    """
    if number <= 0:
        return "Введенное число немьше или равно 0"
    number_bin = format(number, "b")
    more = int("0b" + "1" + "0" * len(number_bin), base=2)
    less = int("0b" + "1" + "0" * (len(number_bin) - 1), base=2)
    if number_input - less <= more - number_input:
        return less
    else:
        return more


number_input = int(input("Введите число больше 0: "))
print(get_degree_two(number_input))
