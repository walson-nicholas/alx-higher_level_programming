#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
=======
"""
Contains the read_file function
"""


def read_file(filename=""):
    """reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        print(f.read(), end="")
