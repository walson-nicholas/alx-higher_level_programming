#!/usr/bin/python3
<<<<<<< HEAD

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
=======
"""A module for working with squares.
"""


class Square:
    """Check for TypeError and ValueError
    """
    def __init__(self, size=0):
        """Initializes a Square with a given size.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
