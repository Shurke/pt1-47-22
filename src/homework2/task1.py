"""
FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


for CHAR in range(1, 101):
    if CHAR % 5 == 0 and CHAR % 3 == 0:
        print('FizzBuzz')
    elif CHAR % 5 == 0:
        print('Buzz')
    elif CHAR % 3 == 0:
        print('Fizz')
    else:
        print(CHAR)
