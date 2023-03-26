#!/usr/bin/python3
def element_at(my_list, idx):
<<<<<<< HEAD
    if idx < 0 or idx > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idx]
=======
    if idx > len(my_list) - 1 or idx < 0:
        return None
    return my_list[idx]
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
