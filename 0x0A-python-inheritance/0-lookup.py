#!/usr/bin/python3
"""
Contains the lookup function
"""


def lookup(obj):
    """ Function that returns the list of
        an object
    Args:
        obj: Instance of the class
    Returns:
         attributes
    """

    return dir(obj)
