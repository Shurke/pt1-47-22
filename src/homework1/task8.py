""" Make a program that filters a list of strings and returns a list with only your friends name in
it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
"""

def friend(x):
    return [i for i in x if len(i) == 4]
    print(i)



'''Implement a function that adds two numbers together and returns their sum in binary. The 
conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
'''


def add_binary(a,b):
    c = a + b
    return bin(c)[2::1]


'''This code does not execute properly. Try to figure out why.
'''

def multiply(a, b):
    return a * b



'''Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: 
(Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
'''

def row_sum_odd_numbers(n):
    return n*n*n


'''Write a function that takes an integer as input, and returns the number of bits that are equal 
to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this 
case
'''

def countBits(n):
    return bin(n).count("1")
