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
"""
Contains the clas "Student"
"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes student"""
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
<<<<<<< HEAD
        """Get a dictionary representation of the Student."""
=======
        """returns a dictionary"""
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        return self.__dict__
