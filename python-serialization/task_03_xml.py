#!/usr/bin/env python3
"""
Serializing and deserializing with XML format.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save to file.

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The filename to save the XML data
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Create ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

    except Exception:
        pass


def deserialize_from_xml(filename):
    """
    Deserialize XML file back to Python dictionary.

    Args:
        filename (str): The filename of the XML file to read

    Returns:
        dict: The deserialized dictionary
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct dictionary
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary

    except Exception:
        return {}
