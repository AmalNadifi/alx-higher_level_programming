#!/usr/bin/python3
""" Definition of the module to print a text with 2 new lines
after each of these characters: ., ? and : """


def text_indentation(text):
    """
    Printing the text with two lines after each '.', '?', and ':' characters
    Args:
        text (str): The text to process and print

    Raises:
        TypeError: If the text is not a string

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".:?":
        text = (delimiter + "\n\n").join(
                [sentence.strip(" ") for sentence in text.split(delimiter)])

    print(text)
