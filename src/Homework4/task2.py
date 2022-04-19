"""Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_range(number_list):

    """Данная функция принимает на вход список чисел и сварачивает его."""

    new_num_list = []
    for num in number_list:
        new_num_list.append(int(num))
    some_list = [new_num_list[0]]
    new_list = []
    total_list = []
    for i in range(1, len(new_num_list)):
        if new_num_list[i] - 1 == new_num_list[i - 1]:
            some_list.append(new_num_list[i])
        else:
            new_list.append(some_list)
            some_list = [new_num_list[i]]
    new_list.append(some_list)
    for i in range(len(new_list)):
        if len(new_list[i]) == 1:
            total_list.append(str(new_list[i][0]))
        else:
            total_list.append(f"{str(new_list[i][0])}-{str(new_list[i][-1])}")
    result = ",".join(total_list)
    return result


your_list = input("введите числа через запятую\n").split(",")
print(f"свернутый список ваших чисел будет выглядеть: \n{get_range(your_list)}")
