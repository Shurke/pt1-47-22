"""Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16),
 12(4).
"""


def maximum_divisor(number):
    """Функция ищет максимальный делитель, являющийся степенью двойки для введенного числа"""
    list_exp = [i**2 for i in range(1, (number + 1)) if i**2 <= number]
    for result in range(number, -1, -1):
        if number % result == 0:
            if list_exp.count(result) == 1:
                break
    print(f'Максимальный делитель введенного числа являющийся степенью двойки: {result}')


input_number = int(input('Введите число: '))
if __name__ == '__main__':
    maximum_divisor(input_number)
