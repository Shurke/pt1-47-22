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
Простое число — это целое число больше 1, которое делится без остатка только на себя и на 1.
"""


class Primes(list):
    """A class for generating a list of prime numbers using various methods"""

    @staticmethod
    def first(first_numb):
        """Return the first prime numbers in range numb"""

        def is_prime(numb):
            """Checks if the number is prime"""

            if numb % 2 == 0:
                return numb == 2
            divide = 3
            while divide ** 2 <= numb and numb % divide != 0:
                divide += 2
            return divide ** 2 > numb

        prime_lst = Primes()
        prime = 2
        if isinstance(first_numb, int) and first_numb > 0:
            while len(prime_lst) < first_numb:
                if is_prime(prime):
                    prime_lst.append(prime)
                prime += 1
            return prime_lst
        else:
            return 'Wrong data!'

    def last(self, last_numb):
        """Return last numbers from list of prime numbers"""

        if isinstance(last_numb, int) and last_numb > 0:
            return self[-last_numb:]
        else:
            return 'Wrong data!'
