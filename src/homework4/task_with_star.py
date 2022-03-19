"""
Реализовать функцию, на вход которой передается имя логической функции (т.е. функция, которая
принимает логические параметры и возвращает логическое значение. Пример: И, ИЛИ, исключающее ИЛИ и
т.д.) и набор аргументов, и возвращает строку, представляющую таблицу истинности функции.

Пример ввода: some_func("AND", A, B)

Правила форматирования:
    Переменные должны называться A, B, C, D ... и так далее, в том же порядке, в котором они
    передаются в логическую функцию.
    Параметров не будет больше 26 (A ... Z)
    Логические значения будут представлены либо 1 (истина), либо 0 (ложь).
Первая строка будет состоять из следующих частей:
    имена переменных, разделенные пробелом ()
    два символа табуляции
    имя функции, параметры которой в круглых скобках разделены запятыми
    два символа новой строки
Следующие строки будут состоять из следующих по порядку:
    значения переменных, разделенные пробелом
    два символа табуляции
    результат функции для этого расположения переменных
    символ новой строки
"""


def get_array(list_of_variables):
    array = []
    str_list = []
    while sum(str_list) < len(list_of_variables):
        for i in range(26 ** 2):
            get_data = bin(i)[2:]
            while len(get_data) < len(list_of_variables):
                get_data = '0' + get_data
            str_list = []
            for elem in get_data:
                str_list.append(int(elem))
            if len(str_list) <= len(list_of_variables):
                array.append(str_list)

    return array


def get_table(func='AND', seq=['A', 'B']):
    value_array = get_array(seq)
    truth_list = []
    if func == 'AND':

        for string in value_array:
            if sum(string) == len(string):
                truth_list.append(1)
            else:
                truth_list.append(0)

    elif func == 'OR':

        for string in value_array:
            if sum(string) >= 1:
                truth_list.append(1)
            else:
                truth_list.append(0)

    elif func == 'NAND':

        for string in value_array:
            if 0 in string:
                truth_list.append(1)
            else:
                truth_list.append(0)

    elif func == 'NOR':

        for string in value_array:
            if sum(string) == 0:
                truth_list.append(1)
            else:
                truth_list.append(0)

    elif func == 'XNOR':

        for string in value_array:
            if sum(string) % 2 == 0:
                truth_list.append(1)
            else:
                truth_list.append(0)

    elif func == 'XOR':

        for string in value_array:
            if sum(string) % 2 == 1:
                truth_list.append(1)
            else:
                truth_list.append(0)

    if truth_list:
        result = ' '.join(seq)
        result += f'\t\t{func}({", ".join(seq)})\n\n'
        for i in range(len(truth_list)):
            value_array_str = []
            for item in value_array[i]:
                value_array_str.append(str(item))
            result += f'{" ".join(value_array_str)}\t\t{truth_list[i]}\n'

    else:
        result = 'Some trouble with logic function :('

    return result


what_to_do = input('Type logic function or press enter for demo: ')
if what_to_do:
    user_seq = input('Type the variables separated by space: ').split()
    print(get_table(what_to_do, user_seq))

else:
    for example_func in ['AND', 'OR', 'NAND', 'NOR', 'XNOR', 'XOR']:
        print(get_table(example_func))
