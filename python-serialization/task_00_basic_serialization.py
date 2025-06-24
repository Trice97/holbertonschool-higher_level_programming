import json


def serialize_and_save_to_file(data, filename):
    """Function to serialize and save data to the specified file"""
    with open(filename, 'w', encoding='utf-8') as fichier:
        json.dump(data, fichier)


def load_and_deserialize(filename):
    """Function to load and deserialize data from the specified file"""
    with open(filename, 'r', encoding='utf-8') as fichier:
        return json.load(fichier)
