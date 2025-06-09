from unittest import TestCase

from blind75.ContainsDuplicate.ContainsDuplicate import has_duplicate


class Test(TestCase):
    def test_has_duplicate(self):
        self.assertFalse(has_duplicate([]), "Empty list has no duplicates")
        self.assertFalse(has_duplicate([1]), "Singleton list has no duplicates")
        self.assertFalse(has_duplicate([1,2,3]), "List of unique elements has no duplicates")
        self.assertTrue(has_duplicate([1,1]), "List containing two of the same elements has duplicates")
        self.assertTrue(has_duplicate([1,2,3,1]), "List containing duplicate")
