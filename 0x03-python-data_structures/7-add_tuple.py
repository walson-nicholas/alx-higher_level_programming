#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
<<<<<<< HEAD
    new_tuple = ()
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return new_tuple
=======
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    new_t = (a1 + b1, a2 + b2)
    return new_t
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
