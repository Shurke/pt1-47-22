"""Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без
исключений (но не более n раз - параметр декоратора). Если превышено количество попыток, должно
быть возбуждено исключение типа TooManyErrors.
Т.е. если во время работы функции возникло какое-то исключение, то функция должна перезапуститься
еще раз. Количество перезапусков ограничено параметром декоратора.
"""


class TooManyErrors(Exception):
    pass


def count(count):
    def try_repeat(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception:
                if count > wrapper.count_try:
                    wrapper.count_try += 1
                    print(f'Использовано попыток {wrapper.count_try} из {count}')
                    return wrapper(*args, **kwargs)
                else:
                    raise TooManyErrors('Превышено количество попыток')
            else:
                return func
        wrapper.count_try = 0
        return wrapper
    return try_repeat


@count(count=10)
def exception_func():
    num_1 = int(input('Vvod 1'))
    num_2 = int(input('Vvod 2'))
    summ = num_1 + num_2
    return summ


print(exception_func())
