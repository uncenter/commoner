__version__ = "0.1.0"
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


def sort_dict_keys(dict, reverse=False):
    """
    Sorts a dictionary by its keys.

    Parameters:
        dict (dict): The dictionary to sort.
        reverse (bool): Whether to sort the dictionary in reverse order.

    Returns:
        dict: The sorted dictionary.
    """
    return {
        k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=reverse)
    }


def sort_dict_values(dict, reverse=False):
    """
    Sorts a dictionary by its values.

    Parameters:
        dict (dict): The dictionary to sort.
        reverse (bool): Whether to sort the dictionary in reverse order.

    Returns:
        dict: The sorted dictionary.
    """
    return {
        k: v for k, v in sorted(dict.items(), key=lambda item: item[0], reverse=reverse)
    }


def swap_keys_values(dict):
    """
    Swaps the keys and values of a dictionary.

    Parameters:
        dict (dict): The dictionary to swap.

    Returns:
        dict: The swapped dictionary.
    """
    return {v: k for k, v in dict.items()}


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
        input(f"{Chalk.format(color)}{message}{Chalk.reset()}")

    class Progress:
        """
        A utility class for printing a progress bar to the console.

        Methods:
            progress(current, total, message): Prints a progress bar.
            timed_progress(seconds, message): Prints a progress bar that counts down from a specified amount of time.
        """

        def __init__(self, total, character="#", reverse=False):
            self.total = total
            self.current = 0
            self.character = character
            self.reverse = reverse

        def display(percent, character, message="Loading . . .", reverse=False):
            """
            Displays a progress bar.

            Parameters:
                current (int): The current progress.
                total (int): The total progress.
                message (str): The message to print.

            Returns:
                None
            """
            bar = character * int(percent * 20)
            spaces = " " * (20 - len(bar))
            if reverse:
                print(f"\r{message} [{bar}{spaces}] {100 - percent * 100:.2f}%", end="")
            else:
                print(f"\r{message} [{bar}{spaces}] {percent * 100:.2f}%", end="")

        def start(self, message="Loading . . ."):
            """
            Prints a progress bar.

            Parameters:
                message (str): The message to print.

            Returns:
                None
            """
            Wait.Progress.display(0, self.character, message, self.reverse)

        def update(self, current, message="Loading . . ."):
            """
            Updates the progress bar.

            Parameters:
                current (int): The current progress.
                message (str): The message to print.

            Returns:
                None
            """
            percent = current / self.total
            Wait.Progress.display(percent, self.character, message, self.reverse)

        def finish(self, message="Finished!"):
            print("\r", end="")
            Wait.Progress.display(1, self.character, message)

        def timed(seconds, character="#", message="Loading . . .", reverse=False):
            """
            Displays a progress bar that counts down from a specified amount of time.

            Parameters:
                seconds (int): The amount of time to count down from.
                character (str): The character to use for the progress bar.
                message (str): The message to print.

            Returns:
                None
            """
            bar = Wait.Progress(1, character, reverse)
            bar.start(message)
            for i in range(seconds):
                bar.update(i / seconds, message)
                time.sleep(1)
            bar.finish()


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


