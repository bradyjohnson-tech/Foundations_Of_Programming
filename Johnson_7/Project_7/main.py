import random
import time
import timeit

import insertion_sort
import merge_sort
import selection_sort


def generate_list(n):
    rand_no_list = []
    for i in range(n):
        rand_no_list.append((random.randint(0, 1000000)))

    return rand_no_list


"""
    The merge sort algorithm is always going to be the best sort algorithm in the worst case scenario. Big picture is 
    that when you sort a lot of data the merge sort grows in an n log n fashion where insert sort insert sort grows in a
    quadratic fashion. n log n is a lower order growth than quadratic hence why we would prefer it when sorting.
"""

# Generate List
unsorted_list_0 = generate_list(1000)
# Run and time the sort
merge_sort_time = timeit.timeit('merge_sort.merge_sort(unsorted_list_0)', globals=globals(), number=1000)
print("Merge Sort: {}".format(merge_sort_time))

# Generate List
unsorted_list_1 = generate_list(1000)
# Run and time the sort
insertion_sort_time = timeit.timeit('insertion_sort.insertion_sort(unsorted_list_1)', globals=globals(), number=1000)
print("Insertsion Sort: {}".format(insertion_sort_time))

if merge_sort_time < insertion_sort_time:
    print("merge sort time was faster this time")
elif merge_sort_time == insertion_sort_time:
    print("Amazing!! The two algorithms took the same amount of time! What are the odds of that?")
else:
    print("Insertion sort method won out this time but on average it will not.")
