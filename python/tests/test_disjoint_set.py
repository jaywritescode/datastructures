import unittest
from datastructures.disjoint_set import DisjointSet


class TestDisjointSet(unittest.TestCase):
    def test_find(self):
        array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        disjoint_set = DisjointSet(array)

        # initially, all elements are in different sets
        self.assertNotEqual(disjoint_set.find('c'), disjoint_set.find('g'))

        disjoint_set.repr = [-1, -1, -1, -1, -1, 4, 4, 6]

        # now, {4, 5, 6, 7} is a set.
        self.assertEqual(disjoint_set.find('f'), disjoint_set.find('h'))

    def test_union(self):
        array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        disjoint_set = DisjointSet(array)

        disjoint_set.union('e', 'f')
        disjoint_set.union('g', 'h')
        disjoint_set.union('e', 'g')

        self.assertEqual(disjoint_set.find('e'), disjoint_set.find('h'))


if __name__ == '__main__':
    unittest.main()