class Text:
    """
    An extension of the str type with additional functionality.

    Parameters:
        text (str): The text to use.

    Returns:
        Text: The text object.

    Methods:
        replace(old, new): Replaces characters in the text.
        reverse(): Reverses the text.
        count(char): Counts the number of times a character (or all characters) appear(s) in the text.
        to_snake(): Converts the text to snake case.
        to_camel(): Converts the text to camel case.
        to_pascal(): Converts the text to pascal case.
        to_kebab(): Converts the text to kebab case.
        to_actual_title(): Converts the text to an actual title (e.g. "this is a title" -> "This Is a Title").
        to_initials(case_sensitive): Converts the text to initials (e.g. "this is a title" -> "T.I.a.T") (case sensitive by default).
    """

    IGNORE_WORDS = [
        "a",
        "an",
        "the",
        "and",
        "but",
        "or",
        "for",
        "nor",
        "on",
        "at",
        "to",
        "from",
        "by",
        "of",
        "off",
        "in",
        "out",
        "over",
        "into",
        "with",
    ]

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text

    def __eq__(self, other):
        return self.text == other

    def __ne__(self, other):
        return self.text != other

    def __len__(self):
        return len(self.text)

    def __add__(self, other):
        return self.text + other

    def __radd__(self, other):
        return other + self.text

    def __mul__(self, other):
        return self.text * other

    def __rmul__(self, other):
        return other * self.text

    def __mod__(self, other):
        return self.text % other

    def __rmod__(self, other):
        return other % self.text

    def __floordiv__(self, other):
        return self.text // other

    def __rfloordiv__(self, other):
        return other // self.text

    def __truediv__(self, other):
        raise ValueError("Text objects cannot be divided by non-numbers")

    def __rtruediv__(self, other):
        raise ValueError("Text objects cannot be divided by non-numbers")

    def __pow__(self, other):
        raise TypeError("Text objects cannot be raised to a power")

    def __rpow__(self, other):
        raise TypeError("Text objects cannot be raised to a power")

    def __lshift__(self, other):
        raise TypeError("Text objects cannot be shifted")

    def __rlshift__(self, other):
        raise TypeError("Text objects cannot be shifted")

    def __rshift__(self, other):
        raise TypeError("Text objects cannot be shifted")

    def __rrshift__(self, other):
        raise TypeError("Text objects cannot be shifted")

    def __neg__(self):
        raise TypeError("Text objects cannot be negated")

    def __pos__(self):
        raise TypeError("Text objects cannot be posited")

    def __getitem__(self, key):
        return self.text[key]

    def __setitem__(self, key, value):
        raise TypeError("Text object does not support item assignment")

    def __delitem__(self, key):
        raise TypeError("Text object does not support item deletion")

    def __iter__(self):
        return iter(self.text)

    def __contains__(self, item):
        return item in self.text

    def __lt__(self, other):
        return self.text < other

    def __le__(self, other):
        return self.text <= other

    def __gt__(self, other):
        return self.text > other

    def __ge__(self, other):
        return self.text >= other

    def replace(self, old, new):
        """
        Replaces characters in the text.

        Parameters:
            old (str or list): The character(s) to replace.
            new (str): The character(s) to replace with.

        Returns:
            str: The text with the characters replaced.
        """
        text = self.text
        if type(old) == list:
            for char in old:
                text = text.replace(char, new)
            return text
        return text.replace(old, new)

    def reverse(self):
        """
        Reverses the text.

        Parameters:
            None

        Returns:
            str: The reversed text.
        """
        return self.text[::-1]

    def count(self, char=None):
        """
        Counts the number of times a character (or all characters) appear(s) in the text.

        Parameters:
            char (str): The character to count (optional).

        Returns:
            int or dict: The number of times the character appears in the text (or a dictionary of all characters and their counts).
        """
        if char != None:
            return self.text.count(char)
        return sort_dict_keys({char: self.text.count(char) for char in self.text})

    def to_snake(self):
        """
        Converts the text to snake case.

        Parameters:
            None

        Returns:
            str: The text in snake case.
        """
        return Text(
            Text(self.text.strip().lower()).replace([" ", "-"], "_"),
        ).replace(
            list((string.punctuation).replace("_", "")),
            "",
        )

    def to_camel(self):
        """
        Converts the text to camel case.

        Parameters:
            None

        Returns:
            str: The text in camel case.
        """
        text = Text(self.text.title().replace(" ", "")).replace(
            list(string.punctuation), ""
        )
        return text[0].lower() + text[1:]

    def to_pascal(self):
        """
        Converts the text to pascal case.

        Parameters:
            None

        Returns:
            str: The text in pascal case.
        """
        return Text(self.text.title().replace(" ", "")).replace(
            list(string.punctuation), ""
        )

    def to_kebab(self):
        """
        Converts the text to kebab case.

        Parameters:
            None

        Returns:
            str: The text in kebab case.
        """
        return Text(Text(self.text.lower()).replace([" ", "_"], "-")).replace(
            list((string.punctuation).replace("-", "")),
            "",
        )

    def to_actual_title(self):
        """
        Converts the text to an actual title (e.g. "this is a title" -> "This Is a Title").

        Parameters:
            None

        Returns:
            str: The text in actual title case.
        """
        words = self.text.split(" ")
        for i in range(len(words)):
            if words[i].lower() not in Text.IGNORE_WORDS or i == 0:
                words[i] = words[i][0].upper() + words[i][1:].lower()
            else:
                words[i] = words[i].lower()
        return " ".join(words)

    def to_initials(self, case_sensitive=True):
        """
        Converts the text to initials (e.g. "John Doe" -> "J.D.").
        If case_sensitive is True, the initials of small words (e.g. "a", "the", "and") will be converted to lowercase.

        Parameters:
            case_sensitive (bool): Whether or not to convert small words to lowercase (optional).

        Returns:
            str: The text in initials.
        """
        words = self.text.split(" ")
        initials = ""
        for word in words:
            if word in Text.IGNORE_WORDS and case_sensitive:
                word = word.lower()
            else:
                word = word.upper()
            initials += word[0] + "."
        return initials
