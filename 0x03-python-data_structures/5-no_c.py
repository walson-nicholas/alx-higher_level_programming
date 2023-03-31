#!/usr/bin/python3
def no_c(my_string):
<<<<<<< HEAD
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string
=======
    new_str = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return new_str
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
