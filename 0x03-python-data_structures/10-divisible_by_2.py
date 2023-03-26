#!/usr/bin/python3
def divisible_by_2(my_list=[]):
<<<<<<< HEAD
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
=======
    new_list = [False] * len(my_list)
    for idx, num in enumerate(my_list):
        if num % 2 == 0:
            new_list[idx] = True
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
    return new_list
