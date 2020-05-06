require 'pry'

require 'minitest/autorun'
require_relative '../src/binary_heap.rb'

class BinaryHeap
  def heap_order_property?
    1.upto(size).all? do |i|
      val = @array[i]
      left_child = @array[i * 2]
      right_child = @array[i * 2 + 1]

      (left_child.nil? || (val <=> left_child) <= 0) && (right_child.nil? || (val <=> right_child) <= 0)
    end
  end

  def compact!
    @array.slice! (@size + 1)..-1
  end
end

describe BinaryHeap do
  it 'builds a binary heap' do
    elements = [150, 80, 40, 30, 10, 70, 110, 100, 20, 90, 60, 50, 120, 140, 130]
    
    heap = BinaryHeap.new(elements)

    _(heap.size).must_equal elements.size
    _(heap.heap_order_property?).must_equal true
  end

  describe 'insert' do
    it 'maintains the heap-order property' do
      heap = BinaryHeap.new([13, 21, 16, 24, 31, 19, 68, 65, 26, 32])
  
      heap.insert(14)
  
      _(heap.size).must_equal 11
      _(heap.heap_order_property?).must_equal true
    end
  end

  describe 'deleteMin' do
    it 'removes and returns the smallest value' do
      elements = [13, 14, 16, 19, 21, 19, 68, 65, 26, 32, 31]
      heap = BinaryHeap.new(elements)

      elements.sort.each do |e|
        _(heap.deleteMin).must_equal e
      end
    end
  end
end