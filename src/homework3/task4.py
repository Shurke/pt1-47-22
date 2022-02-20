"""Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
 (например, есть в первом списке, но нет во втором)."""


def int_list(a):
    return [int(i) for i in a]


def sort(a, b):
    for i in a:
        if i not in b:
            end.append(i)
    return end


end = []
int_list_1 = int_list(list(input('Введите числа: ')))
int_list_2 = int_list(list(input('Введите числа: ')))

sort_1 = sort(int_list_1, int_list_2)
sort_2 = sort(int_list_2, int_list_1)  # Можно убрать если только 1 список на уникальность проверять

print('Не повторяющиеся числа в списках: ', end)
