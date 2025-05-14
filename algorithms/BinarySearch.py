def binary_search(items, elem):
    """
    Returns the index of an element to search for in an input array, or None if the element can't be found
    :param items: The array of items to search
    :param elem: The element to search for
    :return: The index of the element, or None if the element can't be found
    """

    # Initialise the low and high pointers to the start and end of the array
    low = 0
    high = len(items) - 1

    # Whilst the two pointers haven't hit each other
    while low <= high:
        # Find the midpoint index
        midpoint = (low + high) // 2

        # Get the guess from the input array
        guess = items[midpoint]

        if guess == elem:
            # We have found our element, return the index
            return midpoint
        if guess > elem:
            # We know our target is in the left hand side so we constrain to that side
            high = midpoint - 1
        else:
            # Otherwise we constrain to the right hand side
            low = midpoint + 1
    return None