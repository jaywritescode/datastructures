package datastructures;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TrieTest {

    @Nested
    @DisplayName("#add")
    class Add {

        @Test
        @DisplayName("it adds a word whose longest prefix in the trie is length zero")
        void noPrefix() {
            Trie trie = new Trie();

            trie.add("their");
            assertTrue(trie.contains("their"));
        }

        @Test
        @DisplayName("it adds a word with a non-zero length prefix in the trie")
        void prefixExists() {
            Trie trie = new Trie();

            trie.add("their");
            trie.add("there");
            assertTrue(trie.contains("their"));
            assertTrue(trie.contains("there"));
        }

        @Test
        @DisplayName("it adds a word that is a prefix of another word in the trie")
        void isPrefix() {
            Trie trie = new Trie();

            trie.add("their");
            trie.add("the");
            assertTrue(trie.contains("their"));
            assertTrue(trie.contains("the"));
        }
    }

    @Test
    void contains() throws Exception {
    }
}