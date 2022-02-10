"""
Task1 (elementary)
Given an integer, n perform the following conditional actions:
If n is odd, print 'Weird'
If n is even and in the inclusive range of 2 to 5, print 'Not Weird'
If n is even and in the inclusive range of 6 to 20, print 'Weird'
If n is even and greater than 20, print 'Not Weird'
"""

n = int(input())

if n % 2 != 0:
    print('Weird')
elif n % 2 == 0 and 2 <= n <= 5:
    print('Not Weird')
elif n % 2 == 0 and 6 <= n <= 20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')

"""
Task2 (elementary)
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers(first - second).
The third line contains the product of the two numbers.
"""

a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

"""
Task3 (elementary)
The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines.
The first line should contain the result of integer division, a // b.
The second line should contain the result of float division, a / b.
No rounding or formatting is necessary.
"""

a = int(input())
b = int(input())

print(a // b)
print(a / b)

"""
Task4
You are given a positive integer N. Print a numerical triangle of height N - 1 like the one below:
1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines.
The first line (the for statement) is already written for you.
You have to complete the print statement.
"""

for i in range(1, int(input())):
    print(int(i * 10**i / 9))

"""
Task5
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.
For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.
"""

for i in range(1, int(input())+1):
    print(((10**i - 1)//9)**2)