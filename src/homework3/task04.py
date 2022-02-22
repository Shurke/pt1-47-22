"""
Даны два списка чисел. Посчитайте, сколько различных чисел входит
только в один из этих списков (например, есть в первом списке, но нет во втором).
"""


first_list = [int(number) for number in input('Введите числа через пробел: ').split(' ')]
second_list = [int(number) for number in input('Введите числа через пробел: ').split(' ')]
print(f'Во втором списке нет: '
      f'{len(set(first_list).difference(set(second_list)))} цифр')
