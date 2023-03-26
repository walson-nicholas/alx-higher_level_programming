#!/usr/bin/python3
<<<<<<< HEAD

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
=======
if __name__ == "__main__":
    from sys import argv
    i = 1
    if len(argv) < 2:
        print("0 arguments.")
    elif len(argv) < 3:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(argv) - 1))
    for arg in argv[1:]:
        print("{:d}: {:s}".format(i, arg))
        i += 1
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
