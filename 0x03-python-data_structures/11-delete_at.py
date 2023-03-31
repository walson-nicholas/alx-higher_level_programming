#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
<<<<<<< HEAD
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
=======
    if idx >= 0 and idx < len(my_list):
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        del my_list[idx]
    return my_list
