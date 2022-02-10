print('Введите количество рублей: ')
M = int(input())
print('Введите количество копеек: ')
N = int(input())
print('Количество товаров: ')
L = int(input())
total = M * L * 100 + N * L

print('Общая цена ' + str(total // 100) + ' рублей ' + str(total % 100) + ' копеек')