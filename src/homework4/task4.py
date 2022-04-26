"""Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)"""


def two_degree(user_numb):
    """conversion to binary and then finding the nearest degree
    :param user_numb: value from user
    :return: nearest degree of two"""
    binary = str((bin(user_numb)))[2:]

    res_deg = 1
    for deg in range(1, len(binary)):
        if 2 ** deg >= res_deg and abs(user_numb - 2 ** deg) <= abs(user_numb - 2 ** (deg + 1)):
            res_deg = 2 ** deg
        elif 2 ** deg >= res_deg and abs(user_numb - 2 ** deg) >= abs(user_numb - 2 ** (deg + 1)):
            res_deg = 2 ** (deg + 1)

    return f'The nearest degree of two to the entered number: {res_deg}'


numb = int(input('Enter a number to get the nearest degree of two: '))
print(two_degree(numb))
