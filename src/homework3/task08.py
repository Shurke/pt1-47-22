"""
Предоставлен список натуральных чисел. Требуется сформировать из них множество.
Если какое-либо число повторяется, то преобразовать его в строку по образцу: например,
если число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4,
строка «44» (второе повторение, т.е. число дублируется в строке), строка «444»
(третье повторение, т.е. строка множится на 3). Реализуйте вывод множества через функцию set_gen()
"""


def set_get(in_data):
    output = []
    for digit in in_data:
        count = 1
        if in_data.count(digit) > 1:
            count *= in_data.count(digit)
            repeated_digit = f'{digit}, {str(digit) * count}'
            output.append(repeated_digit)
        else:
            output.append(digit)
    return set(output)


digit_list = [int(char) for char in input('Введите числа через пробел: ').split()]
print(f'Итоговое множество: {set_get(digit_list)}')
