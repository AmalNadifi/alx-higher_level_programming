#!/usr/bin/python3
def no_c(my_string):
    res = ''
    for x in my_string:
        if x != 'C' and x != 'c':
            res = res + x
    return (res)
