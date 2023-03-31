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
    """ Class that defines a Square from Rectangle class """
    def __init__(self, size):
        """ Method that initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns a string with the area """
        return super().area()

    def __str__(self):
        """ Special method that returns a printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
