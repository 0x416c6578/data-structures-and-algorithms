from typing import Literal, TypeAlias

LandMat: TypeAlias = list[list[Literal[0, 1]]]
Location: TypeAlias = tuple[int, int]


def find_largest_area(land_mat: LandMat) -> tuple[Location, int]:
    """
    Find the square of 1's of largest area in the land matrix
    :param land_mat: list[list[int]] NxM matrix of land to search, 1 = good land, 0 = bad land
    :return: (origin, size) of the largest square
    """

    # Assume land_mat is an NxM matrix
    height, width = len(land_mat), len(land_mat[0])
    print(f"Land size W:{width} H:{height}")

    current_largest_square_origin: Location = (0, 0)
    current_largest_square_size: int = 0

    for row in range(height):
        for col in range(width):
            # Skip this position if it sits within the bounds of the current largest square
            if _is_in_current_largest_square((row, col), current_largest_square_origin, current_largest_square_size):
                continue

            if land_mat[row][col]:
                # If we hit a 1, we start a "candidate" square
                square_size_from_here = _expand_square(land_mat, (row, col))

                # If we find a square of a larger size than the previously biggest square, we can update our new largest
                if square_size_from_here > current_largest_square_size:
                    current_largest_square_origin = (row, col)
                    current_largest_square_size = square_size_from_here

    return current_largest_square_origin, current_largest_square_size


def _expand_square(land_mat: list[list[int]], origin: Location) -> int:
    """
    Given an origin position in the land matrix, find the size of the maximum square from that origin
    :param land_mat: Matrix of "land" to search
    :param origin: Position to start expanding square from
    :return: Int for the size of the biggest square edge from this position
    """
    height, width = len(land_mat), len(land_mat[0])
    origin_row, origin_col = origin

    if not land_mat[origin_row][origin_col]:
        # Should never hit here
        print(f"Position {origin} is 0; no square here")
        return 0

    # We start of with a square size of 1 (the single element in the origin position)
    largest_square_size = 1
    while True:
        # We now check to see if a square size largest_square_size+1 exists
        candidate_square_size = largest_square_size + 1

        # Check to see if this new square size would hit a boundary of the matrix, if so return the previous largest square size
        if _is_outside_boundary(origin, candidate_square_size, (height, width)):
            return largest_square_size

        if _check_if_square_exists_here(land_mat, origin, candidate_square_size):
            largest_square_size = candidate_square_size
        else:
            return largest_square_size


def _is_outside_boundary(origin: Location, candidate_square_size: int, mat_size: tuple[int, int]) -> bool:
    """
    Check to see whether a candidate square in the given position would expand outside the bounds of the array given it's size
    :param origin: The origin position (row, col)
    :param candidate_square_size: The size of the candidate square in this position
    :param mat_size: The size of the matrix (height, width)
    :return: True if the candidate square expands outside the boundaries of the matrix
    """
    if (origin[0] + (candidate_square_size - 1) >= mat_size[0]
            or origin[1] + (candidate_square_size - 1) >= mat_size[1]):
        return True
    else:
        return False


def _check_if_square_exists_here(land_mat: list[list[int]], origin: Location,
                                 candidate_square_size: int) -> bool:
    """
    Check to see, given an origin, whether a square of size candidate_square_size exists, no bounds checking done
    :param land_mat: Matrix of land to search
    :param origin: Origin of the square (row, col)
    :param candidate_square_size: The size of the candidate square in this position
    :return: True if a square of the given size exists, False otherwise
    """
    origin_row, origin_col = origin

    for row in range(candidate_square_size):
        for col in range(candidate_square_size):
            if not land_mat[origin_row + row][origin_col + col]:
                return False

    print(f"Square of size {candidate_square_size} exists at {origin}")
    return True


def _is_in_current_largest_square(current_position: Location,
                                  current_largest_square_origin: Location,
                                  current_largest_square_size: int) -> bool:
    """
    Check if the current position is in the current largest square
    :param current_position: (row,col) to check
    :param current_largest_square_origin: The origin of the current largest square
    :param current_largest_square_size: The size of the current largest square
    :return: True if the current position falls within the current largest square, False otherwise
    """
    return (current_position[0] - current_largest_square_origin[0] < current_largest_square_size
            and current_position[1] - current_largest_square_origin[1] < current_largest_square_size)


if __name__ == '__main__':
    # land = [[1, 0, 1, 1, 1, 1, 0],
    #         [0, 0, 1, 1, 1, 1, 0],
    #         [0, 0, 1, 1, 1, 1, 0],
    #         [1, 1, 1, 1, 1, 1, 0],
    #         [0, 1, 1, 1, 0, 0, 0]]

    land: LandMat = [[1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1]]
    print("Searching:")
    for _row in range(len(land)):
        print(land[_row])

    print(find_largest_area(land))
