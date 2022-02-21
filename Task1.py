# Напишите программу, которая печатает цифры от 1 до 100, но вместо
# чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
list_of_numbers = [int(i) for i in list(range(1, 101))]
for number in list_of_numbers:
    if number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
    elif number % 5 == 0:
        number = "Buzz"
    elif number % 3 == 0:
        number = "Fizz"
    print(number)
