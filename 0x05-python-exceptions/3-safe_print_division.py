#!/usr/bin/python3
<<<<<<< HEAD

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
=======
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except Exception:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
