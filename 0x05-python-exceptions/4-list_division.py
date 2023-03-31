#!/usr/bin/python3
<<<<<<< HEAD

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
=======
def list_division(my_list_1, my_list_2, list_length):
    my_list_res = []
    for i in range(list_length):
        res = 0
        try:
            a, b = (my_list_1[i], my_list_2[i])
            res = a / b
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            my_list_res.append(res)
    return my_list_res
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
