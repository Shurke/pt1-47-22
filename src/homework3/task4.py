"""
Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
(например, есть в первом списке, но нет во втором)
"""

FIRST_LST = set(input('Введите первый список чисел через пробел: ').split())
SECOND_LST = set(input('Введите второй список чисел через пробел: ').split())
SUM_ELEM_1 = 0
for _ in FIRST_LST.difference(SECOND_LST):
    SUM_ELEM_1 += 1
print(f'Количество уникальных элементов в первом списке: {SUM_ELEM_1} ')
SUM_ELEM_2 = 0
for _ in SECOND_LST.difference(FIRST_LST):
    SUM_ELEM_2 += 1
print(f'Количество уникальных элементов во втором списке: {SUM_ELEM_2} ')
