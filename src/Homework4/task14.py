"""Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится
без исключений (но не более n раз - параметр декоратора). Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors.
Т.е. если во время работы функции возникло какое-то исключение, то функция должна перезапуститься
еще раз. Количество перезапусков ограничено параметром декоратора."""


class LimitOfErrors(Exception):
    pass


def limiter(lim):
    def dec(func):
        def wrapper(*args, **kwargs):
            for number in range(lim):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if number == lim:
                        raise LimitOfErrors("Достигнут предел попыток")
        return wrapper
    return dec


@limiter(lim=5)
def addition(x, y):
    return x + y


print(addition(input("Первое число: "), input("Второе число: ")))
