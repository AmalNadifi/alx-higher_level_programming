#!/usr/bin/python3
for number in range(0, 9):
    for number2 in range(number + 1, 10):
        print("{}{}".format(number, number2), end = '\n' if number == 89 else ", ")
