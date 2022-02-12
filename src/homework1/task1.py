"""
1. Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также
количество S товара. Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""


import string

STR_1 = input('Введите сначала рубли, копейки, а потом количество в произвольной форме:')
STR_2 = ''
NUMBERS = []

for CHAR in list(STR_1):
    if CHAR in string.digits:
        STR_2 += CHAR
    else:
        STR_2 += ' '

for NUM in STR_2.split():
    NUMBERS.append(NUM)

M = float(NUMBERS[0])
N = float(NUMBERS[1])
S = float(NUMBERS[2])

PART_PRICE = int(N * S % 100)
FULL_PRICE = int(M * S + N * S // 100)

if FULL_PRICE % 10 == 1:
    RUB = 'рубль'
elif FULL_PRICE % 10 in [2, 3, 4]:
    RUB = 'рубля'
else:
    RUB = 'рублей'
print(f'Нужно {FULL_PRICE} {RUB} {PART_PRICE} копеек.')