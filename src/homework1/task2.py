"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""
import string


def get_longest_word(s, allow_hyphen=False):
    """Возвращает первое самое длинное слово в строке и его длину

    Существуют слова которые пишутся через дефис, например:
    "Научно-популятрный", "time-out" и тп. Если отрезать в таких словах дефис, то
    результат будет не совсем корректный.
    Чтобы этого избежать реализован аргумент allowHyphen

    :param str s: предложение или текст
    :param bool allow_hyphen: (Default False) количество товаров
    :returns: кортеж (слово, длина)
    :rtype: tuple
    """
    longest_word = ''
    longest_word_length = 0
    punctuation = string.punctuation
    if allow_hyphen:
        punctuation = punctuation.replace('-', '')
    cleared_s = "".join(ch for ch in s if ch not in punctuation)
    for w in cleared_s.split():
        word_length = len(w)
        if word_length > longest_word_length:
            longest_word_length = word_length
            longest_word = w
    return (longest_word, longest_word_length)


input_str = input("Введите строку: ")

result1 = get_longest_word(input_str)
result2 = get_longest_word(input_str, allow_hyphen=True)

print(f"Самое длинное слово: '{result1[0]}' ({result1[1]})")
print(f"Самое длинное слово (allow_hyphen=True): '{result2[0]}' ({result2[1]})")
