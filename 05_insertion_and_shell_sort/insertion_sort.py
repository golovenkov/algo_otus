import random
from collections import defaultdict


def insertion_sort(a):
    """Sort the list `a` in place with insertion sort"""
    count = 0
    for i in range(1, len(a)):
        j = i
        element_to_sort = a[j]
        while j > 0 and a[j - 1] > element_to_sort:   # shift values by 1 element to the right
            a[j] = a[j - 1]
            j -= 1
            count += 1
        a[j] = element_to_sort   # insert the lowest number
    return count


def insertion_sort_gap(a, low, gap=1):
    """Sort the list `a` in place with insertion sort using gaps"""
    count = 0
    for i in range(low + gap, len(a), gap):
        j = i
        element_to_sort = a[j]
        while j > low and a[j - gap] > element_to_sort:
            a[j] = a[j - gap]
            j -= gap
            count += 1
        a[j] = element_to_sort
    return count


def shell_sort(a, d):
    """Sort the list `a` in place with shell sort"""
    count = 0
    for gap in d:
        for low in range(gap):
            count += insertion_sort_gap(a, low=low, gap=gap)
    return count


def partial_shuffle(a, k=0, percent=0.0):
    """In place shuffle k elements or X percent of elements"""
    if k > 0 or percent > 0:
        if k == 0:
            k = int(len(a) * percent)
        # retrieve k random indexes, shuffle array elements, and write them back to the source array
        indexes = sorted(random.sample(range(0, len(a)), k=k))
        # print("Dedug: shuffle indexes: %s" % indexes)
        subarray = [a[i] for i in indexes]
        random.shuffle(subarray)
        for j in range(k):
            a[indexes[j]] = subarray[j]
    return a


def main():
    arrays = dict()
    max_length = 40000
    length = 20
    while length <= max_length:
        # 1a. Generate shuffled array
        a = [random.randrange(1000000) for _ in range(length)]  # shuffled array

        # 1b. Generate 10% shuffled array and 5-element shuffled array from a sorted one
        a_sorted = list(a)
        a_sorted.sort()

        a_10percent = list(a_sorted)
        partial_shuffle(a_10percent, percent=0.1)

        a_5shuffled = list(a_sorted)
        partial_shuffle(a_5shuffled, k=5)

        arrays[length] = {
            "shuffled": {
                "array": a,
                "count": defaultdict(int)
            },
            "10_percent": {
                "array": a_10percent,
                "count": defaultdict(int)
            },
            "5_shuffled": {
                "array": a_5shuffled,
                "count": defaultdict(int)
            }
        }
        length *= 2

    print("Arrays lengths: %s" % sorted(arrays.keys()))

    a102549 = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
    a033622 = [1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929, 16001, 36289, 64769, 146305]
    algorithms = {
        "insertion_sort": lambda x: insertion_sort(list(x)),
        "shell_sort_a102549": lambda x: shell_sort(list(x), d=sorted(a102549, reverse=True)),
        "shell_sort_a033622": lambda x: shell_sort(list(x), d=sorted(a033622, reverse=True)),
    }

    # 2. Count the number of operations for each case (length, array_type)
    for length in sorted(arrays.keys()):
        for array_type in arrays[length].keys():
            for algorithm in algorithms.keys():
                count = algorithms[algorithm](arrays[length][array_type]["array"])
                arrays[length][array_type]["count"][algorithm] = count
                # print(length, array_type, algorithm, count)

    # 3. Save the results
    with open("shuffled_results.tsv", "wt") as shuff_f, \
            open("10percent_results.tsv", "wt") as shuff_10p_f, \
            open("5shuflled_results.tsv", "wt") as shuff_5_f:
        shuff_f.write("length\tinsertion_cnt\ta102549_cnt\ta033622_cnt\n")
        shuff_10p_f.write("length\tinsertion_cnt\ta102549_cnt\ta033622_cnt\n")
        shuff_5_f.write("length\tinsertion_cnt\ta102549_cnt\ta033622_cnt\n")
        # for shuffled array
        # insertion_sort
        for length in sorted(arrays.keys()):
            shuff_f.write(
                "%d\t%s\t%s\t%s\n" % (
                    length,
                    arrays[length]["shuffled"]["count"]["insertion_sort"],
                    arrays[length]["shuffled"]["count"]["shell_sort_a102549"],
                    arrays[length]["shuffled"]["count"]["shell_sort_a033622"]
                )
            )
            shuff_10p_f.write(
                "%d\t%s\t%s\t%s\n" % (
                    length,
                    arrays[length]["10_percent"]["count"]["insertion_sort"],
                    arrays[length]["10_percent"]["count"]["shell_sort_a102549"],
                    arrays[length]["10_percent"]["count"]["shell_sort_a033622"]
                )
            )
            shuff_5_f.write(
                "%d\t%s\t%s\t%s\n" % (
                    length,
                    arrays[length]["5_shuffled"]["count"]["insertion_sort"],
                    arrays[length]["5_shuffled"]["count"]["shell_sort_a102549"],
                    arrays[length]["5_shuffled"]["count"]["shell_sort_a033622"]
                )
            )


if __name__ == "__main__":
    main()
