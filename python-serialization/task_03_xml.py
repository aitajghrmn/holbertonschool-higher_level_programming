#!/usr/bin/env python3
"""
Module for serializing and deserializing a dictionary using XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to a file
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file and returns a Python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for child in root:
        result[child.tag] = child.text

    return result
