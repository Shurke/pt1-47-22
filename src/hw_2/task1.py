"""
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
 а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


for char in range(1, 101):
    if char % 3 == 0:
        print('Fizz')
    elif char % 5 == 0:
        print('Buzz')
    elif char % 3 == 0 and char % 5 == 0:
        print('FizzBuzz')
    else:
        print(char)
