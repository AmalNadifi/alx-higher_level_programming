#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Creating empty set to store the unique integers
    unique_integers = set()
    # Looping through the list elements
    for x in my_list:
        # Adding the int to the set
        unique_integers.add(x)
    # Sum up uniqueintegers then return the final result
    return sum(unique_integers)
