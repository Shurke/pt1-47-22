"""Create a function that takes a string and an integer (n).
The function should return a string that repeats the input string n number of times.
If anything other than a string is passed in you should return "Not a string\""""


def repeat_it(string, n):
    if isinstance(string, str):
        return string * n
    else:
        return "Not a string"
