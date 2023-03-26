#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
=======
"""A class with restrictions.
"""


class LockedClass:
    """The locked class"""

    __slots__ = "first_name"
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
