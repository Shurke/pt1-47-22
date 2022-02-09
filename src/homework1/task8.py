"""
codewars katas for homework #1

Из-за того что это не классический "модульный" файл, а "куски" кода это
решения отдельной каты со своими импортами (реимпортами), переопределением имён функций и переменных
то отключены соответствующие проверки pylint и flake8

Задач было нарешано больше 100, но среди 7 и 8 kyu было крайне мало тех,
что заставляли задуматься больше чем на 5-15 минут, сюда собрал только 6-4 kyu
Полный список решенного: https://www.codewars.com/users/inorangestylee/completed
"""

# 1. Replace With Alphabet Position
# Rank: 6
# URL: https://www.codewars.com/kata/546f922b54af40e1e90001da
# In this kata you are required to, given a string,
# replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return:
# "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
import string


def alphabet_position(text):
    return " ".join([str(string.ascii_lowercase.find(
        x.lower()) + 1) for x in text if x.lower() in string.ascii_lowercase])


# 2. Find the odd int
# Rank: 6
# URL: https://www.codewars.com/kata/54da5a58ea159efa38000836
# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
def find_it(seq):
    return next(x for x in set(seq) if seq.count(x) % 2 != 0)


# 3. Are they the "same"?
# Rank: 6
# URL: https://www.codewars.com/kata/550498447451fbbd7600041c
# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b))
# that checks whether the two arrays have the "same" elements, with the same multiplicities
# (the multiplicity of a member is the number of times it appears).
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
# Examples
# Valid arrays
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121,
# 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on.
# It gets obvious if we write b's elements in terms of squares:
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# Invalid arrays
# If, for example, we change the first number to something else, comp is not returning true anymore:
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 132 is not the square of any number of a.
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 36100 is not the square of any number of a.
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) == 0 and len(array2) == 0:
        return True
    for a in array2:
        if a == 0 and a not in array1:
            return False
        elif a**0.5 not in array1:
            if -(a**0.5) not in array1:
                return False
            else:
                array1.remove(-(a**0.5))
        else:
            array1.remove(a**0.5)
    return True


# 4. Detect Pangram
# Rank: 6
# URL: https://www.codewars.com/kata/545cedaa9943f7fe7b000048
# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
#   because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.
import string  # noqa: F811,E402


def is_pangram(s):
    for ch in string.ascii_lowercase:
        if ch not in s.lower():
            return False
    return True


# 5. Build a pile of Cubes
# Rank: 6
# URL: https://www.codewars.com/kata/5592e3bd57b64d00f3000047
# Your task is to construct a building which will be a pile of n cubes.
# The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and
# so on until the top which will have a volume of 1^3.
# You are given the total volume m of the building.
# Being given m can you find the number n of cubes you will have to build?
# The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m
# and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m
# if such a n exists or -1 if there is no such n.
# Examples:
# findNb(1071225) --> 45
# findNb(91716553919377) --> -1
def find_nb(m):
    x, n = 0, 0
    while m > x:
        n += 1
        x = x + n**3
    if m != x:
        return -1
    return n


# 6. Where my anagrams at?
# Rank: 5
# URL: https://www.codewars.com/kata/523a86aa4230ebb5420001e1
# What is an anagram?
# Well, two words are anagrams of each other if they both contain the same letters.
# For example:
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none.
# For example:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
def anagrams(word, words):
    return [w for w in words if sorted(word) == sorted(w)]


# 7. Memoized Fibonacci
# Rank: 5
# URL: https://www.codewars.com/kata/529adbf7533b761c560004e5
# Problem Context
# The Fibonacci sequence is traditionally used to explain tree recursion.
# def fibonacci(n):
#     if n in [0, 1]:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
# This algorithm serves welll its educative purpose but it's tremendously inefficient,
# not only because of recursion, but because we invoke the fibonacci function twice,
# and the right branch of recursion (i.e. fibonacci(n-2)) recalculates all the Fibonacci numbers
# already calculated by the left branch
# (i.e. fibonacci(n-1)).
# This algorithm is so inefficient that the time to calculate any Fibonacci number over 50
# is simply too much.
# You may go for a cup of coffee or go take a nap while you wait for the answer.
# But if you try it here in Code Wars you will most likely get a code timeout before any answers.
# For this particular Kata we want to implement the memoization solution.
# This will be cool because it will let us keep using the tree recursion algorithm
# while still keeping it sufficiently optimized
# to get an answer very rapidly.
# The trick of the memoized version is that we will keep a cache data structure
# (most likely an associative array) where we will store the Fibonacci numbers as we calculate them.
# When a Fibonacci number is calculated, we first look it up in the cache,
# if it's not there, we calculate it and put it in the cache,
# otherwise we returned the cached number.
# Refactor the function into a recursive Fibonacci function that using a memoized data structure
# avoids the deficiencies of tree recursion.
# Can you make it so the memoization cache is private to this function?
cache = [0, 1, 1]


