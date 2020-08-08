def merge_sort(s):
    if len(s) == 1:
        return s
    split = len(s) // 2
    left, right = merge_sort(s[:split]), merge_sort(s[split:])
    return merge(left, right)


def merge(A, B):
    a, b = 0, 0
    C = []
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            C.append(A[a])
            a += 1
        else:
            C.append(B[b])
            b += 1
    while a < len(A):
        C.append(A[a])
        a += 1
    while b < len(B):
        C.append(B[b])
        b += 1
    return C


def is_unique_char(s: str): # O (N log N) + N
    s = merge_sort(s) # O (N log N)
    print(s)
    for i in range(1, len(s)): # N
        if s[i] == s[i-1]:
            return False
    return True


def is_unique_char_slow(s: str): # N ** 2
    for i in range(len(s)-1): # N
        for j in range(i+1, len(s)): # N
            if s[i] == s[j]:
                return False
    return True


s = 'makarevich'
print(is_unique_char(s))
print(is_unique_char_slow(s))
s = 'sergi'
print(is_unique_char(s))
print(is_unique_char_slow(s))