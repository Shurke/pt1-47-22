"""
6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
"""


def palindrom(num):
    first_num = num
    rev_num = 0


    while num > 0:
        last_num = num % 10
        rev_num = rev_num * 10 + last_num
        num = num // 10
    return rev_num == first_num


input_num = int(input("Введите число: "))
print(palindrom(input_num))
