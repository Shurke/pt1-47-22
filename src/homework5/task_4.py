"""
Реализовать класс Primes, который позволяет реализовать следующий набор действий
Простое число — это целое число больше 1, которое делится без остатка только на
себя и на 1.
"""


class Primes(list):
    """Prime number class with various metadata"""

    @staticmethod
    def first(number_first):
        """Return the first number_first numbers"""
        if number_first <= 0:
            return "The number must be greater than 0"

        def is_prime(num):
            for item in range(2, num // 2 + 1):
                if num % item == 0:
                    return None
            return num

        prime_number = 2
        list_prime_numbers = Primes()
        while len(list_prime_numbers) < number_first:
            if is_prime(prime_number):
                list_prime_numbers.append(prime_number)
            prime_number += 1
        return list_prime_numbers

    def last(self, number_last):
        """Return the first number_last numbers"""
        if number_last <= 0:
            return "The number must be greater than 0"
        return self[-number_last:]
