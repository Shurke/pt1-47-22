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


def get_array_for_truth_table(list_of_variables: tuple or list) -> tuple:
    """Return tuple with tuples for each string in truth table"""

    array = []
    str_list = []
    while sum(str_list) < len(list_of_variables):
        for i in range(26 ** 2):
            get_data = bin(i)[2:]
            if len(get_data) < len(list_of_variables):
                while len(get_data) < len(list_of_variables):
                    get_data = '0' + get_data
            str_list = []
            for elem in get_data:
                str_list.append(int(elem))
            if len(str_list) <= len(list_of_variables):
                array.append(str_list)
            if sum(str_list) == len(str_list):
                return tuple(array)


def and_func(input_array):
    """Return truth table for log func AND"""
    truth_list = []
    for string in input_array:
        if sum(string) == len(string):
            truth_list.append(1)
        else:
            truth_list.append(0)
    return truth_list


def or_func(input_array):
    """Return truth table for log func OR"""
    truth_list = []
    for string in input_array:
        if sum(string) >= 1:
            truth_list.append(1)
        else:
            truth_list.append(0)
    return truth_list


def nand_func(input_array):
    """Return truth table for log func NAND"""
    truth_list = []
    for string in input_array:
        if 0 in string:
            truth_list.append(1)
        else:
            truth_list.append(0)
    return truth_list


def nor_func(input_array):
    """Return truth table for log func NOR"""
    truth_list = []
    for string in input_array:
        if sum(string) == 0:
            truth_list.append(1)
        else:
            truth_list.append(0)
    return truth_list


def xnor_func(input_array):
    """Return truth table for log func XNOR"""
    truth_list = []
    for string in input_array:
        if sum(string) % 2 == 0:
            truth_list.append(1)
        else:
            truth_list.append(0)
    return truth_list


def xor_func(input_array):
    """Return truth table for log func XOR"""
    truth_list = []
    for string in input_array:
        if sum(string) % 2 == 1:
            truth_list.append(1)
        else:
            truth_list.append(0)
    return truth_list


def get_table(func='AND', seq=('A', 'B')) -> str:
    """Return string with truth table"""

    if func in func_dict:

        value_array = get_array_for_truth_table(seq)

        result_truth_list = func_dict[func](value_array)

        result = ' '.join(seq)
        result += f'\t\t{func}({", ".join(seq)})\n\n'
        for i in range(len(result_truth_list)):
            value_array_str = []
            for item in value_array[i]:
                value_array_str.append(str(item))
            result += f'{" ".join(value_array_str)}\t\t{result_truth_list[i]}\n'

    else:
        result = 'Some trouble with logic function :('

    return result


def main():
    while True:
        what_to_do = input('Type logic function or press enter for demo: ')
        if what_to_do:
            input_tuple = what_to_do.split(', ')
            if input_tuple[0][1:-1] in func_dict:
                ans = get_table(input_tuple[0][1:-1], input_tuple[1:])
            else:
                ans = 'Mistakes in input data. Example: "AND", A, B'
            print(ans)

        else:
            for example_func in ('AND', 'OR', 'NAND', 'NOR', 'XNOR', 'XOR'):
                print(get_table(example_func))


func_dict = {
    'AND': and_func,
    'OR': or_func,
    'NAND': nand_func,
    'NOR': nor_func,
    'XNOR': xnor_func,
    'XOR': xor_func
}

if __name__ == '__main__':
    main()
