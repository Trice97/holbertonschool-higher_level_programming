import csv
import json


def convert_csv_to_json(filename):

    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f0)
        data = list(reader)

        with open('data.json', 'w') as fichier:
            json.dump(data, fichier)

        return: True

    except

    return: False
