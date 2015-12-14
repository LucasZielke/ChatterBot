import sys


def input_function(user_input = None):
    """
    Normalize reading input between python 2 and 3.
    'raw_input' is just 'input' in python3
    """
    if user_input = None:
        if sys.version_info[0] < 3:
            user_input = str(raw_input())
        else:
            user_input = input()
    return user_input
