#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    division = 0
    for a_tuple in my_list:
        average = average + a_tuple[0] * a_tuple[1]
        division = division + a_tuple[1]
    return average / division