def fibonacci(n):
    global cache
    if n < len(cache):
        return cache[n]
    cache.append(cache[-2] + cache[-1])
    return fibonacci(n - 1) + fibonacci(n - 2)


# 8. Matrix Determinant
# Rank: 4
# URL: https://www.codewars.com/kata/52a382ee44408cea2500074c
# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant
# of the matrix.
# How to take the determinant of a matrix -- it is simplest to start with the smallest cases:
# A 1x1 matrix |a| has determinant a.
# A 2x2 matrix [ [a, b], [c, d] ] or
# |a  b|
# |c  d|
# has determinant: a*d - b*c.
# The determinant of an n x n sized matrix is calculated by reducing the problem
# to the calculation of the determinants of n matrices ofn-1 x n-1 size.
# For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or
# |a b c|
# |d e f|
# |g h i|
# the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor)
# refers to taking the determinant of the 2x2 matrix
# created by crossing out the row and column in which the element a occurs:
# |- - -|
# |- e f|
# |- h i|
# Note the alternation of signs.
# The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix
# with first row [a, b, c, d], then:
# det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    det = 0
    for c, _ in enumerate(matrix[0]):
        m = copyMatrix(matrix)
        if c % 2 == 0:
            det += m[0][c] * determinant(removeMatrixCross(m, c))
        else:
            det -= m[0][c] * determinant(removeMatrixCross(m, c))
    return det


def removeMatrixRow(matrix, num):
    m = copyMatrix(matrix)
    del m[num]
    return m


def removeMatrixCol(matrix, num):
    m = copyMatrix(matrix)
    for i, _ in enumerate(m):
        del m[i][num]
    return m


def removeMatrixCross(matrix, num):
    m = copyMatrix(matrix)
    m = removeMatrixRow(m, 0)
    m = removeMatrixCol(m, num)
    return m


def copyMatrix(matrix):
    return [row[:] for row in matrix]


# 9. Rot13
# Rank: 5
# URL: codewars.com/kata/530e15517bc88ac656000716
# ROT13 is a simple letter substitution cipher that replaces a letter
# with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string,
# they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted,
# like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.
import string  # noqa: F811,E402


def rot13(message):
    result = []
    for ch in message:
        if ch.isupper():
            alphabet = string.ascii_uppercase
        else:
            alphabet = string.ascii_lowercase
        if ch in alphabet:
            idx = alphabet.index(ch) + 13
            if idx > len(alphabet) - 1:
                idx -= len(alphabet)
            result.append(alphabet[idx])
        else:
            result.append(ch)
    return "".join(result)


# 10. Directions Reduction
# Rank: 5
# URL: https://www.codewars.com/kata/550f22f4d758534c1100025a
# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another.
# The directions were "NORTH", "SOUTH", "WEST", "EAST".
# Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
# Going to one direction and coming back the opposite direction right away is a needless effort.
# Since this is the wild west, with dreadfull weather and not much water,
# it's important to save yourself some energy, otherwise you might die of thirst!
# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):
# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]
# You can immediatly see that going "NORTH" and immediately "SOUTH" is not reasonable,
# better stay to the same place! So the task is to give to the man a simplified version of the plan.
# A better plan in this case is simply:
# ["WEST"]
# or
# { "WEST" }
# or
# [West]
# Other examples:
# In ["NORTH", "SOUTH", "EAST", "WEST"]
# the direction "NORTH" + "SOUTH" is going north and coming back right away.
# The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other,
# therefore, the final result is [] (nil in Clojure).
# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH"
# are not directly opposite but they become directly opposite after the reduction
# of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].
# Task
# Write a function dirReduc which will take an array of strings and
# returns an array of strings with the needless directions removed (W<->E or S<->N side by side).
# The Haskell version takes a list of directions with data Direction = North | East | West | South.
# The Clojure version returns nil when the path is reduced to nothing.
# The Rust version takes a slice of enum Direction {North, East, West, South}.
import enum  # noqa: F811,E402


