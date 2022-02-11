"""
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""


n = int(input('Введите порядковый номер числа Фибоначи: '))
n1 = 0                              # variable for first number in the fibonacci series
n2 = 1                              # variable for second number in the fibonacci series
print(n1, n2, end=' ')
x = 0                               # counter value variable
while x < n - 2:
    n3 = n1 + n2                    # variable for third number in the fibonacci series
    n1 = n2
    n2 = n3
    x = x + 1                       # increment the counter
    print(n2, end=' ')              # displays the entire row up to the specified in the condition
print('\n')
print(n2)
