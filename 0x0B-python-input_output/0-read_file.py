#!/usr/bin/python3
""" 
A function that reads a text file
"""

def read_file(filename=""):
    with open(filename, 'r') as f:
        fo = f.read()
        print(fo)

