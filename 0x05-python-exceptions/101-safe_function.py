#!/usr/bin/python3
<<<<<<< HEAD
from __future__ import print_function
=======
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
import sys


def safe_function(fct, *args):
    try:
<<<<<<< HEAD
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
=======
        return fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: ")
        sys.stderr.write(ex.args[0])
        sys.stderr.write("\n")
        return None
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
