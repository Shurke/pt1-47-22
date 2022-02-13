"""
8. Зарегистрируйтесь на одном (или нескольких) из сайтов:
https://py.checkio.org/ , https://www.codewars.com, https://www.hackerrank.com/, https://acmp.ru
И решите 1-5 задач уровня Elementary и advanced.
Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.
Имя пул реквеста: Homework1: Name Surname
"""


"""
Вам дано положительное целое число. Определите сколько цифр оно имеет.
Входные данные: Положительное целое число
Выходные данные: Целое число.
Пример:
number_length(10) == 2
number_length(0) == 1
"""


def number_length(a: int) -> int:
    num = str(a)
    value = len(num)
    return value


if __name__ == "__main__":
    print("Example:")
    print(number_length(10))


"""
Дана строка и нужно найти ее первое слово.
Это упрощенная версия миссии First Word , которую можно решить позднее.
Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.
Входные данные: строка.
Выходные данные: строка.
Пример:
first_word("Hello world") == "Hello"
"""


def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    text = text.split()
    return text[0]


if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))


"""
В этой задаче, Вам нужно создать функцию проверки пароля.
Условия проверки: длина пароля должна быть больше 6.
Входные данные: Строка.
Выходные данные: Логический тип.
Пример:
is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == True
"""


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        status = 1
    else:
        status = 0
    return bool(status)


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))


"""
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
i.e.
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.
"""


def friend(x):
    new_friends = []
    for char in x:
        if len(char) == 4:
            new_friends.append(char)
    return new_friends


x = ["Ryan", "Kieran", "Jason", "Yous"]

print(friend(x))


"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 
811181 will come out, because 92 is 81 and 12 is 1.
"""


def square_digits(num):
    new_num = ''
    for i in num:
        num = int(i)
        num = num ** 2
        new_num += str(num)
    return new_num


num = input('Number: ')
print(square_digits(num))
