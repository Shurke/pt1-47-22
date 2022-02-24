"""
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""


"""
Первое решение
"""


import math

num_one = int(input('Введите первое число: '))
num_two = int(input('Введите второе число: '))

print(f'Наибольший общий делитель для введённых чисел: {math.gcd(num_one, num_two)}')


"""
Второе решение
"""


num_one = int(input('Введите первое число: '))
num_two = int(input('Введите второе число: '))

while num_one != 0 and num_two != 0:
    if num_one > num_two:
        num_one = num_one % num_two
    else:
        num_two = num_two % num_one

print(f'Наибольший общий делитель для введённых чисел: {num_one + num_two}')
