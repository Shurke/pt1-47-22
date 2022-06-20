"""
Singleton — это класс, который позволяет создать только один экземпляр самого себя и предоставляет
доступ к этому созданному экземпляру. Реализуйте singleton двумя разными способами:
- напишите декоратор класса "singleton", чтобы украсить любой класс и сделать его одноэлементным
- реализовать одиночную логику внутри вашего пользовательского класса, используя метод для
инициализации экземпляра класса
"""


def singleton(cls):
    """Decorator, which makes the class a single element"""

    instance = {}

    def getinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return getinstance


class Singleton:
    """Class that can only create one instance"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)

        return cls.__instance
