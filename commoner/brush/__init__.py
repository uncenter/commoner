"""
A module for colored text.
"""

# "example"     : [x,      y]
# ^^^^^^^^^ NAME   ^ OPEN  ^ CLOSE
styles = {
    "modifier": {
        "reset": [0, 0],
        "bold": [1, 22],
        "dim": [2, 22],
        "italic": [3, 23],
        "underline": [4, 24],
        "overline": [53, 55],
        "inverse": [7, 27],
        "hidden": [8, 28],
        "strikethrough": [9, 29],
    },
    "color": {
        "black": [30, 39],
        "red": [31, 39],
        "green": [32, 39],
        "yellow": [33, 39],
        "blue": [34, 39],
        "magenta": [35, 39],
        "cyan": [36, 39],
        "white": [37, 39],
        "blackBright": [90, 39],
        "gray": [90, 39], # Duplicate of `blackBright`
        "redBright": [91, 39],
        "greenBright": [92, 39],
        "yellowBright": [93, 39],
        "blueBright": [94, 39],
        "magentaBright": [95, 39],
        "cyanBright": [96, 39],
        "whiteBright": [97, 39],
    },
    "bgColor": {
        "bgBlack": [40, 49],
        "bgRed": [41, 49],
        "bgGreen": [42, 49],
        "bgYellow": [43, 49],
        "bgBlue": [44, 49],
        "bgMagenta": [45, 49],
        "bgCyan": [46, 49],
        "bgWhite": [47, 49],
        "bgGray": [100, 49], # Duplicate of `bgBlackBright`

        "bgBlackBright": [100, 49],
        "bgRedBright": [101, 49],
        "bgGreenBright": [102, 49],
        "bgYellowBright": [103, 49],
        "bgBlueBright": [104, 49],
        "bgMagentaBright": [105, 49],
        "bgCyanBright": [106, 49],
        "bgWhiteBright": [107, 49],
    },
}

# "example"     : "example"
# ^^^^^^^^^ NAME  ^^^^^^^^^ ALIAS
aliases = {
    "grey": "gray",
    "underlined": "underline",
    "ul": "underline",
    "overlined": "overline",
    "bgGrey": "bgGray",

    "brightBlack": "blackBright",
    "brightRed": "redBright",
    "brightGreen": "greenBright",
    "brightYellow": "yellowBright",
    "brightBlue": "blueBright",
    "brightMagenta": "magentaBright",
    "brightCyan": "cyanBright",
    "brightWhite": "whiteBright",

    "bgBrightBlack": "bgBlackBright",
    "bgBrightRed": "bgRedBright",
    "bgBrightGreen": "bgGreenBright",   
    "bgBrightYellow": "bgYellowBright",
    "bgBrightBlue": "bgBlueBright",
    "bgBrightMagenta": "bgMagentaBright",
    "bgBrightCyan": "bgCyanBright",
    "bgBrightWhite": "bgWhiteBright",
}

def assemble(open=None, close=None):
    """
    Assembles the ANSI escape codes for the given open and close styles.
    """
    if open is None:
        if close is None:
            return ""
        return f"\033[{close}m"
    if close is None:
        return f"\033[{open}m"
    return f"\033[{open}m\033[{close}m"


def find(style):
    """
    Finds the ANSI escape codes for the given style.
    """
    for category in styles:
        if style in styles[category]:
            return styles[category][style]
    else:
        if style in aliases:
            return find(aliases[style])
    return None

def all_styles():
    output = []
    for category in styles:
        for style in styles[category]:
            output.append(style)
    return output

def all_modifiers():
    output = []
    for style in styles["modifier"]:
        output.append(style)
    return output

def all_colors():
    output = []
    for style in styles["color"]:
        output.append(style)
    return output

def all_bg_colors():
    output = []
    for style in styles["bgColor"]:
        output.append(style)
    return output

class Brush:
    """
    A class for printing colored text to the terminal.

    Methods:
        rainbow(message, colors=None, background=None)
            Prints a rainbow-colored message to the terminal.
            If `colors` is not specified, the default colors are used.
            If `background` is True, the background will be black.
        set(style)
            Sets the style for the next printed text.
        reset()
            Resets the style for the next printed text.
        print(message, style=None)
            Prints a message to the terminal with the given style.
            If `style` is not specified, the current style is used.
        
        *color*(message)
            Prints a message to the terminal with the given color.
            >>> Brush.red("Hello, world!")
            >>> Brush.bgRed("Hello, world!")
            >>> Brush.underline("Hello, world!")
    """
    @staticmethod
    def rainbow(message, colors=None, background=None):
        if colors is None:
            colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        if background == True:
            background = "bgBrightBlack"
            output = []
            for i, char in enumerate(message):
                output.append(f"{assemble(open=find(colors[i % len(colors)])[0])}{assemble(open=find(background)[0])}{char}{assemble(close=find(colors[i % len(colors)])[1])}{assemble(close=find(background)[1])}")
            return "".join(output)
        output = []
        for i, char in enumerate(message):
            output.append(f"{assemble(open=find(colors[i % len(colors)])[0])}{char}{assemble(close=find(colors[i % len(colors)])[1])}")
        return "".join(output)
    
    @staticmethod
    def set(style):
        """
        Sets the style for the next printed text.

        Args:
            style (str): The style to set.
        """
        print(assemble(open=find(style)[0]), end="")
    
    @staticmethod
    def reset():
        """
        Resets the style for the next printed text.
        """
        print(assemble(close=find("reset")[1]), end="")

    @staticmethod
    def print(message, style="white"):
        """
        Prints a message to the terminal with the given style.

        Args:
            message (str): The message to print.
            style (str, optional): The style to print the message in. Defaults to "white".
        """
        print(f"{assemble(open=find(style)[0])}{message}{assemble(close=find(style)[1])}")
    
    @classmethod
    def generate_dynamic_functions(cls):
        for style in styles:
            for name in styles[style]:
                setattr(cls, name, staticmethod(lambda string, n=name: f"{assemble(open=find(n)[0])}{string}{assemble(close=find(n)[1])}"))

Brush.generate_dynamic_functions()