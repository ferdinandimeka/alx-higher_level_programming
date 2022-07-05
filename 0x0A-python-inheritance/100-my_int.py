#!/usr/bin/python3
"""
file: 100-my_int.py
Class:
-> MyInt
"""


class MyInt(int):
        """ __eq__ and __ne__ inverted """

        def __eq__(self, other):
            """ Inverted to not equal """
            return int.__ne__(self, other)

        def __ne__(self, other):
            """ Inverted to equal """
            return int.__eq__(self, other)
