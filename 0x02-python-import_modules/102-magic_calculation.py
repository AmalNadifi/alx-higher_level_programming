#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import sub, add
    if a < b:
        c = add(a, b)
        for itr in range(4, 6):
            c = add(c, itr)
        return c
    else:
        return (sub(a, b))
