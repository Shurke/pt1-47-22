"""
Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def nearest_divisor(inp_num=9) -> str:
    """Return string with nearest (degree of 2) divisor like 'NUMBER(DIVISOR)'"""
    start_degree = 1
    degree_list = [1]

    while degree_list[-1] < inp_num:
        degree_list.append(2 ** start_degree)
        start_degree += 1

    for divisor in degree_list[::-1]:
        if inp_num % divisor == 0:
            break
    if divisor is None:
        return 'Делителя нет (как так?)'
    else:
        return f'{inp_num}({divisor})'


for i in [10, 16, 12]:
    print(nearest_divisor(i))
