#!/usr/bin/python3
<<<<<<< HEAD

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
=======
def safe_print_list(my_list=[], x=0):
    num = 0
    for item in range(x):
        try:
            print(my_list[item], end='')
            num += 1
        except Exception:
            break
    print('')
    return num
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