class DirectionEnum(enum.Enum):
    NORTH = 1 << 0
    SOUTH = 1 << 1
    EAST = 1 << 2
    WEST = 1 << 3


def dirReduc(arr):
    if len(arr) <= 1:
        return arr
    for i in range(0, len(arr) - 1):
        if bin(DirectionEnum[arr[i]].value | DirectionEnum[arr[i + 1]].value) in ['0b11', '0b1100']:
            del arr[i + 1]
            del arr[i]
            return dirReduc(arr)
    return arr


# 11. Strip Comments
# Rank: 4
# URL: https://www.codewars.com/kata/51c8e37cee245da6b40000bd
# Complete the solution so that it strips all text that follows any of a set of comment markers
# passed in.
# Any whitespace at the end of the line should also be stripped out.
# Example:
# Given an input string of:
# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:
# apples, pears
# grapes
# bananas
# The code would be called like so:
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
def solution(s, markers):
    result = s.split("\n")
    for i, l in enumerate(result):
        for m in markers:
            if l.find(m) != -1:
                result[i] = result[i][0:l.find(m)]
    return '\n'.join([a.strip() for a in result])


# 12. Pick peaks
# Rank: 5
# URL: https://www.codewars.com/kata/5279f6fe5ab7f447890006a7
# In this kata, you will write a function that returns the positions and the values of the "peaks"
# (or local maxima) of a numeric array.
# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3
# with a value of 5 (since arr[3] equals 5).
# The output will be returned as an object with two properties: pos and peaks.
# Both of these properties should be arrays.
# If there is no peak in the given array, then the output should be {pos: [], peaks: []}.
# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
# should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)
# All input arrays will be valid integer arrays (although it could still be empty),
# so you won't need to validate the input.
# The first and last elements of the array will not be considered as peaks
# (in the context of a mathematical function, we don't know what is after and before and therefore,
# we don't know if it is a peak or not).
# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3]
# and [1, 2, 2, 2, 2] do not.
# In case of a plateau-peak, please only return the position
# and value of the beginning of the plateau.
# For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]}
def pick_peaks(arr):
    pos = []
    peaks = []
    vpos = None
    vpeak = None
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            vpos = i
            vpeak = arr[i]
            continue

        if arr[i] < arr[i - 1] and vpos is not None and vpeak is not None:
            pos.append(vpos)
            peaks.append(vpeak)
            vpos = None
            vpeak = None

    return {'pos': pos, 'peaks': peaks}


# 13. Sudoku Solution Validator
# Rank: 4
# URL: Sudoku Solution Validator
# Sudoku Background
# Sudoku is a game played on a 9x9 grid.
# The goal of the game is to fill all cells of the grid with digits from 1 to 9,
# so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks)
# contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)
# Sudoku Solution Validator
# Write a function validSolution/ValidateSolution/valid_solution()
# that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution,
# or false otherwise.
# The cells of the sudoku board may also contain 0's, which will represent empty cells.
# Boards containing one or more zeroes are considered to be invalid solutions.
# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
# Examples
# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 5, 3, 4, 8],
#   [1, 9, 8, 3, 4, 2, 5, 6, 7],
#   [8, 5, 9, 7, 6, 1, 4, 2, 3],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 6, 1, 5, 3, 7, 2, 8, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]); // => true
# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ]); // => false
import string  # noqa: F811,E402

DIGITS_KIT = string.digits[1:]


def valid_solution(board):
    return valid_lines(board) and valid_rows(board) and valid_matrix(board)


def valid_lines(board):
    for line in board:
        line_str = "".join(sorted([str(x) for x in line]))
        if line_str != DIGITS_KIT:
            return False
    return True


