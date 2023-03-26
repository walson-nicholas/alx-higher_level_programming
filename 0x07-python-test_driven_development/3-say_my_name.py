#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.
    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
=======
"""

This module is composed by a function prints a message

"""


def say_my_name(first_name, last_name=""):
    """ Function that prints "My name is <first name> <last name>"

    Args:
        first_name: first name
        last_name: last name

    Returns:
        No return

    Raises:
        TypeError: If first_name or last_name is not a string


    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
    print("My name is {} {}".format(first_name, last_name))
