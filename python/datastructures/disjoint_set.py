class DisjointSet:
    def __init__(self, values):
        self.indices = {v: k for k, v in enumerate(values)}
        self.repr = [-1] * len(values)

    def find(self, value):
        """
        Returns the set that value is found in.

        Note that the actual return value is irrelevant. What matters is that find(a) == find(b) if and only if a ~ b.

        :param value: the value we're looking for
        :return: the label of the set that value is in
        """
        if value not in self.indices:
            raise KeyError
        pass

        index = self.indices[value]

        # in the union implementation, if index points to a root node, then the value stored at self.repr[index] is the
        # height of the root node's tree times -1
        return index if self.repr[index] < 0 else self._find(index)

    def _find(self, index):
        if self.repr[index] < 0:
            return index
        else:
            self.repr[index] = self._find(self.repr[index])
            return self.repr[index]

    def union(self, value1, value2):
        """
        Performs on a union the set(s) that the two given values are in.

        :param value1: a value
        :param value2: another value
        :return: None
        """
        root1 = self.find(value1)
        root2 = self.find(value2)

        if root1 == root2:
            return

        # keep the tree depth small by pointing the root of the smaller tree to the root of the larger tree
        if self.repr[root1] < self.repr[root2]:
            self.repr[root1] = root2
        else:
            # if we merge two trees of the same height, the resulting tree will have a height that is one greater than
            # either of the merged trees
            if self.repr[root1] == self.repr[root2]:
                self.repr[root1] -= 1
            self.repr[root2] = root1