#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a JSON file-reading function."""
=======
"""
add "load_from_json_file"
"""


>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
import json


def load_from_json_file(filename):
<<<<<<< HEAD
    """Create a Python object from a JSON file."""
    with open(filename) as f:
=======
    """creates an Object" """
    with open(filename, 'r', encoding="utf-8") as f:
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        return json.load(f)
