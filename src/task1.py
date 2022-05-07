"""Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только
 текущий запуск программы)
"""


def decorator(func):
    """ Декоратор записывающий все результаты вызова задекорированной функции"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('function_results.txt', 'a', encoding="UTF-8") as file:
            file.write(f'{result}\n')
        return result
    return wrapper


@decorator
def one(number, degree):
    """Функция создает спискок с четными числами до 10000"""
    i = [x for x in range(number ** degree) if x % 2 == 0]
    return i


print(one(10, 4))
