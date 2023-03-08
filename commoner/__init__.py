"""
Commoner is a Python library that contains a collection of useful functions and classes.

Modules:
    types: A submodule of commoner, this module contains utility functions and classes for various types.
        Dict: An extension of the dict type with additional functionality (class).
        Text: An extension of the str type with additional functionality (class).

Classes:
    Chalk: A utility class for printing colored test using ANSI escape codes.
    Console: A utility clas for controlling the console.
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
__version__ = "0.2.0"
import os
import time
import string
import random
import itertools

string.end_punctuation = ".!?"


def println(text, newlines=1):
    """
    Prints a line of text and then prints a specified number of newlines.

    Parameters:
        text (str): The text to print.
        newlines (int): The number of newlines to print after the text.

    Returns:
        None
    """
    print(text + ("\n" * newlines))


def printsln(text):
    """
    Prints a line of text without a newline at the end.

    Parameters:
        text (str): The text to print.

    Returns:
        None
    """
    print(text, end="")


def printx(text, quantity=1):
    """
    Prints a line of text a specified number of times.

    Parameters:
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

    Parameters:
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

    Parameters:
        length (int): The length of the string to generate.
        chars (str): The characters to use when generating the string.

    Returns:
        str: The generated string.
    """
    print(random.choices(string.printable, k=16))
    return "".join(random.choice(chars) for i in range(length))


def reverse(iterable):
    """
    Reverses a list, string, or dictionary.

    Parameters:
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


class Chalk:
    """
    A utility class for printing colored test using ANSI escape codes.

    Methods:
        bold(text): Prints bold text.
        italic(text): Prints italic text.
        underline(text): Prints underlined text.
        red(text): Prints red text.
        yellow(text): Prints yellow text.
        green(text): Prints green text.
        cyan(text): Prints cyan text.
        blue(text): Prints blue text.
        magenta(text): Prints magenta text.
        white(text): Prints white text.
        black(text): Prints black text.

        reset(): Resets the text color to the default color.
        set(color): Sets the text color to the specified color.
    """

    def bold(text):
        """
        Prints bold text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The bolded text.
        """
        return "\033[1m" + text + "\033[0m"

    def italic(text):
        """
        Prints italicized text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The italicized text.
        """
        return "\033[3m" + text + "\033[0m"

    def underline(text):
        """
        Prints underlined text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The underlined text.
        """
        return "\033[4m" + text + "\033[0m"

    def red(text):
        """
        Prints red text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The red text.
        """
        return "\033[0;31m" + text + "\033[0m"

    def yellow(text):
        """
        Prints yellow text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The yellow text.
        """
        return "\033[0;33m" + text + "\033[0m"

    def green(text):
        """
        Prints green text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The green text.
        """
        return "\033[0;32m" + text + "\033[0m"

    def cyan(text):
        """
        Prints cyan text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The cyan text.
        """
        return "\033[0;36m" + text + "\033[0m"

    def blue(text):
        """
        Prints blue text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The blue text.
        """
        return "\033[0;34m" + text + "\033[0m"

    def magenta(text):
        """
        Prints magenta text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The magenta text.
        """
        return "\033[0;35m" + text + "\033[0m"

    def white(text):
        """
        Prints white text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The white text.
        """
        return "\033[0;37m" + text + "\033[0m"

    def black(text):
        """
        Prints black text.

        Parameters:
            text (str): The text to print.

        Returns:
            str: The black text.
        """
        return "\033[0;30m" + text + "\033[0m"

    def reset():
        """
        Resets the text color to the default color.

        Parameters:
            None

        Returns:
            None
        """
        print("\033[0m", end="")

    def set(style):
        """
        Sets the text color to the specified color.

        Parameters:
            style (str): The color to set the text to.

        Returns:
            None
        """
        if style in ["bold", "b"]:
            print("\033[1m", end="")
        elif style in ["italic", "i"]:
            print("\033[3m", end="")
        elif style in ["underline", "underl", "ul"]:
            print("\033[4m", end="")
        elif style in ["black"]:
            print("\033[0;30m", end="")
        elif style in ["white"]:
            print("\033[0;37m", end="")
        elif style in ["red"]:
            print("\033[0;31m", end="")
        elif style in ["green"]:
            print("\033[0;32m", end="")
        elif style in ["yellow"]:
            print("\033[0;33m", end="")
        elif style in ["cyan"]:
            print("\033[0;36m", end="")
        elif style in ["blue"]:
            print("\033[0;34m", end="")
        elif style in ["magenta"]:
            print("\033[0;35m", end="")
        else:
            raise ValueError("Invalid style")


