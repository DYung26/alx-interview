#!/usr/bin/env python3
"""
This module provides a utility to validate whether a given list of integers
represents a valid UTF-8 encoding. Each integer is treated as a byte, and the
module confirms if these bytes form a valid UTF-8 encoded sequence.
"""


def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.

    Parameters:
    data (list of int): A list of integers where each integer should be in the
    range 0-255, representing a byte.

    Returns:
    bool: True if the list represents a valid UTF-8 encoding, False otherwise.

    The function converts the list of integers to bytes and attempts to decode
    them as UTF-8. If decoding succeeds, the data is valid UTF-8; otherwise,
    an exception is caught, and the function returns False.
    """
    try:
        bytes(data).decode('utf-8')
        return True
    except ValueError:
        return False
    except UnicodeDecodeError:
        return False
