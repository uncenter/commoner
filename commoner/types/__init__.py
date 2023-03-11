"""
A module for improved Python types.

Classes:
    Dict: An extension of the dict type with additional functionality.
    Text: An extension of the str type with additional functionality.
"""


class Dict:
    """
    An extension of the dict type with additional functionality.

    Methods:
        sort_values(dict, reverse): Sorts the dictionary by its values (default is ascending).
        sort_keys(dict, reverse): Sorts the dictionary by its keys (default is ascending).
        swap_kv(dict): Swaps the keys and values of the dictionary.
        reverse(dict): Reverses the dictionary.

    Returns:
        dict: A normal Python dictionary.

    Examples:
        >>> from commoner.types import Dict
        >>> Dict.sort_values({"a": 3, "b": 2, "c": 4})
        {"b": 2, "a": 3, "c": 4}
        >>> Dict.sort_values({"a": 3, "b": 2, "c": 4}, reverse=True)
        {"c": 4, "a": 3, "b": 2}
    """

    def sort_values(dict, reverse=False):
        """
        Sorts a dictionary by its keys.

        Parameters:
            dict (dict): The dictionary to sort.
            reverse (bool): Whether to sort the dictionary in reverse order.

        Returns:
            dict: The sorted dictionary.
        """
        return {
            k: v
            for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=reverse)
        }

    def sort_keys(dict, reverse=False):
        """
        Sorts a dictionary by its values.

        Parameters:
            dict (dict): The dictionary to sort.
            reverse (bool): Whether to sort the dictionary in reverse order.

        Returns:
            dict: The sorted dictionary.
        """
        return {
            k: v
            for k, v in sorted(dict.items(), key=lambda item: item[0], reverse=reverse)
        }

    def swap_kv(dict):
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
        Reverses

        Parameters:
            iterable (dict): The dictionary to reverse.

        Returns:
            dict: The reversed dictionary.
        """
        return dict(reversed(list(iterable.items())))


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

    Examples:
        >>> from commoner.types import Text
        >>> text = Text("Hello, world!")
        >>> text.replace(["Hello", "world"], "Beep")
        "Beep, Beep!"

        >>> text = Text("Hello, world!")
        >>> text.reverse()
        "!dlrow ,olleH"
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
