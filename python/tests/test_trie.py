import unittest
from datastructures.trie import Trie


class TestTrie(unittest.TestCase):

    def test_insert__zero_length_prefix__no_data(self):
        trie = Trie()

        word = 'their'
        trie.add(word)

        self.assertIn(word, trie)

    @unittest.expectedFailure
    def test_insert__zero_length_prefix__with_data(self):
        trie = Trie()

        word = 'their'
        value = 25
        trie.add(word, weight=value)

        self.assertIn(word, trie)
        self.assertEquals(trie.get(word), value)

    def test_insert__non_zero_length_prefix__no_data(self):
        trie = Trie()
        trie.add('their')

        word = 'there'

        trie.add(word)
        self.assertIn(word, trie)

    @unittest.expectedFailure
    def test_insert__non_zero_length_prefix__with_data(self):
        trie = Trie()
        trie.add('their')

        word = 'there'
        value = 30

        trie.add(word)
        self.assertIn(word, trie)
        self.assertEquals(trie.get(word), value)

    def test_insert__word_is_prefix_in_tree__no_data(self):
        trie = Trie()
        trie.add('their')

        word = 'the'
        trie.add(word)

        self.assertIn(word, trie)

    @unittest.expectedFailure
    def test_insert__word_is_prefix_in_tree__with_data(self):
        trie = Trie()
        trie.add('their')

        word = 'the'
        value = 30

        trie.add(word)
        self.assertIn(word, trie)
        self.assertEquals(trie.get(word), value)

    @unittest.expectedFailure
    def test_insert__word_is_already_in_tree__update_data(self):
        trie = Trie()
        trie.add('their', 25)

        word = 'their'
        value = 30

        trie.add(word)
        self.assertEquals(trie.get(word), value)

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
