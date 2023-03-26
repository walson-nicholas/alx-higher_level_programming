<<<<<<< HEAD
#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
=======

#!/usr/bin/python3
"""
Contains the function append_wrtie
"""


def append_write(filename="", text=""):
    """ Function
    Args:
        filename: filename
        text: txt to write
    Raises
        Exception: open
    """
    with open(filename, 'a', encoding='utf=8') as f:
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        return f.write(text)
