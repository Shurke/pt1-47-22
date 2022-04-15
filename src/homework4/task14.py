"""
Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors.
Т.е. если во время работы функции возникло какое-то исключение, то функция
должна перезапуститься еще раз. Количество перезапусков ограничено параметром
декоратора.
"""

from functools import wraps
import random


class TooManyErrors(ValueError):
    pass


def decor_limit(max_tries):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(1, max_tries + 1):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    if n == max_tries:
                        raise TooManyErrors("Превышено количество попыток")
        return wrapper
    return decorator


@decor_limit(max_tries=5)
def get_test():
    """Генерерует число от 0 до 10

    :return: Возвращает 0 или 1
    """
    number = random.randint(0, 11)
    if number > 1:
        raise IOError
    else:
        return number


print(get_test())
