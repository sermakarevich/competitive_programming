from algorithms.array import create_array


def merge(A, B):
    a, b = 0, 0
    C = []
    while a < len(A) and b < len(B):
        if A[a] <= B[b]:
            C.append(A[a])
            a += 1
        else:
            C.append(B[b])
            b += 1
    if a == len(A):
        C.extend(B[b:])
    else:
        C.extend(A[a:])
    return C


def merge_sort(A):
    if len(A) <= 1:
        return A
    split = len(A) // 2
    left, right = merge_sort(A[:split]), merge_sort(A[split:])
    return merge(left, right)


A = create_array()
print(merge_sort(A))
