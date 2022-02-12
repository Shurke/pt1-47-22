"""
5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""

f1 = f2 = 1

n = input('Please enter the number: n = ')
n = int(n) - 2

while n > 0:
    f1, f2 = f2, f1 + f2
    n -= 1

print('Fibonacci number value =', f2)
