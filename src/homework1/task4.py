"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""
import string


def count_cases(s):
    """Подсчитывает количество строчных и прописных букв в строке

    :param str s: предложение или текст
    :returns: (кол-во строчный, кол-во прописных)
    :rtype: tuple
    """
    lo = up = 0
    for ch in s:
        if ch in string.ascii_lowercase:
            lo += 1
        if ch in string.ascii_uppercase:
            up += 1
    return (lo, up)


input_str = input("Введите строку: ")
r = count_cases(input_str)
print(f"lowercase chars: {r[0]}\nuppercase chars: {r[1]}")
