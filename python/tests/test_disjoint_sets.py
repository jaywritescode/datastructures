import unittest
from datastructures.disjoint_sets import DisjointSets


class TestDisjointSets(unittest.TestCase):
    def test_find(self):
        array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        disjoint_sets = DisjointSets(array)

        # initially, all elements are in different sets
        self.assertNotEqual(disjoint_sets.find('c'), disjoint_sets.find('g'))

        disjoint_sets.repr = [-1, -1, -1, -1, -1, 4, 4, 6]

        # now, {4, 5, 6, 7} is a set.
        self.assertEqual(disjoint_sets.find('f'), disjoint_sets.find('h'))

    def test_union(self):
        array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        disjoint_sets = DisjointSets(array)

        disjoint_sets.union('e', 'f')
        disjoint_sets.union('g', 'h')
        disjoint_sets.union('e', 'g')

        self.assertEqual(disjoint_sets.find('e'), disjoint_sets.find('h'))


if __name__ == '__main__':
    unittest.main()
