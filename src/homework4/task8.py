"""
Напишите функцию, которая будет генерировать случайный пароль. В пароле должно быть от 7 до 10
символов, при этом каждый символ должен быть случайным образом выбран из диапазона от 33 до 126 в
таблице ASCII. Ваша функция не должна принимать на вход параметры, а возвращать будет
сгенерированный пароль. В основной программе вы должны просто вывести созданный случайным
образом пароль. Программа должна запускаться только в том случае, если она не импортирована в виде
модуля в другой файл
"""

import random


def get_password():
    """Generate a random password

    :return: Random password for user
    """
    pass_len = random.randint(7, 10)
    temporary_password = []
    for i in range(0, pass_len):
        temporary_password.append(chr(random.randint(33, 126)))
    password = ''.join(temporary_password)

    return password


print(f'Random password: {get_password()}')
