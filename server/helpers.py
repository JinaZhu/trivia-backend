import random


def shuffleOptions(incorrect, correct):
    """shuffle all possible options"""

    options = incorrect.split(",")
    options.append(correct)
    random.shuffle(options)

    return options
