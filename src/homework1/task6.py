"""
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""


nmbr = int(input('Введите число: '))
reversed_nmbr = 0
entered_number = nmbr
while nmbr > 0:
    k = nmbr % 10                               # last char in number
    reversed_nmbr = reversed_nmbr * 10 + k      # adding last char to reversed number
    nmbr = nmbr // 10                           # remove the last char in a number
if reversed_nmbr == entered_number:
    print('Число является палиндромом')
else:
    print('Не является палиндромом')
