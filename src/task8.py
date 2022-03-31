"""Случайный пароль
Напишите функцию, которая будет генерировать случайный пароль. В пароле должно быть от 7 до 10
символов, при этом каждый символ должен быть случайным образом выбран из диапазона от 33 до 126
в таблице ASCII. Ваша функция не должна принимать на вход параметры, а возвращать будет
сгенерированный пароль. В основной программе вы должны просто вывести созданный случайным образом
пароль. Программа должна запускаться только в том случае, если она не импортирована в виде модуля
в другой файл.
"""


import random


if __name__ == '__main__':
    def Password_Generator():
        len_password = random.randrange(7, 11)
        res = [chr(random.randrange(33, 127)) for i in range(len_password)]
        result = ''.join(res)
        return (f'Сгенерированный пароль: {result}')


print(Password_Generator())
