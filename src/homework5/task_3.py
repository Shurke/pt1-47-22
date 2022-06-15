"""
Singleton — это класс, который позволяет создать только один экземпляр самого
себя и предоставляет доступ к этому созданному экземпляру. Реализуйте singleton
двумя разными способами:
напишите декоратор класса "singleton", чтобы украсить любой класс и сделать его
одноэлементным
реализовать одиночную логику внутри вашего пользовательского класса, используя
метод для инициализации экземпляра класса
"""

import functools


def singleton(cls):
    """Makes the class a singleton class"""

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instances:
            wrapper.instances = cls(*args, **kwargs)
        return wrapper.instances
    wrapper.instances = None
    return wrapper


class Singleton(object):
    """Single threaded singleton class"""
    __instances = None

    def __new__(cls, *args, **kwargs):
        if cls.__instances is None:
            cls.__instances = super(Singleton, cls).__new__(cls)
        return cls.__instances
