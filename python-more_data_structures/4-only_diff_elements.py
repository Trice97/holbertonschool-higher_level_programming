#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.
    Args:
        set_1: First set
        set_2: Second set
    Returns:
        A set of elements that are in only one of the two sets
    """
    return set_1 ^ set_2
