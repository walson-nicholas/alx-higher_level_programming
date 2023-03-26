#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
=======
"""
class BaseGeometry
"""


class BaseGeometry:
    """public instance"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that recieves the value property
        Árgs:
            name: name of the object
            value: value of the property
        """

        if type(value) is not int:
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
