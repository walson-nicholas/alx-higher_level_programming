#!/usr/bin/python3
def common_elements(set_1, set_2):
<<<<<<< HEAD
    return (set_1 & set_2)
=======
    comm = []
    for x in set_1:
        if x in set_2:
            comm.append(x)
    return comm
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
