#!/usr/bin/python3
def roman_to_int(roman_string):
    # First : check if the input is a valid str or an empty str
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    # Define the Roman numerals dictionary with corresponding decimal values
    R_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    # res variable used for resultant value of the roman numeral conversion
    res = 0
    # Loop through the chars of the Roman numeral str
    for i in range(len(roman_string)):
        # Check if the current character is of a substractive notation e.g IV
        if i > 0 and R_dict[roman_string[i]] > R_dict[roman_string[i - 1]]:
            res += R_dict[roman_string[i]] - 2 * R_dict[roman_string[i - 1]]
        else:
            res += R_dict[roman_string[i]]
    return res
