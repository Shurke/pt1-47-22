"""Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых
 чисел, отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(list_numbers):
    """Функция получая список чисел сворачивает его в интервалы"""
    result = []
    temp = []
    for i in range(max(list_numbers) + 2):
        if i in list_numbers:
            temp.append(i)
        else:
            if temp:
                if len(temp) == 1:
                    result.append(temp[0])
                else:
                    result.append(f'{temp[0]}-{temp[-1]}')
                temp.clear()
    return result
