"""Реализовать класс Primes, который позволяет реализовать следующий набор действий

Primes.first(1)
# => [2]

Primes.first(2)
# => [2,3]

Primes.first(5)
# => [2, 3, 5, 7]

Primes.first(20).last(5)
# => [53, 59, 61, 67, 71]


Простое число — это целое число больше 1, которое делится без остатка только на себя и на 1.
"""

from sympy import sieve


class Primes:

    def __init__(self):
        self.primes_list = []

    def first(self, count_of_nums):
        end_of_range = 100 if count_of_nums < 100 else int(f'10{("0"*len(str(count_of_nums)))}')
        for num in range(0, count_of_nums):
            self.primes_list.append(list(sieve.primerange(0, end_of_range))[num])
        return self.primes_list

    def last(self, count_of_nums):
        if self.primes_list:
            return [num for num in self.primes_list[-count_of_nums:]]
        else:
            raise ValueError('Не найден список простых чисел!')
