#!/usr/bin/python3
"""
This module contains a function that indents text.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The string to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters that trigger a double newline
    separators = [".", "?", ":"]

    # We use a flag to skip leading spaces after a separator
    skip_space = True

    for char in text:
        if skip_space and char == " ":
            continue

        print(char, end="")
        skip_space = False

        if char in separators:
            print("\n")
            skip_space = True
