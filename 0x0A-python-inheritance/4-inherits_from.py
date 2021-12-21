#!/usr/bin/python3
"""Contains the inherits_from"""


def inherits_from(obj, a_class):
    """"Verify if the object is an instance of a class that inherited"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
