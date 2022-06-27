"""
Евгения создала класс KgToPounds с параметром kg, куда передается определенное
количество килограмм, а с помощью метода to_pounds() они переводятся в фунты.
Чтобы закрыть доступ к переменной “kg” она реализовала методы set_kg() - для
задания нового значения килограммов, get_kg()  - для вывода текущего значения
кг. Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода
для задания и вывода значений. Помогите ей переделать класс с использованием
функции property() и свойств-декораторов.
"""


class KgToPounds:
    """Class converts kilograms to pounds."""
    def __init__(self, kg):
        if isinstance(kg, (int, float)):
            self.__kg = kg
        else:
            raise ValueError('Kilograms are given only by numbers')

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Kilograms are given only by numbers')
