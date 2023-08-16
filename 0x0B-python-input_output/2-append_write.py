#!/usr/bin/python3
""" Definition function appending text at the end of a text file """


def append_write(filename="", text=""):
    """ This function appends a string at the end of a text file (UTF8)

    Args:
        filename (str): the name of the file
        text (str): the text to write to the file
    Returns:
        Number of characters added

    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
