"""
1. Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также
количество S товара. Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""


import string

str_1 = input('Введите сначала рубли, копейки, а потом количество в произвольной форме:')
str_2 = ''
numbers = []

for char in list(str_1):
    if char in string.digits:
        str_2 += char
    else:
        str_2 += ' '

for num in str_2.split():
    numbers.append(num)

M = float(numbers[0])
N = float(numbers[1])
S = float(numbers[2])

part_price = int(N*S % 100)
full_price = int(M*S + N*S//100)

if full_price % 10 == 1:
    print(f'Нужно {full_price} рубль {part_price} копеек.')
elif full_price % 10 in [2, 3, 4]:
    print(f'Нужно {full_price} рубля {part_price} копеек.')
else:
    print(f'Нужно {full_price} рублей {part_price} копеек.')
