from unittest import TestCase

from algorithms.SquareFinder.SquareFinder import find_largest_area, LandMat, Location


class Test(TestCase):
    def test_find_largest_area(self):
        cases: list[tuple[LandMat, tuple[Location, int]]] = [
            ([[0]], ((0, 0), 0)),

            ([[1]], ((0, 0), 1)),

            ([[1, 0],
              [0, 0]], ((0, 0), 1)),

            ([[1, 1],
              [1, 1]], ((0, 0), 2)),

            ([[0, 0],
              [0, 1]], ((1, 1), 1),),

            ([[0, 0],
              [1, 0]], ((1, 0), 1)),

            ([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], ((0, 0), 1)),

            ([[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]], ((0, 0), 3))
        ]

        for case in cases:
            self.assertEqual(case[1], find_largest_area(case[0]))