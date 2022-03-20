"""
Напишите функцию, которая будет генерировать случайный пароль. В пароле должно быть от 7 до 10
символов, при этом каждый символ должен быть случайным образом выбран из диапазона от 33 до 126 в
таблице ASCII. Ваша функция не должна принимать на вход параметры, а возвращать будет
сгенерированный пароль. В основной программе вы должны просто вывести созданный случайным образом
пароль. Программа должна запускаться только в том случае, если она не импортирована в виде модуля в
другой файл.
"""


if __name__ == "__main__":
    def get_password():
        import random
        len_of_pass = random.randint(7, 10)
        password_list = []
        for i in range(0, len_of_pass):
            password_list.append(chr(random.randint(33, 126)))
        password = ''.join(password_list)
        return password

    for i in range(0, 20):
        print(f'Generated password: {get_password()}')
