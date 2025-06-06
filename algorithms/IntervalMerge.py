def merge_intervals(intervals):
    """
    A simple interval merging algorithm to merge a list of intervals, e.g. [(0,1),(3,6),(2,4),(9,12)] -> [(0,1),(2,6),(9,12)]
    :param intervals: List of interval tuples
    :return: Merged intervals
    """

    if intervals is None:
        return None
    if len(intervals) == 0:
        return []

    # First sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current_interval in intervals[1:]:
        # If the current interval start time is after the current merged interval end time, start a new "merged current" interval
        if current_interval[0] > merged_intervals[-1][1]:
            merged_intervals.append(current_interval)
        else:
            # Otherwise set the end time of the "merged current" interval to the max of the "merged current" or the current
            merged_intervals[-1] = (
                merged_intervals[-1][0],
                max(current_interval[1], merged_intervals[-1][1]),
            )
    return merged_intervals
