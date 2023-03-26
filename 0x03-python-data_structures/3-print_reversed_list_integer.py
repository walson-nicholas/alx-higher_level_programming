#!/usr/bin/python3
<<<<<<< HEAD
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
=======

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
    else:
        return (None)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
