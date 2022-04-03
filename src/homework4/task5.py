"""
Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def main():
    def nearest_divisor(inp_num: int = 9) -> str:
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

    while True:
        what_to_do = input('Please type number, demo or exit: ')

        if what_to_do == 'exit':
            exit('Closed by user')

        elif what_to_do == 'demo':
            for i in [10, 20, 1, 13]:
                print(nearest_divisor(i))

        else:
            print(nearest_divisor(int(what_to_do)))


if __name__ == '__main__':
    main()
