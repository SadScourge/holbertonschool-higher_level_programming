#!/usr/bin/python3
"""Module for appending to a file"""


def append_write(filename="", text=""):
    with open(filename, "a") as file:
        return file.write(text)
