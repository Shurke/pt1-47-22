"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также
количество S товараПосчитайте общую цену в рублях и копейках за L товаров.
"""

M = int(input('Рублей: '))
N = int(input('Копеек: '))
L = int(input('Количество товара: '))

a = L * (100 * M + N)
print(f'Общая цена {a // 100} рублей {a % 100} копеек')
