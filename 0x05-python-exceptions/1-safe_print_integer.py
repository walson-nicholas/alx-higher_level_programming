#!/usr/bin/python3
<<<<<<< HEAD

def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
        value (int): The integer to print.
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
=======
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
