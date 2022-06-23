"""
Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def find_near(numb: int) -> int:
    """Находит максимальный делитель, являющийся степенью двойки

    :param numb: Введённое число
    :return: Максимальный делитель степени два
    """
    count = 0
    div = 1

    while 2 ** count < numb:
        count += 1
        if numb % (2 ** count) == 0:
            div = 2 ** count

    return div


def main():
    numb = int(input('Введите любое число больше 0: '))
    print(f'Максимальный делитель, являющийся степенью двойки: {find_near(numb)}')


if __name__ in '__main__':
    main()
