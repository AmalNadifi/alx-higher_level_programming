#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for itr in range(0, x):
        try:
            print("{:d}".format(my_list[itr]), end=" ")
            counter = counter + 1
        except (ValueError, TypeError):
            pass
    print()
    return(counter)
