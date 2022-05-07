"""
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_string_with_ranges(input_list: list) -> str:
    """Collapses list into string with its ranges

    :param input_list: sorted list with numbers
    :return: string with ranges in list
    """
    range_list_native = [input_list[0]]
    result_list = []
    for elem_ind in range(1, len(input_list)):
        if input_list[elem_ind] - 1 == input_list[elem_ind - 1]:
            range_list_native.append(input_list[elem_ind])
        else:
            result_list.append(range_list_native)
            range_list_native = [input_list[elem_ind]]
    result_list.append(range_list_native)
    range_list = []
    for elem in result_list:
        if len(elem) == 1:
            range_list.append(str(elem[0]))
        else:
            range_list.append(f'{elem[0]}-{elem[-1]}')
    result = ','.join(range_list)

    return result


def main():
    """Main function"""
    while True:
        input_str = input('Type sequence, exit or leave empty to demo: ')
        if input_str == '':
            for sequence in [[0, 1, 2, 3, 4, 7, 8, 10], [4, 7, 10], [2, 3, 8, 9]]:
                print(f'{sequence} --> {get_string_with_ranges(sequence)}')
        elif input_str == 'exit':
            exit('Closed by user')
        else:
            if input_str.replace(' ', '').isdigit():
                input_seq = list(int(i) for i in input_str.split())
                input_seq.sort()
                print(get_string_with_ranges(input_seq))
            else:
                print('Some trouble with input data.')


if __name__ == '__main__':
    main()
