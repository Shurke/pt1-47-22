#  1. Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена,
#  а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров.


print('Введите цену товара: ')

M = input()
N = input()
S = input()

L = (int(M) + int(N) / 100) * int(S)

a = str(L).split('.')
a = int(a[0])
b = str(L).split('.')
b = int(b[1])

print(M, 'руб', N, 'коп')
print(S, 'шт')
print(a, 'руб', b, 'коп')
