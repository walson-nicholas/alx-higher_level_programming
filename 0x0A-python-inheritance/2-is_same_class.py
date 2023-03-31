#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
=======
"""
module is_same_class
"""


def is_same_class(obj, a_class):
    """ Function that returns True/False
    Args:
        obj: object
        a_class: class type
    Returns:
        True if type of obj is a_class
        False, otherwise
    """

    return type(obj) is a_class
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
