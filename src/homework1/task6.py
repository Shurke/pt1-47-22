"""
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
"""


def is_palindrom(num):
    """Вычисляет является ли число полиндромом

    :param int num: число для проверки
    :returns: результат проверки на палиндромность
    :rtype: bool
    """
    temp_num = num
    reversed_num = 0

    while num > 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num = num // 10

    return reversed_num == temp_num


input_int = int(input("Введите число: "))
print(is_palindrom(input_int))
