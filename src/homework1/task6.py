"""
6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
"""


value = int(input("Введите Ваше число: "))
res = value
numb2 = 0

while value > 0:
    numb1 = value % 10
    numb2 = numb2 * 10 + numb1
    value = value // 10

if res == numb2:
    print("Число является полиндромом")
else:
    print("Число не является полиндромом")
