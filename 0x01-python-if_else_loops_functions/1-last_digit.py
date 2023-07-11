#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0 :
    test = number % 10
else:
    test = -1 * (number % 10)
if test > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, test), end = " ")
elif test == 0:
    print("Last digit of {} is {} and is 0".format(number, test), end = " ")
else if test < 6 && test != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, test), end = " ")
