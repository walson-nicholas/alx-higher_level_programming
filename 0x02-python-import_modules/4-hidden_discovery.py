#!/usr/bin/python3
<<<<<<< HEAD

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
=======
if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if name.startswith('__'):
            continue
        print("{:s}".format(name))
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
