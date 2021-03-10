package datastructures;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Field;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class TrieTest {

    @Nested
    @DisplayName("#add")
    class Add {
        @Test
        @DisplayName("words with no common prefix")
        void noPrefix() throws Exception {
            Trie trie = new Trie();
            var words = List.of("their", "follow", "car");

            words.forEach(word -> assertTrue(trie.add(word)));
            assertEquals(size(trie), words.stream().mapToInt(String::length).sum() + 1);
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

    static int size(Trie trie) throws Exception {
        Field field = Trie.class.getDeclaredField("root");
        return size((Trie.Node) field.get(trie));
    }

    private static int size(Trie.Node node) {
        var children = node.children.values();
        var descendantCount = children.stream().mapToInt(n -> size(n)).sum();

        return 1 + descendantCount;
    }
}