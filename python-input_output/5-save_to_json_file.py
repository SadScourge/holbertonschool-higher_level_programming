#!/usr/bin/python3
"""Module for saving an object to a JSON file"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    import json
    with open(filename, "w") as file:
        json.dump(my_obj, file)
