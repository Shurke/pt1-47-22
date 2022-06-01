"""
Вводится число найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4).
"""


def max_divisor(inp_num):
    degree = 1
    list_of_degree = [1]

    while list_of_degree[-1] < inp_num:
        list_of_degree.append(2 ** degree)
        degree += 1
    for divisor in list_of_degree[::-1]:
        if inp_num % divisor == 0:
            break
    return f'{inp_num}({divisor})'


input_data = int(input('Введите число: '))
print(max_divisor(input_data))
