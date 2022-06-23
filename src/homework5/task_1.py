"""
Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
 а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной “kg”
 она реализовала методы set_kg() - для задания нового значения килограммов,
 get_kg()  - для вывода текущего значения кг. Из-за этого возникло неудобство:
 нам нужно теперь использовать эти 2 метода для задания и вывода значений.
 Помогите ей переделать класс с использованием функции property() и свойств-декораторов.
"""


class KgToPounds:

    def __init__(self, kg):
        if isinstance(kg, (int, float)):
            self._kg = kg
        else:
            raise TypeError('Килограммы задаются только числами')

    def to_pounds(self):
        return self._kg * 2.205

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self._kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
