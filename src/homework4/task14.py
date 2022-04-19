"""
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений
(но не более n раз - параметр декоратора). Если превышено количество попыток, должно быть возбуждено
исключение типа TooManyErrors.
Т.е. если во время работы функции возникло какое-то исключение, то функция должна перезапуститься
еще раз. Количество перезапусков ограничено параметром декоратора.
"""


class TooManyErrors(Exception):
    """Exception class showing exceeding the number of tries"""
    pass


def parametrized_dec(numb_try):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                for quant_try in range(1, numb_try + 1):
                    if quant_try == numb_try:
                        raise TooManyErrors(f'Number of attempts exceeded: {numb_try} ')
        return wrapper
    return my_decorator


@parametrized_dec(3)
def count(numb):
    counter = 0
    for elem in range(numb + 1):
        if elem > counter:
            counter += 1
    return counter


print(count(6))
