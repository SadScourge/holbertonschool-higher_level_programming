#!/usr/bin/python3
"""Module for loading from a JSON file"""


def load_from_json_file(filename):
    import json
    with open(filename, "r") as file:
        return json.load(file)
