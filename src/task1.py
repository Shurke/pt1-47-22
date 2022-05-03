"""Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только
 текущий запуск программы)
"""

a = []


def result_add(func):
    def wriper():
        print('Начало декоратора')
        result = func()
        print("Конец декоратора")
        global a
        a.append(result)
        return result
    return wriper
