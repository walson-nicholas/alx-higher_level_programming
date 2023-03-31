#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.
    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
=======
"""

This module is composed by a function that prints a square with the character #

"""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square printed

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer number


    """

>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
<<<<<<< HEAD
        [print("#", end="") for j in range(size)]
        print("")
=======
        print("#" * size)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
