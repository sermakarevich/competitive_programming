from algorithms.array import create_array


def bubble_sort(A):
    length = len(A)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for index in range(length-1):
            if A[index] > A[index + 1]:
                is_sorted = False
                A[index], A[index+1] = A[index + 1], A[index]
    return A


A = create_array()
print(bubble_sort(A))
