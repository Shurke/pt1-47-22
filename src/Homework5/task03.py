"""Singleton — это класс, который позволяет создать только один экземпляр самого себя и
предоставляет доступ к этому созданному экземпляру. Реализуйте singleton двумя разными способами:
напишите декоратор класса "singleton", чтобы украсить любой класс и сделать его одноэлементным
реализовать одиночную логику внутри вашего пользовательского класса, используя метод для
инициализации экземпляра класса"""


def singleton(Cls):
    singletons = {}

    def getinstance(*args, **kwargs):
        if Cls not in singletons:
            singletons[Cls] = Cls(*args, **kwargs)
        return singletons[Cls]

    return getinstance


@singleton
class Class1:
    def __init__(self):
        self.val = 3


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Class2(metaclass=Singleton):
    def __init__(self):
        self.val = 33
