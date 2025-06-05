#!/usr/bin/python3
"""Module that load, Add, save"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
with open(filename, a+, encoding="utf-8") as f:
    my_list = []
    my_list.append(args[1:])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
