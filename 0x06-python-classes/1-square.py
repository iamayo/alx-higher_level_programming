#!/usr/bin/python3
""" Creates an empty class called square """


class Square:
    """ Represents a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
