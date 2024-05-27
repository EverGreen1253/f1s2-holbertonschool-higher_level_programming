#!/usr/bin/python3
""" Nameless module for Task 3 """

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """ does what it says """
    root = ET.Element("root")
    for k in dictionary.keys():
        ET.SubElement(root, k).text = dictionary[k]

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """ does what it says """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
