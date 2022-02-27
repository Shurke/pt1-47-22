'''
Предоставлен список натуральных чисел. Требуется сформировать из них множество. Если какое-либо
число повторяется, то преобразовать его в строку по образцу: например, если число 4 повторяется 3
раза, то в множестве будет следующая запись: само число 4, строка «44» (второе повторение, т.е.
число дублируется в строке), строка «444» (третье повторение, т.е. строка множится на 3). Реализуйте
вывод множества через функцию set_gen().
'''


def set_gen(num_list):
    output = []
    print(type(output))
    dict_of_list = {}
    for elem in num_list:
        dict_of_list[elem] = num_list.count(elem)
    for elem, count in dict_of_list.items():
        if count <= 1:
            output.append(elem)
        else:
            for rep in range(1, count + 1):
                output.append(str(elem) * rep)
    return set(output)


INPUT = input('Введите числа через пробел: ').split()
INPUT_LIST = []

for ELEM_IND in range(0, len(INPUT)):
    INPUT_LIST.append(int(INPUT[ELEM_IND]))

OUTPUT = set_gen(INPUT_LIST)
print(f'Выходное множество: {OUTPUT}')
