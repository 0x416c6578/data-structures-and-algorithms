def selection_sort(items):
    # Outer loop - iterate number of elements in the array
    for i in range(len(items)):
        # Keep track of the index of the largest item in the right hand sublist
        max_item_index = i
        # Also keep track of the largest item in the right hand sublist
        max_item = items[i]
        # Inner loop - over every element in the right hand sublist
        for j in range(i+1, len(items)):
            # If we hit an item larger than our current max
            if items[j] > max_item: # Will sort descending
                # Set the index and new seen max item value
                max_item_index = j
                max_item = items[j]
        # Swap the item at index i and the index at the max value position in the right hand sublist
        swap = items[i]
        items[i] = items[max_item_index]
        items[max_item_index] = swap
    return items


def selection_sort_recursive(items):
    """
    Slightly weird but functional recursive selection sort.
    Could use an accumulator rather than doing an in place swap but oh well
    :param items: Items to sort
    :return: Sorted array in descending order
    """

    # Base case (singleton list)
    if len(items) == 1:
        return items

    # Find the index of the max item
    max_item_index = _find_max_index(items)
    # Extract the max item
    max_item = items[max_item_index]

    # Put the leftmost item in the max item index
    items[max_item_index] = items[0]
    # Return the max item concatenated with the recursively sorted tail
    return [max_item] + selection_sort_recursive(items[1:])

def _find_max_index(items):
    max_item = items[0]
    max_item_index = 0
    for i in range(1, len(items)):
        if items[i] > max_item:
            max_item = items[i]
            max_item_index = i
    return max_item_index
