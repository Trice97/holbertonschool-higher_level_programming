#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The length of the new list.

    Returns:
        list: A new list (length = list_length) with all divisions.
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                result = my_list_1[i] / my_list_2[i]
            elif i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(result)
    return new_list
