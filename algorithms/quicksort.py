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


def quicksort(A):
    if len(A) <= 0:
        return A
    mid_val = A[randint(0, len(A) - 1)]
    l, e, m = [], [], []
    for a in A:
        if a == mid_val:
            e.append(a)
        elif a > mid_val:
            m.append(a)
        else:
            l.append(a)
    return quicksort(l) + e + quicksort(m)


A = create_array()
print(quicksort(A))