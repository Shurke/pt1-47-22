"""Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без
исключений (но не более n раз - параметр декоратора). Если превышено количество попыток, должно
быть возбуждено исключение типа TooManyErrors.
Т.е. если во время работы функции возникло какое-то исключение, то функция должна перезапуститься
еще раз. Количество перезапусков ограничено параметром декоратора.
"""


class TooManyErrors(Exception):
    """Класс исключений"""


def count(limit_try):
    """Декоратор с ограничением запуска вложенной функции"""
    def try_repeat(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except ValueError:
                if limit_try > wrapper.count_try:
                    wrapper.count_try += 1
                    print(f'Использовано попыток {wrapper.count_try} из {limit_try}')
                    return wrapper(*args, **kwargs)
                if limit_try == wrapper.count_try:
                    raise TooManyErrors('Превышено количество попыток') from None
            return func
        wrapper.count_try = 0
        return wrapper
    return try_repeat


@count(limit_try=10)
def exception_func():
    """Тестовая функция"""
    num_1 = int(input('Vvod 1'))
    num_2 = int(input('Vvod 2'))
    summ = num_1 + num_2
    return summ


print(exception_func())
