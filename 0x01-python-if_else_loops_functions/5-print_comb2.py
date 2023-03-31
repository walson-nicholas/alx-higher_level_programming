#!/usr/bin/python3
<<<<<<< HEAD
for i in range(100):
    if i == 99:
        print(i)
    else:
        print("{}".format('0' + str(i) if i < 10 else i), end=", ")
=======
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
