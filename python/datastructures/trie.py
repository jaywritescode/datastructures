class Trie:
    def __init__(self):
        self.root = Trie.Node()

    def add(self, word):
        """
        Adds a word to the trie.

        :param word: the word being added to the trie
        :return: False if the word is already in the trie, otherwise True
        """
        current_node = self.root
        for char in word:
            current_node = current_node.get_child(char)

        if current_node.payload:
            return False
        current_node.payload = True
        return True

    def contains(self, word):
        """
        Looks up a word in the trie.

        :param word: the target word
        :return: True if the target word is in the trie, otherwise False
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.payload is not None

    def __contains__(self, item):
        return self.contains(item)

    class Node:
        def __init__(self):
            self.children = dict()
            self.payload = None

        def get_child(self, char):
            if char not in self.children:
                self.children[char] = Trie.Node()
            return self.children[char]


if __name__ == '__main__':
    t = Trie()

