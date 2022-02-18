""" 8. Множества
Предоставлен список натуральных чисел.
Требуется сформировать из них множество.
Если какое-либо число повторяется, то преобразовать его в строку по образцу:
например, если число 4 повторяется 3 раза, то в множестве будет следующая запись:
само число 4,
строка «44» (второе повторение, т.е. число дублируется в строке),
строка «444» (третье повторение, т.е. строка множится на 3).
Реализуйте вывод множества через функцию set_gen().
"""


def set_gen(numbers_list):
    """генерирует множество согласно задаче"""
    result_set = set(numbers_list)
    numbers = result_set.copy()
    for n in numbers:
        n_count = numbers_list.count(n)
        if n_count > 1:
            for i in range(n_count, 1, -1):
                result_set.add(str(n) * i)
    return result_set


input_lst = [int(x) for x in input("Введите цифры множества ч.з пробел: ").split()]
print(f"Полученное множество: {set_gen(input_lst)}")
