"""
FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

"""


for i in range(1, 101):
    NUM = ''
    if (i % 3 == 0):
        NUM += 'Fizz'
    if (i % 5 == 0):
        NUM += 'Buzz'
    if not NUM:
        NUM += str(i)
    print(NUM)
