import sys


def input_function(prompt = None):
    """
    Normalize reading input between python 2 and 3.
    'raw_input' is just 'input' in python3
    """

    if sys.version_info[0] < 3:
        user_input = str(raw_input(prompt))
    else:
        user_input = input(prompt)
    return user_input
