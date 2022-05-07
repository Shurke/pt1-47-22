"""
Singleton — это класс, который позволяет создать только один экземпляр самого себя и предоставляет
доступ к этому созданному экземпляру. Реализуйте singleton двумя разными способами:

 - напишите декоратор класса "singleton", чтобы украсить любой класс и сделать его одноэлементным
 - реализовать одиночную логику внутри вашего пользовательского класса, используя метод для
инициализации экземпляра класса
"""


def singleton_wrapper(cls):
    """Singleton-wrapper created according to PEP 318"""
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


class SingletonClass:
    """Single threaded singleton class"""

    __instance = None

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = super(SingletonClass, cls).__new__(cls)
            cls.name = name
        return cls.__instance

    @staticmethod
    def some_business_method():
        """Method docstring(pylint)"""
        return 'You are very cool!'

    @staticmethod
    def some_other_business_method():
        """Method docstring(pylint)"""
        return 'You are very cool!'
