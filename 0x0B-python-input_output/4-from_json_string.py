#!/usr/bin/python3
<<<<<<< HEAD
# 6-from_json_string.py
"""Defines a JSON-to-object function."""
=======
"""
Contains the "from_json_string" function
"""


>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
import json


def from_json_string(my_str):
<<<<<<< HEAD
    """Return the Python object representation of a JSON string."""
=======
    """ Function
    Args:
        my_str: JSON
    Raises:
        Exception: decode
    """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
    return json.loads(my_str)
