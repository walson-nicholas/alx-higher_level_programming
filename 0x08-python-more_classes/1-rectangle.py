#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
=======
"""A module for working with rectangles.
"""


class Rectangle:
    """Represents a 2D Polygon with 4 perpendicular sides.
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        """
        self.width = width
        self.height = height

    @property
    def width(self):
<<<<<<< HEAD
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
=======
        """Retrieves the width of this Rectangle.
        Returns:
            int: The width of this Rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height of this Rectangle.
        Returns:
            int: The height of this Rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Updates the width of this Rectangle.
        Args:
            value (int): The new width of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Updates the height of this Rectangle.
        Args:
            value (int): The new height of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
