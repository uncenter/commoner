"""
Commoner is a Python library that contains a collection of useful functions and classes.

Modules:
    types: A submodule of commoner, this module contains utility functions and classes for various types.
        Dict: An extension of the dict type with additional functionality (class).
        Text: An extension of the str type with additional functionality (class).

Classes:
    Chalk: A utility class for printing colored test using ANSI escape codes.
    Console: A utility class for controlling the console.
    Wait: A utility class for waiting-related functions.
    Shout: A utility class for message-related functions.

Functions:
    println(text, newlines=1): Prints a line of text and then prints a specified number of newlines.
    printsln(text): Prints a line of text without a newline at the end.
    printx(text, quantity=1): Prints a line of text a specified number of times.
    typewriter(text, speed=0.2): Prints a line of text with a typewriter effect (one character at a time).
    random_string(length=16, chars=string.printable): Generates a random string of a specified length.
    reverse(iterable): Reverses a list, string, or dictionary.
"""
__version__ = "0.3.0"
import time
import string
import random
import json
import csv

from classes import Chalk, Console, Wait, Shout

string.end_punctuation = ".!?"


def println(text, newlines=1):
    """
    Prints a line of text and then prints a specified number of newlines.

    Args:
        text (str): The text to print.
        newlines (int): The number of newlines to print after the text.

    Returns:
        None
    """
    print(text + ("\n" * newlines))


def printsln(text):
    """
    Prints a line of text without a newline at the end.

    Args:
        text (str): The text to print.

    Returns:
        None
    """
    print(text, end="")


def printx(text, quantity=1):
    """
    Prints a line of text a specified number of times.

    Args:
        text (str): The text to print.
        quantity (int): The number of times to print the text.

    Returns:
        None
    """
    for i in range(0, quantity):
        print(text)


def typewriter(text, speed=0.2):
    """
    Prints a line of text with a typewriter effect (one character at a time).

    Args:
        text (str): The text to print.
        speed (float): The time to wait between printing each character (in seconds).

    Returns:
        None
    """
    for char in text:
        time.sleep(speed)
        print(char, end="", flush=True)
    print()


def random_string(length=16, chars=string.printable):
    """
    Generates a random string of a specified length.

    Args:
        length (int): The length of the string to generate.
        chars (str): The characters to use when generating the string.

    Returns:
        str: The generated string.
    """
    if type(chars) == list or type(chars) == set or type(chars) == tuple:
        chars = "".join(str(char) for char in chars)
    elif type(chars) == dict:
        Shout.error("Cannot generate a random string from a dictionary.")
        return None
    elif type(chars) == int or type(chars) == str:
        chars = str(chars)
    else:
        Shout.error("Invalid type for chars.")
        return None
    return "".join(random.choice(chars) for i in range(length))


def read_json(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        Shout.error(f"Issue reading file: {file}\nMake sure it exists.")
        return None


def copy_csv(source, destination, strip_empty=True):
    """
    Copy a csv file.

    Args:
        source (str): Path to the source file.
        destination (str): Path to the destination file.
        strip_empty (bool, optional): Whether to strip empty lines. Defaults to True.

    Raises:
        TypeError: If `source` or `destination` is not a string.

    Returns:
        None
    """
    if type(source) != str or type(destination) != str:
        raise TypeError(
            f"Invalid type for source or destination: {type(source)}, {type(destination)}"
        )
    try:
        with open(destination, "w") as f:
            if strip_empty:
                f.writelines(
                    [line for line in open(source, "r").readlines() if line.strip() != ""]
                )
            else:
                f.writelines([line for line in open(source, "r").readlines()])
    except FileNotFoundError:
        Shout.error(f"Issue reading file(s): {source}, {destination}\nMake sure they exist.")
        return None


def read_csv(file):
    """
    Read a csv file.

    Args:
        file (str): The csv file to read from.

    Raises:
        TypeError: If `file` is not a string.

    Returns:
        list: A list of rows as dictionaries.
    """
    if type(file) != str:
        raise TypeError(f"Invalid type for file: {type(file)}")
    try:
        with open(file, "r") as f:
            data = csv.DictReader(f)
            return [row for row in data]
    except FileNotFoundError:
        Shout.error(f"Issue reading file: {file}\nMake sure it exists.")
        return None


def write_csv(file, data, headers=None):
    """
    Write to a csv file.

    Args:
        file (str): The csv file to write to.
        data (list): The data to write (list of dictionaries).
        headers (list, optional): The headers for the csv file. Defaults to None.

    Raises:
        TypeError: If `file` or `data` is not a string or list.

    Returns:
        None
    """
    if type(file) != str or type(data) != list:
        raise TypeError(f"Invalid type for file or data: {type(file)}, {type(data)}")
    try:
        if headers:
            for header in headers:
                if type(header) != str:
                    raise TypeError(f"Invalid type for header: {type(header)}")
                if header.lower() == header:
                    Shout.warning(f"Header '{header}' is lowercase. Consider capitalizing it.")
        with open(file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
        Shout.error(f"Issue reading file: {file}\nMake sure it exists.")
        return None


def get_csv_row(key, value, file):
    """
    Get a row from a csv file.

    Args:
        key (str): The key or header of the column to search in.
        value (str): The value to search for.
        file (str): The csv file to read from.

    Returns:
        dict: The row as a dictionary.
    """
    if type(key) != str:
        raise TypeError(f"Invalid type for key: {type(key)}")
    if type(value) != str:
        raise TypeError(f"Invalid type for value: {type(value)}")
    try:
        with open(file, "r") as f:
            data = csv.DictReader(f)
            for row in data:
                if row[key] == value:
                    return row
            else:
                return None
    except (FileNotFoundError, KeyError):
        Shout.error(f"Issue reading file: {file}\nMake sure it exists and the key is correct.")
        return None


def get_csv_col(key, file):
    """
    Get a column from a csv file.

    Args:
        key (str): The column key or header.
        file (str): The csv file to read from.

    Returns:
        _type_: _description_
    """
    if type(key) != str:
        raise TypeError(f"Invalid type for key: {type(key)}")
    if type(file) != str:
        raise TypeError(f"Invalid type for file: {type(file)}")
    try:
        with open(file, "r") as f:
            data = csv.DictReader(f)
            return [row[key] for row in data]
    except (FileNotFoundError, KeyError):
        Shout.error(f"Issue reading file: {file}\nMake sure it exists and the key is correct.")
        return None


def reverse(iterable):
    """
    Reverses a list, string, or dictionary.

    Args:
        iterable (list, str, dict): The list, string, or dictionary to reverse.

    Returns:
        list, str, dict: The reversed list, string, or dictionary.
    """
    if type(iterable) == list or type(iterable) == str:
        return iterable[::-1]
    elif type(iterable) == dict:
        return dict(reversed(list(iterable.items())))
    else:
        return None


def replace_all(text, old, new):
    """
    Replace all instances of a string in a string.

    Args:
        text (str): The string to replace in.
        old (list, str): The string or list of strings to replace.
        new (str): The string to replace with.

    Raises:
        TypeError: If `old` is not a string or list.

    Returns:
        str: The string with all instances of `old` replaced with `new`.
    """
    if isinstance(old, list):
        for i in old:
            text = replace_all(text, i, new)
    elif isinstance(old, str):
        while old in text:
            text = text.replace(old, new)
    else:
        raise TypeError(f"Invalid type: {type(old)}")
    return text