def valid_rows(board):
    row = []
    for j, _ in enumerate(board[0]):
        for i, _ in enumerate(board):
            row.append(board[i][j])
        row_str = "".join(sorted([str(x) for x in row]))
        if row_str != DIGITS_KIT:
            return False
        row.clear()
    return True


def valid_matrix(board):
    matrix = []
    for num in range(0, 9, 3):
        for i in range(0 + num, 0 + num + 3):
            for j in range(0 + num, 0 + num + 3):
                matrix.append(board[i][j])
        matrix_str = "".join(sorted([str(x) for x in matrix]))
        if matrix_str != DIGITS_KIT:
            return False
        matrix.clear()
    return True


# 14. Sum by Factors
# Rank: 4
# URL: https://www.codewars.com/kata/54d496788776e49e6b00052f
# Given an array of positive or negative integers
# I= [i1,..,in]
# you have to produce a sorted array P of the form
# [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]
# P will be sorted by increasing order of the prime numbers.
# The final result has to be given as a string in Java, C#, C, C++
# and as an array of arrays in other languages.
# Example:
# I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
# [2, 3, 5] is the list of all prime factors of the elements of I, hence the result.
def get_prime_factor(num):
    result = []
    num = abs(num)

    while num % 2 == 0:
        num /= 2
        result.append(2)

    for d in range(3, int(num ** 0.5) + 1, 2):
        while num % d == 0:
            num /= d
            result.append(d)
    if num > 2:
        result.append(int(num))
    return result


def sum_for_list(lst):
    result = []

    factors = []
    for n in lst:
        factors.extend(get_prime_factor(n))
    factors = sorted(list(set(factors)))
    for f in factors:
        total = 0
        for n in lst:
            if n % f == 0:
                total += n
        result.append([f, total])
    return result


# 15. Last digit of a large number
# Rank: 5
# URL: https://www.codewars.com/kata/5511b2f550906349a70004e1
# Define a function that takes in two non-negative integers aaa and bbb
# and returns the last decimal digit of a^b
# Note that a and b may be very large!
# For example, the last decimal digit of 9^7 is 9,
# since 9^7=4782969
# The last decimal digit of (2^200)^(2^200),
# which has over 10^92 decimal digits, is 6.
# Also, please take 0^1 to be 1
# You may assume that the input will always be valid.
# Examples
# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6
def last_digit(n1, n2):
    return pow(n1, n2, 10)


# 16. Permutations
# Rank: 4
# URL: https://www.codewars.com/kata/5254ca2719453dcc0b00027d
# In this kata you have to create all permutations of an input string and remove duplicates,
# if present.
# This means, you have to shuffle all letters from the input in all possible orders.
# Examples:
# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# The order of the permutations doesn't matter.
def permutations(s):
    result = []
    result.append(s)
    if len(s) == 2:
        result.append("".join([s[1], s[0]]))
    elif len(s) > 2:
        for i, v in enumerate(s):
            for sub_s in permutations("".join([s[:i], s[i + 1:]])):
                result.append("".join([v, sub_s]))
    return list(set(result))


# 17. Duplicate Encoder
# Rank: 6
# URL: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
# The goal of this exercise is to convert a string to a new string
# where each character in the new string is "(" if that character appears only once
# in the original string, or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
def duplicate_encode(word):
    result = list(word)
    for i, v in enumerate(word):
        if word.lower().count(v.lower()) > 1:
            result[i] = ")"
        else:
            result[i] = "("
    return "".join(result)


# 18. Delete occurrences of an element if it occurs more than n times
# Rank: 6
# URL: https://www.codewars.com/kata/554ca54ffa7d91b236000023
# Enough is enough!
# Alice and Bob were on a holiday. Both of them took many pictures of the places they've been,
# and now they want to show Charlie their entire collection.
# However, Charlie doesn't like these sessions, since the motive usually repeats.
# He isn't fond of seeing the Eiffel tower 40 times.
# He tells them that he will only sit during the session if they show the same motive
# at most N times. Luckily, Alice and Bob are able to encode the motive as a number.
# Can you help them to remove numbers such that their list contains each number only up to N times,
# without changing the order?
# Task
# Given a list lst and a number N, create a new list that contains each number of lst
# at most N times without reordering.
# For example if N = 2, and the input is [1,2,3,1,2,1,2,3],
# you take [1,2,3,1,2],
# drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times,
# and then take 3, which leads to [1,2,3,1,2,3].
# Example
#   delete_nth ([1,1,1,1],2) # return [1,1]
#   delete_nth ([20,37,20,21],1) # return [20,37,21]
def delete_nth(lst, max_e):
    result = []
    lst_dict = {}
    for v in set(lst):
        lst_dict[v] = 0
    for n in lst:
        if lst_dict[n] < max_e:
            result.append(n)
            lst_dict[n] += 1
    return result


