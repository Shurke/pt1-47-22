""" 10. Оглянемся назад. Числа
Даны два натуральных числа.
Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
"""

numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

while True:
    devider = numbers[0] % numbers[1]
    if not devider:
        print(f"НОД = {numbers[1]}")
        break
    numbers[0], numbers[1] = numbers[1], devider
