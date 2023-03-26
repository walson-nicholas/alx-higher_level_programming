#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a Rectangle subclass Square."""
=======
"""
class BaseGeometry and subclass Rectangle
"""


>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
<<<<<<< HEAD
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
=======
    """A rep of a square"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
