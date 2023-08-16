#!/usr/bin/python3
""" Definition function writing text to a file """


def write_file(filename="", text=""):
    """ This function writes a string to a text file (UTF8)

    Args:
        filename (str): the name of the file
        text (str): the text to write to the file
    Returns:
        Number of characters written

    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
