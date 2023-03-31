#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

<<<<<<< HEAD
    num = 0
    den = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)
=======
    x = 0
    y = 0

    for z in my_list:
        x += z[0] * z[1]
        y += z[1]

    return (x / y)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
