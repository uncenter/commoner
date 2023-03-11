import time
import os


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

    @staticmethod
    def bold(text):
        """
        Prints bold text.

        Args:
            text (str): The text to print.

        Returns:
            str: The bolded text.
        """
        return "\033[1m" + text + "\033[0m"

    @staticmethod
    def italic(text):
        """
        Prints italicized text.

        Args:
            text (str): The text to print.

        Returns:
            str: The italicized text.
        """
        return "\033[3m" + text + "\033[0m"

    @staticmethod
    def underline(text):
        """
        Prints underlined text.

        Args:
            text (str): The text to print.

        Returns:
            str: The underlined text.
        """
        return "\033[4m" + text + "\033[0m"

    @staticmethod
    def red(text):
        """
        Prints red text.

        Args:
            text (str): The text to print.

        Returns:
            str: The red text.
        """
        return "\033[0;31m" + text + "\033[0m"

    @staticmethod
    def yellow(text):
        """
        Prints yellow text.

        Args:
            text (str): The text to print.

        Returns:
            str: The yellow text.
        """
        return "\033[0;33m" + text + "\033[0m"

    @staticmethod
    def green(text):
        """
        Prints green text.

        Args:
            text (str): The text to print.

        Returns:
            str: The green text.
        """
        return "\033[0;32m" + text + "\033[0m"

    @staticmethod
    def cyan(text):
        """
        Prints cyan text.

        Args:
            text (str): The text to print.

        Returns:
            str: The cyan text.
        """
        return "\033[0;36m" + text + "\033[0m"

    @staticmethod
    def blue(text):
        """
        Prints blue text.

        Args:
            text (str): The text to print.

        Returns:
            str: The blue text.
        """
        return "\033[0;34m" + text + "\033[0m"

    @staticmethod
    def magenta(text):
        """
        Prints magenta text.

        Args:
            text (str): The text to print.

        Returns:
            str: The magenta text.
        """
        return "\033[0;35m" + text + "\033[0m"

    @staticmethod
    def white(text):
        """
        Prints white text.

        Args:
            text (str): The text to print.

        Returns:
            str: The white text.
        """
        return "\033[0;37m" + text + "\033[0m"

    @staticmethod
    def black(text):
        """
        Prints black text.

        Args:
            text (str): The text to print.

        Returns:
            str: The black text.
        """
        return "\033[0;30m" + text + "\033[0m"

    @staticmethod
    def reset():
        """
        Resets the text color to the default color.

        Returns:
            None
        """
        print("\033[0m", end="")

    @staticmethod
    def set(style):
        """
        Sets the text color to the specified color.

        Args:
            style (str): The color to set the text to.

        Returns:
            None
        """
        if style in ["bold", "b"]:
            print("\033[1m", end="")
        elif style in ["italic", "italics", "i"]:
            print("\033[3m", end="")
        elif style in ["underline", "underlined", "underl", "ul"]:
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
        elif style in ["magenta", "purple"]:
            print("\033[0;35m", end="")
        else:
            raise ValueError("Invalid style")


Chalk.bold("Hello World")


class Console:
    """
    A utility class for interacting with the console.

    Methods:
        clear(): Clears the console.
        format(style): Sets the text color to the specified color.
    """

    @staticmethod
    def clear():
        """
        Clears the console.

        Returns:
            None
        """
        os.system("clear")

    @staticmethod
    def format(style):
        """
        Sets the text color to the specified color.

        Args:
            style (str): The color to set the text to.

        Returns:
            None
        """
        if style is None:
            Chalk.reset()
        else:
            Chalk.set(style)


class Wait:
    """
    A utility class for printing a loading animation to the console.

    Methods:
        start(): Starts the loading animation.
        stop(): Stops the loading animation.
        wait(seconds): Waits for the specified amount of time.
        input(message, color): Waits for the user to press a key.
    """

    @staticmethod
    def wait(seconds):
        """
        Waits for the specified amount of time.

        Parameters:
            seconds (int): The amount of time to wait.

        Returns:
            None
        """
        time.sleep(seconds)

    @staticmethod
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

    @staticmethod
    def warning(message):
        """
        Prints a warning message to the console (yellow text).

        Args:
            message (str): The message to print.

        Returns:
            None
        """
        print(f"{Chalk.yellow('Warning')}: {message}")

    @staticmethod
    def error(message):
        """
        Prints an error message to the console (red text).

        Args:
            message (str): The message to print.

        Returns:
            None
        """
        print(f"{Chalk.red('Error')}: {message}")

    @staticmethod
    def success(message):
        """
        Prints a success message to the console (green text).

        Args:
            message (str): The message to print.

        Returns:
            None
        """
        print(f"{Chalk.green('Success')}: {message}")

    @staticmethod
    def info(message):
        """
        Prints an info message to the console (blue text).

        Args:
            message (str): The message to print.

        Returns:
            None
        """
        print(f"{Chalk.blue('Info')}: {message}")

    @staticmethod
    def welcome(title, name, version="", source="", license="", message="", pause=True):
        """
        Prints a welcome message to the console.

        Args:
            title (str): The title of the program.
            name (str): The name of the program.
            version (str): The version of the program (optional).
            source (str): The source of the data (optional).
            license (str): The license of the program (optional).
            message (str): The message to print (optional).
            pause (bool): Whether to pause the program (optional).

        Returns:
            None
        """
        Console.clear()
        Chalk.set("italic")
        print(f"{title} {Chalk.bold(version)}\n")
        if license != "":
            print(f"Licensed under the {Chalk.bold(license)}.")
        print(f"(c) 2023 {Chalk.bold(name)}.")
        if source != "":
            print(f"Data sourced from {Chalk.underline(source)}.")
        if message != "":
            print(f"{message}")
        Chalk.reset()
        if pause:
            Wait.until()
        Console.clear()
