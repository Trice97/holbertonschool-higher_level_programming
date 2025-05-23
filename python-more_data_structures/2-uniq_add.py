#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).
    Args:
        my_list: The input list
    Returns:
        The sum of all unique integers in the list
    """
    unique_integers = set()
    for num in my_list:
        unique_integers.add(num)
    return sum(unique_integers)
