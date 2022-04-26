"""
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(sort_list):
    """list minimization

    :param sort_list: sorted list from function user_lst
    :return: modified list
    """

    null_list = [sort_list[0]]
    temporary_result_list = []
    for elem in range(1, len(sort_list)):
        if sort_list[elem] == sort_list[elem - 1] + 1:
            null_list.append(sort_list[elem])
        else:
            temporary_result_list.append(null_list)
            null_list = [sort_list[elem]]
    temporary_result_list.append(null_list)
    result_list = []
    for item in temporary_result_list:
        if len(item) > 1:
            result_list.append(f'{item[0]} - {item[-1]}')
        else:
            result_list.append(f'{item[0]}')

    return result_list


def user_lst():
    input_list = input('Enter a list of integers, separated by space: ').split()
    temporary_user_list = []
    for i in input_list:
        if input_list.count(i) == 1:
            temporary_user_list.append(i)
    return list(sorted(map(int, temporary_user_list)))


print(get_ranges(user_lst()))
