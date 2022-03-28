"""
Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors.
Т.е. если во время работы функции возникло какое-то исключение, то функция
должна перезапуститься еще раз. Количество перезапусков ограничено параметром
декоратора.
"""


class TooManyErrors(ValueError):
    pass


def decor_limit(num_dec):
    def decorator(func):
        def wrapper():
            counter = 0
            while counter < num_dec:
                try:
                    result = func()
                    return result
                except ValueError:
                    counter += 1
            raise TooManyErrors("Превышено количество попыток")
        return wrapper
    return decorator


par_decor = int(input("Введите количество перезапусков: "))


@decor_limit(par_decor)
def get_test():
    p = par_decor
    try:
        while p != 0:
            print(p)
            p -= 1
    finally:
        raise ValueError


get_test()
