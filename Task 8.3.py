"""In this kata, your job is to return the two distinct highest values in a list.
If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest."""


def two_highest(arg1):
    unique_elements = set(arg1)
    if len(unique_elements) == 0:
        return []
    elif len(unique_elements) == 1:
        return [max(unique_elements)]
    else:
        max_number1 = max(unique_elements)
        unique_elements.remove(max_number1)
        max_number2 = max(unique_elements)
        return [max_number1, max_number2]
