"""
6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)

"""


ENTERED_NUM = input('''Пожалуйста, введите положительное целое число, 
которое необходимо проверить, является ли оно палиндромом:
''')

NUM = len(ENTERED_NUM)
for i in range(NUM // 2):
    if ENTERED_NUM[i] != ENTERED_NUM[-1 - i]:
        print('Введенное число не является палиндромом')
        break
else:
    print('Введенное число является палиндромом')
