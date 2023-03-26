#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
=======
"""
Contains the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """ Function
    Args:
        filename: filename
        text: text
    Raises
        Exception: opened
    """
    with open(filename, 'w', encoding="utf-8") as f:
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        return f.write(text)
