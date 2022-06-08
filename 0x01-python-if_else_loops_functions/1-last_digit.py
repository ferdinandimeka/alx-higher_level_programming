#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if last == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))
elif number < 0:
    numb = number * -1
    last = numb % 10
    print("Last digit of -{:d} is -{:d} and "
          "is less than 6 and not 0".format(numb, last))
elif number > 0:
    if last < 6:
        print("Last digit of {:d} is {:d} and "
              "is less than 6 and not 0".format(number, last))
    else:
        print("Last digit of {:d} is {:d} and "
              "is greater than 5".format(number, last))
