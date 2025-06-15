#!/usr/bin/python3
"""Module to load, addarguments, and save to json file"""


import sys
#importation d'un module nécessaire à la réalisation de l'exercice 7

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


try:
    add_item = load_from_json_file("add_item.json")

except:
add_item = []

arguments = []
add_item.extend(arguments)
save_to_json(add_item, "add_item.json")
