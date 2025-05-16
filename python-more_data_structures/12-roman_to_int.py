#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.
    Args:
        roman_string: The Roman numeral string to convert
    Returns:
        The integer value of the Roman numeral, or 0 if invalid input
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_value = 0

    # Process the string from right to left
    for char in reversed(roman_string):
        if char not in roman_values:
            return 0

        current_value = roman_values[char]

        # If current value is greater than or equal to previous value,
        # add it to the result (standard addition)
        if current_value >= prev_value:
            result += current_value
        # If current value is less than previous value,
        # subtract it from the result (for cases like IV, IX, etc.)
        else:
            result -= current_value

        prev_value = current_value

    return result
