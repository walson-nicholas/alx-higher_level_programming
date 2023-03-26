#!/usr/bin/python3
def new_in_list(my_list, idx, element):
<<<<<<< HEAD
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
=======
    new_list = my_list[:]
    if idx > len(new_list) - 1 or idx < 0:
        return new_list
    new_list[idx] = element
    return new_list
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
