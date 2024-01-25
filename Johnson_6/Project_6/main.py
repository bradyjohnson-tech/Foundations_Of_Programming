def calculate_area_of_rectangle(length, width):
    """
    Calculates the area of a rectangle.
    INPUT:
    length: length of the rectangle
    width: width of the rectangle

    RETURNS:
        products of the length and width.

    >>> calculate_area_of_rectangle(5,10)
    50
    >>> calculate_area_of_rectangle(1,1)
    1
    >>> calculate_area_of_rectangle(4,4)
    16
    >>> calculate_area_of_rectangle(10,10)
    100
    >>> calculate_area_of_rectangle(-3, 6)
    Traceback (most recent call last):
        ...
    ValueError: Length and width must be positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

    return length * width




if __name__ == "__main__":
    import doctest
    doctest.testmod()
