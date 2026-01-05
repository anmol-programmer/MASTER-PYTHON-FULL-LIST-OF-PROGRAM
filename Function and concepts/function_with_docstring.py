def is_even(number):
    """
    Checks whether a given number is even or odd.

    Parameters:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0
print(is_even(23))
print(is_even(20))
print(is_even.__doc__)