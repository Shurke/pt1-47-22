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

# В задании на сайте www.codewars.com нужно было написать только функцию.
# Поэтому условия к вводу данных я формировал сам.


