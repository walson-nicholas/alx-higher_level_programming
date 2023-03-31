#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a JSON file-writing function."""
=======
""" Module
"""


>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
import json


def save_to_json_file(my_obj, filename):
<<<<<<< HEAD
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
=======
    """writes an Object"""
    with open(filename, 'w', encoding='utf-8') as f:
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        json.dump(my_obj, f)
