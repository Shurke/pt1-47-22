"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""
import string


def get_longest_word(s, allowHyphen=False):
    """Возвращает первое самое длинное слово в строке и его длину

    Существуют слова которые пишутся через дефис, например:
    "Научно-популятрный", "time-out" и тп. Если отрезать в таких словах дефис, то
    результат будет не совсем корректный.
    Чтобы этого избежать реализован аргумент allowHyphen

    :param str s: предложение или текст
    :param bool allowHyphen: (Default False) количество товаров
    :returns: кортеж (слово, длина)
    :rtype: tuple
    """
    longest_word = ''
    longest_word_length = 0
    punctuation = string.punctuation
    if allowHyphen:
        punctuation = punctuation.replace('-', '')
    cleared_s = "".join(ch for ch in s if ch not in punctuation)
    for w in cleared_s.split():
        if len(w) > longest_word_length:
            longest_word_length = len(w)
            longest_word = w
    return (longest_word, longest_word_length)


input_str = input("Введите строку: ")

r1 = get_longest_word(input_str)
r2 = get_longest_word(input_str, allowHyphen=True)

print(f"Самое длинное слово: '{r1[0]}' ({r1[1]})")
print(f"Самое длинное слово (allowHyphen=True): '{r2[0]}' ({r2[1]})")
