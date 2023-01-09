
#!/usr/bin/python3
"""
is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True/False
    Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
