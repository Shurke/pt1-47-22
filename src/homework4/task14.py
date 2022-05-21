"""
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без
исключений (но не более n раз - параметр декоратора). Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors. Т.е. если во время работы функции
возникло какое-то исключение, то функция должна перезапуститься еще раз.
Количество перезапусков ограничено параметром декоратора.
"""


class TooManyErrors(Exception):
    pass


def decor_limit(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for n in range(limit):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if n == limit:
                        raise TooManyErrors("Превышено количество попыток")
        return wrapper
    return decorator


@decor_limit(limit=5)
def summary(a, b):
    return a + b


print(summary(5, 15))