# 19. The Supermarket Queue
# Rank: 6
# URL: https://www.codewars.com/kata/57b06f90e298a7b53d000a86
# There is a queue for the self-checkout tills at the supermarket.
# Your task is write a function to calculate the total time required for all the customers
# to check out!
# input
# customers: an array of positive integers representing the queue.
# Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.
# Examples
# queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times
# queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.
# queue_time([2,3,10], 2)
# should return 12
def queue_time(customers, n):
    stack = [0] * n
    for i in customers:
        stack[stack.index(min(stack))] += i
    return max(stack)


# 20. Your order, please
# Rank: 6
# URL: https://www.codewars.com/kata/55c45be3b2079eccff00010f
# Your task is to sort a given string.
# Each word in the string will contain a single number.
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""
def order(sentence):
    sentence_list = sentence.split()
    if len(sentence_list) > 0:
        result = [""] * len(sentence_list)
    else:
        result = [""]
    for w in sentence_list:
        result[get_word_num(w) - 1] = w
    return " ".join(result)


def get_word_num(word):
    for v in word:
        if v.isdigit():
            return int(v)
    return


# 21. Sort the odd
# Rank: 6
# URL: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
# Task
# You will be given an array of numbers.
# You have to sort the odd numbers in ascending order
# while leaving the even numbers at their original positions.
# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
def sort_array(source_array):
    odd_nums = sorted([x for x in source_array if x % 2 != 0])
    for i, v in enumerate(source_array):
        if v % 2 != 0:
            source_array[i] = odd_nums.pop(0)
    return source_array


# 22. Equal Sides Of An Array
# Rank: 6
# URL: https://www.codewars.com/kata/5679aa472b8f57fb8c000047
# You are going to be given an array of integers.
# Your job is to take that array and find an index N where
# the sum of the integers to the left of N is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.
# For example:
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array,
# the sum of left side of the index ({1,2,3}) and
# the sum of the right side of the index ({3,2,1}) both equal 6.
# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1,
# because at the 1st position of the array, the sum of left side of the index ({1}) and
# the sum of the right side of the index ({50,-51,1,1}) both equal 1.
# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


