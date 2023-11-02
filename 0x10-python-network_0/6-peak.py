#!/usr/bin/python3
""" The following module contains the function that
finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    This method Finds a peak element in an unsorted list of integers

    Args:
        list_of_integers (list): The list of integers

    Returns:
        int or None: The peak element found in the list,
                    or None if the list is empty.
    """

    # Checking if the list is empty
    if not list_of_integers or list_of_integers == []:
        return None
    # Initializing the left and right pointers
    left_ptr, right_ptr = 0, len(list_of_integers) - 1

    # Binary search to find the peak
    while left_ptr < right_ptr:
        mid = int((left_ptr + right_ptr) / 2)  # Calculating the middle index

        # Comparing the middle element with its right neighbor
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left_ptr = mid + 1  # Moving left pointer to mid + 1
        else:
            right_ptr = mid  # Moving right pointer to mid

    # Returning the peak element found
    return list_of_integers[left_ptr]
