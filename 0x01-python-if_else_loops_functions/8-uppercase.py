#!/usr/bin/python3
def uppercase(str):
<<<<<<< HEAD
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            letter = 32
        else:
            letter = 0
        print("{:c}".format(ord(str[i]) - letter), end='')
=======
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
    print()
