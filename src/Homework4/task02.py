"""
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся
целых чисел, отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(input_data):

    def get_list(ls):

        list_length = len(ls)
        while ls:
            # single element remains, yield the trivial range
            if list_length == 1:
                yield ls[0], ls[0]
                break

            # find the last index that satisfies the determined difference
            i = next(
                i for i in range(0, list_length)
                if i + 1 == list_length
                or ls[i + 1] - ls[i] != 1
            )
            yield ls[0], ls[i]

            # update variables
            ls = ls[i + 1:]
            list_length -= i + 1

    output_string = ''
    generator = get_list(input_data)

    for input_data in generator:
        first_number = ''.join(str(input_data[0]))
        second_number = ''.join(str(input_data[1]))
        if first_number == second_number:
            generated_string = f'{first_number}, '
        else:
            generated_string = f'{first_number}-{second_number}, '
        output_string += generated_string
    final_data = output_string[:-2]
    return final_data


input_list = sorted([int(i) for i in input('Введите числа через пробел: ').split()])
print(f'Сокращённый вариант введённого списка: "{get_ranges(input_list)}"')
