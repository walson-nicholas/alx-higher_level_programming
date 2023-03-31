#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
lastDigit = 0

if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = (-number % 10) * -1

message = f"Last digit of {number} is {lastDigit}"

if lastDigit == 0:
    print(f"{message} and is 0")
elif lastDigit > 5 and lastDigit % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
=======
digit = abs(number) % 10
if number < 0:
    digit = -digit
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
