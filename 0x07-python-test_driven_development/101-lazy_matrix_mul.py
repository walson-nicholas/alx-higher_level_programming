<<<<<<< HEAD
#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
=======
#!/usr/bin/python3.5
"""

Module composed by a function that multiplies 2 matrices

"""
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
<<<<<<< HEAD
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
=======
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication


>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
    """

    return (np.matmul(m_a, m_b))
