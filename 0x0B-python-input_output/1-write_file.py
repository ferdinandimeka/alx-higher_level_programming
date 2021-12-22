#!/usr/bin/python3
"""
 writes a string to a text file
"""

def write_file(filename="", text=""):
    count = 0
    with open("filename", "r") as fp:
        for line in fp:
            count += 1
        return count
