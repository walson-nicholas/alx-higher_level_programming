#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
=======
    new = matrix.copy()
    for i in range(len(matrix)):
        new[i] = list(map(lambda x: x**2, matrix[i]))
    return new
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
