"""
Модуль collections имеет defaultdict, который дает вам значение по умолчанию для попытки получить
значение ключа, которого нет в словаре, вместо того, чтобы вызвать ошибку. Почему бы не сделать это
для списка?
Ваша задача — создать класс (или функцию, возвращающую объект) с именем DefaultList. Класс будет
иметь два параметра: список и значение по умолчанию. Список, очевидно, будет списком,
соответствующим этому объекту. Значение по умолчанию будет возвращено каждый раз, когда индекс
списка вызывается в коде, который обычно вызывает ошибку
(т. е. i > len(list) - 1 или i < -len(list)).
Этот класс также должен поддерживать обычные функции списка: расширение, добавление, вставка,
удаление и извлечение (extend, append, insert, remove, and pop)
"""


class DefaultList(list):
    """
    Returns the default value entered by the user in case of an error.
    If there is no error, returns the list item by the entered index

    """
    def __init__(self, lst, default_value):
        super(DefaultList, self).__init__()
        self.lst = lst
        self.default_value = default_value

    def __getitem__(self, item):
        if item > len(self.lst) - 1 or item < -len(self.lst):
            return self.default_value
        else:
            return self.lst[item]
