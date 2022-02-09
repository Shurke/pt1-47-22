"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""
from collections import OrderedDict  # для второго варианты
import string


def process_string(s):
    """Убирает из строки пробелы и повторяющиеся символы

    :param str s: предложение или текст
    :returns: результат выполнения
    :rtype: str
    """
    result = []
    for ch in s:
        if ch not in result and ch not in string.whitespace:
            result.append(ch)
    return "".join(result)


def process_string2(s):
    """Убирает из строки пробелы и повторяющиеся символы

    Однострочный вариант пришел на ум после практики на codewars
    :param str s: предложение или текст
    :returns: результат выполнения
    :rtype: str
    """
    return("".join(OrderedDict.fromkeys(s.replace(' ', '')).keys()))


input_str = input("Введите строку: ")
print("Вариант 1:", process_string(input_str))
print("Вариант 2:", process_string2(input_str))