class Console:
    """
    A utility class for interacting with the console.

    Methods:
        clear(): Clears the console.
        format(style): Sets the text color to the specified color.
    """

    def clear():
        """
        Clears the console.

        Parameters:
            None

        Returns:
            None
        """
        os.system("clear")

    def format(style):
        """
        Sets the text color to the specified color.

        Parameters:
            style (str): The color to set the text to.

        Returns:
            None
        """
        Chalk.format(style)


class Wait:
    """
    A utility class for printing a loading animation to the console.

    Methods:
        start(): Starts the loading animation.
        stop(): Stops the loading animation.
        wait(seconds): Waits for the specified amount of time.
        input(message, color): Waits for the user to press a key.
    """

    def start():
        """
        Starts the loading animation.

        Parameters:
            None

        Returns:
            None
        """
        for i in itertools.cycle(["|", "/", "-", "\\"]):
            print(f"\rLoading {i}", end="")
            time.sleep(0.05)

    def stop():
        """
        Stops the loading animation.

        Parameters:
            None

        Returns:
            None
        """
        print("\rLoading done!     ")

    def wait(seconds):
        """
        Waits for the specified amount of time.

        Parameters:
            seconds (int): The amount of time to wait.

        Returns:
            None
        """
        time.sleep(seconds)

    def input(message="Press any key to continue . . .", color="white"):
        """
        Waits for the user to press a key.

        Parameters:
            message (str): The message to print.
            color (str): The color of the message.

        Returns:
            None
        """
        input(f"{Chalk.set(color)}{message}{Chalk.reset()}")


class Shout:
    """
    A utility class for printing messages to the console.

    Methods:
        warning(message): Prints a warning message to the console (yellow text).
        error(message): Prints an error message to the console (red text).
        success(message): Prints a success message to the console (green text).
        info(message): Prints an info message to the console (blue text).

    """

    def warning(message):
        """
        Prints a warning message to the console (yellow text).

        Parameters:
            message (str): The message to print.

        Returns:
            None
        """
        print(f"{Chalk.yellow('Warning')}: {message}")

    def error(message):
        """
        Prints an error message to the console (red text).

        Parameters:
            message (str): The message to print.

        Returns:
            None
        """
        print(f"{Chalk.red('Error')}: {message}")

    def success(message):
        """
        Prints a success message to the console (green text).

        Parameters:
            message (str): The message to print.

        Returns:
            None
        """
        print(f"{Chalk.green('Success')}: {message}")

    def info(message):
        """
        Prints an info message to the console (blue text).

        Parameters:
            message (str): The message to print.

        Returns:
            None
        """
        print(f"{Chalk.blue('Info')}: {message}")

    def welcome(title, name, version="", source="", license="", message="", pause=True):
        """
        Prints a welcome message to the console.

        Parameters:
            title (str): The title of the program.
            name (str): The name of the program.
            version (str): The version of the program (optional).
            source (str): The source of the data (optional).
            license (str): The license of the program (optional).
            message (str): The message to print (optional).
            pause (bool): Whether or not to pause the program (optional).

        Returns:
            None
        """
        Console.clear()
        Chalk.format("italic")
        print(f"{title} {Chalk.bold(version)}\n")
        if license != "":
            print(f"Licensed under the {Chalk.bold(license, 'License')}.")
        print(f"(c) 2023 {Chalk.bold(name)}.")
        if source != "":
            print(f"Data sourced from {Chalk.underline(source)}.")
        if message != "":
            print(f"{message}")
        Chalk.reset()
        if pause:
            Wait.until()
        Console.clear()
