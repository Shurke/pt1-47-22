"""Вам дано положительное целое число. Определите сколько цифр оно имеет.
Входные данные: Положительное целое число
Выходные данные: Целое число.

"""


def number_length(a: int) -> int:
    return len(str(a))


if __name__ == "__main__":
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""Дана строка и нужно найти ее первое слово.
Это упрощенная версия миссии First Word , которую можно решить позднее.
Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.
Входные данные: строка.
Выходные данные: строка.

"""


def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    # your code here
    return text.split()[0]


if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""Попробуйте выяснить какое количество нулей содержит данное число в конце.
Входные данные: Положительное целое число (int).
Выходные данные: Целое число (int).

"""


def end_zeros(num: int) -> int:
    # your code here
    return len(str(num)) - len(str(num).rstrip('0'))


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""Верните данную строку в перевернутом виде.
Входные данные: Строка.
Выходные данные: Строка.

"""


def backward_string(val: str) -> str:
    # your code here
    return val [::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""В данном списке первый элемент должен стать последним.
Пустой список или список из одного элемента не должен измениться.
Входные данные: Список.
Выходные данные: Набор элементов.

"""


from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    return items[1:] + items[:1]

if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
