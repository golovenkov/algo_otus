import random
import math


def assert_sort_asc(array):
    """Test the array to being sorted"""
    for i in range(1, len(array)):
        assert array[i] >= array[i - 1]


def print_heap(heap):
    """Print heap as a tree"""
    height = int(math.log(len(heap), 2)) + 1
    k = 0
    for level in range(height):
        line = "".join([" " for j in range(int(2 ** (height - level)))])
        delimeter = "".join([" "] * (2 ** (height - level)))
        line = line + delimeter.join([str(j) for j in heap[k:k + int(2**level)]])
        print(line)
        k += int(2**level)


def parent(node_index):
    """Find the index of a parent"""
    return (node_index + 1) // 2 - 1


def left(node_index):
    """Find the index of a left child"""
    return (node_index + 1) * 2 - 1


def right(node_index):
    """Find the index of a right child"""
    return (node_index + 1) * 2


def swap(array, first_idx, second_idx):
    """Swap 2 elements with indexes `first_idx` and `second_idx` in place """
    array[first_idx], array[second_idx] = array[second_idx], array[first_idx]


def max_heapify(array, heap_size, i):
    """Drown the element at index `i` if needed. Return a number of operations"""
    count = 1

    l = left(i)
    r = right(i)

    largest_index = i
    if l < heap_size and array[l] > array[i]:
            largest_index = l

    if r < heap_size and array[r] > array[largest_index]:
            largest_index = r

    # print(heap, i, l, r, largest_index)
    if largest_index != i:
        swap(array, i, largest_index)
        count += max_heapify(array, heap_size, largest_index)

    return count


def build_heap(array, heap_size):
    """Build a heap from unsorted array in place. Return a number of operations"""
    count = 0
    # Iterate over all non-leaves (nodes with at least one child) in reverse order
    for i in range(len(array) // 2 - 1, -1, -1):
        # print("========================\ni: %d, array[i]:%d" % (i, array[i]))  # DEBUG
        count += max_heapify(array, heap_size, i)
        # print_heap(array)   # DEBUG
    return count


def heap_sort(array):
    """Heap sort the `array` in place. Return a number of operations"""
    heap_size = len(array)
    count = build_heap(array, heap_size)  # first, build the heap
    for i in range(heap_size - 1, 0, -1):
        # Remove the first (and the largest) element from the heap, then replace it with the last element. 
        # This operation is implemented as swaping of two elements and decreasing heap size by one
        swap(array, 0, i) 
        heap_size -= 1
        count += max_heapify(array, heap_size, 0)    # rebuild the heap
    return count


def main():
    length = 20480
    max_number = length * 10
    # 1a. Generate shuffled array
    a_shuffled = [random.randrange(max_number) for _ in range(length)]  # shuffled array
    print("heap_length: %d" % length)

    # 2a. Run max_heapify from the root
    a = list(a_shuffled)
    # print_heap(a)
    count = max_heapify(a, length, 0)
    print("[max_heapify] count: %d" % count)

    # 2. Build Heap
    a = list(a_shuffled)
    # print_heap(a)
    count = build_heap(a, length)
    print("[build_heap] count: %s" % count)
    # print("result: %s" % a)

    # 3. Heap Sort
    a = list(a_shuffled)
    # print("[heap_sort] a:\t\t%s" % a)
    count = heap_sort(a)
    # print("[heap_sort] sorted:\t%s" % a)
    print("[heap_sort] count: %d" % count)
    # print_heap(a)
    assert_sort_asc(a)


if __name__ == "__main__":
    main()

    # Example results:
    #
    # heap_length: 20480
    # [max_heapify] count: 8
    # [build_heap] count: 25534
    # [heap_sort] count: 285964
