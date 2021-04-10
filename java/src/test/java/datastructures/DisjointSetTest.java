package datastructures;

import org.assertj.core.api.AutoCloseableSoftAssertions;
import org.junit.jupiter.api.Test;

import java.util.Set;
import java.util.function.BiPredicate;

public class DisjointSetTest {

    Set<String> elements = Set.of("aardvark", "bison", "cougar", "dolphin", "eagle", "eel", "elephant", "elk");

    BiPredicate<String, String> R = (i, j) -> i.charAt(0) == j.charAt(0);

    @Test
    void testUnionAndFind() throws Exception {
        DisjointSet<String> disjointSet = new DisjointSet<>(elements);

        disjointSet.
                union("eagle", "eel").
                union("elephant", "elk").
                union("eagle", "elephant");

        try (AutoCloseableSoftAssertions softly = new AutoCloseableSoftAssertions()) {
            for (String i : elements) {
                for (String j : elements) {
                    softly.assertThat(disjointSet.sameEquivalenceClass(i, j))
                            .as("%s %s %s", i, R.test(i, j) ? "∼" : "≁", j)
                            .isEqualTo(i.charAt(0) == j.charAt(0));
                }
            }
        }
    }
}
