"""
Реализовать класс Primes, который позволяет реализовать следующий набор действий
Простое число — это целое число больше 1, которое делится без остатка только на себя и на 1.
"""


class Primes:

    @staticmethod
    def __generate_primes():
        max_prime_amount = 10 ** 3
        prime_list = []
        for i in range(2, max_prime_amount + 1):
            divider = 0
            for j in range(2, i):
                if i % j == 0:
                    divider = j
            if not divider:
                prime_list.append(i)
        return prime_list

    prime_list = __generate_primes()

    def __init__(self, _prime_list):
        self.prime_list = _prime_list

    @classmethod
    def first(cls, amount):
        return Primes(cls.prime_list[:amount])

    def last(self, amount):
        return self.prime_list[-amount:]
