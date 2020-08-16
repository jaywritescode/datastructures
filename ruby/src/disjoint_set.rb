class DisjointSet
  def initialize(elements)
    @indices = Hash[elements.zip(0..)]
    @forest = [-1] * elements.size
  end

  # Finds the set containing `value`.
  #
  # Note that the actual return value (assuming it's non-nil) is arbitrary.
  # What matters is that find(a) == find(b) if and only if a ~ b.
  #
  # @param value the value we're looking for
  # @return the label of the set `value` is in
  def find(value)
    find_root @indices.fetch(value)
  end

  # Merges the set containing `x` and the set containing `y`
  #
  # @param value1 a value
  # @param value2 another value
  # @return nil
  def union(value1, value2)
    union_by_size find(value1), find(value2)
  end

  private

  def find_root(index)
    return index if @forest[index] < 0
    @forest[index] = find_root(@forest[index])
  end

  def union_by_size(root1, root2)
    return if root1 == root2

    # make the tree with fewer nodes a child of the tree with more nodes
    if @forest[root2] < @forest[root1]
      @forest[root2] += @forest[root1]
      @forest[root1] = root2
    else
      @forest[root1] += @forest[root2]
      @forest[root2] = root1
    end
  end

  def rank_at_root(index)
    return @forest[index].abs if @forest[index] < 0
  end
end
