#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a class Rectangle that inherits from BaseGeometry."""
=======
"""
class BaseGeometry and subclass Rectangle
"""

>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
<<<<<<< HEAD
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
=======
    """ Class that defines a rectangle from BaseGeometry Class """

    def __init__(self, width, height):
        """ Initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method that returns the area of the instance"""
        return self.__width * self.__height

    def __str__(self):
        """ Special method that returns the printable string """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
