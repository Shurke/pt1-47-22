"""
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений
(но не более n раз - параметр декоратора). Если превышено количество попыток, должно быть возбуждено
исключение типа TooManyErrors.
Т.е. если во время работы функции возникло какое-то исключение, то функция должна перезапуститься
еще раз. Количество перезапусков ограничено параметром декоратора.
"""


class TooManyErrors(Exception):
    def __init__(self, text):
        self.txt = text


def decorator_with_limit(limit=10):
    """Repeat /limit/ times or exception"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            num_of_try = 0
            exit_flag = False
            while not exit_flag and num_of_try < limit:
                try:
                    result = func(*args, **kwargs)
                    exit_flag = True
                except TypeError:
                    num_of_try += 1

            if exit_flag is True:
                print(f'Function executed after {num_of_try + 1} try.')
            else:
                raise TooManyErrors(f'Function not executed after {limit} times')
            return result
        return wrapper
    return decorator


print(decorator_with_limit(5)(sum)([3, 4]))
print(decorator_with_limit(5)(sum)(['frd', 4]))
