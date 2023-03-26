#!/usr/bin/python3
<<<<<<< HEAD
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
=======
"""
inherits_from function
"""


def inherits_from(obj, a_class):
    """ Function that returns True/False
    Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
