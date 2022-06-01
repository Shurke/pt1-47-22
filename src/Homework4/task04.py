"""
Написать программу, которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def seq2pow(input_number):
    degree = 1
    list_of_degree = [1]
    while list_of_degree[-1] < input_number:
        list_of_degree.append(2 ** degree)
        degree += 1
    if abs(input_number - list_of_degree[-1]) > abs(input_number - list_of_degree[-2]):
        result = f'{input_number}({list_of_degree[-2]})'
    else:
        result = f'{input_number}({list_of_degree[-1]})'

    return result


input_data = int(input('Введите число: '))
print(seq2pow(input_data))
