#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without
    modifying the original list.

    Args:
        my_list: The original list.
        idx: The index of the element to replace (starting at 0).
        element: The new element to insert.

    Returns:
        A new list with the element replaced at the specified index.
        If idx is negative or out of range, returns a copy of the
        original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list

    new_list = my_list[:]  # Create a copy of the original list
    new_list[idx] = element  # Modify the element in the new list
    return new_list
