#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    if not my_list:
        return None
    biggest = my_list[0]
    for number in my_list:
        if number > biggest:
            biggest = number
    return biggest
