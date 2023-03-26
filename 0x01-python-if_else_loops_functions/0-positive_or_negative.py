#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
<<<<<<< HEAD
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
=======
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
