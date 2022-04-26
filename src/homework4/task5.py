"""Вводится число. Найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4)"""


def maximum_divisor(user_numb):
    """conversion to binary and then finding the maximal divisor, which is a degree of two
    :param user_numb: value from user
    :return: max divisor"""
    binary = str((bin(user_numb)))[2:]
    divisor = 1
    for degree in range(1, len(binary)):
        while user_numb % 2 ** degree == 0:
            if divisor < 2 ** degree:
                divisor = 2 ** degree
                break

    return f'Max divisor: {divisor}'


numb = int(input('Enter a number to get the max divisor: '))
print(maximum_divisor(numb))
