"""
5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""

F1, F2 = 0, 1

n = input('Please enter the number: n = ')
n = int(n) - 2

while n > 0:
    F1, F2 = F2, F1 + F2
    n -= 1

print('Fibonacci number value =', F2)
