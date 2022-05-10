"""
Simple wrapper to control the output to the terminal
"""


from io import BytesIO
from io import TextIOWrapper
import sys


def print_wrapper(func):
    """Test Wrapper

    :param func: wrapped function
    :return: tuple, were [0] - console output text, [1] - result of function
    """
    def wrapper(*args, **kwargs):
        old_stdout = sys.stdout
        sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)
        func_result = func(*args, **kwargs)
        sys.stdout.seek(0)
        result = sys.stdout.read()
        sys.stdout.close()
        sys.stdout = old_stdout
        return result, func_result

    return wrapper
