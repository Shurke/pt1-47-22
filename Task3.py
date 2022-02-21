from collections import OrderedDict

"""Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde
def", то должно быть выведено "abcdef"."""


def result(sentence):
    return "".join(OrderedDict.fromkeys(sentence))


sentence = input("Введите предложение:")
final_sentence = result(sentence).replace(" ", "")
print(final_sentence)
