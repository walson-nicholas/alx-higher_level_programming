#!/usr/bin/python3
<<<<<<< HEAD
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{num} ", end="")
=======

"""Print the numbers from 1 to 100 separated by a space.
  For multiples of three, print Fizz instead of the number
  For multiples of five, print Buzz instead of the number.
  For multiples of three and five, print FizzBuzz instead of the number.
  """


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
