"""Написать программу которая находит ближайшую степень двойки к введенному числу. 10(8), 20(16),
 1(1), 13(16)
"""


def find_degree(number):
    """Функция находит ближайшую степень двойки к введенному числу"""
    last_result = 1
    while number >= 2**last_result:
        previous = last_result
        last_result += 1

    if number == 1:
        print('Ближайшую степень двойки к введенному числу', number)
    elif number - (2 ** previous) > (2 ** last_result) - number:
        print('Ближайшую степень двойки к введенному числу', (2 ** last_result))
    else:
        print('Ближайшую степень двойки к введенному числу', (2 ** previous))


if __name__ == "__main__":
    input_number = int(input('Введиче число для нахождения ближайшей степени двойки: '))
    find_degree(input_number)
