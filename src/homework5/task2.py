"""
Строки в Python сравниваются на основании значений символов. Т.е. если мы захотим выяснить, что
больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки), а русская
буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
Такое положение дел не устроило Анну.
Она считает, что строки нужно сравнивать по количеству входящих в них символов.
Для этого девушка создала класс RealString и реализовала озвученный инструментарий. Сравнивать
между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения
задуманного.
"""


class RealString:
    """Class to compare strings by number of symbols"""

    def __init__(self, word):
        if not isinstance(word, str):
            raise TypeError('You should use string for compare')
        self.word = word

    def __eq__(self, other):
        if not isinstance(other, (str, RealString)):
            raise TypeError('You should use a comparison string for the value on the right')
        sec_str_compare = other if isinstance(other, str) else other.word
        return len(self.word) == len(sec_str_compare)

    def __lt__(self, other):
        if not isinstance(other, (str, RealString)):
            raise TypeError('You should use a comparison string for the value on the right')
        sec_str_compare = other if isinstance(other, str) else other.word
        return len(self.word) < len(sec_str_compare)
