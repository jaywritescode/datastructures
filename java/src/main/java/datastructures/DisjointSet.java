package datastructures;

import java.util.Arrays;
import java.util.Collection;
import java.util.Map;
import java.util.Set;
import java.util.function.Function;
import java.util.stream.Collectors;

import static com.google.common.base.Preconditions.*;



public class DisjointSet<T> {

    int[] forest;
    Map<T, Integer> indices;

    DisjointSet(Set<T> elements) {
        forest = new int[elements.size()];
        Arrays.fill(forest, -1);

        Function<T, Integer> counter = new Function() {
            int i = 0;

            @Override
            public Integer apply(Object o) {
                return i++;
            }
        };
        indices = elements.stream().collect(Collectors.toMap(Function.identity(), counter));
    }

    public DisjointSet union(T i, T j) {
        checkNotNull(i);
        checkNotNull(j);
        checkArgument(indices.containsKey(i), "%s not found in forest.", i);
        checkArgument(indices.containsKey(j), "%s not found in forest.", j);

        if (!i.equals(j)) {
            forest[indices.get(j)] = indices.get(i);
        }

        return this;
    }

    public int find(T i) {
        checkNotNull(i);
        checkArgument(indices.containsKey(i), "%s not found in forest.", i);

        return find(indices.get(i));
    }

    private int find(int x) {
        if (forest[x] < 0) {
            return x;
        }
        return find(forest[x]);
    }
}
