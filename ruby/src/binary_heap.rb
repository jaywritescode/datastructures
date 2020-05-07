# Binary (min) heap implementation.
#
# Supports two operations: insert and deleteMin.
#
# All the elements in the heap must be Comparable to each other. That is, for
# for any `a` and `b` in the heap, `a <=> b` must be non-`nil`.
class BinaryHeap
  # Constructs a binary heap with the given values.
  #
  # @param values [Array<Comparable>] initial values
  def initialize(values = [])
    @array = [nil] + values
    @size = values.length

    build
  end

  # Inserts `val` into this binary heap.
  #
  # @param val [Comparable] the element
  def insert(val)
    @size += 1

    hole = size
    loop do
      parent_index = hole >> 1
      cmp = array[parent_index]

      # min-heap property: @array[x] <= @array[x >> 1] && @array[x] <= @array[(x >> 1) + 1]
      break if cmp.nil? || (cmp <=> val).negative?

      array[hole] = cmp
      hole = parent_index
    end

    @array[hole] = val
  end

  # Removes and returns the minimum value from this heap.
  #
  # @return [Comparable] the minimum value
  def deleteMin
    return nil if empty?

    val = array[1]
    array[1] = array[size]

    @size -= 1

    percolateDown(1)
    val
  end

  def size
    @size
  end

  def empty?
    size == 0
  end

  private

  def array
    @array
  end

  def percolateDown(hole)
    tmp = array[hole]

    loop do
      child = hole << 1     # child points to the left child of the hole node

      # hole is a leaf node
      break if child > size

      # hole is a node with two children, find the smaller of the two
      unless child == size
        child += 1 if (array[child + 1] <=> array[child]).negative?
      end

      break if (tmp <=> array[child]) <= 0

      array[hole] = array[child]
      hole = child
    end

    array[hole] = tmp
  end

  def build
    i = size >> 1
    loop do
      break unless i > 0
      percolateDown i
      i -= 1
    end
  end
end
