#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(num + 1, 10):
        print("{}{}".format(num, num2), end='\n' if num == 89 else ", ")
