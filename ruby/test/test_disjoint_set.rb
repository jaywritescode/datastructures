require 'pry'

require 'minitest/autorun'
require_relative '../src/disjoint_set.rb'

class DisjointSet
  attr_accessor :forest

  def same_set?(x, y)
    find(x) == find(y)
  end
end

class TestDisjointSet < Minitest::Test
  def setup
    @elements = %w(a b c d e f g h)
    @disjoint_set = DisjointSet.new(@elements)
  end

  def test_find
    @disjoint_set.forest = [-1, -1, -1, -1, -4, 4, 4, 6]

    assert_equal @disjoint_set.find('f'), @disjoint_set.find('h')
    refute_equal @disjoint_set.find('a'), @disjoint_set.find('g')
  end

  def test_path_compression
    disjoint_set = DisjointSet.new ('a'..'p').to_a
    disjoint_set.forest = [-16, 0, 0, 2, 0, 4, 4, 6, 0, 8, 8, 10, 8, 12, 12, 14]

    disjoint_set.find('o')
    assert_equal [-16, 0, 0, 2, 0, 4, 4, 6, 0, 8, 8, 10, 0, 12, 0, 14], disjoint_set.forest
  end

  def test_union
    @disjoint_set.forest = [-1, -1, -1, -1, -4, 4, 4, 6]
    @disjoint_set.union('d', 'e')

    assert @disjoint_set.same_set?('d', 'e')
  end

  def test_union_by_size
    @disjoint_set.forest = [-1, -1, -1, -1, -4, 4, 4, 6]
    @disjoint_set.union('d', 'g')

    assert_equal [-1, -1, -1, 4, -5, 4, 4, 6], @disjoint_set.forest

    # attempt to merge two elements in the same set
    @disjoint_set.union('f', 'g')
    assert_equal [-1, -1, -1, 4, -5, 4, 4, 6], @disjoint_set.forest

    # merge two sets of equal rank
    @disjoint_set.union('a', 'c')
    assert [
      [-2, -1, 0, 4, -5, 4, 4, 6],
      [2, -1, -2, 4, -5, 4, 4, 6]
    ].include?(@disjoint_set.forest)
  end

  def test_count
    @disjoint_set.forest = [-1, -1, -1, -1, -4, 4, 4, 6]
    assert_equal 5, @disjoint_set.count
  end
end
