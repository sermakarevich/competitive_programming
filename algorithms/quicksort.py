from random import randint

from algorithms.array import create_array


def quicksort(A):
    if len(A) <= 0:
        return A
    center_val = A[randint(0, len(A) - 1)]
    less, equal, more = [], [], []

    for val in A:
        if val == center_val:
            equal.append(val)
        if val < center_val:
            less.append(val)
        if val > center_val:
            more.append(val)
    return quicksort(less) + equal + quicksort(more)


A = create_array()
print(quicksort(A))