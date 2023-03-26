#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
<<<<<<< HEAD
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
=======
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
