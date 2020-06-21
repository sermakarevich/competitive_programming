from algorithms.array import create_array


def selection_sort(A):
    length = len(A)

    for i in range(length-1):
        min_val_index = i

        for j in range(i+1, length):
            if A[j] < A[min_val_index]:
                min_val_index = j

        if min_val_index != i:
            A[i], A[min_val_index] = A[min_val_index], A[i]

    return A


A = create_array()
print(selection_sort(A))