#!/usr/bin/python3
<<<<<<< HEAD
# Author - Nwabueze Franklin
=======
# Author - Gabriel Dan
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
