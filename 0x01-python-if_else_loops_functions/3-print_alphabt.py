#!/usr/bin/python3
<<<<<<< HEAD
for char in range(26):
    if char != 4 and char != 16:
        print("{:s}".format(chr(char + ord("a"))), end="")
=======
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
