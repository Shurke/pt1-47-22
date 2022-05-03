"""
Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def find_near(numb: int) -> int:
    """Находит ближающую степень двойки, относительно введённого числа

    :param numb: Введённое число
    :return: Ближайшая степень двойки
    """
    count_before, count_after = 0, 0

    while 2 ** count_after < numb:
        count_after += 1

    count_before = count_after - 1

    if numb - 2 ** count_before < 2 ** count_after - numb:
        return count_before
    else:
        return count_after


def main():
    numb = int(input('Введите любое число больше 0: '))
    print(f'Ближайшая степень двойки к введенному числу: {find_near(numb)}')


if __name__ in '__main__':
    main()
