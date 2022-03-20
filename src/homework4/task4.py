"""
Написать программу которая находит ближайшую степень двойки к введенному числу. 10(8), 20(16), 1(1),
13(16)
"""


def nearest_degree(inp_num=9) -> str:
    """Return nearest degree of 2 in str like 'NUM(DEGREE)'"""
    start_degree = 1
    degree_list = [1]
    while degree_list[-1] < inp_num:
        degree_list.append(2 ** start_degree)
        start_degree += 1
    if len(degree_list) > 1:
        if abs(inp_num - degree_list[-1]) > abs(inp_num - degree_list[-2]):
            ret = f'{inp_num}({degree_list[-2]})'
        else:
            ret = f'{inp_num}({degree_list[-1]})'
    else:
        ret = f'{inp_num}({degree_list[0]})'
    degree_list.clear()

    return ret


if __name__ == '__main__':
    while True:
        what_to_do = input('Please type number, demo or exit: ')

        if what_to_do == 'exit':
            exit('Closed by user')

        elif what_to_do == 'demo':
            for i in [10, 20, 1, 13]:
                print(nearest_degree(i))

        else:
            print(nearest_degree(int(what_to_do)))
