"""
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных
и 3 и 5 - FizzBuzz
"""

list1 = []
for item in range(1, 101):
    if item % 15 == 0:
        list1.append('FizzBuzz')
    elif item % 3 == 0:
        list1.append('Fizz')
    elif item % 5 == 0:
        list1.append('Buzz')
    else:
        list1.append(item)
print(list1)
