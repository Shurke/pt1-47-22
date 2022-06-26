"""
Строки в Python сравниваются на основании значений символов. Т.е. если мы захотим выяснить, что
больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки), а русская
буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
Такое положение дел не устроило Анну.
Она считает, что строки нужно сравнивать по количеству входящих в них символов.
Для этого девушка создала класс RealString и реализовала озвученный инструментарий. Сравнивать между
собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения
задуманного.
"""


class RealString(str):
    """Custom class inherited from built-in class 'str'

    Changes the comparison of instances of a child or parent and child class to a string length
    comparison.
    [Optional] added '==' comparison
    """

    def __gt__(self, other):
        if isinstance(other, (RealString, str)):
            return len(self) > len(other)
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, (RealString, str)):
            return len(self) < len(other)
        raise TypeError

    def __eq__(self, other):  # not required to complete the technical task
        if isinstance(other, (RealString, str)):
            return len(self) == len(other)
        raise TypeError
