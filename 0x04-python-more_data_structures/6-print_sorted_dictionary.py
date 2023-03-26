#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
<<<<<<< HEAD
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for i in list_ord:
=======
    ordli = list(a_dictionary.keys())
    ordli.sort()
    for i in ordli:
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        print("{}: {}".format(i, a_dictionary.get(i)))
