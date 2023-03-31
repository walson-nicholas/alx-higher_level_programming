#!/usr/bin/python3
<<<<<<< HEAD
def print_last_digit(number):
    if number >= 0:
        ld = number % 10
    else:
        ld = number % -10
        ld *= -1

    print("{:d}".format(ld), end='')
    return (ld)
=======

def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
