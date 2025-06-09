def has_duplicate(nums: list[int]) -> bool:
    """
    Determine whether a list contains a duplicate value
    :param nums: List to check
    :return: True if the list contains a duplicate
    """
    """
    Thoughts: We could convert the list to a set (which is O(n)), then check to see whether the length of that set is
    less than the length of the list - if so the list contains a duplicate
    """
    nums_set = set(nums)
    return not (len(nums) == len(nums_set))