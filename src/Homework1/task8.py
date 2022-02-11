from typing import List, Any

"""def is_even(num: int) -> bool:
    # your code here
    return False
if __name__ == '__main__':
    print("Example:")
    print(is_even(2))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")"""


def is_even(num: int) -> bool:
    # your code here
    return num % 2 == 0


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) is True
    assert is_even(5) is False
    assert is_even(0) is True
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""def between_markers(text: str, begin: str, end: str) -> str:
       # returns substring between two given markers
    # your code here
    return ''
if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')"""


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    a = text.find(begin)
    b = text.find(end)
    return text[a + 1:b]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')


""" def is_acceptable_password(password: str) -> bool:
    # your code here
    return True
if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!") """


def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password) > 6


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') is False
    assert is_acceptable_password('muchlonger') is True
    assert is_acceptable_password('ashort') is False
    print("Coding complete? Click 'Check' to earn cool rewards!")

""" from typing import List, Any
def all_the_same(elements: List[Any]) -> bool:
    if elements == []:
        return True
    y = elements.count(elements[0])
    if y == len(elements):
        return True
    return False
if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!") """


def all_the_same(elements: List[Any]) -> bool:
    if not elements:
        return True
    y = elements.count(elements[0])
    if y == len(elements):
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) is True
    assert all_the_same([1, 2, 1]) is False
    assert all_the_same(['a', 'a', 'a']) is True
    assert all_the_same([]) is True
    assert all_the_same([1]) is True
    print("Coding complete? Click 'Check' to earn cool rewards!")

""" def first_word(text: str) -> str:
    returns the first word in a given text.
    # your code here
    return text[0:2]
if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!") """


def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    text = text.split()
    return text[0]


if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")

""" def correct_sentence(text: str) -> str:
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    # your code here
    return text
if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))                                                

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    print("Coding complete? Click 'Check' to earn cool rewards!") """


def correct_sentence(text: str) -> str:
    """
    returns a corrected sentence which starts with a capital letter
    and ends with a dot.
    """
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text


if __name__ == "__main__":
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") is "Greetings, friends."
    assert correct_sentence("Greetings, friends") is "Greetings, friends."
    assert correct_sentence("Greetings, friends.") is "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") is "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
