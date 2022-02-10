"""
В заданиях на сайте www.codewars.com нужно было написать только функцию.
Поэтому условия к вводу данных я формировал сам.
"""


"""
Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained.

Examples:
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words(text):
    rev = []
    lst = text.split(' ')
    for word in lst:
        rev.append(word[::-1])
    return ' '.join(rev)


string = input('Введите строку: ')
print(reverse_words(string))


"""
Given an array of integers your solution should find the smallest integer.
For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
"""


def find_smallest_int(arr):
    smallest = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest


string = input('Введите числа через пробел: ')
x = string.split(' ')
array = [int(elem) for elem in x]
print('Наименьшее число: ' + str(find_smallest_int(array)))


"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
"""


def basic_op(operator, value1, value2):
    if operator == '+':
        x = value1 + value2
    elif operator == '-':
        x = value1 - value2
    elif operator == '*':
        x = value1 * value2
    elif operator == '/':
        x = value1 / value2
    return x


"""
Write a function which converts the input string to uppercase.
https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/train/python
"""


def make_upper_case(s):
    upper = s.upper()
    return upper



"""
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
"""


def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False