# 23. Build Tower
# Rank: 6
# URL: https://www.codewars.com/kata/576757b1df89ecf5bd00073b
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# Tower block is represented as *
# for example, a tower of 3 floors looks like below
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]
# and a tower of 6 floors looks like below
# [
#   '     *     ',
#   '    ***    ',
#   '   *****   ',
#   '  *******  ',
#   ' ********* ',
#   '***********'
# ]
def tower_builder(n_floors):
    result = []
    for i in range(1, n_floors + 1):
        spaces = (n_floors * 2 - 1) - (i * 2 - 1)
        line = "{0}{1}{0}".format(" " * (spaces // 2), "*" * (i * 2 - 1))
        result.append(line)
    return result


# 24. Count the smiley faces!
# Rank: 6
# URL: https://www.codewars.com/kata/583203e6eb35d7980400002a
# Given an array (arr) as an argument complete the function countSmileys
# that should return the total number of smiling faces.
# Rules for a smiling face:
# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]
# Example
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
def count_smileys(arr):
    c = 0
    for s in arr:
        if s[0] in [":", ";"] and s[-1] in [")", "D"]:
            if len(s) == 3 and s[1] in ["-", "~"]:
                c += 1
            if len(s) == 2:
                c += 1
    return c


# 25. Mexican Wave
# Rank: 6
# URL: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
# Introduction
# The wave (known as the Mexican wave in the English-speaking world outside North America)
# is an example of metachronal rhythm achieved in a packed stadium
# when successive groups of spectators briefly stand, yell, and raise their arms.
# Immediately upon stretching to full height, the spectator returns to the usual seated position.
# The result is a wave of standing spectators that travels through the crowd,
# even though individual spectators never move away from their seats.
# Task
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
# You will be passed a string and you must return that string in an array where an uppercase letter
# is a person standing up.
# Rules
#  1.  The input string will always be lower case but maybe empty.
#  2.  If the character in the string is whitespace then pass over it as if it was an empty seat
# Example
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
def wave(p):
    return [p[:i] + p[i].upper() + p[i + 1:] for i in range(len(p)) if p[i].isalpha()]


# 26. Unique In Order
# Rank: 6
# URL: https://www.codewars.com/kata/54e6533c92449cc251001667
# Implement the function unique_in_order which takes as argument a sequence and
# returns a list of items without any elements with the same value next to each other and
# preserving the original order of elements.
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
def unique_in_order(iterable):
    result = []
    for ch in iterable:
        if len(result) < 1 or result[len(result) - 1] != ch:
            result.append(ch)
    return result


# 27. Product of consecutive Fib numbers
# Rank: 5
# URL: https://www.codewars.com/kata/5541f58a944b85ce6d00006a
# The Fibonacci numbers are the numbers in the following integer sequence (Fn):
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
# such as
# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
# F(n) * F(n+1) = prod.
# Your function productFib takes an integer (prod) and returns an array:
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
# If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return
# [F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(n) being the smallest one such as F(n) * F(n+1) > prod.
# Some Examples of Return:
# (depend on the language)
# productFib(714) # should return (21, 34, true),
#                 # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
# productFib(800) # should return (34, 55, false),
#                 # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
# -----
# productFib(714) # should return [21, 34, true],
# productFib(800) # should return [34, 55, false],
# -----
# productFib(714) # should return {21, 34, 1},
# productFib(800) # should return {34, 55, 0},
# -----
# productFib(714) # should return {21, 34, true},
# productFib(800) # should return {34, 55, false}
def productFib(prod):
    p, n = 0, 1
    while p * n < prod:
        p, n = n, p + n
    return [p, n, p * n == prod]


# 28. Counting Duplicates
# Rank: 6
# URL: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and
# numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
def duplicate_count(text):
    my_dict = {ch: text.lower().count(ch) for ch in set(text.lower())}
    return len(dict(filter(lambda elem: elem[1] > 1, my_dict.items())))


# 29. Write Number in Expanded Form
# Rank: 6
# URL: https://www.codewars.com/kata/5842df8ccbd22792a4000245
# You will be given a number and you will need to return it as a string in Expanded Form.
# For example:
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.
def expanded_form(num):
    result = []
    d = 10
    while num != 0:
        if num % d != 0:
            result.insert(0, num % d)
            num -= num % d
        d *= 10
    return " + ".join([str(x) for x in result])


# 30. Two Sum
# Rank: 6
# URL: https://www.codewars.com/kata/52c31f8e6605bcc646000082
# Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple like so: (index1, index2).
# For the purposes of this kata, some tests may have multiple answers;
# any valid solutions will be accepted.
# The input will always be valid (numbers will be an array of length 2 or greater,
# and all of the items will be numbers;
# target will always be the sum of two different items from that array).
# Based on: http://oj.leetcode.com/problems/two-sum/
# twoSum [1, 2, 3] 4 === (0, 2)
def two_sum(numbers, target):
    for i, _ in enumerate(numbers):
        for j, _ in enumerate(numbers):
            if i != j and numbers[i] + numbers[j] == target:
                return [i, j]
    return


# 31. Extract the domain name from a URL
# Rank: 5
# URL: https://www.codewars.com/kata/514a024011ea4fb54200004b
# Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string.
# For example:
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"
import re  # noqa: F811,E402


def domain_name(url):
    result = re.match(r'^(?:\w+:\/\/)?(?:www)?(?:\.)?([\w\-]+)(?:.+)$', url)
    return result.groups()[0]


# 32. Count characters in your string
# Rank: 6
# URL: https://www.codewars.com/kata/52efefcbcdf57161d4000091
# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.
def count(s):
    result = {}
    for ch in s:
        if ch not in result:
            result[ch] = 1
        else:
            result[ch] += 1
    return result


# 33. Break camelCase
# Rank: 6
# URL: https://www.codewars.com/kata/5208f99aee097e6552000148
# Complete the solution so that the function will break up camel casing, using a space between words
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
def my_solution(s):
    return "".join([" " + ch if ch.isupper() else ch for ch in s])


# 34. Array.diff
# Rank: 6
# URL: https://www.codewars.com/kata/523f5d21c841566fde000009
# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]
def array_diff(a, b):
    return [x for x in a if x not in b]


# 35. Find the unique number
# Rank: 6
# URL: https://www.codewars.com/kata/585d7d5adb20cf33cb000235
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.
from collections import Counter  # noqa: F811,E402


def find_uniq(arr):
    mydict = Counter(arr)
    return next(k for k in mydict.keys() if mydict[k] == 1)


# 36. Bouncing Balls
# Rank: 6
# URL: https://www.codewars.com/kata/5544c7a5cb454edb3c000047
# A child is playing with a ball on the nth floor of a tall building.
# The height of this floor, h, is known.
# He drops the ball out of the window.
# The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
# His mother looks out of a window 1.5 meters from the ground.
# How many times will the mother see the ball pass in front of her window
# (including when it's falling and bouncing?
# Three conditions must be met for a valid experiment:
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.
# If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
# Note:
# The ball can only be seen if the height of the rebounding ball is strictly greater
# than the window parameter.
# Examples:
# - h = 3, bounce = 0.66, window = 1.5, result is 3
# - h = 3, bounce = 1, window = 1.5, result is -1 (Condition 2) not fulfilled).
def bouncing_ball(h, bounce, window):
    c = 0
    if h > 0 and 0 < bounce < 1 and window < h:
        while h > window:
            c += 1
            h = h * bounce
            if h > window:
                c += 1
        return c
    return -1


# 37. Who likes it?
# Rank: 6
# URL: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.
def likes(names):
    if len(names) == 1:
        return f"{names[0]} likes this"
    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    if len(names) > 3:
        return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
    return "no one likes this"


# 38. Highest Scoring Word
# Rank: 6
# URL: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet:
# a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.
import string  # noqa: F811,E402


def high(x):
    result = {"word": "", "score": 0}
    for w in x.split():
        s = 0
        for ch in w:
            s += string.ascii_lowercase.index(ch) + 1
        if s > result["score"]:
            result["word"] = w
            result["score"] = s
    return result["word"]


# 39. Simple Encryption #1 - Alternating Split
# Rank: 6
# URL: https://www.codewars.com/kata/57814d79a56c88e3e0000786
# Implement a pseudo-encryption algorithm which given a string S and an integer N
# concatenates all the odd-indexed characters of S with all the even-indexed characters of S,
# this process should be repeated N times.
# Examples:
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"
# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function
# which reverses the process.
# If the string S is an empty value or the integer N is not positive,
# return the first argument without changes.
def decrypt(s, n):
    i = 0
    while i < n:
        odd = s[:len(s) // 2]
        even = s[len(s) // 2:]
        result = [""] * len(s)
        e_idx = 0
        o_idx = 1
        for e in even:
            result[e_idx] = e
            e_idx += 2
        for o in odd:
            result[o_idx] = o
            o_idx += 2
        s = "".join(result)
        i += 1
    return s


def encrypt(s, n):
    i = 0
    while i < n:
        odd = s[::2]
        even = s[1::2]
        s = "".join((even, odd))
        i += 1
    return s


# 40. String incrementer
# Rank: 5
# URL: https://www.codewars.com/kata/54a91a4883a7de5d7800009c
# Description:
# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100
# Attention: If the number has leading zeros the amount of digits should be considered.
import re  # noqa: F811,E402


def increment_string(strng):
    match = re.match(r'^(.*?)(\d*)$', strng)
    if not match:
        return "1"
    if match.group(2):
        n = match.group(2)
    else:
        n = "0"
    ln = len(n)
    n = int(n) + 1
    n = str(n).zfill(ln)
    return f"{match.group(1)}{n}"
