"""
5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""


n = int(input('Введите число n: '))
number1 = 0
number2 = 1
sum = 0
index = 0

while index < n - 2:
    sum = number1 + number2
    number1 = number2
    number2 = sum
    index += 1

print('n-ое число Фибаначи:', sum)
