# Commoner

[![PyPI](https://img.shields.io/pypi/v/commoner)](https://pypi.org/project/commoner/)
[![PyPI - License](https://img.shields.io/pypi/l/commoner)](https://pypi.org/project/commoner/)

Commoner provides a set of common functions and classes for Python projects.

## Installation

Commoner is available on PyPI and can be installed with `pip`:

Either run:
```sh
pip install commoner
```
or run:
```sh
python3 -m pip install commoner
```

## Usage

Commoner is a collection of common functions and classes that can be used in any Python project. It is not meant to be used as a standalone library, but rather as a collection of useful functions and classes that can be imported into other projects. The following is a list of the modules and classes that are available in Commoner:

* println() - Prints a line of text and then prints a specified number of newlines.
* printsln() - Prints a line of text without a newline at the end.
* printx() - Prints a line of text a specified number of times.
* typewriter() - Prints a line of text with a typewriter effect (one character at a time).
* random_string() - Generates a random string of a specified length.
* sort_dict_keys() - Sorts a dictionary by its keys.
* sort_dict_values() - Sorts a dictionary by its values.
* swap_keys_values() - Swaps the keys and values of a dictionary.
* reverse() - Reverses a list, string, or dictionary.

### Chalk

The Chalk class provides a set of methods for printing colored text using ANSI escape codes.

* bold(text) - Prints bold text.
* italic(text) - Prints italic text.
* underline(text) - Prints underlined text.
* red(text) - Prints red text.
* yellow(text) - Prints yellow text.
* green(text) - Prints green text.
* cyan(text) - Prints cyan text.
* blue(text) - Prints blue text.
* magenta(text) - Prints magenta text.
* white(text) - Prints white text.
* black(text) - Prints black text.

* set(color): Sets the text color to the specified color.
* reset(): Resets the text color to the default color.

### Wait

The Wait class provides a set of methods for printing a loading animation to the console.

* start() - Starts the loading animation.
* stop() - Stops the loading animation.
* wait(seconds): Waits for the specified amount of time.
* input(message, color): Waits for the user to press a key (with an optional message and optional color).

#### Progress

The Progress sub-class of Wait provides a set of methods for printing a progress bar to the console.

* Progress(total, character="#", reverse=False): Creates a new progress bar.
* Progress.start(message): Starts the progress bar (with an optional message).
* Progress.update(current, message): Updates the progress bar (with an optional message).
* Progress.finish(message): Finishes the progress bar (with an optional message).
* Progress.timed(seconds, character, message): Starts a progress bar that counts down from a specified amount of time.

For example:
```py
my_progress = Wait.Progress(100)
my_progress.start()
for i in range(100):
    run_some_code()
    my_progress.update(i + 1)
my_progress.finish()
```
or for a timed progress bar:
```py
my_progress = Wait.Progress.timed(10)
````

### Shout

The Shout class provides a set of methods for printing preconfigured messages to the console.

* warning(message) - Prints a warning message to the console (yellow text).
* error(message) - Prints an error message to the console (red text).
* success(message) - Prints a success message to the console (green text).
* info(message) - Prints an info message to the console (blue text).

### Text

The Text class is an extension of the str type with additional functionality.

* replace(old, new) - Replaces characters in the text.
* reverse() - Reverses the text.
* count(char) - Counts the number of times a character (or all characters) appear(s) in the text.
* to_snake() - Converts the text to snake case.
* to_camel() - Converts the text to camel case.
* to_pascal() - Converts the text to pascal case.
* to_kebab() - Converts the text to kebab case.
* to_actual_title() - Converts the text to an actual title (e.g. "this is a title" -> "This Is a Title").
* to_initials(case_sensitive) - Converts the text to initials (e.g. "this is a title" -> "T.I.a.T") (case sensitive by default).

### Console

The Console class provides a set of methods for interacting with the console.

* clear() - Clears the console.
* format(style) - Sets the text color to the specified color.

## License

Commoner is licensed under the MIT License. See the LICENSE file for more information.
