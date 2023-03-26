#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
=======
""" Module
"""


class Student:
    """ Class """

    def __init__(self, first_name, last_name, age):
        """method to initialize """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
<<<<<<< HEAD
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
=======
        """ Method that returns directory """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list

        return obj

    def reload_from_json(self, json):
        """ Replaces all attributes instance """
        for atr in json:
            self.__dict__[atr] = json[atr]
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
