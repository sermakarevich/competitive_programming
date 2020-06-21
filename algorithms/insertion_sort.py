from algorithms.array import create_array


def insertion_sort(A):
    length = len(A)

    for i in range(1, length):
        min_val = A[i]

        while A[i-1] > min_val and i > 0:
            A[i-1], A[i] = A[i], A[i-1]
            i -= 1
    return A


A = create_array()
print(insertion_sort(A))

