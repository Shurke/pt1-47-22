"""
1. Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""


print('Введите стоимость:')
M = float(input('Рублей: '))
N = float(input('Копеек: '))
S = float(input('Введите кол-во: '))

part_price = int(N*S % 100)
full_price = int(M*S + N*S//100)

if full_price % 10 == 1:
    print(f'Нужно {full_price} рубль {part_price} копеек.')
elif full_price % 10 in [2, 3, 4]:
    print(f'Нужно {full_price} рубля {part_price} копеек.')
else:
    print(f'Нужно {full_price} рублей {part_price} копеек.')
