# assuming that fibonacci row starts with 1 (vs. 0)
# fibonacci 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
n = int(input())
f1 = 1
f2 = 1
if n == 1:
    print("Fibonacci 1 element = " + str(f1))
elif n == 2:
    print("Fibonacci 2 element = " + str(f2))
else:
    n_element = 0
    for i in range(n-2):
        n_element = f1 + f2
        f1 = f2
        f2 = n_element
    print("Fibonacci " + str(n) + " element = " + str(n_element))