"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот список
“сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(list_input):
    """Collapses an ascending sorted list.

    :param list_input: List entered in ascending order
    :return: A row with a collapsed list

    """
    list_range = [list_input[0]]
    interim_list = []
    for item in range(1, len(list_input)):
        if list_input[item] == list_input[item - 1] + 1:
            list_range.append(list_input[item])
        else:
            interim_list.append(list_range)
            list_range = [list_input[item]]
    interim_list.append(list_range)

    result_list = []
    for item in interim_list:
        if len(item) > 1:
            result_list.append(f"{item[0]}" "-" f"{item[-1]}")
        else:
            result_list.append(str(item[0]))
    result = ','.join(result_list)
    return result


if __name__ == '__main__':
    list_in = list(
        map(int, input("Enter a space-separated list in ascending order: ").split()))
    print(get_ranges(list_in))
