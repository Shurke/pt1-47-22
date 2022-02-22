"""
Даны два списка чисел. Посчитайте, сколько различных (встречаются только в одном из множеств)
чисел содержится одновременно как в первом списке, так и во втором.
"""


first_list = [int(number) for number in input('Введите числа через пробел: ').split(' ')]
second_list = [int(number) for number in input('Введите числа через пробел: ').split(' ')]
print(f'Количество различных цифр в обоих списках: '
      f'{len(set(first_list).symmetric_difference(set(second_list)))}')
