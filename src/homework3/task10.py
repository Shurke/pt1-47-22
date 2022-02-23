"""Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида
 (мы не знаем функции и рекурсию).
"""

number_1 = int(input('Введите число: '))
number_2 = int(input('Введите число: '))

while number_1 and number_2 != 0:
    if number_1 > number_2:
        number_1 = number_1 % number_2
    else:
        number_2 = number_2 % number_1

print(f'Общий делитель введенных чисел равен: {number_1 + number_2}')
