"""
Реализовать класс Primes, который позволяет реализовать следующий набор действий:

Primes.first(1)
=> [2]

Primes.first(2)
=> [2, 3]

Primes.first(5)
=> [2, 3, 5, 7, 11]

Primes.first(20).last(5)
=> [53, 59, 61, 67, 71]
"""


class Primes(list):
    """Child class from a 'list' that works with prime numbers

    first(n) - return the first n prime numbers starting with 2
    last(n) - return the last n numbers from the prime list
    """

    @staticmethod
    def first(right_limit):
        """Return the first n prime numbers starting with 2"""

        def is_prime(num):
            if num % 2 == 0:
                return num == 2
            divide = 3
            while divide * divide <= num and num % divide != 0:
                divide += 2
            return divide * divide > num

        prime_number = 2
        result_list = Primes()

        while len(result_list) < right_limit:
            if is_prime(prime_number):
                result_list.append(prime_number)
            prime_number += 1

        return result_list

    def last(self, left_limit):
        """Return the last n numbers from the prime list"""
        if left_limit <= 0:
            return []
        return self[-left_limit:]
