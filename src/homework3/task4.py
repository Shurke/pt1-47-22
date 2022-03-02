"""Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
 (например, есть в первом списке, но нет во втором)."""


def int_list(a):
    return (int(i) for i in a)


int_list_1 = int_list(list(input('Введите числа: ')))
int_list_2 = int_list(list(input('Введите числа: ')))

difference_in_lists = list(set(int_list_1) - set(int_list_2))

print(f'Количество цифр не сожержащихся во втором списке: {len(difference_in_lists)}')
