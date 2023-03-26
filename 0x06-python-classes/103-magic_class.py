#!/usr/bin/python3
<<<<<<< HEAD

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

=======
"""magic class definition"""
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
import math


class MagicClass:
<<<<<<< HEAD
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.
        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
=======
    """magicclass that makes same bytecode as in the task"""

    def __init__(self, radius=0):
        """Initialize class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """area function calculates some weird stuff"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """also this func calculate some weird stuff"""
        return (2 * math.pi) * self.__radius
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
