#!/usr/bin/python3
def max_integer(my_list=[]):
<<<<<<< HEAD
    if len(my_list) == 0:
        return "None"
    else:
        max = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
=======
    if len(my_list) < 1 or my_list is None:
        return None
    big = my_list[0]
    for int in my_list:
        if int > big:
            big = int
    return big
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
