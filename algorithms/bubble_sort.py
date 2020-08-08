from algorithms.array import create_array


def bubble_sort(A):
    length = len(A)
    is_sorted = False
    iters = 0

    while not is_sorted:
        is_sorted = True
        for index in range(length-1):
            if A[index] > A[index + 1]:
                iters+=1
                is_sorted = False
                A[index], A[index+1] = A[index + 1], A[index]
    print(iters)
    return A


A = create_array(30)
print(A)
print(bubble_sort(A))
