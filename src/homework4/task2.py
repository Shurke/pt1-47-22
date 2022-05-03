"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(list_in: list) -> str:
    """Сворачивает список неповторяющихся целых чисел

    :param list_in: Непустой список неповторяющихся целых чисел, отсортированных по возрастанию
    :return: Строку, с результатом сворачивания полученного списка
    """
    list_range = [list_in[0]]
    temporary_list = []
    result_list = []

    for item in range(1, len(list_in)):
        if list_in[item] == list_in[item - 1] + 1:
            list_range.append(list_in[item])
        else:
            temporary_list.append(list_range)
            list_range = [list_in[item]]
    temporary_list.append(list_range)

    for item in temporary_list:
        if len(item) > 1:
            result_list.append(f'{item[0]}' '-' f'{item[-1]}')
        else:
            result_list.append(f'{item[0]}')

    result = ','.join(result_list)

    return result


def main():
    user_list = set(input('Введите список целых чисел: ').split())
    user_list = sorted([int(item) for item in user_list])
    print(f'Результат сворачивания введенного списка: {get_ranges(user_list)}')


if __name__ in '__main__':
    main()
