#!/usr/bin/python3
def complex_delete(a_dictionary, value):
<<<<<<< HEAD
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
=======
    li = list(a_dictionary.keys())

    for value_dic in li:
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
