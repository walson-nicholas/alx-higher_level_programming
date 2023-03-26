#!/usr/bin/python3
def multiply_by_2(a_dictionary):
<<<<<<< HEAD
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        new_dir[i] *= 2

    return (new_dir)
=======
    new = a_dictionary.copy()
    for val in new.keys():
        new[val] *= 2
    return new
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
