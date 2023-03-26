#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
<<<<<<< HEAD
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
=======
    for e in matrix:
        for i in e:
            print('{:d}'.format(i), end='')
            if i != e[-1]:
                print(' ', end='')
        print("")
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
