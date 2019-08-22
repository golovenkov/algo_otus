import random
import math


def assert_sort_asc(a):
    for i in range(1, len(a)):
        assert a[i] >= a[i - 1]


def print_heap(a):
    """Print heap as a tree"""
    h = int(math.log(len(a), 2)) + 1
    k = 0
    for i in range(h):
        line = "".join([" " for j in range(int(2 ** (h - i)))])
        delimeter = "".join([" "] * (2 ** (h - i)))
        line = line + delimeter.join([str(j) for j in a[k:k + int(2**i)]])
        print(line)
        k += int(2**i)


def parent(i):
    """Find the index of a parent"""
    return (i + 1) // 2 - 1


def left(i):
    """Find the index of a left child"""
    return (i + 1) * 2 - 1


def right(i):
    """Find the index of a right child"""
    return (i + 1) * 2


def swap(a, i, j):
    """Swap 2 elements in place """
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def max_heapify(a, heap_size, i):
    """Drown the element at index `i` if needed. Return a number of operations"""
    count = 1

    l = left(i)
    r = right(i)

    largest_index = i
    if l < heap_size:
        if a[l] > a[i]:
            largest_index = l

    if r < heap_size:
        if a[r] > a[largest_index]:
            largest_index = r

    # print(a, i, l, r, largest_index)
    if largest_index != i:
        swap(a, i, largest_index)
        count += max_heapify(a, heap_size, largest_index)

    return count


def build_heap(a, heap_size):
    """Build a heap from unsorted array in place. Return a number of operations"""
    count = 0
    for i in range(len(a) // 2 - 1, -1, -1):
        # print("========================\ni: %d, a[i]:%d" % (i, a[i]))
        count += max_heapify(a, heap_size, i)
        # print_heap(a)
    return count


def heap_sort(a):
    """Heap sort in place. Return sorted array and a number of operations"""
    count = 0
    heap_size = len(a)
    count += build_heap(a, heap_size)  # first, build the heap
    for i in range(len(a) - 1, 0, -1):
        swap(a, 0, i)                            # swap a[0] and a[-1]
        heap_size -= 1
        count += max_heapify(a, heap_size, 0)   # rebuild the heap
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

    assert_sort_asc(a)


if __name__ == "__main__":
    main()

    # Example results:
    #
    # heap_length: 20480
    # [max_heapify] count: 8
    # [build_heap] count: 25534
    # [heap_sort] count: 285964
