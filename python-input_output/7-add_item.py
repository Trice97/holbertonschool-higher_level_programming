#!/usr/bin/python3
""" Module about adding argument to a Python list"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

try:
    new_list = load_from_json_file(filename)
    except File_doesnt_exist:
        new_list = []
    new_list.extend(agrv[1:])
    save_to_json_file(new_list, filename)
