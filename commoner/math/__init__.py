"""
A module for mathematical functions.

Functions:
    distance(token1, token2, display=False): Calculates the Levenshtein distance between two tokens.
"""
import numpy

def distance(token1, token2, display=False):
    """
    Calculates the Levenshtein distance between two tokens.

    Args:
        token1 (str): The first token.
        token2 (str): The second token.
        display (bool, optional): Whether to display the distance matrix. Defaults to False.

    Returns:
        int: The Levenshtein distance between the two tokens.
    """
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1
    if display:
        for t1 in range(len(token1) + 1):
            for t2 in range(len(token2) + 1):
                print(int(distances[t1][t2]), end=" ")
            print()

    return distances[len(token1)][len(token2)]