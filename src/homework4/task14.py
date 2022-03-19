"""
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений
(но не более n раз - параметр декоратора). Если превышено количество попыток, должно быть возбуждено
исключение типа TooManyErrors.
Т.е. если во время работы функции возникло какое-то исключение, то функция должна перезапуститься
еще раз. Количество перезапусков ограничено параметром декоратора.
"""


def decorator_with_limit(func, limit=10):

    def wrapper(*args, **kwargs):

        num_of_try = 0
        exit_flag = False
        while exit_flag is False and num_of_try < limit:
            try:
                func(*args, **kwargs)
                exit_flag = True
            except Exception:
                num_of_try += 1

        if exit_flag is True:
            print(f'Function executed after {num_of_try + 1} try.')
        else:
            raise BufferError('TooManyErrors')

    return wrapper


decorator_with_limit(sum, 5)([3, 4])
decorator_with_limit(sum, 5)(['frd', 4])
