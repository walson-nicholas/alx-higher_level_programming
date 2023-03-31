#!/usr/bin/python3
def search_replace(my_list, search, replace):
<<<<<<< HEAD
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
=======
    new = list(map(lambda x: replace if x == search else x, my_list))
    return new
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
