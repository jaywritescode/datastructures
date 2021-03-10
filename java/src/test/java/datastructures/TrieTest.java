package datastructures;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Field;
import java.util.List;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class TrieTest {

    @Nested
    @DisplayName("#add")
    class Add {
        @Test
        @DisplayName("words with no common prefix")
        void noPrefix() throws Exception {
            var trie = new Trie();
            var words = List.of("their", "follow", "car");

            words.forEach(word -> assertThat(trie.add(word)).as("add \"%s\"", word).isTrue());

            var expectedSize = words.stream().mapToInt(String::length).sum() + 1;
            assertThat(size(trie)).isEqualTo(expectedSize);
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