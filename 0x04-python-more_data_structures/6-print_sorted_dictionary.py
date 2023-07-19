#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort thedictionary keys in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())
    # Loop through the sorted keys then print their values
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
