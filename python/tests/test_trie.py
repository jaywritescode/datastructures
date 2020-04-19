import unittest
from datastructures.trie import Trie

class TestTrie(unittest.TestCase):

    words = ['the', 'their', 'there', 'a', 'any', 'answer', 'by', 'bye']

    def test_insert(self):
        trie = Trie()

        # It inserts a word whose longest prefix in the trie is length zero.
        word = 'their'
        trie.add(word)
        self.assertIn(word, trie)

        # It inserts a word whose longest prefix in the trie has length greater than zero.
        word = 'there'
        trie.add(word)
        self.assertIn(word, trie)

        # It inserts a word that is a prefix of a word already in the trie
        word = 'the'
        trie.add(word)
        self.assertIn(word, trie)

    def test_contains(self):
        words = ['the', 'their', 'there', 'a', 'any', 'answer', 'by', 'bye']

        trie = Trie()
        for word in words:
            trie.add(word)

        self.assertIn('answer', trie)
        self.assertIn('any', trie)
        self.assertNotIn('anybody', trie)


if __name__ == '__main__':
    unittest.main()
