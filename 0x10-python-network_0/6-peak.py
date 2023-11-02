#!/usr/bin/python3
""" The following module contains the function that
finds a peak in a list of unsorted integers """
def find_peak(list_of_integers):
    # Checking if the list is empty
    if not list_of_integers:
        return None
    # Initializing the left and right pointers
    left_ptr, right_ptr = 0, len(list_of_integers) - 1

    # Binary search to find the peak
    while left_ptr < right_ptr:
        mid = (left_ptr + right_ptr) // 2  # Calculating the middle index

        # Comparing the middle element with its right neighbor
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1  # Moving left pointer to mid + 1
        else:
            right = mid  # Moving right pointer to mid

    # Returning the peak element found
    return list_of_integers[left]
