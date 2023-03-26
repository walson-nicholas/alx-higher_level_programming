#!/usr/bin/python3
def multiple_returns(sentence):
<<<<<<< HEAD
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple
=======
    t = (len(sentence), sentence[0] if len(sentence) > 0 else None)
    return t
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
