#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        return True

    except FileNotFoundError:
        return False
