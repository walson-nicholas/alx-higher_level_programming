#!/usr/bin/python3
def magic_string():
<<<<<<< HEAD
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
=======
    magic_string.c, t = (magic_string.__dict__.get('c', 0) + 1, ', Holberton')
    return '{:s}{:s}'.format(t[2:], t * (magic_string.c - 1))
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
