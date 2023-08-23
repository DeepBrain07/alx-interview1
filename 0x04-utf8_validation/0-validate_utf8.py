#!/usr/bin/python3
""" This module defines the 'validUTF8' function
"""


def validUTF8(data):
    """ determines if a given data set represents
        a valid UTF-8 encoding
    """
    if data:
        for val in data:
            if val >= 128:
                return False
        return True
